---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 08:04
repertoire_path: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T08:04:29
**Source folder:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6243

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 0 / 6243 — **0.00%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 19 / 6243 — 0.30%
- **Failed** (at least one Required rule fails): 6224 / 6243 — 99.70%

- Schema-compliant (enriched + skeleton): 19 / 6243 (0.30%)
- Frontmatter parseable: 19 / 6243 (0.3%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 19 | 6224 | 0.3% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 19 | 6224 | 0.3% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 19 | 6224 | 0.3% |
| `R04` | mode is valid value, lowercase, or `unknown` | 19 | 6224 | 0.3% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6243 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6243 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 19 | 6224 | 0.3% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6243 | 0 | 100.0% |
| `R15` | tempo field value is a quoted string | 6243 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6243 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6243 | 0 | 100.0% |
| `R_TITLE` | # Title heading present | 6243 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 19 | 6224 | 0.3% |
| `REC_chapters` | recommended field 'chapters' populated | 0 | 6243 | 0.0% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 19 | 6224 | 0.3% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 19 | 6224 | 0.3% |
| `REC_form` | recommended field 'form' populated | 0 | 6243 | 0.0% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 0 | 6243 | 0.0% |
| `REC_tags` | recommended field 'tags' populated | 0 | 6243 | 0.0% |
| `REC_tempo` | recommended field 'tempo' populated | 0 | 6243 | 0.0% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 0 | 6243 | 0.0% |

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
| 6 | 0 | 0.0% |
| 7 | 6224 | 99.7% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 0 | 0.0% |
| 12 | 19 | 0.3% |

## Sample failing files (5 per rule)

### `R01` — ct_format field present in frontmatter

- 10000_MANIACS - CANDY_EVERYBODY_WANTS.md — no frontmatter
- 10CC - IM_NOT_IN_LOVE.md — no frontmatter
- 25_OR_6_TO_4 - CHICAGO.md — no frontmatter
- 2PAC - BRENDAS_GOT_A_BABY.md — no frontmatter
- 2PAC - CHANGES.md — no frontmatter

### `R02` — required fields present (song, artist, year, tonic, mode, meter)

- 10000_MANIACS - CANDY_EVERYBODY_WANTS.md — missing: ct_format,song,artist,year,tonic,mode,meter
- 10CC - IM_NOT_IN_LOVE.md — missing: ct_format,song,artist,year,tonic,mode,meter
- 25_OR_6_TO_4 - CHICAGO.md — missing: ct_format,song,artist,year,tonic,mode,meter
- 2PAC - BRENDAS_GOT_A_BABY.md — missing: ct_format,song,artist,year,tonic,mode,meter
- 2PAC - CHANGES.md — missing: ct_format,song,artist,year,tonic,mode,meter

### `R03` — tonic is letter name (A-G with optional ♭/♯) or `unknown`

- 10000_MANIACS - CANDY_EVERYBODY_WANTS.md — tonic empty/missing
- 10CC - IM_NOT_IN_LOVE.md — tonic empty/missing
- 25_OR_6_TO_4 - CHICAGO.md — tonic empty/missing
- 2PAC - BRENDAS_GOT_A_BABY.md — tonic empty/missing
- 2PAC - CHANGES.md — tonic empty/missing

### `R04` — mode is valid value, lowercase, or `unknown`

- 10000_MANIACS - CANDY_EVERYBODY_WANTS.md — mode empty/missing
- 10CC - IM_NOT_IN_LOVE.md — mode empty/missing
- 25_OR_6_TO_4 - CHICAGO.md — mode empty/missing
- 2PAC - BRENDAS_GOT_A_BABY.md — mode empty/missing
- 2PAC - CHANGES.md — mode empty/missing

### `R08` — filename follows §1.1 CTSF convention

- 10000_MANIACS - CANDY_EVERYBODY_WANTS.md — cannot check — song/artist missing
- 10CC - IM_NOT_IN_LOVE.md — cannot check — song/artist missing
- 25_OR_6_TO_4 - CHICAGO.md — cannot check — song/artist missing
- 2PAC - BRENDAS_GOT_A_BABY.md — cannot check — song/artist missing
- 2PAC - CHANGES.md — cannot check — song/artist missing

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | R01, R02, R03, R04, R08 | 6224 |
| 2 | (fully compliant) | 19 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*