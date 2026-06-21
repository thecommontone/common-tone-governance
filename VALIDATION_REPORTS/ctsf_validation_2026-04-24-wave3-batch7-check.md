---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 19:52
repertoire_path: "02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T19:52:33
**Source folder:** `02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6004

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 197 / 6004 — **3.28%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 5794 / 6004 — 96.50%
- **Failed** (at least one Required rule fails): 13 / 6004 — 0.22%

- Schema-compliant (enriched + skeleton): 5991 / 6004 (99.78%)
- Frontmatter parseable: 6004 / 6004 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6004 | 0 | 100.0% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6004 | 0 | 100.0% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6004 | 0 | 100.0% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6004 | 0 | 100.0% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6004 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6004 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6004 | 0 | 100.0% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 5991 | 13 | 99.8% |
| `R15` | tempo field value is a quoted string | 6004 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6004 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6004 | 0 | 100.0% |
| `R_TITLE` | # Title heading present | 6004 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 5535 | 469 | 92.2% |
| `REC_chapters` | recommended field 'chapters' populated | 334 | 5670 | 5.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6004 | 0 | 100.0% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6004 | 0 | 100.0% |
| `REC_form` | recommended field 'form' populated | 211 | 5793 | 3.5% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 210 | 5794 | 3.5% |
| `REC_tags` | recommended field 'tags' populated | 211 | 5793 | 3.5% |
| `REC_tempo` | recommended field 'tempo' populated | 210 | 5794 | 3.5% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 210 | 5794 | 3.5% |

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
| 7 | 0 | 0.0% |
| 8 | 0 | 0.0% |
| 9 | 0 | 0.0% |
| 10 | 0 | 0.0% |
| 11 | 13 | 0.2% |
| 12 | 5991 | 99.8% |

## Sample failing files (5 per rule)

### `R14` — every form value maps to a Timeline header (suffix-stripped)

- CAROLE_KING - ITS_TOO_LATE.md — form values without Timeline header: ['chorus', 'intro', 'outro', 'solo', 'verse']
- FATS_DOMINO - BLUEBERRY_HILL.md — form values without Timeline header: ['bridge', 'intro', 'outro', 'verse']
- GARTH_BROOKS - FRIENDS_IN_LOW_PLACES.md — form values without Timeline header: ['chorus', 'intro', 'verse']
- HENRY_CREAMER_AND_TURNER_LAYTON - AFTER_YOUVE_GONE.md — form values without Timeline header: ['a', 'b', 'verse']
- IRVING_BERLIN - ALEXANDERS_RAGTIME_BAND.md — form values without Timeline header: ['chorus', 'verse']

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 5991 |
| 2 | R14 | 13 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*