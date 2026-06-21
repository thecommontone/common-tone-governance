---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 07:11
repertoire_path: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T07:11:35
**Source folder:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6220

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 23 / 6220 — **0.37%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6169 / 6220 — 99.18%
- **Failed** (at least one Required rule fails): 28 / 6220 — 0.45%

- Schema-compliant (enriched + skeleton): 6192 / 6220 (99.55%)
- Frontmatter parseable: 6219 / 6220 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6205 | 15 | 99.8% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6205 | 15 | 99.8% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6205 | 15 | 99.8% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6205 | 15 | 99.8% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6220 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6220 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6204 | 16 | 99.7% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6207 | 13 | 99.8% |
| `R15` | tempo field value is a quoted string | 6220 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6220 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6205 | 15 | 99.8% |
| `R_TITLE` | # Title heading present | 6220 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 642 | 5578 | 10.3% |
| `REC_chapters` | recommended field 'chapters' populated | 36 | 6184 | 0.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6205 | 15 | 99.8% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6205 | 15 | 99.8% |
| `REC_form` | recommended field 'form' populated | 36 | 6184 | 0.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 36 | 6184 | 0.6% |
| `REC_tags` | recommended field 'tags' populated | 36 | 6184 | 0.6% |
| `REC_tempo` | recommended field 'tempo' populated | 36 | 6184 | 0.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 36 | 6184 | 0.6% |

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
| 6 | 15 | 0.2% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 1 | 0.0% |
| 11 | 12 | 0.2% |
| 12 | 6192 | 99.5% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- DAWN - TIE_A_YELLOW_RIBBON_ROUND_THE_OLE_OAK_TREE.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)
- JEANNIE_C_RILEY - HARPER_VALLEY_PTA.md — ct_format missing (found: ['album', 'artist', 'date_ingested', 'ingested', 'key_note', 'meter']...)

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md — missing: ct_format,song,tonic
- BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md — missing: ct_format,song,tonic
- BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md — missing: ct_format,song,tonic
- DAWN - TIE_A_YELLOW_RIBBON_ROUND_THE_OLE_OAK_TREE.md — missing: ct_format,song,tonic
- JEANNIE_C_RILEY - HARPER_VALLEY_PTA.md — missing: ct_format,song,tonic

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md — tonic empty/missing
- BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md — tonic empty/missing
- BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md — tonic empty/missing
- DAWN - TIE_A_YELLOW_RIBBON_ROUND_THE_OLE_OAK_TREE.md — tonic empty/missing
- JEANNIE_C_RILEY - HARPER_VALLEY_PTA.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md — mode='Major (bluesy)' not in valid mode table
- BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md — mode='Major (martial)' not in valid mode table
- BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md — mode='Dorian / Minor' not in valid mode table
- DAWN - TIE_A_YELLOW_RIBBON_ROUND_THE_OLE_OAK_TREE.md — mode='Major' not in valid mode table
- JEANNIE_C_RILEY - HARPER_VALLEY_PTA.md — mode='Major' not in valid mode table

### `R08` — filename follows §1.1 CTSF convention

- ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md — cannot check — song/artist missing
- BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md — cannot check — song/artist missing
- BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md — cannot check — song/artist missing
- DAWN - TIE_A_YELLOW_RIBBON_ROUND_THE_OLE_OAK_TREE.md — cannot check — song/artist missing
- JEANNIE_C_RILEY - HARPER_VALLEY_PTA.md — cannot check — song/artist missing

### `R14` — every form value maps to a Timeline header (suffix-stripped)

- AL_GREEN - IM_STILL_IN_LOVE_WITH_YOU.md — form values without Timeline header: ['bridge', 'chorus-out', 'verse', 'intro', 'chorus']
- AL_GREEN - TAKE_ME_TO_THE_RIVER.md — form values without Timeline header: ['bridge', 'verse', 'intro', 'chorus-out', 'pre-chorus']
- ANDRAE_CROUCH - THROUGH_IT_ALL.md — form values without Timeline header: ['chorus', 'verse']
- BILL_WITHERS - USE_ME.md — form values without Timeline header: ['bridge', 'chorus-out', 'verse', 'intro', 'chorus']
- CURTIS_MAYFIELD - MOVE_ON_UP.md — form values without Timeline header: ['chorus-out', 'verse', 'intro', 'instrumental-break', 'chorus']

### `R_BODY` — all required body sections present

- ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- DAWN - TIE_A_YELLOW_RIBBON_ROUND_THE_OLE_OAK_TREE.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- JEANNIE_C_RILEY - HARPER_VALLEY_PTA.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6192 |
| 2 | R01, R02, R03, R04, R08, R_BODY | 15 |
| 3 | R14 | 12 |
| 4 | R08, R14 | 1 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*