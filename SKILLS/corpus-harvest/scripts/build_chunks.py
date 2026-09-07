#!/usr/bin/env python3
"""corpus-harvest chunk planner: MANIFEST.csv -> CHUNKS.csv.

Lineage: the chunking half of 12tone vtt_to_txt.py (greedy consecutive
chronological fill, <= word_limit per chunk). New work: the limit comes from
STATE.json's frozen chunk_policy; an unchanged plan is an idempotent no-op;
a CHANGED plan requires --rechunk REASON and is recorded in rechunk_history
(retired plan hash + reason) — never an ad-hoc recalculation. Oversized single
items get their own chunk and an anomaly.
"""
import argparse, csv, hashlib, os, sys

import state as S

CHUNK_FIELDS = ["chunk", "item_id", "published_at", "title",
                "word_count", "quality_grade", "txt_file"]


def read_manifest(root):
    with open(os.path.join(root, "MANIFEST.csv"), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def plan_chunks(rows, word_limit):
    chunks, cur, cur_w = [], [], 0
    oversized = []
    for r in rows:
        wc = int(r["word_count"])
        if wc > word_limit:
            if cur:
                chunks.append(cur); cur, cur_w = [], 0
            chunks.append([r])
            oversized.append(r["item_id"])
            continue
        if cur and cur_w + wc > word_limit:
            chunks.append(cur); cur, cur_w = [], 0
        cur.append(r); cur_w += wc
    if cur:
        chunks.append(cur)
    return chunks, oversized


def render_rows(chunks):
    out = []
    for i, ch in enumerate(chunks, 1):
        for r in ch:
            out.append({"chunk": f"{i:02d}", "item_id": r["item_id"],
                        "published_at": r["published_at"], "title": r["title"],
                        "word_count": r["word_count"],
                        "quality_grade": r["quality_grade"],
                        "txt_file": r["txt_file"]})
    return out


def plan_hash(rows):
    h = hashlib.sha256()
    for r in rows:
        h.update(("|".join(r[k] for k in CHUNK_FIELDS)).encode("utf-8"))
    return h.hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--rechunk", metavar="REASON", default=None,
                    help="required to replace an existing, different chunk plan; "
                         "the reason is recorded in STATE.json rechunk_history")
    a = ap.parse_args(argv)
    with S.state_lock(a.root):
        return _run_locked(a)


def _run_locked(a):
    root = a.root
    state = S.load_state(root)
    limit = state["chunk_policy"]["word_limit"]
    rows = read_manifest(root)
    chunks, oversized = plan_chunks(rows, limit)
    new_rows = render_rows(chunks)
    new_hash = plan_hash(new_rows)

    chunks_path = os.path.join(root, "CHUNKS.csv")
    arts = state["stages"]["s2_survey"]["artifacts"] or {}
    old_hash = arts.get("CHUNKS.csv")

    if old_hash == new_hash and os.path.exists(chunks_path):
        print(f"chunk plan unchanged ({len(chunks)} chunks) — no-op")
        return 0
    if old_hash and old_hash != new_hash:
        if not a.rechunk:
            print("REFUSED: a different chunk plan already exists. Re-chunking is an "
                  "explicit, recorded STATE operation — rerun with --rechunk REASON.",
                  file=sys.stderr)
            return 1
        state["chunk_policy"]["rechunk_history"].append({
            "retired_plan_hash": old_hash, "reason": a.rechunk,
            "at": state["writer"]["updated_at"],
            "by": state["writer"]["last_writer"]})

    run = S.add_run(state, "s2_survey", state["writer"]["last_writer"],
                    notes="chunk plan build")
    with open(chunks_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CHUNK_FIELDS)
        w.writeheader()
        w.writerows(new_rows)
    for item_id in oversized:
        S.add_anomaly(state, "other",
                      f"item exceeds word_limit {limit} alone — isolated in its own "
                      "chunk; consider splitting upstream or raising the limit by "
                      "recorded re-chunk", item_id=item_id)
    arts["CHUNKS.csv"] = new_hash
    state["stages"]["s2_survey"]["artifacts"] = arts
    run["output_hashes"]["CHUNKS.csv"] = S.sha256_file(chunks_path)
    S.finish_run(run)
    S.save_state(root, state)
    S.write_progress(root, state)
    sizes = [sum(int(r["word_count"]) for r in ch) for ch in chunks]
    print(f"chunks: {len(chunks)}  sizes: {sizes}  oversized-isolated: {len(oversized)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
