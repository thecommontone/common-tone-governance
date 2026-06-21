---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 17:17
repertoire_path: "/sessions/gallant-optimistic-gauss/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T17:17:46
**Source folder:** `/sessions/gallant-optimistic-gauss/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6252

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 172 / 6252 — **2.75%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6077 / 6252 — 97.20%
- **Failed** (at least one Required rule fails): 3 / 6252 — 0.05%

- Schema-compliant (enriched + skeleton): 6249 / 6252 (99.95%)
- Frontmatter parseable: 6252 / 6252 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6249 | 3 | 100.0% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6249 | 3 | 100.0% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6249 | 3 | 100.0% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6249 | 3 | 100.0% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6252 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6252 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6249 | 3 | 100.0% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6252 | 0 | 100.0% |
| `R15` | tempo field value is a quoted string | 6252 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6252 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6249 | 3 | 100.0% |
| `R_TITLE` | # Title heading present | 6252 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 702 | 5550 | 11.2% |
| `REC_chapters` | recommended field 'chapters' populated | 278 | 5974 | 4.4% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6249 | 3 | 100.0% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6249 | 3 | 100.0% |
| `REC_form` | recommended field 'form' populated | 172 | 6080 | 2.8% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 171 | 6081 | 2.7% |
| `REC_tags` | recommended field 'tags' populated | 172 | 6080 | 2.8% |
| `REC_tempo` | recommended field 'tempo' populated | 171 | 6081 | 2.7% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 171 | 6081 | 2.7% |

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
| 6 | 3 | 0.0% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 0 | 0.0% |
| 12 | 6249 | 100.0% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- KENDRICK_LAMAR - NOT_LIKE_US.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- MILEY_CYRUS - FLOWERS.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- TAYLOR_SWIFT - ANTI_HERO.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- KENDRICK_LAMAR - NOT_LIKE_US.md — missing: ct_format,song,tonic
- MILEY_CYRUS - FLOWERS.md — missing: ct_format,song,tonic
- TAYLOR_SWIFT - ANTI_HERO.md — missing: ct_format,song,tonic

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- KENDRICK_LAMAR - NOT_LIKE_US.md — tonic empty/missing
- MILEY_CYRUS - FLOWERS.md — tonic empty/missing
- TAYLOR_SWIFT - ANTI_HERO.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- KENDRICK_LAMAR - NOT_LIKE_US.md — mode='Minor' not in valid mode table
- MILEY_CYRUS - FLOWERS.md — mode='Minor' not in valid mode table
- TAYLOR_SWIFT - ANTI_HERO.md — mode='Major' not in valid mode table

### `R08` — filename follows §1.1 CTSF convention

- KENDRICK_LAMAR - NOT_LIKE_US.md — cannot check — song/artist missing
- MILEY_CYRUS - FLOWERS.md — cannot check — song/artist missing
- TAYLOR_SWIFT - ANTI_HERO.md — cannot check — song/artist missing

### `R_BODY` — all required body sections present

- KENDRICK_LAMAR - NOT_LIKE_US.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- MILEY_CYRUS - FLOWERS.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- TAYLOR_SWIFT - ANTI_HERO.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6249 |
| 2 | R01, R02, R03, R04, R08, R_BODY | 3 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*