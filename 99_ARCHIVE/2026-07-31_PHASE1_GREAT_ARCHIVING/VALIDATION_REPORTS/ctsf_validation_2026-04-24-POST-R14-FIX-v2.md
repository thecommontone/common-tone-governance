---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 07:36
repertoire_path: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T07:36:36
**Source folder:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6232

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 37 / 6232 — **0.59%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6181 / 6232 — 99.18%
- **Failed** (at least one Required rule fails): 14 / 6232 — 0.22%

- Schema-compliant (enriched + skeleton): 6218 / 6232 (99.78%)
- Frontmatter parseable: 6232 / 6232 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6218 | 14 | 99.8% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6218 | 14 | 99.8% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6218 | 14 | 99.8% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6218 | 14 | 99.8% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6232 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6232 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6218 | 14 | 99.8% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6232 | 0 | 100.0% |
| `R15` | tempo field value is a quoted string | 6232 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6232 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6218 | 14 | 99.8% |
| `R_TITLE` | # Title heading present | 6232 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 659 | 5573 | 10.6% |
| `REC_chapters` | recommended field 'chapters' populated | 36 | 6196 | 0.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6218 | 14 | 99.8% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6218 | 14 | 99.8% |
| `REC_form` | recommended field 'form' populated | 37 | 6195 | 0.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 36 | 6196 | 0.6% |
| `REC_tags` | recommended field 'tags' populated | 37 | 6195 | 0.6% |
| `REC_tempo` | recommended field 'tempo' populated | 36 | 6196 | 0.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 36 | 6196 | 0.6% |

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
| 6 | 14 | 0.2% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 0 | 0.0% |
| 12 | 6218 | 99.8% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- DOLLY_PARTON - 9_TO_5.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- JOHN_MELLENCAMP - JACK_AND_DIANE.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- KIM_CARNES - BETTE_DAVIS_EYES.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- LOS_LOBOS - LA_BAMBA.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md — missing: ct_format,song,tonic
- DOLLY_PARTON - 9_TO_5.md — missing: ct_format,song,tonic
- JOHN_MELLENCAMP - JACK_AND_DIANE.md — missing: ct_format,song,tonic
- KIM_CARNES - BETTE_DAVIS_EYES.md — missing: ct_format,song,tonic
- LOS_LOBOS - LA_BAMBA.md — missing: ct_format,song,tonic

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md — tonic empty/missing
- DOLLY_PARTON - 9_TO_5.md — tonic empty/missing
- JOHN_MELLENCAMP - JACK_AND_DIANE.md — tonic empty/missing
- KIM_CARNES - BETTE_DAVIS_EYES.md — tonic empty/missing
- LOS_LOBOS - LA_BAMBA.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md — mode='Major' not in valid mode table
- DOLLY_PARTON - 9_TO_5.md — mode='Major' not in valid mode table
- JOHN_MELLENCAMP - JACK_AND_DIANE.md — mode='Major (Mixolydian inflection)' not in valid mode table
- KIM_CARNES - BETTE_DAVIS_EYES.md — mode='Minor' not in valid mode table
- LOS_LOBOS - LA_BAMBA.md — mode='Major' not in valid mode table

### `R08` — filename follows §1.1 CTSF convention

- BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md — cannot check — song/artist missing
- DOLLY_PARTON - 9_TO_5.md — cannot check — song/artist missing
- JOHN_MELLENCAMP - JACK_AND_DIANE.md — cannot check — song/artist missing
- KIM_CARNES - BETTE_DAVIS_EYES.md — cannot check — song/artist missing
- LOS_LOBOS - LA_BAMBA.md — cannot check — song/artist missing

### `R_BODY` — all required body sections present

- BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- DOLLY_PARTON - 9_TO_5.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- JOHN_MELLENCAMP - JACK_AND_DIANE.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- KIM_CARNES - BETTE_DAVIS_EYES.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- LOS_LOBOS - LA_BAMBA.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6218 |
| 2 | R01, R02, R03, R04, R08, R_BODY | 14 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*