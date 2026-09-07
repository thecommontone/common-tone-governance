#!/usr/bin/env python3
"""Provider-neutral validation and transfer core for music-file-intake.

The public validation boundary accepts only corpus-harvest's recorded Stage-5
allowlist.  It never discovers candidates by walking the staging directory.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

import fcntl


SKILL_VERSION = "0.1.0-build"
STATE_FILENAME = "STATE.json"
QUARANTINE_RELATIVE = Path("02_SOURCE_MATERIAL") / "INBOUND_QUARANTINE"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
APPROVED_RULINGS = frozenset({"approved", "approved_with_edits"})


class IntakeError(RuntimeError):
    """A fail-closed handoff validation or transfer refusal."""


@dataclass(frozen=True)
class Candidate:
    relative_path: str
    source_path: Path
    sha256: str


@dataclass(frozen=True)
class Handoff:
    staging_root: Path
    vault_root: Path
    quarantine_root: Path
    state_path: Path
    state_sha256: str
    source_slug: str
    batch_id: str
    candidates: tuple[Candidate, ...]


@contextmanager
def _locked_quarantine(vault_root: Path):
    """Hold the provider-neutral intake transaction lock.

    The quarantine directory itself is the lock object, so acquiring the lock
    creates no filesystem entry before validation succeeds.
    """

    _require_real_directory(vault_root, "vault root")
    source_material = vault_root / "02_SOURCE_MATERIAL"
    quarantine = vault_root / QUARANTINE_RELATIVE
    _require_real_directory(source_material, "source-material root")
    _require_real_directory(quarantine, "quarantine root")
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        fd = os.open(quarantine, flags)
    except OSError as exc:
        raise IntakeError(
            f"cannot lock quarantine without following symlinks: {exc}"
        ) from exc
    try:
        if not stat.S_ISDIR(os.fstat(fd).st_mode):
            raise IntakeError("quarantine lock target is not a directory")
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield quarantine
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _absolute(path: os.PathLike[str] | str) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def _lstat(path: Path, label: str) -> os.stat_result:
    try:
        return os.lstat(path)
    except FileNotFoundError as exc:
        raise IntakeError(f"{label} is missing: {path}") from exc
    except OSError as exc:
        raise IntakeError(f"cannot inspect {label}: {path}: {exc}") from exc


def _require_real_directory(path: Path, label: str) -> None:
    mode = _lstat(path, label).st_mode
    if stat.S_ISLNK(mode):
        raise IntakeError(f"{label} must not be a symlink: {path}")
    if not stat.S_ISDIR(mode):
        raise IntakeError(f"{label} is not a directory: {path}")


def _require_relative_components_real(root: Path, relative: PurePosixPath) -> Path:
    current = root
    for index, part in enumerate(relative.parts):
        current = current / part
        info = _lstat(current, f"allowlisted path component {relative}")
        if stat.S_ISLNK(info.st_mode):
            raise IntakeError(f"allowlisted path contains a symlink: {relative}")
        if index < len(relative.parts) - 1 and not stat.S_ISDIR(info.st_mode):
            raise IntakeError(f"allowlisted parent is not a directory: {relative}")
    return current


def _read_regular_bytes(path: Path, label: str) -> bytes:
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        fd = os.open(path, flags)
    except OSError as exc:
        raise IntakeError(
            f"cannot open {label} without following symlinks: {path}: {exc}"
        ) from exc
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode):
            raise IntakeError(f"{label} must be a regular file: {path}")
        chunks: list[bytes] = []
        while True:
            chunk = os.read(fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(fd)


def _parse_state(state_path: Path) -> tuple[dict[str, Any], bytes]:
    info = _lstat(state_path, "STATE.json")
    if stat.S_ISLNK(info.st_mode):
        raise IntakeError(f"STATE.json must not be a symlink: {state_path}")
    raw = _read_regular_bytes(state_path, "STATE.json")
    try:
        state = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise IntakeError(f"STATE.json is not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(state, dict):
        raise IntakeError("STATE.json root must be an object")
    return state, raw


def _relative_markdown(value: Any) -> PurePosixPath:
    if not isinstance(value, str) or not value:
        raise IntakeError("allowlist file must be a non-empty relative path")
    if "\\" in value:
        raise IntakeError(f"allowlist file must use a relative POSIX path: {value!r}")
    relative = PurePosixPath(value)
    if relative.is_absolute():
        raise IntakeError(f"allowlist file must be relative: {value}")
    if any(part in ("", ".", "..") for part in relative.parts):
        raise IntakeError(f"allowlist path traversal is forbidden: {value}")
    if relative.suffix != ".md":
        raise IntakeError(f"allowlist candidate is not a Markdown file: {value}")
    return relative


def _approved_ruling_pairs(state: dict[str, Any]) -> set[tuple[str, str]]:
    try:
        gate2 = state["gates"]["gate2_rulings"]
    except (KeyError, TypeError) as exc:
        raise IntakeError("STATE.json is missing Gate 2 rulings") from exc
    if not isinstance(gate2, dict):
        raise IntakeError("Gate-2 rulings must be an object")
    if gate2.get("status") != "ruled":
        raise IntakeError("Gate 2 must be closed with status 'ruled'")
    rulings = gate2.get("rulings")
    if not isinstance(rulings, list):
        raise IntakeError("Gate-2 rulings must be a list")
    approved: set[tuple[str, str]] = set()
    approved_paths: set[str] = set()
    for ruling in rulings:
        if not isinstance(ruling, dict):
            raise IntakeError("each Gate-2 ruling must be an object")
        if ruling.get("ruling") not in APPROVED_RULINGS:
            continue
        file_value = ruling.get("candidate_file")
        digest = ruling.get("sha256")
        if not isinstance(file_value, str) or not SHA256_RE.fullmatch(digest or ""):
            raise IntakeError(
                "approved Gate-2 ruling has an invalid candidate_file or sha256"
            )
        if file_value in approved_paths:
            raise IntakeError(f"duplicate approved Gate-2 ruling: {file_value}")
        approved_paths.add(file_value)
        approved.add((file_value, digest))
    return approved


def _require_stage5_ready(state: dict[str, Any]) -> None:
    try:
        status = state["stages"]["s5_canonical_intake"]["status"]
    except (KeyError, TypeError) as exc:
        raise IntakeError("STATE.json is missing Stage 5 status") from exc
    if status != "in_progress":
        raise IntakeError("Stage 5 must have status 'in_progress' before handoff")
    anomalies = state.get("anomalies")
    if not isinstance(anomalies, list):
        raise IntakeError("STATE.json anomalies must be a list")
    for anomaly in anomalies:
        if not isinstance(anomaly, dict):
            continue
        if (
            anomaly.get("blocking") is True
            and not anomaly.get("resolved_at")
            and anomaly.get("scope") in (None, "global", "s5_canonical_intake")
        ):
            raise IntakeError("an unresolved blocking anomaly prevents Stage 5 intake")


def validate_handoff(
    staging_root: os.PathLike[str] | str,
    vault_root: os.PathLike[str] | str,
) -> Handoff:
    """Validate the complete Stage-5 handoff without writing anything.

    All checks happen before a caller may copy any candidate.  The returned
    object binds current STATE.json bytes and current candidate bytes.
    """

    staging = _absolute(staging_root)
    vault = _absolute(vault_root)
    _require_real_directory(staging, "staging root")
    _require_real_directory(vault, "vault root")

    quarantine = vault / QUARANTINE_RELATIVE
    _require_real_directory(vault / "02_SOURCE_MATERIAL", "source-material root")
    _require_real_directory(quarantine, "quarantine root")

    state_path = staging / STATE_FILENAME
    state, state_bytes = _parse_state(state_path)
    if state.get("schema_version") != "1.1":
        raise IntakeError(
            "unsupported STATE.json schema_version; music-file-intake 0.1.0-build "
            "requires corpus-harvest schema_version 1.1"
        )
    program = state.get("program")
    if not isinstance(program, dict):
        raise IntakeError("STATE.json program must be an object")
    recorded_root = program.get("staging_root")
    if not isinstance(recorded_root, str) or _absolute(recorded_root) != staging:
        raise IntakeError(
            "STATE.json staging_root does not match the supplied staging root"
        )
    source_slug = program.get("source_slug")
    if not isinstance(source_slug, str) or not re.fullmatch(
        r"[a-z0-9][a-z0-9_-]*", source_slug
    ):
        raise IntakeError("STATE.json source_slug is missing or unsafe")

    _require_stage5_ready(state)
    approved = _approved_ruling_pairs(state)
    allowlist = state.get("stage5_allowlist")
    if not isinstance(allowlist, list) or not allowlist:
        raise IntakeError("Stage-5 allowlist is empty")

    seen_paths: set[str] = set()
    allowlist_pairs: set[tuple[str, str]] = set()
    candidates: list[Candidate] = []
    for entry in allowlist:
        if not isinstance(entry, dict) or set(entry) != {"file", "sha256"}:
            raise IntakeError(
                "each allowlist entry must contain exactly file and sha256"
            )
        relative = _relative_markdown(entry["file"])
        relative_text = relative.as_posix()
        digest = entry["sha256"]
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            raise IntakeError(
                f"allowlist sha256 must be a lowercase 64-hex digest: {relative_text}"
            )
        if relative_text in seen_paths:
            raise IntakeError(f"duplicate allowlist path: {relative_text}")
        seen_paths.add(relative_text)
        allowlist_pairs.add((relative_text, digest))

        source = _require_relative_components_real(staging, relative)
        data = _read_regular_bytes(source, f"allowlisted candidate {relative_text}")
        actual = hashlib.sha256(data).hexdigest()
        if actual != digest:
            raise IntakeError(
                f"candidate hash does not match current bytes: {relative_text}"
            )
        candidates.append(Candidate(relative_text, source, digest))

    if allowlist_pairs != approved:
        raise IntakeError(
            "allowlist does not exactly match the approved Gate-2 rulings"
        )

    state_sha = hashlib.sha256(state_bytes).hexdigest()
    return Handoff(
        staging_root=staging,
        vault_root=vault,
        quarantine_root=quarantine,
        state_path=state_path,
        state_sha256=state_sha,
        source_slug=source_slug,
        batch_id=f"{source_slug}--{state_sha[:12]}",
        candidates=tuple(candidates),
    )


def _write_new_file(path: Path, data: bytes, mode: int = 0o600) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        fd = os.open(path, flags, mode)
    except OSError as exc:
        raise IntakeError(
            f"cannot create quarantine file safely: {path}: {exc}"
        ) from exc
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise IntakeError(f"new quarantine path is not a regular file: {path}")
        view = memoryview(data)
        written = 0
        while written < len(view):
            count = os.write(fd, view[written:])
            if count <= 0:
                raise IntakeError(f"short write while creating quarantine file: {path}")
            written += count
        os.fsync(fd)
    finally:
        os.close(fd)


def _fsync_directory(path: Path) -> None:
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    fd = os.open(path, flags)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def transfer_handoff(
    staging_root: os.PathLike[str] | str,
    vault_root: os.PathLike[str] | str,
    *,
    invoked_by: str,
) -> Path:
    """Atomically copy one validated corpus-harvest handoff to quarantine.

    Source files are never moved or deleted.  The complete batch becomes
    visible with one directory rename; any failure before that point removes
    only the transaction directory created by this invocation.
    """

    if not isinstance(invoked_by, str) or not invoked_by.strip():
        raise IntakeError("invoked_by must be a non-empty protocol assertion")
    if len(invoked_by) > 200:
        raise IntakeError("invoked_by is too long")

    staging = _absolute(staging_root)
    vault = _absolute(vault_root)
    with _locked_quarantine(vault) as quarantine:
        # Validation is intentionally inside the lock: two cooperating intake
        # processes cannot validate stale destination state and then race.
        handoff = validate_handoff(staging, vault)
        batch_parent = quarantine / "corpus-harvest"
        created_batch_parent = False
        try:
            parent_info = os.lstat(batch_parent)
        except FileNotFoundError:
            os.mkdir(batch_parent, 0o700)
            created_batch_parent = True
        else:
            if stat.S_ISLNK(parent_info.st_mode):
                raise IntakeError(
                    f"quarantine batch parent must not be a symlink: {batch_parent}"
                )
            if not stat.S_ISDIR(parent_info.st_mode):
                raise IntakeError(
                    f"quarantine batch parent is not a directory: {batch_parent}"
                )

        destination = batch_parent / handoff.batch_id
        try:
            os.lstat(destination)
        except FileNotFoundError:
            pass
        else:
            raise IntakeError(
                f"quarantine batch already exists; refusing overwrite: {destination}"
            )

        try:
            transaction = Path(
                tempfile.mkdtemp(prefix=f".txn-{handoff.batch_id}-", dir=batch_parent)
            )
        except Exception:
            if created_batch_parent:
                os.rmdir(batch_parent)
            raise
        committed = False
        try:
            files_dir = transaction / "files"
            os.mkdir(files_dir, 0o700)
            receipt_files: list[dict[str, str]] = []
            for index, candidate in enumerate(handoff.candidates, start=1):
                # Re-open without following symlinks and re-hash the bytes being
                # copied.  A post-validation edit therefore aborts the batch.
                data = _read_regular_bytes(
                    candidate.source_path,
                    f"allowlisted candidate {candidate.relative_path}",
                )
                actual = hashlib.sha256(data).hexdigest()
                if actual != candidate.sha256:
                    raise IntakeError(
                        f"candidate changed during transfer: {candidate.relative_path}"
                    )
                quarantine_name = f"{index:04d}--{candidate.source_path.name}"
                quarantine_relative = f"files/{quarantine_name}"
                _write_new_file(files_dir / quarantine_name, data)
                receipt_files.append(
                    {
                        "source_file": candidate.relative_path,
                        "quarantine_file": quarantine_relative,
                        "sha256": actual,
                    }
                )

            receipt = {
                "receipt_schema": "1.0",
                "skill_version": SKILL_VERSION,
                "source_slug": handoff.source_slug,
                "state_file": STATE_FILENAME,
                "state_sha256": handoff.state_sha256,
                "invoked_by": invoked_by.strip(),
                "created_at": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "files": receipt_files,
            }
            receipt_bytes = (
                json.dumps(receipt, indent=2, sort_keys=True) + "\n"
            ).encode("utf-8")
            _write_new_file(transaction / "INTAKE_RECEIPT.json", receipt_bytes)

            # Bind the commit to current bytes, not merely the earlier snapshot.
            final_check = validate_handoff(staging, vault)
            if final_check.state_sha256 != handoff.state_sha256:
                raise IntakeError(
                    "STATE.json changed during transfer; refusing the batch"
                )
            if final_check.candidates != handoff.candidates:
                raise IntakeError(
                    "allowlisted candidates changed during transfer; refusing the batch"
                )

            _fsync_directory(files_dir)
            _fsync_directory(transaction)
            os.rename(transaction, destination)
            committed = True
            _fsync_directory(batch_parent)
            return destination
        finally:
            if not committed and transaction.exists():
                shutil.rmtree(transaction)
            if not committed and created_batch_parent:
                try:
                    os.rmdir(batch_parent)
                except OSError:
                    # Never remove an unexpected entry. A non-empty directory is
                    # preserved for investigation rather than cleaned broadly.
                    pass
