---
title: "CTSF Migration Plan"
date: 2026-04-24 08:08
mode: EXECUTE
source: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6252
**Will migrate:** 2
**Will skip:** 6250
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6249 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 3 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 2 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6247 |
| utility file (not a song entry) | 3 |

## Renames

- Files keeping current filename: **2**
- Files being renamed:            **0**

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 0 | 0.0% |
| `tonic` | 2 | 100.0% |
| `mode` | 2 | 100.0% |
| `meter` | 2 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `album` | 2 | 100.0% |
| `legacy_source` | 2 | 100.0% |
| `legacy_tempo_bpm` | 2 | 100.0% |

## Sample preview — first 3 migrated files

### `GLASS_ANIMALS - HEAT_WAVES.md` → `GLASS_ANIMALS - HEAT_WAVES.md`

```markdown
---
ct_format: '1.3'
song: HEAT_WAVES
artist: GLASS_ANIMALS
year: 2020 (original release) / 2022 (commercial peak)
tonic: unknown
mode: unknown
meter: unknown
album: Wolf Tone / Polydor — 'Dreamland'
legacy_source: general music theory knowledge + 2020s indie-pop historical record
legacy_tempo_bpm: 81
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# HEAT_WAVES — GLASS_ANIMALS (2020 (original release) / 2022 (commercial peak))

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

# Heat Waves — Glass Animals

**Artist:** [[GLASS_ANIMALS]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=heat+waves+glass+animals+2020)
- **Chord Chart:**

## Theoretical Tags
`#era/2020s` `#genre/indie-pop` `#form/verse-chorus` `#harmony/major-key` `#historical/tiktok-slow-climb` `#historical/59-weeks-on-chart` `#historical/dave-bayley-production` `#historical/pandemic-era-hit`

## Concepts Demonstrated

### 1. The Slow-Climb Chart Record → [[01.1 Pop Music, huh?]]

"Heat Waves" achieved a specific commercial milestone: the slowest-ever climb to #1 on the Billboard Hot 100. Released June 2020, it took 59 weeks to reach #1 (March 2022) — over a year of gradually building chart position before finally topping. This unusual trajectory reflects streaming-era commercial dynamics where songs can accumulate streams over extended periods via playlist inclusion, TikTok viral moments, and algorithmic amplification.

Compare this with traditional commercial mecha
... [truncated]
```

### `HARRY_STYLES - AS_IT_WAS.md` → `HARRY_STYLES - AS_IT_WAS.md`

```markdown
---
ct_format: '1.3'
song: AS_IT_WAS
artist: HARRY_STYLES
year: 2022
tonic: unknown
mode: unknown
meter: unknown
album: Erskine / Columbia — 'Harry's House'
legacy_source: general music theory knowledge + 2020s pop historical record
legacy_tempo_bpm: 174
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# AS_IT_WAS — HARRY_STYLES (2022)

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

# As It Was — Harry Styles

**Artist:** [[HARRY_STYLES]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=as+it+was+harry+styles+2022)
- **Chord Chart:**

## Theoretical Tags
`#era/2020s` `#genre/indie-pop` `#form/verse-chorus` `#harmony/major-key` `#texture/80s-synth-pop-revival` `#historical/15-weeks-number-one` `#historical/kid-harpoon-production` `#historical/pandemic-nostalgia`

## Concepts Demonstrated

### 1. 15 Weeks at #1 → [[01.1 Pop Music, huh?]]

"As It Was" reached #1 on the Billboard Hot 100 in April 2022 and stayed there for 15 weeks — the longest #1 run since "Old Town Road" (19 weeks, 2019). The song dominated the 2022 commercial-pop landscape more completely than any single record since the streaming era began. It also became the most-streamed song globally in 2022 on Spotify.

The 15-week #1 run reflects specific 2022 commercial dynamics. Styles had built substantial fan infrastructure through his One Direction and solo careers; his album *Harry's House* received extensive critical praise; "As It Was" combined broad-demographic ap
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*