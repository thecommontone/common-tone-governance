#!/usr/bin/env python3
"""corpus-harvest Stage 1: RAW/ -> SEGMENTS/ (timestamped JSONL) + TXT/ + MANIFEST.csv.

Lineage: 12TONE_CAPTIONS/vtt_to_txt.py (VTT cleaning, ASR heuristic, paragraph
flow, manifest, canonical-file selection). New work: timestamped SEGMENTS
sidecars (the reference discarded timestamps), quality checks for the failure
modes the 12tone agents caught by hand (doubled transcripts, unpunctuated
"human" files, corrupt items), grade provenance, STATE.json run recording.

Never modifies RAW/. Idempotent: rerun regenerates identical outputs and adds
no duplicate anomalies. Stdlib only.
"""
import argparse, csv, html, json, os, re, sys
from difflib import SequenceMatcher

import state as S

TAG = re.compile(r"<[^>]*>")
YT_FNAME = re.compile(r"^(\d{8})_([A-Za-z0-9_-]{11})_(.*)\.en\.vtt$")
TS_LINE = re.compile(
    r"^(\d{2}):(\d{2}):(\d{2})\.(\d{3})\s+-->\s+(\d{2}):(\d{2}):(\d{2})\.(\d{3})")


def _to_seconds(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def clean_cue_text(s):
    s = html.unescape(TAG.sub("", s)).replace("\xa0", " ").strip()
    return s


def parse_vtt(raw):
    """-> (segments [(start_s, end_s, text)], asr_flag). Consecutive duplicate
    cue texts (ASR rolling captions) collapse into the first cue."""
    asr = "<c>" in raw or "align:start position:0%" in raw
    segments, last_text = [], None
    cur_ts = None
    for line in raw.splitlines():
        s = line.strip()
        m = TS_LINE.match(s)
        if m:
            cur_ts = (_to_seconds(*m.groups()[:4]), _to_seconds(*m.groups()[4:]))
            continue
        if (not s or s == "WEBVTT" or s.isdigit()
                or s.startswith(("Kind:", "Language:", "NOTE", "STYLE"))):
            continue
        text = clean_cue_text(s)
        if not text or text == last_text:
            continue
        if cur_ts is None:
            continue
        # merge multi-line cues into the open segment for this timestamp
        if segments and segments[-1][0] == cur_ts[0] and segments[-1][1] == cur_ts[1]:
            segments[-1] = (cur_ts[0], cur_ts[1], segments[-1][2] + " " + text)
        else:
            segments.append((cur_ts[0], cur_ts[1], text))
        last_text = text
    return segments, asr


def flatten(words):
    """12tone paragraph flow: break at sentence end past 120 words, hard at 250."""
    paras, cur = [], []
    for w in words:
        cur.append(w)
        if (len(cur) >= 120 and w[-1] in ".!?") or len(cur) >= 250:
            paras.append(" ".join(cur)); cur = []
    if cur:
        paras.append(" ".join(cur))
    return "\n\n".join(paras) + "\n"


def assess_quality(text, words, asr_flag):
    """-> (grade, [(anomaly_kind, description), ...]).

    Encodes the mis-grade modes the 12tone program caught only by agent
    review: corrupt items, doubled transcripts, unpunctuated 'human' files.
    """
    anomalies = []
    n = len(words)
    if n < 5 or (n and text.count("�") / max(len(text), 1) > 0.02):
        return "corrupt", [("corrupt_item",
                            "content empty, near-empty, or dominated by replacement "
                            "characters — flag for re-fetch; not usable for extraction")]
    grade = "asr" if asr_flag else "verbatim"
    # doubled transcript: first half ~= second half
    half = n // 2
    if n >= 40:
        a, b = " ".join(words[:half]).lower(), " ".join(words[half:2 * half]).lower()
        if SequenceMatcher(None, a, b).ratio() > 0.85:
            grade = "mixed"
            anomalies.append(("doubled_transcript",
                              "transcript body repeats itself (first half ≈ second half) "
                              "— quotes will match twice; validator will fail closed on them"))
    # unpunctuated but not flagged asr: treat as asr-grade
    if not asr_flag and n > 50:
        sentence_marks = sum(1 for w in words if w and w[-1] in ".!?")
        if sentence_marks / n < 0.005:
            grade = "asr"
            anomalies.append(("misgraded_caption",
                              "no ASR markers but essentially unpunctuated — regraded "
                              "asr; quotes are approximate until checked against audio"))
    return grade, anomalies


def slugify(stem):
    s = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_").lower()
    return s or "item"


def discover_items(root, adapter, state):
    """-> (items [{...}], anomalies [(kind, description, item_id)]).
    Canonical selection per adapter. Never touches file contents here."""
    raw_dir = os.path.join(root, "RAW")
    items, anomalies = [], []
    seen_ids = set()
    for fn in sorted(os.listdir(raw_dir)):
        path = os.path.join(raw_dir, fn)
        if not os.path.isfile(path):
            continue
        if adapter == "youtube":
            if not fn.endswith(".en.vtt") or fn.endswith((".en-orig.vtt", ".en-en.vtt")):
                continue
            m = YT_FNAME.match(fn)
            if not m:
                anomalies.append(("other",
                                  f"filename does not match YYYYMMDD_<id>_<title>.en.vtt: {fn} "
                                  "— skipped, no manifest row", None))
                continue
            date, vid, title = m.groups()
            items.append({
                "item_id": vid,
                "published_at": f"{date[:4]}-{date[4:6]}-{date[6:]}",
                "title": title.replace("_", " "),
                "raw_file": os.path.join("RAW", fn),
                "kind": "vtt",
                "source_locator": f"https://www.youtube.com/watch?v={vid}",
            })
        else:  # local-folder
            stem, ext = os.path.splitext(fn)
            if ext.lower() not in (".vtt", ".txt"):
                continue
            item_id = slugify(stem)
            k = 2
            while item_id in seen_ids:
                item_id = f"{slugify(stem)}-{k}"; k += 1
            seen_ids.add(item_id)
            items.append({
                "item_id": item_id,
                "published_at": "",
                "title": stem.replace("_", " "),
                "raw_file": os.path.join("RAW", fn),
                "kind": "vtt" if ext.lower() == ".vtt" else "txt",
                "source_locator": os.path.join(state["program"]["source_locator"], fn),
            })
    return items, anomalies


def load_receipts(root):
    """item_id -> acquired_at, from RAW/_RECEIPTS/*.json if present."""
    rdir = os.path.join(root, "RAW", "_RECEIPTS")
    out = {}
    if not os.path.isdir(rdir):
        return out
    for fn in sorted(os.listdir(rdir)):
        if not fn.endswith(".json"):
            continue
        try:
            with open(os.path.join(rdir, fn), encoding="utf-8") as f:
                rec = json.load(f)
            out[rec.get("item_id", "")] = rec.get("acquired_at", "")
        except (json.JSONDecodeError, OSError):
            continue
    return out


def process(root):
    """All state mutation under the process-level staging lock — every
    package writer serializes through it (2026-08-28 round-4 P0-2)."""
    with S.state_lock(root):
        return _process_locked(root)


def _process_locked(root):
    state = S.load_state(root)
    adapter = state["program"]["adapter"]
    run = S.add_run(state, "s1_normalize", state["writer"]["last_writer"])
    receipts = load_receipts(root)
    default_acquired = state["program"]["created_at"]

    for d in ("SEGMENTS", "TXT"):
        os.makedirs(os.path.join(root, d), exist_ok=True)

    items, discovery_anoms = discover_items(root, adapter, state)
    for kind, desc, item_id in discovery_anoms:
        S.add_anomaly(state, kind, desc, item_id=item_id)

    rows = []
    for it in items:
        raw_path = os.path.join(root, it["raw_file"])
        with open(raw_path, encoding="utf-8", errors="replace") as f:
            raw = f.read()
        base = os.path.splitext(os.path.basename(it["raw_file"]))[0]
        if base.endswith(".en"):
            base = base[:-3]
        if it["kind"] == "vtt":
            segments, asr_flag = parse_vtt(raw)
            words = " ".join(t for _, _, t in segments).split()
            seg_rel = os.path.join("SEGMENTS", f"{it['item_id']}.jsonl")
            with open(os.path.join(root, seg_rel), "w", encoding="utf-8") as f:
                for i, (a, b, t) in enumerate(segments):
                    f.write(json.dumps({"item_id": it["item_id"], "seq": i,
                                        "start_s": a, "end_s": b, "text": t},
                                       ensure_ascii=False) + "\n")
        else:  # plain text: no timing data, no segments
            words = " ".join(clean_cue_text(l) for l in raw.splitlines()).split()
            asr_flag, seg_rel = False, ""
        text_flat = flatten(words) if words else "\n"
        grade, quality_anoms = assess_quality(text_flat, words, asr_flag)
        for kind, desc in quality_anoms:
            S.add_anomaly(state, kind, desc, item_id=it["item_id"])
        txt_rel = os.path.join("TXT", f"{base}.txt")
        with open(os.path.join(root, txt_rel), "w", encoding="utf-8") as f:
            f.write(text_flat)
        rows.append({
            "item_id": it["item_id"],
            "source_locator": it["source_locator"],
            "published_at": it["published_at"],
            "acquired_at": receipts.get(it["item_id"], default_acquired),
            "title": it["title"],
            "word_count": len(words),
            "quality_grade": grade,
            "grade_provenance": "auto",
            "raw_file": it["raw_file"],
            "txt_file": txt_rel,
            "segments_file": seg_rel,
            "notes": "",
        })

    rows.sort(key=lambda r: (r["published_at"] == "", r["published_at"], r["item_id"]))
    man_path = os.path.join(root, "MANIFEST.csv")
    with open(man_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else
                           ["item_id", "source_locator", "published_at", "acquired_at",
                            "title", "word_count", "quality_grade", "grade_provenance",
                            "raw_file", "txt_file", "segments_file", "notes"])
        w.writeheader()
        w.writerows(rows)

    run["output_hashes"]["MANIFEST.csv"] = S.sha256_file(man_path)
    S.finish_run(run)
    S.set_stage(state, "s1_normalize", "complete")
    S.save_state(root, state)
    S.write_progress(root, state)

    total = sum(int(r["word_count"]) for r in rows)
    grades = {}
    for r in rows:
        grades[r["quality_grade"]] = grades.get(r["quality_grade"], 0) + 1
    print(f"items: {len(rows)}  total words: {total}  grades: {grades}")
    open_anoms = [a for a in state["anomalies"] if a["status"] == "open"]
    print(f"open anomalies: {len(open_anoms)} (see PROGRESS.md / STATE.json)")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True, help="staging root containing RAW/ and STATE.json")
    a = ap.parse_args(argv)
    return process(a.root)


if __name__ == "__main__":
    sys.exit(main())
