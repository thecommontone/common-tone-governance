#!/usr/bin/env python3
"""corpus-harvest Stage 0 adapter: local-folder — a recorded product feature.

Added 2026-08-28 after the step-3 dry run exposed that local acquisition
existed only as SKILL.md prose performed by hand (Codex review, finding 1).

Copies Doug's transcript files (.vtt/.txt) from the source folder into
staging RAW/, writes one sha256 acquisition receipt per item, records a
Stage-0 run in STATE.json, and marks s0_acquire complete. The source folder
is READ-ONLY — never modified. YouTube-scrape caption variants
(.en-orig.vtt / .en-en.vtt) are excluded by default as duplicates (pass
--include-variants to take everything); exclusions are counted, receipted in
notes, and reported — never deleted.

Idempotent: a rerun re-verifies existing copies by hash instead of
re-copying, adds no duplicate receipts, and fails loudly if a staged copy no
longer matches its receipt.
"""
import argparse, datetime, fnmatch, hashlib, json, os, shutil, sys

import state as S
from normalize import slugify

VARIANT_SUFFIXES = (".en-orig.vtt", ".en-en.vtt")
TAKE_EXTS = (".vtt", ".txt")


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def acquire(root, source, include_variants=False, select=None):
    """All state mutation under the process-level staging lock (round-4 P0-2)."""
    with S.state_lock(root):
        return _acquire_locked(root, source, include_variants, select)


def _acquire_locked(root, source, include_variants=False, select=None):
    state = S.load_state(root)
    if state["program"]["adapter"] != "local-folder":
        print(f"REFUSED: program adapter is {state['program']['adapter']!r}, "
              "not local-folder", file=sys.stderr)
        return 1
    source = os.path.realpath(os.path.abspath(source))
    if not os.path.isdir(source):
        print(f"REFUSED: source folder not found: {source}", file=sys.stderr)
        return 1
    raw = os.path.join(root, "RAW")
    rdir = os.path.join(raw, "_RECEIPTS")
    os.makedirs(rdir, exist_ok=True)

    run = S.add_run(state, "s0_acquire", state["writer"]["last_writer"],
                    notes=f"local-folder acquire from {source}"
                          + (f"; select={select!r}" if select else "")
                          + ("; variants included" if include_variants else ""))
    existing = {}
    for fn in os.listdir(rdir):
        if fn.endswith(".json"):
            with open(os.path.join(rdir, fn), encoding="utf-8") as f:
                rec = json.load(f)
            for entry in rec.get("files", []):
                existing[entry["path"]] = entry["sha256"]

    now = _now()
    copied = verified = skipped_variants = 0
    seen_ids = set(iid[:-5] for iid in os.listdir(rdir) if iid.endswith(".json"))
    mismatches = []
    for fn in sorted(os.listdir(source)):
        src_path = os.path.join(source, fn)
        if not os.path.isfile(src_path):
            continue
        if not fn.lower().endswith(TAKE_EXTS):
            continue
        if select and not fnmatch.fnmatch(fn, select):
            skipped_variants += 1
            continue
        if not include_variants and fn.endswith(VARIANT_SUFFIXES):
            skipped_variants += 1
            continue
        rel = os.path.join("RAW", fn)
        dst = os.path.join(root, rel)
        src_hash = S.sha256_file(src_path)
        if rel in existing:
            actual = S.sha256_file(dst) if os.path.isfile(dst) else None
            if actual != existing[rel]:
                mismatches.append(rel)
            else:
                verified += 1
            continue
        shutil.copy2(src_path, dst)
        dst_hash = S.sha256_file(dst)
        if dst_hash != src_hash:
            print(f"ERROR: copy hash mismatch for {fn} — aborting", file=sys.stderr)
            S.finish_run(run, "failed")
            S.save_state(root, state)
            return 1
        item_id = slugify(os.path.splitext(fn)[0])
        k = 2
        while item_id in seen_ids:
            item_id = f"{slugify(os.path.splitext(fn)[0])}-{k}"; k += 1
        seen_ids.add(item_id)
        receipt = {
            "item_id": item_id, "adapter": "local-folder",
            "source_locator": src_path, "source_url": None,
            "published_at": None, "acquired_at": now,
            "tool": {"name": "acquire_local.py",
                     "version": state["skill"]["version"]},
            "files": [{"path": rel, "sha256": dst_hash,
                       "bytes": os.path.getsize(dst)}],
            "notes": (None if include_variants else
                      "scrape variants (.en-orig/.en-en) excluded as duplicates; "
                      "left untouched in the source folder"),
        }
        with open(os.path.join(rdir, f"{item_id}.json"), "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=1)
        run["output_hashes"][rel] = dst_hash
        copied += 1

    if mismatches:
        for rel in mismatches:
            S.add_anomaly(state, "checksum_mismatch",
                          f"staged copy no longer matches its acquisition receipt: {rel}",
                          blocking=True)
        S.finish_run(run, "failed")
        S.save_state(root, state)
        S.write_progress(root, state)
        print(f"FAILED: {len(mismatches)} staged file(s) differ from their "
              "receipts — see anomalies; RAW/ is never silently rewritten",
              file=sys.stderr)
        return 1

    if copied + verified == 0:
        # zero acquisitions is a failure, not a success (2026-08-28 dry-run
        # review 2): a selection that matches nothing must not mark Stage 0
        # complete
        S.finish_run(run, "failed")
        S.save_state(root, state)
        S.write_progress(root, state)
        print("FAILED: no files matched the selection — 0 acquired, 0 verified "
              f"({skipped_variants} excluded). Check --select/--include-variants "
              "and the source folder; Stage 0 left incomplete.", file=sys.stderr)
        return 1

    S.finish_run(run)
    S.set_stage(state, "s0_acquire", "complete")
    S.save_state(root, state)
    S.write_progress(root, state)
    print(f"acquired: {copied} new, {verified} verified existing, "
          f"{skipped_variants} excluded by selection/variant rules (not deleted); "
          f"receipts in RAW/_RECEIPTS/")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True, help="staging root with STATE.json")
    ap.add_argument("--source", required=True, help="Doug's transcript folder (read-only)")
    ap.add_argument("--include-variants", action="store_true",
                    help="also take .en-orig.vtt/.en-en.vtt scrape variants")
    ap.add_argument("--select", default=None, metavar="GLOB",
                    help="only take files matching this glob (e.g. '*.en.vtt' "
                         "for a youtube-scrape folder with stray part-"
                         "translations); recorded in the run notes")
    a = ap.parse_args(argv)
    return acquire(a.root, a.source, a.include_variants, a.select)


if __name__ == "__main__":
    sys.exit(main())
