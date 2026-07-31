---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 08:02
repertoire_path: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T08:02:32
**Source folder:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6243

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 9 / 6243 — **0.14%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6188 / 6243 — 99.12%
- **Failed** (at least one Required rule fails): 46 / 6243 — 0.74%

- Schema-compliant (enriched + skeleton): 6197 / 6243 (99.26%)
- Frontmatter parseable: 6243 / 6243 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6225 | 18 | 99.7% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6225 | 18 | 99.7% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6225 | 18 | 99.7% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6225 | 18 | 99.7% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6243 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6243 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6225 | 18 | 99.7% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6243 | 0 | 100.0% |
| `R15` | tempo field value is a quoted string | 6215 | 28 | 99.6% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6243 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6225 | 18 | 99.7% |
| `R_TITLE` | # Title heading present | 6243 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 677 | 5566 | 10.8% |
| `REC_chapters` | recommended field 'chapters' populated | 36 | 6207 | 0.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6225 | 18 | 99.7% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6225 | 18 | 99.7% |
| `REC_form` | recommended field 'form' populated | 37 | 6206 | 0.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 36 | 6207 | 0.6% |
| `REC_tags` | recommended field 'tags' populated | 37 | 6206 | 0.6% |
| `REC_tempo` | recommended field 'tempo' populated | 36 | 6207 | 0.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 36 | 6207 | 0.6% |

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
| 6 | 18 | 0.3% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 28 | 0.4% |
| 12 | 6197 | 99.3% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- 50_CENT - IN_DA_CLUB.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- ADELE - ROLLING_IN_THE_DEEP.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- BEYONCE - IRREPLACEABLE.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- BRITNEY_SPEARS - OOPS_I_DID_IT_AGAIN.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- CARLY_RAE_JEPSEN - CALL_ME_MAYBE.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- 50_CENT - IN_DA_CLUB.md — missing: ct_format,song,tonic
- ADELE - ROLLING_IN_THE_DEEP.md — missing: ct_format,song,tonic
- BEYONCE - IRREPLACEABLE.md — missing: ct_format,song,tonic
- BRITNEY_SPEARS - OOPS_I_DID_IT_AGAIN.md — missing: ct_format,song,tonic
- CARLY_RAE_JEPSEN - CALL_ME_MAYBE.md — missing: ct_format,song,tonic

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- 50_CENT - IN_DA_CLUB.md — tonic empty/missing
- ADELE - ROLLING_IN_THE_DEEP.md — tonic empty/missing
- BEYONCE - IRREPLACEABLE.md — tonic empty/missing
- BRITNEY_SPEARS - OOPS_I_DID_IT_AGAIN.md — tonic empty/missing
- CARLY_RAE_JEPSEN - CALL_ME_MAYBE.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- 50_CENT - IN_DA_CLUB.md — mode='Minor' not in valid mode table
- ADELE - ROLLING_IN_THE_DEEP.md — mode='Minor' not in valid mode table
- BEYONCE - IRREPLACEABLE.md — mode='Major' not in valid mode table
- BRITNEY_SPEARS - OOPS_I_DID_IT_AGAIN.md — mode='Minor' not in valid mode table
- CARLY_RAE_JEPSEN - CALL_ME_MAYBE.md — mode='Major' not in valid mode table

### `R08` — filename follows §1.1 CTSF convention

- 50_CENT - IN_DA_CLUB.md — cannot check — song/artist missing
- ADELE - ROLLING_IN_THE_DEEP.md — cannot check — song/artist missing
- BEYONCE - IRREPLACEABLE.md — cannot check — song/artist missing
- BRITNEY_SPEARS - OOPS_I_DID_IT_AGAIN.md — cannot check — song/artist missing
- CARLY_RAE_JEPSEN - CALL_ME_MAYBE.md — cannot check — song/artist missing

### `R15` — tempo field value is a quoted string

- AL_GREEN - IM_STILL_IN_LOVE_WITH_YOU.md — tempo value is unquoted (likely bare integer)
- AL_GREEN - TAKE_ME_TO_THE_RIVER.md — tempo value is unquoted (likely bare integer)
- ANDRAE_CROUCH - THROUGH_IT_ALL.md — tempo value is unquoted (likely bare integer)
- ANTONIO_CARLOS_JOBIM - HOW_INSENSITIVE.md — tempo value is unquoted (likely bare integer)
- BILL_WITHERS - USE_ME.md — tempo value is unquoted (likely bare integer)

### `R_BODY` — all required body sections present

- 50_CENT - IN_DA_CLUB.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- ADELE - ROLLING_IN_THE_DEEP.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- BEYONCE - IRREPLACEABLE.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- BRITNEY_SPEARS - OOPS_I_DID_IT_AGAIN.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- CARLY_RAE_JEPSEN - CALL_ME_MAYBE.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6197 |
| 2 | R15 | 28 |
| 3 | R01, R02, R03, R04, R08, R_BODY | 18 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*