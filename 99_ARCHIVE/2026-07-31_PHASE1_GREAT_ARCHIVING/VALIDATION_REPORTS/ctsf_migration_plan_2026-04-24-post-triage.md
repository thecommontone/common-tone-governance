---
title: "CTSF Migration Plan"
date: 2026-04-24 07:12
mode: EXECUTE
source: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6222
**Will migrate:** 14
**Will skip:** 6208
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6219 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 3 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 14 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6205 |
| utility file (not a song entry) | 3 |

## Renames

- Files keeping current filename: **14**
- Files being renamed:            **0**

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 0 | 0.0% |
| `tonic` | 14 | 100.0% |
| `mode` | 14 | 100.0% |
| `meter` | 14 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `album` | 14 | 100.0% |
| `legacy_source` | 14 | 100.0% |
| `legacy_tempo_bpm` | 14 | 100.0% |

## Sample preview — first 3 migrated files

### `ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md` → `ARCHIE_BELL_AND_THE_DRELLS - TIGHTEN_UP.md`

```markdown
---
ct_format: '1.3'
song: TIGHTEN_UP
artist: ARCHIE_BELL_AND_THE_DRELLS
year: 1968
tonic: unknown
mode: unknown
meter: unknown
album: Atlantic Records — Archie Bell & the Drells
legacy_source: general music theory knowledge + early-funk historical record
legacy_tempo_bpm: 112
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# TIGHTEN_UP — ARCHIE_BELL_AND_THE_DRELLS (1968)

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

# Tighten Up — Archie Bell & the Drells

**Artist:** [[ARCHIE_BELL_AND_THE_DRELLS]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=tighten+up+archie+bell+drells+1968)
- **Chord Chart:**

## Theoretical Tags
`#era/1960s` `#genre/early-funk` `#genre/r-and-b` `#form/two-part-with-break` `#rhythm/funk-groove` `#harmony/blues-i-iv` `#historical/houston-sound` `#historical/archie-bell-drells`

## Concepts Demonstrated

### 1. Early-Funk Proto-Groove → [[01.3 It's About Time]]

"Tighten Up" reached #1 on the Billboard Hot 100 in May 1968 and became one of the defining early-funk records. The song's groove — a tight, precise bass-and-drum pattern with sparse horn punctuation and rhythm-guitar chanks on the offbeats — anticipates the full-formed funk aesthetic that James Brown, Sly & the Family Stone, and The Meters would develop through 1968-1970.

Understanding "Tighten Up" as proto-funk illuminates a specific moment in Black American popular music: the transition from 1960s R&B / soul (Motown's dominant sound, Atlan
... [truncated]
```

### `BARBRA_STREISAND - EVERGREEN.md` → `BARBRA_STREISAND - EVERGREEN.md`

```markdown
---
ct_format: '1.3'
song: EVERGREEN
artist: BARBRA_STREISAND
year: 1976
tonic: unknown
mode: unknown
meter: unknown
album: Columbia Records — 'A Star Is Born' soundtrack
legacy_source: general music theory knowledge + film-musical historical record
legacy_tempo_bpm: 72
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# EVERGREEN — BARBRA_STREISAND (1976)

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

# Evergreen (Love Theme from "A Star Is Born") — Barbra Streisand

**Artist:** [[BARBRA_STREISAND]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=evergreen+streisand+star+is+born+1976)
- **Chord Chart:**

## Theoretical Tags
`#era/1970s` `#genre/film-song` `#genre/adult-contemporary` `#form/aaba` `#harmony/extended-chords` `#historical/oscar-best-song-1977` `#historical/streisand-composer` `#historical/star-is-born-1976`

## Concepts Demonstrated

### 1. Streisand as Composer, Not Just Performer → [[01.1 Pop Music, huh?]]

"Evergreen" was composed by Barbra Streisand herself (with lyrics by Paul Williams) — a significant creative-authorship fact. Streisand had built her career primarily as a performer of other writers' material; "Evergreen" was her first major commercial composition. The song won the 1977 Academy Award for Best Original Song and the 1977 Grammy for Song of the Year, establishing Streisand as a compositional force alongside her performing career.

Female composers in mainstream 1970s pop were rare and often und
... [truncated]
```

### `BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md` → `BARRY_SADLER - BALLAD_OF_THE_GREEN_BERETS.md`

```markdown
---
ct_format: '1.3'
song: BALLAD_OF_THE_GREEN_BERETS
artist: BARRY_SADLER
year: 1966
tonic: unknown
mode: unknown
meter: unknown
album: RCA Victor — Staff Sergeant Barry Sadler
legacy_source: general music theory knowledge + Vietnam-era popular-song historical
  record
legacy_tempo_bpm: 108
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# BALLAD_OF_THE_GREEN_BERETS — BARRY_SADLER (1966)

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

# The Ballad of the Green Berets — SSgt. Barry Sadler

**Artist:** [[BARRY_SADLER]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=ballad+of+the+green+berets+barry+sadler+1966)
- **Chord Chart:**

## Theoretical Tags
`#era/1960s` `#genre/military-song` `#genre/patriotic-ballad` `#form/verse-chorus` `#harmony/martial` `#historical/vietnam-era` `#historical/pro-war-mainstream` `#historical/counter-counterculture`

## Concepts Demonstrated

### 1. The Pro-War Mainstream Hit → [[01.1 Pop Music, huh?]]

"The Ballad of the Green Berets" was the #1 Billboard Hot 100 single for five weeks in early 1966 and the best-selling pop single of the entire year — a remarkable commercial result for a song that was explicitly pro-military, pro-Vietnam War, and written by an active-duty U.S. Army Special Forces medic. The record sold over 9 million copies, more than any Beatles single released in 1966.

This commercial result complicates the standard narrative about 1960s popular music's relationship to Vietnam. 
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*