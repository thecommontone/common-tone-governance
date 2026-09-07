#!/usr/bin/env python3
"""Read-only, lstat-based verifier for CHECKSUMS.txt."""

from __future__ import annotations

import hashlib
import os
import re
import stat
import sys
from pathlib import Path, PurePosixPath


SHA_RE = re.compile(r"^[0-9a-f]{64}$")
MANIFEST = "CHECKSUMS.txt"


def _walk(root: Path):
    stack = [(root, PurePosixPath())]
    while stack:
        directory, relative_dir = stack.pop()
        for entry in sorted(os.scandir(directory), key=lambda item: item.name):
            relative = relative_dir / entry.name
            yield relative, entry
            if entry.is_dir(follow_symlinks=False):
                stack.append((Path(entry.path), relative))


def _parse_manifest(path: Path) -> tuple[dict[str, str], list[str]]:
    findings: list[str] = []
    try:
        info = os.lstat(path)
    except FileNotFoundError:
        return {}, [f"MISSING: {MANIFEST}"]
    if stat.S_ISLNK(info.st_mode):
        return {}, [f"SYMLINK: {MANIFEST}"]
    if not stat.S_ISREG(info.st_mode):
        return {}, [f"NOT REGULAR: {MANIFEST}"]
    try:
        lines = path.read_text("utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        return {}, [f"UNREADABLE: {MANIFEST}: {exc}"]
    expected: dict[str, str] = {}
    for number, line in enumerate(lines, start=1):
        if not line:
            continue
        parts = line.split("  ", 1)
        if len(parts) != 2 or not SHA_RE.fullmatch(parts[0]):
            findings.append(f"BAD MANIFEST LINE {number}")
            continue
        digest, name = parts
        relative = PurePosixPath(name)
        if (
            not name
            or "\\" in name
            or relative.is_absolute()
            or any(part in ("", ".", "..") for part in relative.parts)
            or name == MANIFEST
        ):
            findings.append(f"UNSAFE MANIFEST PATH: {name!r}")
            continue
        if name in expected:
            findings.append(f"DUPLICATE MANIFEST PATH: {name}")
            continue
        expected[name] = digest
    return expected, findings


def verify(root_value: os.PathLike[str] | str) -> tuple[bool, list[str]]:
    root = Path(os.path.abspath(os.fspath(root_value)))
    findings: list[str] = []
    try:
        root_info = os.lstat(root)
    except FileNotFoundError:
        return False, [f"MISSING ROOT: {root}"]
    if stat.S_ISLNK(root_info.st_mode):
        return False, [f"SYMLINK ROOT: {root}"]
    if not stat.S_ISDIR(root_info.st_mode):
        return False, [f"NOT A DIRECTORY: {root}"]

    expected, parse_findings = _parse_manifest(root / MANIFEST)
    findings.extend(parse_findings)
    actual_files: set[str] = set()
    for relative, entry in _walk(root):
        name = relative.as_posix()
        if name == MANIFEST:
            continue
        try:
            info = entry.stat(follow_symlinks=False)
        except OSError as exc:
            findings.append(f"UNREADABLE: {name}: {exc}")
            continue
        if stat.S_ISLNK(info.st_mode):
            findings.append(f"SYMLINK: {name} (structural drift, not followed)")
            continue
        if stat.S_ISDIR(info.st_mode):
            continue
        if not stat.S_ISREG(info.st_mode):
            findings.append(f"NOT REGULAR: {name}")
            continue
        actual_files.add(name)
        wanted = expected.get(name)
        if wanted is None:
            findings.append(f"EXTRA: {name}")
            continue
        digest = hashlib.sha256(Path(entry.path).read_bytes()).hexdigest()
        if digest != wanted:
            findings.append(f"DRIFT: {name}")

    for missing in sorted(set(expected) - actual_files):
        findings.append(f"MISSING: {missing}")
    return not findings, findings


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("usage: verify_manifest.py [skill-root]", file=sys.stderr)
        return 2
    root = Path(args[0]) if args else Path(__file__).resolve().parents[1]
    okay, findings = verify(root)
    if not okay:
        for finding in findings:
            print(finding)
        return 1
    count = sum(1 for line in (root / MANIFEST).read_text("utf-8").splitlines() if line)
    print(f"VERIFIED: {count} files; no drift, extras, or symlinks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
