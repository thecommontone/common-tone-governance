#!/usr/bin/env python3
"""corpus-harvest citation validator (new work — the reference had none).

String-matches every verbatim quote (relation: quotation) into the item's
SEGMENTS sidecar and attaches the time range mechanically. Matching runs
through THE PROJECT'S SHARED PROSE NORMALIZER
(03_ENGINES_AND_TOOLS/web-projection/merge_report.py::norm) — P4: no ad-hoc
matching, ever. If the normalizer is unreachable this script EXITS 2 and
writes nothing: fail closed, never fall back to a private normalizer.

Verdicts per record:
  verified     exactly one match, verbatim-grade transcript
  approximate  exactly one match, but ASR/mixed-origin (barred from
               print-candidate status until checked against audio)
  ambiguous    multiple matches — FAILS CLOSED, no time range, human review
  not_found    zero matches — FAILS CLOSED
Non-quotation records (paraphrase/synthesis) pass through untouched.
Exit 0 only when every quotation is verified or approximate.
"""
import argparse, csv, importlib.util, json, os, sys

import state as S


def load_normalizer(path):
    if not path or not os.path.isfile(path):
        return None
    spec = importlib.util.spec_from_file_location("ct_shared_normalizer", path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception:
        return None
    return getattr(mod, "norm", None)


def build_token_stream(segments, norm):
    """-> (tokens [str], seg_of_token [int]) over the normalized segment texts."""
    tokens, seg_of = [], []
    for i, seg in enumerate(segments):
        for t in norm(seg["text"]).split():
            tokens.append(t)
            seg_of.append(i)
    return tokens, seg_of


def find_occurrences(stream, query):
    if not query:
        return []
    hits, n, m = [], len(stream), len(query)
    for i in range(n - m + 1):
        if stream[i:i + m] == query:
            hits.append(i)
    return hits


def validate_record(rec, segments, norm):
    stream, seg_of = build_token_stream(segments, norm)
    query = norm(rec["quote_or_claim"]).split()
    hits = find_occurrences(stream, query)
    if not hits:
        rec["verification_status"] = "not_found"
        rec["time_range"] = None
    elif len(hits) > 1:
        rec["verification_status"] = "ambiguous"
        rec["time_range"] = None
    else:
        i = hits[0]
        first, last = seg_of[i], seg_of[i + len(query) - 1]
        rec["time_range"] = {"start_s": segments[first]["start_s"],
                             "end_s": segments[last]["end_s"]}
        asr_ish = (rec.get("quality_grade") in ("asr", "mixed")
                   or rec.get("transcript_origin") == "asr")
        rec["verification_status"] = "approximate" if asr_ish else "verified"
    return rec


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True)
    ap.add_argument("--records", required=True, help="extraction JSONL to validate")
    ap.add_argument("--normalizer", default=None,
                    help="path to merge_report.py; default from STATE.json "
                         "dependencies.prose_normalizer.location")
    a = ap.parse_args(argv)
    with S.state_lock(a.root):
        return _run_locked(a)


def _run_locked(a):
    root = a.root
    state = S.load_state(root)
    norm_path = a.normalizer or state["dependencies"]["prose_normalizer"]["location"]
    norm = load_normalizer(norm_path)
    if norm is None:
        print("FAIL CLOSED: shared prose normalizer not loadable at "
              f"{norm_path!r} (merge_report.py::norm). P4 forbids ad-hoc "
              "matching — nothing validated, nothing written.", file=sys.stderr)
        return 2
    state["dependencies"]["prose_normalizer"].update({
        "status": "verified", "location": os.path.abspath(norm_path),
        "checksum": S.sha256_file(norm_path),
        "verified_at": state["writer"]["updated_at"]})

    with open(os.path.join(root, "MANIFEST.csv"), encoding="utf-8") as f:
        manifest = {r["item_id"]: r for r in csv.DictReader(f)}

    records = []
    with open(a.records, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))

    seg_cache = {}
    counts = {"verified": 0, "approximate": 0, "ambiguous": 0,
              "not_found": 0, "passed_through": 0, "no_segments": 0}
    for rec in records:
        if rec.get("relation") != "quotation":
            counts["passed_through"] += 1
            continue
        item = manifest.get(rec["item_id"])
        segfile = item["segments_file"] if item else ""
        if not segfile:
            rec["verification_status"] = "not_found"
            rec["time_range"] = None
            counts["no_segments"] += 1
            continue
        if segfile not in seg_cache:
            with open(os.path.join(root, segfile), encoding="utf-8") as f:
                seg_cache[segfile] = [json.loads(l) for l in f if l.strip()]
        validate_record(rec, seg_cache[segfile], norm)
        counts[rec["verification_status"]] += 1

    out_path = os.path.splitext(a.records)[0] + ".validated.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    run = S.add_run(state, "s4_merge_validate", state["writer"]["last_writer"],
                    notes=f"citation validation: {counts}")
    run["input_hashes"][os.path.basename(a.records)] = S.sha256_file(a.records)
    run["output_hashes"][os.path.basename(out_path)] = S.sha256_file(out_path)
    failed = counts["ambiguous"] + counts["not_found"] + counts["no_segments"]
    for rec in records:
        if rec.get("relation") == "quotation" and \
                rec.get("verification_status") in ("ambiguous", "not_found"):
            S.add_anomaly(state, "citation_ambiguous",
                          f"{rec['record_id']}: {rec['verification_status']} — "
                          f"quote: {rec['quote_or_claim'][:80]!r}",
                          item_id=rec.get("item_id"))
    S.finish_run(run, "complete" if not failed else "failed")
    S.save_state(root, state)
    S.write_progress(root, state)

    print(f"validated -> {out_path}")
    print("  " + "  ".join(f"{k}: {v}" for k, v in counts.items()))
    if failed:
        print(f"FAILED CLOSED on {failed} record(s) — flagged for review, "
              "never auto-resolved.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
