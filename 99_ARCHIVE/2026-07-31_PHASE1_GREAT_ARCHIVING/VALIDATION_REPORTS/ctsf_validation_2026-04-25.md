---
title: "CTSF v1.3 Validation Report"
date: 2026-04-25 11:52
repertoire_path: "/Users/dougsmith/Docs/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md"
tags: [audit, ctsf, validation]
---

# CTSF v1.3 Validation Report

**Generated:** 2026-04-25T11:52:58
**Source folder:** `/Users/dougsmith/Docs/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Files scanned:** 6009

## Headline

- **Enriched** (schema-compliant AND no `unknown` placeholders): 545 / 6009 — **9.07%**
- **Skeleton** (schema-compliant, but one or more Required fields is `unknown`): 5464 / 6009 — 90.93%
- **Failed** (at least one Required rule fails): 0 / 6009 — 0.00%

- Schema-compliant (enriched + skeleton): 6009 / 6009 (100.00%)
- Frontmatter parseable: 6009 / 6009 (100.0%)

## Required Rules — pass/fail breakdown

| Rule | Name | Pass | Fail | Pass % |
|---|---|---:|---:|---:|
| `R01` | ct_format field present in frontmatter | 6009 | 0 | 100.0% |
| `R02` | required fields present (song, artist, year, tonic, mode, meter) | 6009 | 0 | 100.0% |
| `R03` | tonic is letter name (A-G with optional ♭/♯) or `unknown` | 6009 | 0 | 100.0% |
| `R04` | mode is valid value, lowercase, or `unknown` | 6009 | 0 | 100.0% |
| `R05` | Timeline uses ♭/♯ not ASCII b/# | 6009 | 0 | 100.0% |
| `R07` | section headers well-formed (brackets optional) | 6009 | 0 | 100.0% |
| `R08` | filename follows §1.1 CTSF convention | 6009 | 0 | 100.0% |
| `R14` | every form value maps to a Timeline header (suffix-stripped) | 6009 | 0 | 100.0% |
| `R15` | tempo field value is a quoted string | 6009 | 0 | 100.0% |
| `R16` | mode-change separator uses ' / ' (lowercase mode) | 6009 | 0 | 100.0% |
| `R_BODY` | all required body sections present | 6009 | 0 | 100.0% |
| `R_TITLE` | # Title heading present | 6009 | 0 | 100.0% |

## Recommended Rules — pass/fail breakdown

| Rule | Field | Populated | Empty | Pass % |
|---|---|---:|---:|---:|
| `REC_album` | recommended field 'album' populated | 5540 | 469 | 92.2% |
| `REC_chapters` | recommended field 'chapters' populated | 340 | 5669 | 5.7% |
| `REC_ct_entry_date` | recommended field 'ct_entry_date' populated | 6009 | 0 | 100.0% |
| `REC_ct_last_updated` | recommended field 'ct_last_updated' populated | 6009 | 0 | 100.0% |
| `REC_form` | recommended field 'form' populated | 217 | 5792 | 3.6% |
| `REC_source_confidence` | recommended field 'source_confidence' populated | 216 | 5793 | 3.6% |
| `REC_tags` | recommended field 'tags' populated | 217 | 5792 | 3.6% |
| `REC_tempo` | recommended field 'tempo' populated | 216 | 5793 | 3.6% |
| `REC_tempo_feel` | recommended field 'tempo_feel' populated | 622 | 5387 | 10.4% |

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
| 11 | 0 | 0.0% |
| 12 | 6009 | 100.0% |

## Sample failing files (5 per rule)

## Most common failure patterns

| Rank | Failing rules | # files |
|---:|---|---:|
| 1 | (fully compliant) | 6009 |

---

*Report produced by `_SYSTEM/scripts/ctsf_validator.py` against the v1.3 spec at `01_SPECS/CTSF_SPEC.md`.*