# MANIFEST.csv — column spec (corpus-harvest)

Written by `normalize.py`, one row per canonical corpus item, sorted by
(`published_at`, `item_id`) with null `published_at` rows last, sorted by
`item_id`. UTF-8, header row required. Lineage: the 12tone MANIFEST.csv
(`video_id, upload_date, title, word_count, caption_grade, txt_file`),
generalized for platform-agnostic sources and grade provenance.

| Column | Required | Values / format | Notes |
|---|---|---|---|
| `item_id` | yes | adapter-assigned, unique | YouTube: 11-char video ID. local-folder: slug derived from filename, disambiguated `-2`, `-3` on collision |
| `source_locator` | yes | URL / path / feed ref | per item |
| `published_at` | no | `YYYY-MM-DD` or empty | empty when the source carries no date (e.g. bare local files) |
| `acquired_at` | yes | ISO date-time | from the acquisition receipt |
| `title` | yes | free text | underscores from filenames rendered as spaces |
| `word_count` | yes | integer | words in the flattened TXT |
| `quality_grade` | yes | `verbatim` \| `asr` \| `mixed` \| `corrupt` | `verbatim` = creator-provided captions/transcript; heuristics per normalize.py |
| `grade_provenance` | yes | `auto` \| `agent` \| `doug` | who assigned the current grade; agent corrections overwrite `auto` and log an anomaly |
| `raw_file` | yes | path relative to staging root | under `RAW/`; never modified |
| `txt_file` | yes | path relative to staging root | under `TXT/` |
| `segments_file` | yes | path relative to staging root, or empty | under `SEGMENTS/`; empty only for sources with no timing data (plain-text local files) |
| `notes` | no | free text | short; anything longer becomes a STATE.json anomaly |

Rules:

- The manifest is regenerated idempotently from `RAW/` + receipts; agent/doug
  grade corrections live in STATE.json anomalies and are re-applied on
  regeneration (the manifest is derived data; STATE.json is authority).
- No row for non-canonical duplicates (e.g. `.en-orig.vtt`); duplicates are
  counted and reported, never deleted (Hard Rail #8).
- Any file the adapter cannot parse into a row → reported in the run summary
  and logged as an anomaly, never silently skipped.
