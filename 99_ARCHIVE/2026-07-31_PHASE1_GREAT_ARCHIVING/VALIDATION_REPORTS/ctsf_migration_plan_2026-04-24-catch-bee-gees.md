---
title: "CTSF Migration Plan"
date: 2026-04-24 07:14
mode: EXECUTE
source: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6224
**Will migrate:** 1
**Will skip:** 6223
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6221 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 3 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 1 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6220 |
| utility file (not a song entry) | 3 |

## Renames

- Files keeping current filename: **1**
- Files being renamed:            **0**

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 0 | 0.0% |
| `tonic` | 1 | 100.0% |
| `mode` | 1 | 100.0% |
| `meter` | 1 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `album` | 1 | 100.0% |
| `legacy_source` | 1 | 100.0% |
| `legacy_tempo_bpm` | 1 | 100.0% |

## Sample preview — first 3 migrated files

### `BEE_GEES - TRAGEDY.md` → `BEE_GEES - TRAGEDY.md`

```markdown
---
ct_format: '1.3'
song: TRAGEDY
artist: BEE_GEES
year: 1979
tonic: unknown
mode: unknown
meter: unknown
album: RSO Records — 'Spirits Having Flown'
legacy_source: general music theory knowledge + disco historical record
legacy_tempo_bpm: 112
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# TRAGEDY — BEE_GEES (1979)

## Summary

*TBD — awaiting analytical enrichment.*

## Timeline

*TBD — awaiting harmonic analysis. See §5 of `01_SPECS/CTSF_SPEC.md`.*

## Chord Vocabulary

*TBD — populated from the Timeline once analysis is complete.*

## Theoretical Notes

*TBD — awaiting analytical enrichment.*

## Connections

**Chapters:** *TBD*  
**Concepts:** *TBD*  
**Related songs:** *TBD*

## Source Notes

*Entry created by automated migration on 2026-04-24. Provenance: legacy frontmatter + filename.*

---

## Preserved Original Content

> The content below was carried forward verbatim from the pre-migration file. It may include non-standard headings, duplicated titles, or early Doug-notes. Use it as raw material when the Summary / Timeline / Theoretical Notes sections above are enriched; then consider removing this block.

# Tragedy — Bee Gees

**Artist:** [[BEE_GEES]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=tragedy+bee+gees+1979)
- **Chord Chart:**

## Theoretical Tags
`#era/1970s` `#genre/disco` `#genre/dramatic-pop` `#form/verse-chorus` `#harmony/minor-key-disco` `#rhythm/four-on-the-floor` `#vocal/falsetto` `#historical/bee-gees-peak` `#historical/rso-records`

## Concepts Demonstrated

### 1. Disco at Its Commercial Peak → [[01.1 Pop Music, huh?]]

"Tragedy" reached #1 on the Billboard Hot 100 in March 1979 — at the very peak of disco's commercial dominance, months before the anti-disco backlash (including the July 1979 "Disco Demolition Night" at Comiskey Park) began reshaping the commercial landscape. The Bee Gees had six consecutive #1 singles from 1977-1979, a streak matched only by the Beatles in pop-chart history. "Tragedy" was the fifth of those six.

Teaching "Tragedy" in 1979 context illuminates the specific moment of disco's commercial apex. *Saturday Night Fever* (1977) had made disco the dominant commercial sound; the Bee Gees were disco's commercial centerp
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*