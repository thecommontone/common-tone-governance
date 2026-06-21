---
title: "CTSF v1.3 Validation Report"
date: 2026-04-24 07:15
repertoire_path: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-24T07:15:02
**Source folder:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6221

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 23 / 6221 — **0.37%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 6185 / 6221 — 99.42%
- **Failed** (at least one Required rule fails): 13 / 6221 — 0.21%

- Schema-compliant (enriched + skeleton): 6208 / 6221 (99.79%)
- Frontmatter parseable: 6221 / 6221 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6221 | 0 | 100.0% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6221 | 0 | 100.0% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6221 | 0 | 100.0% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6221 | 0 | 100.0% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6221 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6221 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6221 | 0 | 100.0% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6208 | 13 | 99.8% |
| `R15` | tempo field value is a quoted string | 6221 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6221 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6221 | 0 | 100.0% |
| `R_TITLE` | # Title heading present | 6221 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 646 | 5575 | 10.4% |
| `REC_chapters` | recommended field 'chapters' populated | 36 | 6185 | 0.6% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6221 | 0 | 100.0% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6221 | 0 | 100.0% |
| `REC_form` | recommended field 'form' populated | 36 | 6185 | 0.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 36 | 6185 | 0.6% |
| `REC_tags` | recommended field 'tags' populated | 36 | 6185 | 0.6% |
| `REC_tempo` | recommended field 'tempo' populated | 36 | 6185 | 0.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 36 | 6185 | 0.6% |

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
| 12 | 6208 | 99.8% |

## Sample failing files (5 per rule)

### `R14` — every form value maps to a Timeline header (suffix-stripped)

- AL_GREEN - IM_STILL_IN_LOVE_WITH_YOU.md — form values without Timeline header: ['chorus-out', 'intro', 'bridge', 'verse', 'chorus']
- AL_GREEN - TAKE_ME_TO_THE_RIVER.md — form values without Timeline header: ['intro', 'chorus-out', 'bridge', 'pre-chorus', 'verse']
- ANDRAE_CROUCH - THROUGH_IT_ALL.md — form values without Timeline header: ['verse', 'chorus']
- BILL_WITHERS - USE_ME.md — form values without Timeline header: ['chorus-out', 'intro', 'bridge', 'verse', 'chorus']
- CURTIS_MAYFIELD - MOVE_ON_UP.md — form values without Timeline header: ['chorus-out', 'intro', 'verse', 'chorus', 'instrumental-break']

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6208 |
| 2 | R14 | 13 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*