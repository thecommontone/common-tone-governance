---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 05:53
repertoire_path: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T05:53:39
**Source folder:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6348

## Headline

- **Fully compliant (all Required rules passed):** 18 / 6348 — **0.28%**
- Frontmatter parseable: 1744 / 6348 (27.5%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 53 | 6295 | 0.8% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 53 | 6295 | 0.8% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) | 53 | 6295 | 0.8% |
| `R04` | mode is valid value, lowercase | 51 | 6297 | 0.8% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6340 | 8 | 99.9% |
| `R07` | section headers use [Brackets] | 6333 | 15 | 99.8% |
| `R08` | filename follows §1.1 CTSF convention | 51 | 6297 | 0.8% |
| `R14` | every form value has a Timeline header | 6320 | 28 | 99.6% |
| `R15` | tempo field value is a quoted string | 6343 | 5 | 99.9% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6347 | 1 | 100.0% |
| `R_BODY` | all required body sections present | 46 | 6302 | 0.7% |
| `R_TITLE` | # Title heading present | 6193 | 155 | 97.6% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 427 | 5921 | 6.7% |
| `REC_chapters` | recommended field 'chapters' populated | 52 | 6296 | 0.8% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 52 | 6296 | 0.8% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 52 | 6296 | 0.8% |
| `REC_form` | recommended field 'form' populated | 125 | 6223 | 2.0% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 52 | 6296 | 0.8% |
| `REC_tags` | recommended field 'tags' populated | 56 | 6292 | 0.9% |
| `REC_tempo` | recommended field 'tempo' populated | 55 | 6293 | 0.9% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 52 | 6296 | 0.8% |

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
| 6 | 6136 | 96.7% |
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 28 | 0.4% |
| 11 | 7 | 0.1% |
| 12 | 18 | 0.3% |

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

### `R03` — tonic is letter name (A-G with optional ♭/♯)

- (G)Idle - LION.md — tonic empty/missing
- - Black Orpheus.md — tonic empty/missing
- - Blue Moon.md — tonic empty/missing
- - Corvocado.md — tonic empty/missing
- - Days of Wine And Roses.md — tonic empty/missing

### `R04` — mode is valid value, lowercase

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

### `R07` — section headers use [Brackets]

- BOB_WILLS_AND_HIS_TEXAS_PLAYBOYS - SAN_ANTONIO_ROSE.md — 8/8 ### headers missing [brackets]
- BUCK_OWENS - ACT_NATURALLY.md — 8/8 ### headers missing [brackets]
- DON_GIBSON - OH_LONESOME_ME.md — 4/4 ### headers missing [brackets]
- GLEN_CAMPBELL - WICHITA_LINEMAN.md — 7/7 ### headers missing [brackets]
- HANK_WILLIAMS - IM_SO_LONESOME_I_COULD_CRY.md — 1/1 ### headers missing [brackets]

### `R08` — filename follows §1.1 CTSF convention

- (G)Idle - LION.md — cannot check — song/artist missing
- - Black Orpheus.md — cannot check — song/artist missing
- - Blue Moon.md — cannot check — song/artist missing
- - Corvocado.md — cannot check — song/artist missing
- - Days of Wine And Roses.md — cannot check — song/artist missing

### `R14` — every form value has a Timeline header

- AL_GREEN - IM_STILL_IN_LOVE_WITH_YOU.md — form values without Timeline header: ['verse', 'bridge', 'chorus-out', 'chorus', 'intro']
- AL_GREEN - TAKE_ME_TO_THE_RIVER.md — form values without Timeline header: ['verse', 'bridge', 'pre-chorus', 'chorus-out', 'chorus']
- ANDRAE_CROUCH - THROUGH_IT_ALL.md — form values without Timeline header: ['chorus', 'verse']
- BILL_WITHERS - USE_ME.md — form values without Timeline header: ['verse', 'bridge', 'chorus-out', 'chorus', 'intro']
- BOB_WILLS_AND_HIS_TEXAS_PLAYBOYS - SAN_ANTONIO_ROSE.md — form values without Timeline header: ['verse', 'bridge', 'verse-2', 'outro', 'chorus-2']

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
| 1 | R01, R02, R03, R04, R08, R_BODY | 6136 |
| 2 | R01, R02, R03, R04, R08, R_BODY, R_TITLE | 154 |
| 3 | (fully compliant) | 18 |
| 4 | R07, R14 | 14 |
| 5 | R05, R14 | 8 |
| 6 | R14 | 4 |
| 7 | R01, R02, R03, R04, R08, R15, R_BODY | 4 |
| 8 | R_BODY | 3 |
| 9 | R04, R_BODY | 2 |
| 10 | R08, R14 | 2 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*