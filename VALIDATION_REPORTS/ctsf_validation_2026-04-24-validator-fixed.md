---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 06:52
repertoire_path: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T06:52:31
**Source folder:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6366

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 16 / 6366 — **0.25%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6167 / 6366 — 96.87%
- **Failed** (at least one Required rule fails): 183 / 6366 — 2.87%

- Schema-compliant (enriched + skeleton): 6183 / 6366 (97.13%)
- Frontmatter parseable: 6270 / 6366 (98.5%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6204 | 162 | 97.5% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6204 | 162 | 97.5% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6204 | 162 | 97.5% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6204 | 162 | 97.5% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6358 | 8 | 99.9% |
| `R07` | section headers well-formed (brackets optional) | 6366 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6202 | 164 | 97.4% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6352 | 14 | 99.8% |
| `R15` | tempo field value is a quoted string | 6366 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6365 | 1 | 100.0% |
| `R_BODY` | all required body sections present | 6197 | 169 | 97.3% |
| `R_TITLE` | # Title heading present | 6268 | 98 | 98.5% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 626 | 5740 | 9.8% |
| `REC_chapters` | recommended field 'chapters' populated | 36 | 6330 | 0.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6203 | 163 | 97.4% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6203 | 163 | 97.4% |
| `REC_form` | recommended field 'form' populated | 37 | 6329 | 0.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 36 | 6330 | 0.6% |
| `REC_tags` | recommended field 'tags' populated | 36 | 6330 | 0.6% |
| `REC_tempo` | recommended field 'tempo' populated | 36 | 6330 | 0.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 36 | 6330 | 0.6% |

## Compliance distribution

Each file is checked against 12 Required rules. Here is the distribution:

| Rules passed | Files | % |
|---:|---:|---:|
| 0 | 0 | 0.0% |
| 1 | 0 | 0.0% |
| 2 | 0 | 0.0% |
| 3 | 0 | 0.0% |
| 4 | 0 | 0.0% |
| 5 | 98 | 1.5% |
| 6 | 64 | 1.0% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 11 | 0.2% |
| 11 | 10 | 0.2% |
| 12 | 6183 | 97.1% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- - Koko.md — no frontmatter
- - Song Name.md — ct_format missing (found: ['artist', 'source', 'spotify_link', 'title', 'year']...)
- Analysis of Nirvana Songs Part 1.md — ct_format missing (found: ['source']...)
- Barrie Manilow.md — ct_format missing (found: ['source']...)
- Bon Jovi.md — ct_format missing (found: ['artist', 'source', 'spotify_link', 'title', 'year']...)

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- - Koko.md — missing: ct_format,song,artist,year,tonic,mode,meter
- - Song Name.md — missing: ct_format,song,tonic,mode,meter
- Analysis of Nirvana Songs Part 1.md — missing: ct_format,song,artist,year,tonic,mode,meter
- Barrie Manilow.md — missing: ct_format,song,artist,year,tonic,mode,meter
- Bon Jovi.md — missing: ct_format,song,tonic,mode,meter

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- - Koko.md — tonic empty/missing
- - Song Name.md — tonic empty/missing
- Analysis of Nirvana Songs Part 1.md — tonic empty/missing
- Barrie Manilow.md — tonic empty/missing
- Bon Jovi.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- - Koko.md — mode empty/missing
- - Song Name.md — mode empty/missing
- Analysis of Nirvana Songs Part 1.md — mode empty/missing
- Barrie Manilow.md — mode empty/missing
- Bon Jovi.md — mode empty/missing

### `R05` — Timeline uses ♭/♯ not ASCII b/#

- BILL_WITHERS - USE_ME.md — 11 suspected ASCII b/# in Roman numerals
- CURTIS_MAYFIELD - SUPERFLY.md — 3 suspected ASCII b/# in Roman numerals
- EARTH_WIND_AND_FIRE - THATS_THE_WAY_OF_THE_WORLD.md — 2 suspected ASCII b/# in Roman numerals
- RUFUS_AND_CHAKA_KHAN - TELL_ME_SOMETHING_GOOD.md — 2 suspected ASCII b/# in Roman numerals
- THE_OJAYS - BACK_STABBERS.md — 5 suspected ASCII b/# in Roman numerals

### `R08` — filename follows §1.1 CTSF convention

- - Koko.md — cannot check — song/artist missing
- - Song Name.md — cannot check — song/artist missing
- Analysis of Nirvana Songs Part 1.md — cannot check — song/artist missing
- Barrie Manilow.md — cannot check — song/artist missing
- Bon Jovi.md — cannot check — song/artist missing

### `R14` — every form value maps to a Timeline header (suffix-stripped)

- AL_GREEN - IM_STILL_IN_LOVE_WITH_YOU.md — form values without Timeline header: ['intro', 'verse', 'bridge', 'chorus-out', 'chorus']
- AL_GREEN - TAKE_ME_TO_THE_RIVER.md — form values without Timeline header: ['pre-chorus', 'intro', 'verse', 'bridge', 'chorus-out']
- ANDRAE_CROUCH - THROUGH_IT_ALL.md — form values without Timeline header: ['verse', 'chorus']
- BILL_WITHERS - USE_ME.md — form values without Timeline header: ['intro', 'verse', 'bridge', 'chorus-out', 'chorus']
- CURTIS_MAYFIELD - MOVE_ON_UP.md — form values without Timeline header: ['instrumental-break', 'intro', 'verse', 'chorus-out', 'chorus']

### `R16` — mode-change separator uses ' / ' (lowercase mode)

- JEROME_KERN - ALL_THE_THINGS_YOU_ARE.md — 1 malformed (key:) header — e.g., (key: I — Ab major)

### `R_BODY` — all required body sections present

- - Koko.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- - Song Name.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- ANTONIO_CARLOS_JOBIM - HOW_INSENSITIVE.md — missing sections: Theoretical Notes,Connections
- Analysis of Nirvana Songs Part 1.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- Barrie Manilow.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

### `R_TITLE` — # Title heading present

- EXTRACTED_A Horse with No Name_20260408.md — no level-1 heading found
- EXTRACTED_Analysis of Nirvana Songs Part 1_20260408.md — no level-1 heading found
- EXTRACTED_Analysis of-She’s Always a Woman_20260408.md — no level-1 heading found
- EXTRACTED_Arcade Fire_20260408.md — no level-1 heading found
- EXTRACTED_Army of Me_20260408.md — no level-1 heading found

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6183 |
| 2 | R01, R02, R03, R04, R08, R_BODY, R_TITLE | 98 |
| 3 | R01, R02, R03, R04, R08, R_BODY | 64 |
| 4 | R05, R14 | 8 |
| 5 | R_BODY | 6 |
| 6 | R14 | 4 |
| 7 | R08, R14 | 2 |
| 8 | R16, R_BODY | 1 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*