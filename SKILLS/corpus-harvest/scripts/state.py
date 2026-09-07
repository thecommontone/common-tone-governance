#!/usr/bin/env python3
"""corpus-harvest STATE.json authority.

Single-writer, atomic, schema-versioned. PROGRESS.md is GENERATED from this
file. Stdlib only — assistant-agnostic. Contract: references/STATE.schema.json.

New work (no 12tone lineage): the reference program kept state in a hand-ticked
PROGRESS.md; cold resume needed runbook + handoff + checkboxes together. Here
the machine state is one file, and the human view is derived.
"""
import argparse, contextlib, datetime, fcntl, hashlib, json, os, stat, sys, tempfile

SCHEMA_VERSION = "1.1"  # 1.1: budget block + per-run model/usage fields (2026-08-28 amendment); 1.0 files load compatibly
MODEL_TIERS = ("none", "economy", "balanced", "frontier")
STATE_NAME = "STATE.json"
CANONICAL_PARENT = "_CT_RESEARCH_INTAKE"
FORBIDDEN_PATH_PARTS = {"INBOUND_QUARANTINE", "02_SOURCE_MATERIAL", "TEXTBOOK",
                        "00_CONSTITUTION", "04_ARCHIVE", "99_ARCHIVE"}
STAGES = ["s0_acquire", "s1_normalize", "s2_survey",
          "s3_deep_passes", "s4_merge_validate", "s5_canonical_intake"]
STAGE_TITLES = {
    "s0_acquire": "STAGE 0 · Acquire",
    "s1_normalize": "STAGE 1 · Normalize",
    "s2_survey": "STAGE 2 · Survey",
    "s3_deep_passes": "STAGE 3 · Deep passes",
    "s4_merge_validate": "STAGE 4 · Merge + validate",
    "s5_canonical_intake": "STAGE 5 · Canonical intake",
}
ANOMALY_KINDS = {"corrupt_item", "misgraded_caption", "doubled_transcript",
                 "guest_attribution", "naming_conflict", "citation_ambiguous",
                 "schema_version_mismatch", "dependency_missing",
                 "checksum_mismatch", "other"}


class StateError(Exception): pass
class ConcurrentWriteError(StateError): pass
class SchemaVersionError(StateError): pass
class GateError(StateError): pass


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def _state_path(root):
    return os.path.join(root, STATE_NAME)


def _check_root_for_lock(root):
    """Slug-independent staging validation BEFORE any write (2026-08-28
    round-4 P0: the lock itself must not touch a refused path). Forbidden
    components refuse; the root must already exist and sit in canonical or
    fixture territory. The slug-exact check still runs at load."""
    resolved = os.path.realpath(os.path.abspath(root))
    bad = set(resolved.split(os.sep)) & FORBIDDEN_PATH_PARTS
    if bad:
        raise StateError(f"refusing to lock inside forbidden location(s) "
                         f"{sorted(bad)}: {resolved}")
    if not os.path.isdir(resolved):
        raise StateError(f"staging root does not exist: {resolved}")
    canonicalish = os.path.basename(os.path.dirname(resolved)) == CANONICAL_PARENT
    if not (canonicalish or is_fixture_territory(resolved)):
        raise StateError(f"refusing to lock outside sanctioned staging "
                         f"territory: {resolved}")
    return resolved


@contextlib.contextmanager
def state_lock(root):
    """PROCESS-LEVEL exclusive lock for the whole reload -> validate ->
    mutate -> write cycle. Root is validated BEFORE any filesystem write;
    the lock file opens with O_CREAT|O_NOFOLLOW and NO truncation, so a
    symlink planted at .state.lock is refused rather than followed, and an
    existing target is never clobbered (2026-08-28 round-4 P0)."""
    resolved = _check_root_for_lock(root)
    lock_path = os.path.join(resolved, ".state.lock")
    flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(lock_path, flags, 0o644)
    except OSError as e:
        raise StateError(f"refusing lock file at {lock_path}: {e}") from e
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


@contextlib.contextmanager
def state_transaction(root, writer=None):
    """Locked load-mutate-save convenience: locks, loads, yields the state,
    saves on clean exit, discards on exception. Used by the CLI and by
    in-process callers. NOTE (stated precisely, round-5): the five pipeline
    scripts hold state_lock() directly around their own load/save cycles —
    the same lock, the same guarantee, not this helper. Every package writer
    serializes on state_lock; nothing writes outside it."""
    with state_lock(root):
        state = load_state(root)
        yield state
        save_state(root, state, writer=writer)


# ---------------------------------------------------------------- lifecycle

FIXTURE_SENTINEL = ".corpus-harvest-fixture-root"


def is_temp_path(resolved):
    """True if resolved sits inside the system temp tree (fixture territory)."""
    tmp = os.path.realpath(tempfile.gettempdir())
    return resolved == tmp or resolved.startswith(tmp + os.sep)


def has_fixture_sentinel(resolved):
    """True if resolved or an ancestor carries the fixture sentinel file —
    an explicitly marked isolated workspace root (2026-08-28 review: a
    sentinel, not an arbitrary path, sanctions non-temp fixture staging)."""
    d = resolved
    while True:
        if os.path.isfile(os.path.join(d, FIXTURE_SENTINEL)):
            return True
        parent = os.path.dirname(d)
        if parent == d:
            return False
        d = parent


def is_fixture_territory(resolved):
    return is_temp_path(resolved) or has_fixture_sentinel(resolved)


def check_staging_policy(root, source_slug):
    """The staging policy, applied wherever program state can come into being
    (scaffold AND state init — 2026-08-28 review, finding 3): forbidden
    directories always refused; otherwise the root must be canonical
    (…/_CT_RESEARCH_INTAKE/<source_slug>/) or live inside the system temp
    tree (isolated fixtures). Returns the resolved path."""
    resolved = os.path.realpath(os.path.abspath(root))
    bad = set(resolved.split(os.sep)) & FORBIDDEN_PATH_PARTS
    if bad:
        raise StateError(f"staging root resolves into forbidden location(s) "
                         f"{sorted(bad)}: {resolved}")
    canonical = (os.path.basename(os.path.dirname(resolved)) == CANONICAL_PARENT
                 and os.path.basename(resolved) == source_slug)
    if not (canonical or is_fixture_territory(resolved)):
        raise StateError(
            f"staging root must be …/{CANONICAL_PARENT}/{source_slug}/, or an "
            f"isolated workspace (system temp tree, or a root marked with "
            f"{FIXTURE_SENTINEL}); got: {resolved}")
    return resolved


def init_state(root, source_slug, adapter, source_locator, assistant,
               skill_version, word_limit=90000, token_ceiling=120000):
    if adapter not in ("youtube", "local-folder"):
        raise StateError(f"unknown adapter: {adapter}")
    check_staging_policy(root, source_slug)
    path = _state_path(root)
    if os.path.exists(path):
        raise StateError(f"{path} already exists — refusing to overwrite")
    now = _now()
    state = {
        "schema_version": SCHEMA_VERSION,
        "skill": {"name": "corpus-harvest", "version": skill_version,
                  "install_checksum": None},
        "program": {"source_slug": source_slug, "adapter": adapter,
                    "source_locator": source_locator, "created_at": now,
                    "created_by": assistant, "staging_root": os.path.abspath(root)},
        "chunk_policy": {"word_limit": word_limit, "token_ceiling": token_ceiling,
                         "frozen_at": now, "rechunk_history": []},
        "stages": {s: {"status": "pending", "started_at": None, "completed_at": None,
                       "blocking_anomaly": None, "chunk_progress": None,
                       "artifacts": None} for s in STAGES},
        "gates": {
            "gate1_directives": {"status": "pending", "proposal_file": None,
                                 "directive_set_hash": None,
                                 "ratified_at": None, "ratified_by": None},
            "gate2_rulings": {"status": "pending", "rulings": [],
                              "staging_disposition": None},
        },
        "runs": [],
        "anomalies": [],
        "dependencies": {
            "music_file_intake": {"status": "unverified", "location": None,
                                  "version_or_checksum": None, "verified_at": None},
            "prose_normalizer": {"status": "unverified", "location": None,
                                 "checksum": None, "verified_at": None},
        },
        "stage5_allowlist": None,
        "budget": {},
        "writer": {"revision": 0, "last_writer": assistant, "updated_at": now},
    }
    _write_atomic(path, state)
    return state


def load_state(root):
    path = _state_path(root)
    if not os.path.exists(path):
        raise StateError(f"no {STATE_NAME} in {root}")
    with open(path, encoding="utf-8") as f:
        state = json.load(f)
    ver = state.get("schema_version", "")
    if ver == "1.0":
        # Known older version: loads READ-ONLY. Using 1.1 features requires a
        # recorded migration (state.py migrate-state) — save_state refuses
        # until then. Never silently relabeled.
        state["_readonly_compat"] = True
    elif ver != SCHEMA_VERSION:
        raise SchemaVersionError(
            f"STATE.json schema_version {ver!r} not supported by this skill "
            f"(supports {SCHEMA_VERSION}; 1.0 loads read-only pending "
            "migrate-state) — flag to Doug, never migrate silently")
    # The staging policy applies UNCONDITIONALLY on every load (2026-08-28
    # P0: a state file whose recorded path already matched a forbidden
    # location slipped past the rebind-only check). The staging root is
    # wherever this STATE.json actually lives — the recorded absolute path
    # is provenance, not authority.
    check_staging_policy(root, state["program"]["source_slug"])
    actual = os.path.realpath(os.path.abspath(root))
    if state["program"].get("staging_root") != actual:
        state["program"].setdefault("staging_root_recorded",
                                    state["program"].get("staging_root"))
        state["program"]["staging_root"] = actual
    return state


def migrate_state(root, by):
    """Explicit, recorded 1.0 -> 1.1 migration. Applies the staging policy,
    preserves a backup and the pre-migration hash, adds the budget block and
    a migrations entry; bumps schema_version; increments revision atomically."""
    path = _state_path(root)
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    check_staging_policy(root, raw["program"]["source_slug"])
    if raw.get("schema_version") != "1.0":
        raise StateError(f"migrate-state handles 1.0 only; found "
                         f"{raw.get('schema_version')!r}")
    pre_hash = sha256_file(path)
    backup = path + ".v1.0.bak"
    if os.path.exists(backup):
        raise StateError(f"backup already exists, refusing to overwrite: {backup}")
    import shutil
    shutil.copy2(path, backup)
    raw["schema_version"] = SCHEMA_VERSION
    raw.setdefault("budget", {})
    raw.setdefault("migrations", []).append(
        {"from": "1.0", "to": SCHEMA_VERSION, "at": _now(), "by": by,
         "pre_migration_sha256": pre_hash,
         "backup": os.path.basename(backup)})
    raw["writer"]["revision"] += 1
    raw["writer"]["last_writer"] = by
    raw["writer"]["updated_at"] = _now()
    _write_atomic(path, raw)
    return raw


def save_state(root, state, writer=None):
    """Atomic single-writer save: disk revision must equal the revision this
    state was loaded with; anything else means a concurrent writer."""
    if state.pop("_readonly_compat", None):
        raise StateError("this STATE.json is schema 1.0 and loaded read-only — "
                         "record the migration first (state.py migrate-state)")
    path = _state_path(root)
    with open(path, encoding="utf-8") as f:
        on_disk = json.load(f)
    if on_disk["writer"]["revision"] != state["writer"]["revision"]:
        raise ConcurrentWriteError(
            f"disk revision {on_disk['writer']['revision']} != loaded revision "
            f"{state['writer']['revision']} — another writer has saved; reload and retry")
    state["writer"]["revision"] += 1
    state["writer"]["last_writer"] = writer or state["writer"]["last_writer"]
    state["writer"]["updated_at"] = _now()
    _write_atomic(path, state)
    return state


def _write_atomic(path, state):
    d = os.path.dirname(os.path.abspath(path))
    fd, tmp = tempfile.mkstemp(prefix=STATE_NAME + ".tmp", dir=d)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


# ---------------------------------------------------------------- validation

def validate_state(state):
    errs = []
    for key in ("schema_version", "skill", "program", "chunk_policy", "stages",
                "gates", "runs", "anomalies", "dependencies", "writer"):
        if key not in state:
            errs.append(f"missing top-level key: {key}")
    if errs:
        return errs
    if state["skill"].get("name") != "corpus-harvest":
        errs.append("skill.name must be 'corpus-harvest'")
    for s in STAGES:
        if s not in state["stages"]:
            errs.append(f"missing stage: {s}")
        elif state["stages"][s]["status"] not in ("pending", "in_progress", "complete", "blocked"):
            errs.append(f"bad status for {s}")
    g1 = state["gates"]["gate1_directives"]["status"]
    if g1 not in ("pending", "proposed", "ratified"):
        errs.append("bad gate1 status")
    for a in state["anomalies"]:
        if a["kind"] not in ANOMALY_KINDS:
            errs.append(f"bad anomaly kind: {a['kind']}")
    if not isinstance(state["writer"].get("revision"), int):
        errs.append("writer.revision must be an integer")
    cp = state["chunk_policy"]
    if not (isinstance(cp.get("word_limit"), int) and cp["word_limit"] > 0):
        errs.append("chunk_policy.word_limit must be a positive integer")
    if not (isinstance(cp.get("token_ceiling"), int) and cp["token_ceiling"] > 0):
        errs.append("chunk_policy.token_ceiling must be a positive integer")
    return errs


# ---------------------------------------------------------------- mutations

def _next_id(items, key, prefix):
    n = max([int(i[key][1:]) for i in items], default=0) + 1
    return f"{prefix}{n:04d}"


def add_run(state, stage, assistant, directive_id=None, chunk_id=None, notes=None):
    """Script-run recording ONLY (tier 'none'). Model runs MUST go through
    start_model_run(), which enforces budget, tier authority, and concurrency
    — this function refuses to be a bypass."""
    run = {"run_id": _next_id(state["runs"], "run_id", "r"),
           "stage": stage, "directive_id": directive_id, "chunk_id": chunk_id,
           "assistant": assistant, "started_at": _now(), "finished_at": None,
           "status": "running", "input_hashes": {}, "output_hashes": {},
           "model_tier": None, "model": None, "escalation_reason": None,
           "budget_scope": None, "reserved_tokens": None,
           "tokens_in": None, "tokens_out": None,
           "notes": notes}
    state["runs"].append(run)
    return run


# ------------------------------------------------- model-run enforcement

BUDGET_SCOPES = list(STAGES) + ["gate1_proposal", "calibration", "audit",
                                "orchestration"]
MAX_CONCURRENT_MODEL_RUNS = 4
_TIER_RANK = {"economy": 1, "balanced": 2, "frontier": 3}


def load_tier_map():
    """references/MODEL_TIER_MAP.json — the only place models map to tiers.
    Unknown models are refused, never guessed."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "references", "MODEL_TIER_MAP.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for tier in ("economy", "balanced", "frontier"):
        for m in data.get(tier, []):
            out[m.lower()] = tier
    return out


def set_budget(state, scope, ceiling_tokens, approved_by, max_tier="balanced"):
    """Doug's budget ruling for one scope: token ceiling + MAXIMUM AUTHORIZED
    TIER. Frontier use requires Doug to have set max_tier=frontier for the
    scope — a launching assistant's reason alone never authorizes it."""
    if scope not in BUDGET_SCOPES:
        raise StateError(f"unknown budget scope: {scope} (scopes: {BUDGET_SCOPES})")
    if not (isinstance(ceiling_tokens, int) and ceiling_tokens > 0):
        raise StateError("ceiling must be a positive integer")
    if max_tier not in _TIER_RANK:
        raise StateError(f"max_tier must be one of {sorted(_TIER_RANK)}")
    state.setdefault("budget", {})[scope] = {
        "ceiling_tokens": ceiling_tokens, "max_tier": max_tier,
        "approved_by": approved_by, "at": _now()}


def _active_model_runs(state):
    return [r for r in state["runs"]
            if r["status"] == "running" and r.get("model")]


def start_model_run(state, scope, assistant, model, max_tokens, input_hashes=None,
                    directive_id=None, chunk_id=None, escalation_reason=None,
                    notes=None):
    """Atomic pre-dispatch gate (2026-08-28 enforcement round). Refuses when:
    no Doug-approved budget for the scope; model unknown to the tier map;
    model's tier above the scope's max_tier; frontier without an escalation
    reason; 4 model runs already active; or used + active reservations +
    this reservation would exceed the ceiling. On success the run carries a
    token reservation counted against the ceiling until finish/abort."""
    if not isinstance(input_hashes, dict) or not input_hashes:
        raise StateError("model runs require at least one hashed --input-file")
    if scope not in BUDGET_SCOPES:
        raise StateError(f"unknown budget scope: {scope}")
    blockers = open_blocking(state, scope)
    if blockers:
        raise GateError(
            f"launch refused: open BLOCKING anomalies for {scope}: "
            + "; ".join(f"{a['anomaly_id']} ({a['description'][:60]}…)"
                        for a in blockers)
            + " — resolve each with a recorded ruling (resolve-anomaly) first")
    budget = (state.get("budget") or {}).get(scope)
    if not budget:
        raise GateError(f"no Doug-approved budget for scope {scope!r} — "
                        "no ceiling, no launch (state.py set-budget)")
    tier = load_tier_map().get((model or "").lower())
    if tier is None:
        raise StateError(f"model {model!r} is not in MODEL_TIER_MAP.json — "
                         "extend the map deliberately; tiers are never guessed")
    if _TIER_RANK[tier] > _TIER_RANK[budget["max_tier"]]:
        raise GateError(f"model {model} is {tier}-tier but Doug's budget for "
                        f"{scope} authorizes at most {budget['max_tier']} — "
                        "a scoped frontier approval requires his ruling")
    if tier == "frontier" and not escalation_reason:
        raise StateError("frontier run requires a recorded escalation_reason "
                         "in addition to Doug's max_tier authorization")
    if not (isinstance(max_tokens, int) and max_tokens > 0):
        raise StateError("max_tokens reservation must be a positive integer")
    active = _active_model_runs(state)
    if len(active) >= MAX_CONCURRENT_MODEL_RUNS:
        raise GateError(f"concurrency cap: {MAX_CONCURRENT_MODEL_RUNS} model "
                        "runs already active — work in waves")
    used, reserved = _scope_usage(state, scope)
    if used + reserved + max_tokens > budget["ceiling_tokens"]:
        raise GateError(
            f"reservation refused for {scope}: used {used} + reserved {reserved} "
            f"+ requested {max_tokens} > ceiling {budget['ceiling_tokens']}")
    stage = scope if scope in STAGES else "admin"
    run = add_run(state, stage, assistant, directive_id=directive_id,
                  chunk_id=chunk_id, notes=notes)
    run.update({"budget_scope": scope, "model": model, "model_tier": tier,
                "reserved_tokens": max_tokens,
                "escalation_reason": escalation_reason,
                "input_hashes": dict(input_hashes)})
    return run


def _hash_input_openat(staging_alias, parts, rel):
    """Open each component beneath staging without following symlinks."""
    directory_flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    directory_fd = os.open(staging_alias, directory_flags)
    try:
        for part in parts[:-1]:
            next_fd = os.open(part, directory_flags | nofollow,
                              dir_fd=directory_fd)
            os.close(directory_fd)
            directory_fd = next_fd
        leaf_fd = os.open(parts[-1], os.O_RDONLY | nofollow,
                          dir_fd=directory_fd)
        try:
            leaf_stat = os.fstat(leaf_fd)
            if not stat.S_ISREG(leaf_stat.st_mode):
                raise StateError(f"input is not a regular file: {rel}")
            digest = hashlib.sha256()
            for block in iter(lambda: os.read(leaf_fd, 65536), b""):
                digest.update(block)
            return digest.hexdigest()
        finally:
            os.close(leaf_fd)
    except FileNotFoundError as error:
        raise StateError(f"input file not found in staging: {rel}") from error
    except OSError as error:
        raise StateError(f"input path is symlinked or unsafe: {rel}: {error}") from error
    finally:
        os.close(directory_fd)


def hash_input_files(state, files):
    """Return {staging-relative path: sha256} for model inputs.

    Inputs are evidence, not informal launch notes: every model dispatch must
    bind at least one existing regular file inside staging. Each path
    component is checked with lstat so a symlink cannot redirect the bytes
    used by the run record. Duplicate paths refuse.
    """
    if not files:
        raise StateError("model runs require at least one --input-file")
    root = os.path.realpath(state["program"]["staging_root"])
    hashes = {}
    for supplied in files:
        candidate = (supplied if os.path.isabs(supplied)
                     else os.path.join(root, supplied))
        candidate = os.path.abspath(candidate)

        # Find the lexical ancestor that names the staging root. This handles
        # benign host aliases above staging (macOS /var -> /private/var) while
        # preserving the original path components below staging for lstat.
        cursor = candidate
        parts = []
        staging_alias = None
        while True:
            if os.path.realpath(cursor) == root:
                staging_alias = cursor
                break
            parent = os.path.dirname(cursor)
            if parent == cursor:
                break
            parts.insert(0, os.path.basename(cursor))
            cursor = parent
        if staging_alias is None:
            raise StateError(f"input file outside staging: {supplied}")

        if not parts:
            raise StateError(f"input is not a regular file: {supplied}")
        rel = os.path.join(*parts)
        current = staging_alias
        leaf_stat = None
        for part in rel.split(os.sep):
            current = os.path.join(current, part)
            try:
                leaf_stat = os.lstat(current)
            except FileNotFoundError as e:
                raise StateError(f"input file not found in staging: {rel}") from e
            if stat.S_ISLNK(leaf_stat.st_mode):
                raise StateError(f"input path contains a symlink: {rel}")
        if leaf_stat is None or not stat.S_ISREG(leaf_stat.st_mode):
            raise StateError(f"input is not a regular file: {rel}")
        if rel in hashes:
            raise StateError(f"duplicate input path: {rel}")
        hashes[rel] = _hash_input_openat(staging_alias, parts, rel)
    return hashes


def hash_output_files(state, files):
    """-> {contained_relpath: sha256}. Output evidence must live INSIDE the
    staging root; paths are normalized relative paths (not basenames), so
    same-named files in different folders cannot collide (2026-08-28 P0
    round). Duplicate resolved paths are refused."""
    hashes = {}
    root = state["program"]["staging_root"]
    for f in files:
        rel = _contained_relpath(state, f)
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            raise StateError(f"output file not found in staging: {rel}")
        if rel in hashes:
            raise StateError(f"duplicate output path: {rel}")
        hashes[rel] = sha256_file(path)
    return hashes


def verify_model_run_inputs(state, run):
    """Re-hash a model run's bound inputs before accepting its outputs."""
    expected = run.get("input_hashes")
    if not isinstance(expected, dict) or not expected:
        raise GateError("model run has no bound input hashes")
    current = hash_input_files(state, list(expected))
    changed = sorted(path for path, digest in expected.items()
                     if current.get(path) != digest)
    if changed:
        raise GateError("model input changed after launch: " + ", ".join(changed))


def finish_model_run(state, run, tokens_in, tokens_out, output_hashes):
    """Completion requires NONNEGATIVE actual usage and at least one output
    hash (keys are staging-contained relative paths — use hash_output_files).
    The reservation is released; actual usage counts thereafter. Actuals that
    exceed the reservation or push the scope over its ceiling are recorded
    honestly AND raise a blocking anomaly automatically."""
    if run.get("status") != "running" or not run.get("model"):
        raise StateError("finish_model_run: not an active model run")
    verify_model_run_inputs(state, run)
    ti, to = int(tokens_in), int(tokens_out)
    if ti < 0 or to < 0:
        raise StateError("token counts must be nonnegative")
    if not output_hashes or not isinstance(output_hashes, dict):
        raise StateError("completion requires at least one output hash")
    reserved = run.get("reserved_tokens") or 0
    run["tokens_in"], run["tokens_out"] = ti, to
    run["output_hashes"].update(output_hashes)
    run["reserved_tokens"] = None
    finish_run(run, "complete")
    scope = run.get("budget_scope")
    if ti + to > reserved:
        add_anomaly(state, "other",
                    f"{run['run_id']}: actual usage {ti + to} exceeded its "
                    f"reservation {reserved} — reservations are estimates the "
                    "supervising assistant must size honestly; review before "
                    "the next wave", blocking=True, scope=scope)
    if scope:
        budget = (state.get("budget") or {}).get(scope)
        used, res = _scope_usage(state, scope)
        if budget and used + res > budget["ceiling_tokens"]:
            add_anomaly(state, "other",
                        f"token ceiling exceeded for {scope} at completion of "
                        f"{run['run_id']} ({used}+{res} > "
                        f"{budget['ceiling_tokens']}) — stop; Doug approves "
                        "any new ceiling", blocking=True, scope=scope)


def abort_model_run(state, run, reason):
    if run.get("status") != "running" or not run.get("model"):
        raise StateError("abort_model_run: not an active model run")
    run["notes"] = ((run.get("notes") or "") + f" [aborted: {reason}]").strip()
    run["tokens_in"] = run["tokens_in"] if run["tokens_in"] is not None else 0
    run["tokens_out"] = run["tokens_out"] if run["tokens_out"] is not None else 0
    run["reserved_tokens"] = None
    finish_run(run, "failed")


def _scope_usage(state, scope):
    """-> (used_actual_tokens, active_reserved_tokens) for one scope."""
    used = reserved = 0
    for r in state["runs"]:
        if (r.get("budget_scope") or r["stage"]) != scope:
            continue
        used += (r.get("tokens_in") or 0) + (r.get("tokens_out") or 0)
        if r["status"] == "running" and r.get("reserved_tokens"):
            reserved += r["reserved_tokens"]
    return used, reserved


def budget_status(state):
    """-> {scope: {ceiling, max_tier, used, reserved, exceeded}}."""
    out = {}
    budget = state.get("budget") or {}
    for scope in BUDGET_SCOPES:
        used, reserved = _scope_usage(state, scope)
        entry = budget.get(scope)
        if entry is None and used == 0 and reserved == 0:
            continue
        ceiling = entry["ceiling_tokens"] if entry else None
        out[scope] = {"ceiling_tokens": ceiling,
                      "max_tier": entry.get("max_tier") if entry else None,
                      "used_tokens": used, "reserved_tokens": reserved,
                      "exceeded": ceiling is not None and used + reserved > ceiling}
    return out


def finish_run(run, status="complete"):
    run["finished_at"] = _now()
    run["status"] = status


def add_anomaly(state, kind, description, item_id=None, blocking=False,
                status="open", scope=None):
    """scope: budget scope / stage the anomaly blocks (None = program-wide,
    blocks everything). Blocking anomalies actually block (round-4 P0-3):
    start_model_run and stage completion refuse while relevant ones are open;
    they clear only through a recorded resolution (resolve_anomaly)."""
    if kind not in ANOMALY_KINDS:
        raise StateError(f"unknown anomaly kind: {kind}")
    for a in state["anomalies"]:
        if (a["kind"], a.get("item_id"), a["description"]) == (kind, item_id, description):
            return a  # idempotent: identical anomaly not duplicated
    a = {"anomaly_id": _next_id(state["anomalies"], "anomaly_id", "a"),
         "item_id": item_id, "kind": kind, "description": description,
         "status": status, "blocking": blocking, "scope": scope,
         "resolution": None, "at": _now()}
    state["anomalies"].append(a)
    return a


def open_blocking(state, scope=None):
    """Open blocking anomalies relevant to `scope`: scope-matching ones plus
    all program-wide (scope None) ones. scope=None -> every open blocker."""
    out = []
    for a in state["anomalies"]:
        if not (a.get("blocking") and a["status"] in ("open", "for_doug")):
            continue
        a_scope = a.get("scope")
        if scope is None or a_scope is None or a_scope == scope:
            out.append(a)
    return out


def resolve_anomaly(state, anomaly_id, ruling, by):
    """The only way a blocking anomaly stops blocking: a recorded ruling."""
    if not ruling or not ruling.strip():
        raise StateError("resolution requires a ruling text")
    for a in state["anomalies"]:
        if a["anomaly_id"] == anomaly_id:
            if a["status"] == "resolved":
                raise StateError(f"{anomaly_id} is already resolved")
            a["status"] = "resolved"
            a["resolution"] = {"ruling": ruling, "by": by, "at": _now()}
            return a
    raise StateError(f"no anomaly {anomaly_id}")


def propose_gate1(state, proposal_file):
    """Record the Gate-1 proposal. The file must exist inside staging; it is
    the exact document Doug will rule on."""
    rel = _contained_relpath(state, proposal_file)
    path = os.path.join(state["program"]["staging_root"], rel)
    if not os.path.isfile(path):
        raise StateError(f"proposal file does not exist in staging: {rel}")
    g = state["gates"]["gate1_directives"]
    if g["status"] == "ratified":
        raise GateError("Gate 1 already ratified — a new directive set is a new gate")
    g.update({"status": "proposed", "proposal_file": rel,
              "proposal_sha256": sha256_file(path)})
    return rel


def ratify_gate1(state, ratified_by, audit_policy=None):
    """Ratification requires a recorded proposal (status 'proposed'; hash from
    the exact recorded file) AND a numerical audit policy (2026-08-28
    enforcement round): recall/attribution thresholds and the duplicate-audit
    sample fraction, so the stop rule is parameterized, not prose."""
    if not audit_policy:
        raise GateError("Gate-1 ratification requires an audit policy: "
                        "recall_threshold, attribution_threshold, "
                        "sample_fraction (MODEL_ROUTING_POLICY.md stop rule)")
    for k in ("recall_threshold", "attribution_threshold", "sample_fraction"):
        v = audit_policy.get(k)
        if not (isinstance(v, (int, float)) and 0 < v <= 1):
            raise StateError(f"audit_policy.{k} must be a number in (0, 1]")
    g = state["gates"]["gate1_directives"]
    if g["status"] != "proposed" or not g["proposal_file"]:
        raise GateError("Gate 1 can only be ratified from status 'proposed' with "
                        "a recorded proposal_file — record the proposal first "
                        "(gate1-propose)")
    path = os.path.join(state["program"]["staging_root"], g["proposal_file"])
    if not os.path.isfile(path):
        raise GateError(f"recorded proposal file is missing: {g['proposal_file']}")
    actual = sha256_file(path)
    if g.get("proposal_sha256") and actual != g["proposal_sha256"]:
        raise GateError(
            f"proposal file changed since it was recorded "
            f"(proposed {g['proposal_sha256'][:12]}…, now {actual[:12]}…) — "
            "Doug must see the current bytes; re-run gate1-propose first")
    g.update({"status": "ratified", "directive_set_hash": actual,
              "ratified_at": _now(), "ratified_by": ratified_by,
              "audit_policy": {k: audit_policy[k] for k in
                               ("recall_threshold", "attribution_threshold",
                                "sample_fraction")}})


def record_gate2_ruling(state, candidate_file, ruling, destination=None,
                        credit_notes=None):
    """Record one Gate-2 ruling. candidate_file is stored relative to the
    staging root; it must exist inside it, and its hash is computed NOW so the
    ruling pins the exact bytes Doug ruled on."""
    if ruling not in ("approved", "approved_with_edits", "rejected", "deferred"):
        raise StateError(f"unknown ruling: {ruling}")
    rel = _contained_relpath(state, candidate_file)
    path = os.path.join(state["program"]["staging_root"], rel)
    if not os.path.isfile(path):
        raise StateError(f"candidate file does not exist in staging: {rel}")
    g2 = state["gates"]["gate2_rulings"]
    g2["rulings"] = [r for r in g2["rulings"] if r["candidate_file"] != rel]
    g2["rulings"].append({"candidate_file": rel, "sha256": sha256_file(path),
                          "ruling": ruling, "destination": destination,
                          "credit_notes": credit_notes, "at": _now()})
    if g2["status"] == "pending":
        g2["status"] = "presented"
    return g2["rulings"][-1]


def record_gate2_disposition(state, disposition, detail=None):
    if disposition not in ("retain", "relocate_proposed", "deletion_proposed"):
        raise StateError(f"unknown disposition: {disposition}")
    state["gates"]["gate2_rulings"]["staging_disposition"] = {
        "disposition": disposition, "detail": detail, "at": _now()}


def close_gate2(state):
    g2 = state["gates"]["gate2_rulings"]
    if not g2["rulings"]:
        raise GateError("Gate 2 cannot close with no rulings recorded")
    if not g2["staging_disposition"]:
        raise GateError("Gate 2 cannot close without a staging-folder disposition "
                        "(retain / relocate_proposed / deletion_proposed)")
    g2["status"] = "ruled"


def build_allowlist(state):
    """Stage-5 allowlist = EXACTLY the Gate-2 approved files, re-hashed and
    re-verified now. Refuses if any approved file moved or changed since the
    ruling (checksum_mismatch)."""
    g2 = state["gates"]["gate2_rulings"]
    if g2["status"] != "ruled":
        raise GateError("allowlist can only be built after Gate 2 is closed (ruled)")
    approved = [r for r in g2["rulings"]
                if r["ruling"] in ("approved", "approved_with_edits")]
    if not approved:
        raise GateError("no approved candidates — nothing for Stage 5")
    allow = []
    for r in approved:
        path = os.path.join(state["program"]["staging_root"], r["candidate_file"])
        if not os.path.isfile(path):
            raise GateError(f"approved file missing from staging: {r['candidate_file']}")
        actual = sha256_file(path)
        if actual != r["sha256"]:
            add_anomaly(state, "checksum_mismatch",
                        f"{r['candidate_file']} changed after Doug's ruling "
                        f"(ruled {r['sha256'][:12]}…, now {actual[:12]}…) — re-present",
                        blocking=True, scope="s5_canonical_intake")
            raise GateError(f"{r['candidate_file']} changed since Doug's ruling — "
                            "re-present it at Gate 2")
        allow.append({"file": r["candidate_file"], "sha256": actual})
    state["stage5_allowlist"] = allow
    return allow


_SHA256_RE = None


def _contained_relpath(state, file_path):
    """Resolve file_path (absolute, or relative to staging root) and require
    containment inside the staging root. Returns the relative path."""
    root = os.path.realpath(state["program"]["staging_root"])
    cand = file_path if os.path.isabs(file_path) else os.path.join(root, file_path)
    resolved = os.path.realpath(cand)
    if not (resolved == root or resolved.startswith(root + os.sep)):
        raise StateError(f"path escapes the staging root: {file_path}")
    return os.path.relpath(resolved, root)


def validate_allowlist(state):
    """Full Stage-5 allowlist enforcement (plan addendum note 1). Every entry:
    a Markdown file, a real 64-hex sha256, existing inside the staging root,
    hash matching the actual bytes — and the entry set corresponds EXACTLY to
    the Gate-2 approved rulings. Returns a list of violation strings."""
    global _SHA256_RE
    if _SHA256_RE is None:
        import re
        _SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
    errs = []
    allow = state.get("stage5_allowlist") or []
    if not allow:
        return ["allowlist is empty"]
    root = os.path.realpath(state["program"]["staging_root"])
    seen = set()
    for e in allow:
        f, h = e.get("file", ""), e.get("sha256", "")
        label = f or "<missing file>"
        if not f.endswith(".md"):
            errs.append(f"{label}: not a Markdown file")
        if not _SHA256_RE.match(h or ""):
            errs.append(f"{label}: sha256 is not a 64-hex digest: {h!r}")
            h = None
        try:
            rel = _contained_relpath(state, f)
        except StateError as ex:
            errs.append(str(ex))
            continue
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            errs.append(f"{rel}: file does not exist in staging")
        elif h and sha256_file(path) != h:
            errs.append(f"{rel}: actual file hash differs from allowlist entry")
        seen.add((rel, h))
    approved = {(r["candidate_file"], r["sha256"])
                for r in state["gates"]["gate2_rulings"]["rulings"]
                if r["ruling"] in ("approved", "approved_with_edits")}
    if seen != approved:
        extra = sorted(f for f, _ in seen - approved)
        missing = sorted(f for f, _ in approved - seen)
        if extra:
            errs.append(f"allowlist entries not approved at Gate 2: {extra}")
        if missing:
            errs.append(f"Gate-2 approved files missing from allowlist: {missing}")
    return errs


AUDITED_STAGES = ("s2_survey", "s3_deep_passes")


def _stage_watermark_and_digest(state, stage):
    """-> (last_run_id, digest, population). The digest is computed by
    REHASHING every recorded artifact's CURRENT BYTES on disk (round-5 P1-2:
    a digest over stored hashes let post-audit edits slip through). Refuses
    files that are missing, escaped from staging, or changed since their run
    recorded them. Population = completed model runs with outputs."""
    runs = [r for r in state["runs"]
            if (r.get("budget_scope") or r["stage"]) == stage]
    watermark = runs[-1]["run_id"] if runs else None
    root = state["program"]["staging_root"]
    h = hashlib.sha256()
    population = 0
    for r in runs:
        if r["status"] == "complete" and r.get("model") and r["output_hashes"]:
            population += 1
            for rel in sorted(r["output_hashes"]):
                checked = _contained_relpath(state, rel)  # escape -> refuse
                path = os.path.join(root, checked)
                if not os.path.isfile(path):
                    raise StateError(
                        f"audited artifact missing from staging: {rel} "
                        f"(recorded by {r['run_id']})")
                current = sha256_file(path)
                if current != r["output_hashes"][rel]:
                    raise StateError(
                        f"audited artifact changed since {r['run_id']} recorded "
                        f"it: {rel} — evidence integrity broken; investigate "
                        "before auditing or completing")
                h.update(f"{checked}:{current}".encode())
    return watermark, h.hexdigest(), population


def record_audit_result(state, stage, recall, attribution, sample_fraction, by):
    """Record one duplicate-audit result for an audited stage, BOUND to the
    stage's current run watermark and artifact-set digest — later model
    output invalidates it. Compared against the Gate-1 audit policy; a
    below-threshold result is recorded with passed=false AND raises a
    blocking anomaly scoped to the stage, which only Doug's recorded
    resolution clears (the stop rule)."""
    if stage not in AUDITED_STAGES:
        raise StateError(f"audit results apply to {AUDITED_STAGES}")
    ap = (state["gates"]["gate1_directives"].get("audit_policy") or None)
    if not ap:
        raise GateError("no audit policy recorded — Gate 1 must be ratified first")
    for name, v in (("recall", recall), ("attribution", attribution),
                    ("sample_fraction", sample_fraction)):
        if not (isinstance(v, (int, float)) and 0 <= v <= 1):
            raise StateError(f"{name} must be a number in [0, 1]")
    passed = (recall >= ap["recall_threshold"]
              and attribution >= ap["attribution_threshold"]
              and sample_fraction >= ap["sample_fraction"])
    watermark, digest, population = _stage_watermark_and_digest(state, stage)
    if population == 0:
        raise GateError(
            f"audit refused: {stage} has no completed model runs with outputs "
            "— an audit needs a nonempty, identified population; there is "
            "nothing to sample (round-5 P1-1)")
    entry = {"stage": stage, "recall": recall, "attribution": attribution,
             "sample_fraction": sample_fraction, "passed": passed,
             "run_watermark": watermark, "artifacts_digest": digest,
             "population": population,
             "by": by, "at": _now()}
    state.setdefault("audit_results", []).append(entry)
    if not passed:
        add_anomaly(state, "other",
                    f"audit for {stage} below Gate-1 thresholds "
                    f"(recall {recall}/{ap['recall_threshold']}, attribution "
                    f"{attribution}/{ap['attribution_threshold']}, sample "
                    f"{sample_fraction}/{ap['sample_fraction']}) — STOP; "
                    "finding goes to Doug, never quietly re-run",
                    blocking=True, scope=stage)
    return entry


def set_stage(state, stage, status):
    """Stage transitions enforce the gates. This is the anti-bypass rail:
    nothing downstream of a gate moves while the gate is open, and a stage
    cannot COMPLETE with active model runs, an exceeded budget, or (for
    audited stages) without a passing audit result (2026-08-28 P0 round)."""
    if stage not in STAGES:
        raise StateError(f"unknown stage: {stage}")
    if status == "complete":
        blockers = open_blocking(state, stage)
        if blockers:
            raise GateError(
                f"{stage} cannot complete with open BLOCKING anomalies: "
                + ", ".join(a["anomaly_id"] for a in blockers)
                + " — each needs a recorded resolution (resolve-anomaly)")
        active = [r["run_id"] for r in _active_model_runs(state)
                  if (r.get("budget_scope") or r["stage"]) == stage]
        if active:
            raise GateError(f"{stage} cannot complete with active model runs: "
                            f"{active} — finish or abort them first")
        bs = budget_status(state).get(stage)
        if bs and bs["exceeded"]:
            raise GateError(f"{stage} cannot complete with its budget exceeded "
                            f"({bs['used_tokens']}+{bs['reserved_tokens']} > "
                            f"{bs['ceiling_tokens']}) — Doug rules first")
        if stage in AUDITED_STAGES:
            results = [a for a in state.get("audit_results", [])
                       if a["stage"] == stage]
            if not results:
                raise GateError(f"{stage} cannot complete without a recorded "
                                "audit result (record-audit)")
            latest = results[-1]
            if not latest["passed"]:
                raise GateError(f"{stage} cannot complete: latest audit failed "
                                "its thresholds — the finding goes to Doug")
            watermark, digest, population = _stage_watermark_and_digest(state, stage)
            if population == 0:
                raise GateError(
                    f"{stage} cannot complete: no completed model runs with "
                    "outputs — an audited stage cannot complete empty")
            if (latest.get("run_watermark") != watermark
                    or latest.get("artifacts_digest") != digest):
                raise GateError(
                    f"{stage} cannot complete: model output was produced or "
                    "changed AFTER the passing audit (evidence binding, "
                    "rehashed from current bytes) — re-audit the current "
                    "artifact set")
    if status in ("in_progress", "complete"):
        post_gate1 = STAGES.index(stage) >= STAGES.index("s2_survey")
        if post_gate1 and state["gates"]["gate1_directives"]["status"] != "ratified":
            raise GateError(f"{stage} requires Gate 1 (directive ratification by Doug) — "
                            f"current gate1 status: {state['gates']['gate1_directives']['status']}")
        if stage == "s5_canonical_intake":
            g2 = state["gates"]["gate2_rulings"]
            dep = state["dependencies"]["music_file_intake"]
            if g2["status"] != "ruled":
                raise GateError("Stage 5 requires Gate 2 rulings by Doug")
            if dep["status"] != "verified":
                raise GateError("Stage 5 requires a verified music-file-intake dependency "
                                "— stop with a handoff, never imitate the Gate")
            allow_errs = validate_allowlist(state)
            if allow_errs:
                raise GateError("Stage 5 allowlist enforcement failed:\n  - " +
                                "\n  - ".join(allow_errs))
    entry = state["stages"][stage]
    entry["status"] = status
    if status == "in_progress" and not entry["started_at"]:
        entry["started_at"] = _now()
    if status == "complete":
        entry["completed_at"] = _now()
    return entry


def verify_intake_dependency(state, search_roots):
    """Hard Stage-5 dependency check. Verified = SKILL.md found in a root;
    checksum recorded. Unavailable = blocking anomaly, caller stops with handoff."""
    dep = state["dependencies"]["music_file_intake"]
    for root in search_roots:
        cand = os.path.join(root, "music-file-intake", "SKILL.md")
        if os.path.exists(cand):
            dep.update({"status": "verified", "location": cand,
                        "version_or_checksum": sha256_file(cand),
                        "verified_at": _now()})
            return True
    dep.update({"status": "unavailable", "location": None,
                "version_or_checksum": None, "verified_at": _now()})
    add_anomaly(state, "dependency_missing",
                "music-file-intake not found in any search root — Stage 5 blocked; "
                "write a handoff, do not imitate the Gate",
                blocking=True, scope="s5_canonical_intake")
    return False


# ---------------------------------------------------------------- progress view

def render_progress(state):
    p = state["program"]
    g1, g2 = state["gates"]["gate1_directives"], state["gates"]["gate2_rulings"]
    mark = {"pending": "[ ]", "in_progress": "[~]", "complete": "[x]", "blocked": "[!]"}
    lines = [
        "---",
        "type: progress_tracker",
        f'program: "corpus-harvest: {p["source_slug"]}"',
        f'generated: "{_now()}"',
        "---",
        "",
        f"# corpus-harvest — {p['source_slug']} — PROGRESS",
        "",
        "*This file is generated from STATE.json (the machine authority). "
        "Do not tick boxes here — they will be overwritten.*",
        "",
        f"**Source:** {p['source_locator']}  ",
        f"**Adapter:** {p['adapter']}  ",
        f"**Staging root:** {p['staging_root']}",
        "",
        "## Stages",
        "",
    ]
    for s in STAGES:
        e = state["stages"][s]
        extra = ""
        if e.get("chunk_progress"):
            done = sum(1 for v in e["chunk_progress"].values() if v == "complete")
            extra = f" — chunks {done}/{len(e['chunk_progress'])}"
        if s == "s2_survey":
            lines.append(f"- **Gate 1 · Directive ratification (Doug):** {g1['status']}")
        if s == "s5_canonical_intake":
            lines.append(f"- **Gate 2 · Doug's rulings:** {g2['status']}")
        lines.append(f"- {mark[e['status']]} {STAGE_TITLES[s]}{extra}")
    open_anoms = [a for a in state["anomalies"] if a["status"] in ("open", "for_doug")]
    lines += ["", "## Open anomalies", ""]
    if open_anoms:
        for a in open_anoms:
            flag = " **BLOCKING**" if a.get("blocking") else ""
            lines.append(f"- `{a['anomaly_id']}` ({a['kind']}{flag}) {a['description']}")
    else:
        lines.append("- none")
    bs = budget_status(state)
    if bs:
        lines += ["", "## Budget", ""]
        for s2, v in bs.items():
            flag = " ⚠️ **EXCEEDED**" if v["exceeded"] else ""
            ceil = v["ceiling_tokens"] if v["ceiling_tokens"] is not None else "no ceiling set"
            lines.append(f"- {s2}: {v['used_tokens']} used + "
                         f"{v['reserved_tokens']} reserved / {ceil} "
                         f"(max tier {v['max_tier']}){flag}")
    lines += ["", f"## Runs ({len(state['runs'])})", ""]
    for r in state["runs"][-10:]:
        lines.append(f"- {r['run_id']} · {r['stage']} · {r['assistant']} · {r['status']}")
    if len(state["runs"]) > 10:
        lines.append(f"- … ({len(state['runs']) - 10} earlier runs in STATE.json)")
    return "\n".join(lines) + "\n"


def write_progress(root, state):
    with open(os.path.join(root, "PROGRESS.md"), "w", encoding="utf-8") as f:
        f.write(render_progress(state))


# ---------------------------------------------------------------- CLI

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("validate", "render", "show"):
        s = sub.add_parser(name)
        s.add_argument("--root", required=True)
    s = sub.add_parser("init")
    for flag in ("--root", "--source-slug", "--adapter", "--locator",
                 "--assistant", "--skill-version"):
        s.add_argument(flag, required=True)
    s.add_argument("--word-limit", type=int, default=90000)
    s.add_argument("--token-ceiling", type=int, default=120000)
    s = sub.add_parser("verify-intake")
    s.add_argument("--root", required=True)
    s.add_argument("--skill-roots", nargs="+", required=True)
    # --- gate-recording commands: STATE.json is never hand-edited ---
    s = sub.add_parser("gate1-propose",
                       help="record the Gate-1 proposal file (status: proposed)")
    s.add_argument("--root", required=True)
    s.add_argument("--proposal-file", required=True)
    s = sub.add_parser("gate1-ratify",
                       help="record Doug's Gate-1 ratification; freezes the sha256 "
                            "of the RECORDED proposal file (requires gate1-propose "
                            "first) and the numerical audit policy")
    s.add_argument("--root", required=True)
    s.add_argument("--ratified-by", required=True)
    s.add_argument("--recall-threshold", required=True, type=float)
    s.add_argument("--attribution-threshold", required=True, type=float)
    s.add_argument("--sample-fraction", required=True, type=float)
    s = sub.add_parser("gate2-rule",
                       help="record one of Doug's Gate-2 rulings on a candidate file")
    s.add_argument("--root", required=True)
    s.add_argument("--file", required=True)
    s.add_argument("--ruling", required=True,
                   choices=["approved", "approved_with_edits", "rejected", "deferred"])
    s.add_argument("--destination", default=None)
    s.add_argument("--credit-notes", default=None)
    s = sub.add_parser("gate2-disposition",
                       help="record the staging folder's disposition (Hard Rail #8: deletion only by proposal)")
    s.add_argument("--root", required=True)
    s.add_argument("--disposition", required=True,
                   choices=["retain", "relocate_proposed", "deletion_proposed"])
    s.add_argument("--detail", default=None)
    s = sub.add_parser("gate2-close",
                       help="close Gate 2 (requires rulings + disposition)")
    s.add_argument("--root", required=True)
    s = sub.add_parser("build-allowlist",
                       help="build the Stage-5 allowlist from Gate-2 approved rulings (re-verifies hashes)")
    s.add_argument("--root", required=True)
    s = sub.add_parser("set-stage",
                       help="record a stage transition (gate rails enforced)")
    s.add_argument("--root", required=True)
    s.add_argument("--stage", required=True, choices=STAGES)
    s.add_argument("--status", required=True,
                   choices=["pending", "in_progress", "complete", "blocked"])
    s = sub.add_parser("set-budget",
                       help="record Doug's budget ruling for one scope: ceiling + max authorized tier")
    s.add_argument("--root", required=True)
    s.add_argument("--scope", required=True, choices=BUDGET_SCOPES)
    s.add_argument("--ceiling", required=True, type=int)
    s.add_argument("--max-tier", default="balanced",
                   choices=["economy", "balanced", "frontier"])
    s.add_argument("--approved-by", required=True)
    s = sub.add_parser("budget-status",
                       help="usage + reservations vs ceiling per scope; exits 1 (+ blocking anomaly) on any excess")
    s.add_argument("--root", required=True)
    s = sub.add_parser("model-run-start",
                       help="atomic pre-dispatch gate: reserves max tokens against the scope ceiling; enforces tier authority + concurrency")
    s.add_argument("--root", required=True)
    s.add_argument("--scope", required=True, choices=BUDGET_SCOPES)
    s.add_argument("--model", required=True)
    s.add_argument("--max-tokens", required=True, type=int)
    s.add_argument("--assistant", required=True)
    s.add_argument("--input-file", action="append", required=True,
                   help="repeatable; staging-contained regular file hashed into the run record")
    s.add_argument("--directive", default=None)
    s.add_argument("--chunk", default=None)
    s.add_argument("--escalation-reason", default=None)
    s.add_argument("--notes", default=None)
    s = sub.add_parser("model-run-finish",
                       help="complete a model run: requires nonnegative actual tokens + at least one output file to hash")
    s.add_argument("--root", required=True)
    s.add_argument("--run-id", required=True)
    s.add_argument("--tokens-in", required=True, type=int)
    s.add_argument("--tokens-out", required=True, type=int)
    s.add_argument("--output-file", action="append", required=True,
                   help="repeatable; each is hashed into the run record")
    s = sub.add_parser("model-run-abort")
    s.add_argument("--root", required=True)
    s.add_argument("--run-id", required=True)
    s.add_argument("--reason", required=True)
    s = sub.add_parser("migrate-state",
                       help="explicit, recorded 1.0 -> 1.1 STATE migration (backup + pre-hash preserved)")
    s.add_argument("--root", required=True)
    s.add_argument("--by", required=True)
    s = sub.add_parser("resolve-anomaly",
                       help="resolve a blocking anomaly through a recorded ruling — the only way it stops blocking")
    s.add_argument("--root", required=True)
    s.add_argument("--id", required=True, dest="anomaly_id")
    s.add_argument("--ruling", required=True)
    s.add_argument("--by", required=True)
    s = sub.add_parser("record-audit",
                       help="record a duplicate-audit result for an audited stage; below-threshold results raise the blocking stop-rule anomaly")
    s.add_argument("--root", required=True)
    s.add_argument("--stage", required=True, choices=list(AUDITED_STAGES))
    s.add_argument("--recall", required=True, type=float)
    s.add_argument("--attribution", required=True, type=float)
    s.add_argument("--sample-fraction", required=True, type=float)
    s.add_argument("--by", required=True)
    a = ap.parse_args(argv)
    root = getattr(a, "root", None)
    if root:
        # every command serializes on the staging lock across its whole
        # reload -> validate -> mutate -> write cycle (2026-08-28 P0)
        with state_lock(root):
            return _run_command(a)
    return _run_command(a)


def _run_command(a):
    if a.cmd == "migrate-state":
        try:
            migrate_state(a.root, a.by)
        except StateError as e:
            print(f"REFUSED: {e}", file=sys.stderr)
            return 1
        print(f"migrated to schema {SCHEMA_VERSION} (recorded)")
        return 0

    if a.cmd == "init":
        st = init_state(a.root, a.source_slug, a.adapter, a.locator,
                        a.assistant, a.skill_version, a.word_limit, a.token_ceiling)
        write_progress(a.root, st)
        print(f"initialized {os.path.join(a.root, STATE_NAME)}")
        return 0
    st = load_state(a.root)
    if a.cmd == "validate":
        errs = validate_state(st)
        for e in errs:
            print(f"ERROR: {e}", file=sys.stderr)
        print("valid" if not errs else f"{len(errs)} error(s)")
        return 1 if errs else 0
    if a.cmd == "render":
        write_progress(a.root, st)
        print("PROGRESS.md written")
        return 0
    if a.cmd == "show":
        json.dump(st, sys.stdout, indent=2)
        print()
        return 0
    if a.cmd == "verify-intake":
        ok = verify_intake_dependency(st, a.skill_roots)
        save_state(a.root, st)
        write_progress(a.root, st)
        print("verified" if ok else "UNAVAILABLE — Stage 5 blocked; write a handoff")
        return 0 if ok else 1
    try:
        if a.cmd == "gate1-propose":
            rel = propose_gate1(st, a.proposal_file)
            msg = f"Gate 1: proposal recorded ({rel})"
        elif a.cmd == "gate1-ratify":
            ratify_gate1(st, a.ratified_by, audit_policy={
                "recall_threshold": a.recall_threshold,
                "attribution_threshold": a.attribution_threshold,
                "sample_fraction": a.sample_fraction})
            g1 = st["gates"]["gate1_directives"]
            msg = (f"Gate 1: RATIFIED by {a.ratified_by}; proposal "
                   f"{g1['proposal_file']} frozen "
                   f"(sha256 {g1['directive_set_hash'][:12]}…); audit policy "
                   f"recorded {g1['audit_policy']}")
        elif a.cmd == "gate2-rule":
            r = record_gate2_ruling(st, a.file, a.ruling,
                                    a.destination, a.credit_notes)
            msg = f"Gate 2: {r['ruling']} — {r['candidate_file']} ({r['sha256'][:12]}…)"
        elif a.cmd == "gate2-disposition":
            record_gate2_disposition(st, a.disposition, a.detail)
            msg = f"Gate 2: staging disposition recorded — {a.disposition}"
        elif a.cmd == "gate2-close":
            close_gate2(st)
            msg = "Gate 2: CLOSED (ruled)"
        elif a.cmd == "build-allowlist":
            allow = build_allowlist(st)
            msg = f"Stage-5 allowlist built: {len(allow)} approved file(s), hashes re-verified"
        elif a.cmd == "set-stage":
            set_stage(st, a.stage, a.status)
            msg = f"{a.stage} -> {a.status}"
        elif a.cmd == "set-budget":
            set_budget(st, a.scope, a.ceiling, a.approved_by, a.max_tier)
            msg = (f"budget: {a.scope} ceiling {a.ceiling} tokens, max tier "
                   f"{a.max_tier} (approved by {a.approved_by})")
        elif a.cmd == "model-run-start":
            inputs = hash_input_files(st, a.input_file)
            run = start_model_run(st, a.scope, a.assistant, a.model,
                                  a.max_tokens, input_hashes=inputs,
                                  directive_id=a.directive,
                                  chunk_id=a.chunk,
                                  escalation_reason=a.escalation_reason,
                                  notes=a.notes)
            msg = (f"{run['run_id']}: {a.model} ({run['model_tier']}) on "
                   f"{a.scope}, {a.max_tokens} tokens reserved")
        elif a.cmd == "model-run-finish":
            runs = {r["run_id"]: r for r in st["runs"]}
            if a.run_id not in runs:
                raise StateError(f"no run {a.run_id}")
            hashes = hash_output_files(st, a.output_file)
            finish_model_run(st, runs[a.run_id], a.tokens_in, a.tokens_out, hashes)
            msg = (f"{a.run_id} complete: {a.tokens_in}+{a.tokens_out} tokens, "
                   f"{len(hashes)} output hash(es)")
        elif a.cmd == "record-audit":
            entry = record_audit_result(st, a.stage, a.recall, a.attribution,
                                        a.sample_fraction, a.by)
            msg = (f"audit recorded for {a.stage}: "
                   f"{'PASSED' if entry['passed'] else 'FAILED — STOP'}")
        elif a.cmd == "resolve-anomaly":
            an = resolve_anomaly(st, a.anomaly_id, a.ruling, a.by)
            msg = f"{an['anomaly_id']} resolved by {a.by}: {a.ruling[:70]}"
        elif a.cmd == "model-run-abort":
            runs = {r["run_id"]: r for r in st["runs"]}
            if a.run_id not in runs:
                raise StateError(f"no run {a.run_id}")
            abort_model_run(st, runs[a.run_id], a.reason)
            msg = f"{a.run_id} aborted (reservation released)"
        elif a.cmd == "budget-status":
            bs = budget_status(st)
            exceeded = [s2 for s2, v in bs.items() if v["exceeded"]]
            for s2, v in bs.items():
                flag = " EXCEEDED" if v["exceeded"] else ""
                print(f"{s2}: used {v['used_tokens']} + reserved "
                      f"{v['reserved_tokens']} / ceiling {v['ceiling_tokens']} "
                      f"(max tier {v['max_tier']}){flag}")
            if not bs:
                print("no budgets or model usage recorded")
            if exceeded:
                for s2 in exceeded:
                    add_anomaly(st, "other",
                                f"token ceiling exceeded for {s2} "
                                f"({bs[s2]['used_tokens']}+{bs[s2]['reserved_tokens']} "
                                f"> {bs[s2]['ceiling_tokens']}) — stop; Doug "
                                "approves any new ceiling", blocking=True,
                                scope=s2)
                save_state(a.root, st)
                write_progress(a.root, st)
                print("CEILING EXCEEDED — blocking anomaly recorded", file=sys.stderr)
                return 1
            return 0
        else:
            print(f"unknown command: {a.cmd}", file=sys.stderr)
            return 2
    except (GateError, StateError) as e:
        print(f"REFUSED: {e}", file=sys.stderr)
        return 1
    save_state(a.root, st)
    write_progress(a.root, st)
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
