---
title: "CTSF Migration Plan"
date: 2026-04-24 19:26
mode: EXECUTE
source: "/sessions/gifted-sweet-galileo/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/gifted-sweet-galileo/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6119
**Will migrate:** 3
**Will skip:** 6116
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6116 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 3 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 3 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6113 |
| utility file (not a song entry) | 3 |

## Renames

- Files keeping current filename: **3**
- Files being renamed:            **0**

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 0 | 0.0% |
| `tonic` | 3 | 100.0% |
| `mode` | 3 | 100.0% |
| `meter` | 3 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `album` | 3 | 100.0% |
| `legacy_source` | 3 | 100.0% |
| `legacy_tempo_bpm` | 3 | 100.0% |

## Sample preview — first 3 migrated files

### `KENDRICK_LAMAR - NOT_LIKE_US.md` → `KENDRICK_LAMAR - NOT_LIKE_US.md`

```markdown
---
ct_format: '1.3'
song: NOT_LIKE_US
artist: KENDRICK_LAMAR
year: 2024
tonic: unknown
mode: unknown
meter: unknown
album: pgLang / Interscope Records — Drake diss single
legacy_source: general music theory knowledge + 2020s hip-hop historical record
legacy_tempo_bpm: 101
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# NOT_LIKE_US — KENDRICK_LAMAR (2024)

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

# Not Like Us — Kendrick Lamar

**Artist:** [[KENDRICK_LAMAR]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=not+like+us+kendrick+lamar+2024)
- **Chord Chart:**

## Theoretical Tags
`#era/2020s` `#genre/hip-hop` `#genre/diss-track` `#form/verse-chorus` `#harmony/minor-key` `#texture/mustard-production` `#historical/drake-feud-2024` `#historical/grammy-record-of-year-2025` `#historical/super-bowl-halftime-2025`

## Concepts Demonstrated

### 1. Commercial Peak of the Kendrick-Drake Feud → [[01.1 Pop Music, huh?]]

"Not Like Us" was released May 4, 2024 as the culminating diss track in Kendrick Lamar's ongoing feud with Drake (the feud had intensified across multiple tracks from both artists throughout spring 2024: "Push Ups," "Taylor Made Freestyle," "Euphoria," "6:16 in LA," "Family Matters," "Meet the Grahams," "Not Like Us"). The track reached #1 on the Billboard Hot 100 its first week — a rare diss-track commercial achievement.

Hip-hop diss tracks have recurring cultural presence but rarely achieve mainstream #1 chart s
... [truncated]
```

### `MILEY_CYRUS - FLOWERS.md` → `MILEY_CYRUS - FLOWERS.md`

```markdown
---
ct_format: '1.3'
song: FLOWERS
artist: MILEY_CYRUS
year: 2023
tonic: unknown
mode: unknown
meter: unknown
album: Columbia Records — 'Endless Summer Vacation'
legacy_source: general music theory knowledge + 2020s pop historical record
legacy_tempo_bpm: 118
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# FLOWERS — MILEY_CYRUS (2023)

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

# Flowers — Miley Cyrus

**Artist:** [[MILEY_CYRUS]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=flowers+miley+cyrus+2023)
- **Chord Chart:**

## Theoretical Tags
`#era/2020s` `#genre/pop` `#form/verse-prechorus-chorus` `#harmony/minor-key` `#lyrics/breakup-anthem-inversion` `#historical/miley-cyrus-commercial-peak` `#historical/grammy-record-of-year-2024` `#historical/bruno-mars-response-reading`

## Concepts Demonstrated

### 1. The "When I Was Your Man" Lyric Inversion → [[01.1 Pop Music, huh?]]

"Flowers" has been widely interpreted as a lyrical response to Bruno Mars's "When I Was Your Man" (2013) — specifically an inversion of that song's regretful content. Mars sang "I should have bought you flowers / And held your hand"; Cyrus sang "I can buy myself flowers / Write my name in the sand / Talk to myself for hours / Say things you don't understand."

The Mars "When I Was Your Man" had reportedly been Miley Cyrus's wedding song with ex-husband Liam Hemsworth (they divorced in 2020). The lyrical inversion became part of the song's commerci
... [truncated]
```

### `TAYLOR_SWIFT - ANTI_HERO.md` → `TAYLOR_SWIFT - ANTI_HERO.md`

```markdown
---
ct_format: '1.3'
song: ANTI_HERO
artist: TAYLOR_SWIFT
year: 2022
tonic: unknown
mode: unknown
meter: unknown
album: Republic Records — 'Midnights'
legacy_source: general music theory knowledge + 2020s pop historical record
legacy_tempo_bpm: 97
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# ANTI_HERO — TAYLOR_SWIFT (2022)

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

# Anti-Hero — Taylor Swift

**Artist:** [[TAYLOR_SWIFT]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=anti-hero+taylor+swift+2022)
- **Chord Chart:**

## Theoretical Tags
`#era/2020s` `#genre/synth-pop` `#form/verse-chorus` `#harmony/major-key` `#texture/jack-antonoff-production` `#lyrics/self-critical` `#historical/8-weeks-number-one` `#historical/taylors-version-era`

## Concepts Demonstrated

### 1. Taylor Swift's Mature-Career Commercial Dominance → [[01.1 Pop Music, huh?]]

"Anti-Hero" reached #1 on the Billboard Hot 100 for eight weeks in late 2022 / early 2023 — confirming Taylor Swift's position as the dominant artist of the early-2020s commercial-pop landscape. *Midnights* (October 2022) sold 1.14 million copies in its first week; subsequent releases (*Taylor's Version* re-recordings of her earlier albums, *The Tortured Poets Department* 2024) have continued her commercial-peak trajectory.

Swift's career trajectory has specific late-career characteristics: she achieved childhood-superstar commercial success (2006-2012 country-pop era), succes
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*