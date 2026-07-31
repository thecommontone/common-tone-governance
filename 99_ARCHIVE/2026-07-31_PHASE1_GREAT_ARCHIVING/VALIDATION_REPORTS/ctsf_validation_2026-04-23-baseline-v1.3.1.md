---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 06:03
repertoire_path: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T06:03:10
**Source folder:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6350

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 32 / 6350 — **0.50%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 0 / 6350 — 0.00%
- **Failed** (at least one Required rule fails): 6318 / 6350 — 99.50%

- Schema-compliant (enriched + skeleton): 32 / 6350 (0.50%)
- Frontmatter parseable: 1746 / 6350 (27.5%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 53 | 6297 | 0.8% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 53 | 6297 | 0.8% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 53 | 6297 | 0.8% |
| `R04` | mode is valid value, lowercase, or `unknown` | 51 | 6299 | 0.8% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6342 | 8 | 99.9% |
| `R07` | section headers well-formed (brackets optional) | 6350 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 51 | 6299 | 0.8% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6336 | 14 | 99.8% |
| `R15` | tempo field value is a quoted string | 6345 | 5 | 99.9% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6349 | 1 | 100.0% |
| `R_BODY` | all required body sections present | 46 | 6304 | 0.7% |
| `R_TITLE` | # Title heading present | 6195 | 155 | 97.6% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 429 | 5921 | 6.8% |
| `REC_chapters` | recommended field 'chapters' populated | 52 | 6298 | 0.8% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 52 | 6298 | 0.8% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 52 | 6298 | 0.8% |
| `REC_form` | recommended field 'form' populated | 125 | 6225 | 2.0% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 52 | 6298 | 0.8% |
| `REC_tags` | recommended field 'tags' populated | 56 | 6294 | 0.9% |
| `REC_tempo` | recommended field 'tempo' populated | 55 | 6295 | 0.9% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 52 | 6298 | 0.8% |

## Compliance distribution

Each file is checked against 12 Required rules. Here is the distribution:

| Rules passed | Files | % |
|---:|---:|---:|
| 0 | 0 | 0.0% |
| 1 | 0 | 0.0% |
| 2 | 0 | 0.0% |
| 3 | 0 | 0.0% |
| 4 | 1 | 0.0% |
| 5 | 158 | 2.5% |
| 6 | 6138 | 96.7% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 13 | 0.2% |
| 11 | 8 | 0.1% |
| 12 | 32 | 0.5% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- (G)Idle - LION.md — no frontmatter
- - Black Orpheus.md — no frontmatter
- - Blue Moon.md — no frontmatter
- - Corvocado.md — ct_format missing (found: ['artist', 'form', 'genre', 'source', 'spotify_link', 'title']...)
- - Days of Wine And Roses.md — no frontmatter

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- (G)Idle - LION.md — missing: ct_format,song,artist,year,tonic,mode,meter
- - Black Orpheus.md — missing: ct_format,song,artist,year,tonic,mode,meter
- - Blue Moon.md — missing: ct_format,song,artist,year,tonic,mode,meter
- - Corvocado.md — missing: ct_format,song,tonic,mode,meter
- - Days of Wine And Roses.md — missing: ct_format,song,artist,year,tonic,mode,meter

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- (G)Idle - LION.md — tonic empty/missing
- - Black Orpheus.md — tonic empty/missing
- - Blue Moon.md — tonic empty/missing
- - Corvocado.md — tonic empty/missing
- - Days of Wine And Roses.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- (G)Idle - LION.md — mode empty/missing
- - Black Orpheus.md — mode empty/missing
- - Blue Moon.md — mode empty/missing
- - Corvocado.md — mode empty/missing
- - Days of Wine And Roses.md — mode empty/missing

### `R05` — Timeline uses ♭/♯ not ASCII b/#

- BILL_WITHERS - USE_ME.md — 11 suspected ASCII b/# in Roman numerals
- CURTIS_MAYFIELD - SUPERFLY.md — 3 suspected ASCII b/# in Roman numerals
- EARTH_WIND_AND_FIRE - THATS_THE_WAY_OF_THE_WORLD.md — 2 suspected ASCII b/# in Roman numerals
- RUFUS_AND_CHAKA_KHAN - TELL_ME_SOMETHING_GOOD.md — 2 suspected ASCII b/# in Roman numerals
- THE_OJAYS - BACK_STABBERS.md — 5 suspected ASCII b/# in Roman numerals

### `R08` — filename follows §1.1 CTSF convention

- (G)Idle - LION.md — cannot check — song/artist missing
- - Black Orpheus.md — cannot check — song/artist missing
- - Blue Moon.md — cannot check — song/artist missing
- - Corvocado.md — cannot check — song/artist missing
- - Days of Wine And Roses.md — cannot check — song/artist missing

### `R14` — every form value maps to a Timeline header (suffix-stripped)

- AL_GREEN - IM_STILL_IN_LOVE_WITH_YOU.md — form values without Timeline header: ['intro', 'verse', 'chorus-out', 'chorus', 'bridge']
- AL_GREEN - TAKE_ME_TO_THE_RIVER.md — form values without Timeline header: ['intro', 'verse', 'pre-chorus', 'chorus-out', 'chorus']
- ANDRAE_CROUCH - THROUGH_IT_ALL.md — form values without Timeline header: ['chorus', 'verse']
- BILL_WITHERS - USE_ME.md — form values without Timeline header: ['intro', 'verse', 'chorus-out', 'chorus', 'bridge']
- CURTIS_MAYFIELD - MOVE_ON_UP.md — form values without Timeline header: ['intro', 'verse', 'chorus', 'chorus-out', 'instrumental-break']

### `R15` — tempo field value is a quoted string

- Amy Winehouse - Back to Black.md — tempo value is unquoted (likely bare integer)
- Gotye - Somebody That I Used to Know.md — tempo value is unquoted (likely bare integer)
- Michael Jackson - Man In The Mirror.md — tempo value is unquoted (likely bare integer)
- Muse - Hysteria.md — tempo value is unquoted (likely bare integer)
- Radiohead - Pyramid Song.md — tempo value is unquoted (likely bare integer)

### `R16` — mode-change separator uses ' / ' (lowercase mode)

- JEROME_KERN - ALL_THE_THINGS_YOU_ARE.md — 1 malformed (key:) header — e.g., (key: I — Ab major)

### `R_BODY` — all required body sections present

- (G)Idle - LION.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- - Black Orpheus.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- - Blue Moon.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- - Corvocado.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections
- - Days of Wine And Roses.md — missing sections: Summary,Timeline,Chord Vocabulary,Theoretical Notes,Connections

### `R_TITLE` — # Title heading present

- Alanis Morissette - Ironic.md — no level-1 heading found
- Avril Lavigne - Complicated.md — no level-1 heading found
- Beyoncé - Single Ladies (Put a Ring on It).md — no level-1 heading found
- Billy Talent - Surrender.md — no level-1 heading found
- Charli XCX - Chains of Love.md — no level-1 heading found

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | R01, R02, R03, R04, R08, R_BODY | 6138 |
| 2 | R01, R02, R03, R04, R08, R_BODY, R_TITLE | 154 |
| 3 | (fully compliant) | 32 |
| 4 | R05, R14 | 8 |
| 5 | R14 | 4 |
| 6 | R01, R02, R03, R04, R08, R15, R_BODY | 4 |
| 7 | R_BODY | 4 |
| 8 | R04, R_BODY | 2 |
| 9 | R08, R14 | 2 |
| 10 | R16, R_BODY | 1 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*