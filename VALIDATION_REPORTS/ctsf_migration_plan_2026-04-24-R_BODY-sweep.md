---
title: "CTSF Migration Plan"
date: 2026-04-24 07:38
mode: EXECUTE
source: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6236
**Will migrate:** 16
**Will skip:** 6220
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6233 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 3 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 16 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6217 |
| utility file (not a song entry) | 3 |

## Renames

- Files keeping current filename: **16**
- Files being renamed:            **0**

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 0 | 0.0% |
| `tonic` | 16 | 100.0% |
| `mode` | 16 | 100.0% |
| `meter` | 16 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `album` | 16 | 100.0% |
| `legacy_source` | 16 | 100.0% |
| `legacy_tempo_bpm` | 16 | 100.0% |

## Sample preview — first 3 migrated files

### `BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md` → `BRYAN_ADAMS - EVERYTHING_I_DO_I_DO_IT_FOR_YOU.md`

```markdown
---
ct_format: '1.3'
song: EVERYTHING_I_DO_I_DO_IT_FOR_YOU
artist: BRYAN_ADAMS
year: 1991
tonic: unknown
mode: unknown
meter: unknown
album: 'A&M Records — ''Waking Up the Neighbours'' / ''Robin Hood: Prince of Thieves''
  soundtrack'
legacy_source: general music theory knowledge + 1990s pop historical record
legacy_tempo_bpm: 62
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# EVERYTHING_I_DO_I_DO_IT_FOR_YOU — BRYAN_ADAMS (1991)

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

# (Everything I Do) I Do It for You — Bryan Adams

**Artist:** [[BRYAN_ADAMS]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=everything+i+do+i+do+it+for+you+bryan+adams+1991)
- **Chord Chart:**

## Theoretical Tags
`#era/1990s` `#genre/power-ballad` `#genre/film-song` `#form/verse-chorus` `#harmony/extended-chords` `#historical/mutt-lange-production` `#historical/robin-hood-soundtrack` `#historical/longest-running-uk-number-one`

## Concepts Demonstrated

### 1. The Longest-Running UK #1 in Chart History → [[01.1 Pop Music, huh?]]

"(Everything I Do) I Do It for You" spent 16 consecutive weeks at #1 on the UK Singles Chart in summer 1991 — the longest-running UK #1 in the entire chart's history, a record that stood until Frankie Laine's 18-week run with "I Believe" (1953) was eventually surpassed by "Candle in the Wind 1997" (which ran 45 weeks though reached #1 only for 5 weeks). Even today, Adams's 16-week continuous run remains among the longest.

... [truncated]
```

### `DOLLY_PARTON - 9_TO_5.md` → `DOLLY_PARTON - 9_TO_5.md`

```markdown
---
ct_format: '1.3'
song: 9_TO_5
artist: DOLLY_PARTON
year: 1980
tonic: unknown
mode: unknown
meter: unknown
album: RCA — '9 to 5 and Odd Jobs' / title song from the film
legacy_source: general music theory knowledge + country-pop historical record
legacy_tempo_bpm: 116
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# 9_TO_5 — DOLLY_PARTON (1980)

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

# 9 to 5 — Dolly Parton

**Artist:** [[DOLLY_PARTON]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=dolly+parton+9+to+5+1980)
- **Chord Chart:**

## Theoretical Tags
`#era/1980s` `#genre/country-pop` `#genre/film-song` `#form/aaba` `#lyrics/working-class-anthem` `#harmony/secondary-dominants` `#texture/typewriter-percussion` `#historical/dolly-parton-crossover`

## Concepts Demonstrated

### 1. The Working-Class Anthem → [[01.1 Pop Music, huh?]]

"9 to 5" became a #1 pop hit, a #1 country hit, and an Oscar-nominated film song — a rare triple achievement that confirmed Dolly Parton's ability to operate simultaneously in country, pop, and film markets. The song's lyric voiced the frustrations of salaried workers in the Reagan-era American workplace: "Workin' nine to five, what a way to make a livin'... barely gettin' by." This made it the defining working-class anthem of the early 1980s and an unusually political song for mainstream pop-country.

Working-class anthems have a specific tradition in American popular music (Merle Haggard'
... [truncated]
```

### `JOHN_MELLENCAMP - JACK_AND_DIANE.md` → `JOHN_MELLENCAMP - JACK_AND_DIANE.md`

```markdown
---
ct_format: '1.3'
song: JACK_AND_DIANE
artist: JOHN_MELLENCAMP
year: 1982
tonic: unknown
mode: unknown
meter: unknown
album: Riva Records — 'American Fool'
legacy_source: general music theory knowledge + heartland-rock historical record
legacy_tempo_bpm: 104
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# JACK_AND_DIANE — JOHN_MELLENCAMP (1982)

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

# Jack and Diane — John Mellencamp

**Artist:** [[JOHN_MELLENCAMP]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=jack+and+diane+john+mellencamp+1982)
- **Chord Chart:**

## Theoretical Tags
`#era/1980s` `#genre/heartland-rock` `#genre/narrative-rock` `#form/verse-chorus` `#harmony/primary-chords` `#texture/hand-clap-percussion` `#historical/heartland-rock` `#historical/john-mellencamp`

## Concepts Demonstrated

### 1. Heartland Rock as Genre Category → [[01.1 Pop Music, huh?]]

"Jack and Diane" is one of the canonical early-1980s "heartland rock" records — a specific subgenre defined by American working-class subject matter, rural / small-town settings, straight-ahead rock instrumentation, and narrative lyric specificity. Other canonical heartland-rock artists: Bruce Springsteen (New Jersey), Bob Seger (Detroit), Tom Petty (Florida → California), Mellencamp (Indiana). Each staked out a specific American regional identity and wrote songs rooted in those specific places.

Heartland rock emerged as a commercially significant categor
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*