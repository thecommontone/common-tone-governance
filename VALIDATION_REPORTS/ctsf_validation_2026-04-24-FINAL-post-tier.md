---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 08:09
repertoire_path: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T08:09:39
**Source folder:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6250

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 37 / 6250 — **0.59%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6212 / 6250 — 99.39%
- **Failed** (at least one Required rule fails): 1 / 6250 — 0.02%

- Schema-compliant (enriched + skeleton): 6249 / 6250 (99.98%)
- Frontmatter parseable: 6250 / 6250 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6249 | 1 | 100.0% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6249 | 1 | 100.0% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6249 | 1 | 100.0% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6249 | 1 | 100.0% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6250 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6250 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6249 | 1 | 100.0% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6250 | 0 | 100.0% |
| `R15` | tempo field value is a quoted string | 6250 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6250 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6249 | 1 | 100.0% |
| `R_TITLE` | # Title heading present | 6250 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 685 | 5565 | 11.0% |
| `REC_chapters` | recommended field 'chapters' populated | 36 | 6214 | 0.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6249 | 1 | 100.0% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6249 | 1 | 100.0% |
| `REC_form` | recommended field 'form' populated | 37 | 6213 | 0.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 36 | 6214 | 0.6% |
| `REC_tags` | recommended field 'tags' populated | 37 | 6213 | 0.6% |
| `REC_tempo` | recommended field 'tempo' populated | 36 | 6214 | 0.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 36 | 6214 | 0.6% |

## Compliance distribution

Each file is checked against 12 Required rules. Here is the distribution:

| Rules passed | Files | % |
|---:|---:|---:|
| 0 | 0 | 0.0% |
| 1 | 0 | 0.0% |
| 2 | 0 | 0.0% |
| 3 | 0 | 0.0% |
| 4 | 0 | 0.0% |
| 5 | 0 | 0.0% |
| 6 | 1 | 0.0% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 0 | 0.0% |
| 12 | 6249 | 100.0% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- TAYLOR_SWIFT - ANTI_HERO.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- TAYLOR_SWIFT - ANTI_HERO.md — missing: ct_format,song,tonic

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- TAYLOR_SWIFT - ANTI_HERO.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- TAYLOR_SWIFT - ANTI_HERO.md — mode='Major' not in valid mode table

### `R08` — filename follows §1.1 CTSF convention

- TAYLOR_SWIFT - ANTI_HERO.md — cannot check — song/artist missing

### `R_BODY` — all required body sections present

- TAYLOR_SWIFT - ANTI_HERO.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6249 |
| 2 | R01, R02, R03, R04, R08, R_BODY | 1 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*