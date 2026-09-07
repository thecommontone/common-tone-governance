#!/usr/bin/env python3
"""corpus-harvest targeting-map builder: TARGETS.csv x MANIFEST.csv -> D<NN>_CHUNKS.csv.

Lineage: the 12tone program's manual TARGETS->D<NN>_CHUNKS join. Accepts the
new column set (item_id, directive, note) and the legacy 12tone one
(video_id, date, title, directive, note). FAIL CLOSED: a target row whose
item is not in the manifest aborts the whole build for that directive —
no partial map is written (P7: refuse over guess).
"""
import argparse, csv, os, sys

import state as S

OUT_FIELDS = ["chunk", "item_id", "published_at", "title", "word_count",
              "quality_grade", "txt_file", "phase1_note"]


def read_targets(path):
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        item = r.get("item_id") or r.get("video_id")
        directive = (r.get("directive") or "").strip()
        # normalize D1 -> D01
        if directive.startswith("D") and directive[1:].isdigit():
            directive = f"D{int(directive[1:]):02d}"
        out.append({"item_id": (item or "").strip(), "directive": directive,
                    "note": (r.get("note") or "").strip()})
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--targets", default=None,
                    help="default: <root>/EXTRACTIONS/TARGETS.csv")
    ap.add_argument("--directive", required=True, help="e.g. D01")
    a = ap.parse_args(argv)
    with S.state_lock(a.root):
        return _run_locked(a)


def _run_locked(a):
    root = a.root
    targets_path = a.targets or os.path.join(root, "EXTRACTIONS", "TARGETS.csv")
    directive = a.directive if not a.directive[1:].isdigit() \
        else f"D{int(a.directive[1:]):02d}"

    state = S.load_state(root)
    with open(os.path.join(root, "MANIFEST.csv"), encoding="utf-8") as f:
        manifest = {r["item_id"]: r for r in csv.DictReader(f)}

    targets = [t for t in read_targets(targets_path) if t["directive"] == directive]
    if not targets:
        print(f"no targets for {directive} in {targets_path}", file=sys.stderr)
        return 1
    unknown = [t["item_id"] for t in targets if t["item_id"] not in manifest]
    if unknown:
        print(f"FAIL CLOSED: {len(unknown)} target item(s) not in MANIFEST.csv: "
              f"{unknown} — no map written; fix TARGETS.csv or re-run normalize",
              file=sys.stderr)
        return 1

    limit = state["chunk_policy"]["word_limit"]
    rows = sorted((dict(manifest[t["item_id"]], phase1_note=t["note"]) for t in targets),
                  key=lambda r: (r["published_at"] == "", r["published_at"], r["item_id"]))
    chunks, cur, cur_w = [], [], 0
    for r in rows:
        wc = int(r["word_count"])
        if cur and cur_w + wc > limit:
            chunks.append(cur); cur, cur_w = [], 0
        cur.append(r); cur_w += wc
    if cur:
        chunks.append(cur)

    out_path = os.path.join(root, "EXTRACTIONS", f"{directive}_CHUNKS.csv")
    run = S.add_run(state, "s3_deep_passes", state["writer"]["last_writer"],
                    directive_id=directive, notes="targeting map build")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_FIELDS, extrasaction="ignore")
        w.writeheader()
        for i, ch in enumerate(chunks, 1):
            for r in ch:
                w.writerow(dict(r, chunk=f"{i:02d}"))
    run["output_hashes"][os.path.basename(out_path)] = S.sha256_file(out_path)
    S.finish_run(run)
    S.save_state(root, state)
    print(f"{directive}: {len(rows)} items in {len(chunks)} chunk(s) -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
