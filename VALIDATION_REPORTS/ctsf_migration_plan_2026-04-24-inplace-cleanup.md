---
title: "CTSF Migration Plan"
date: 2026-04-24 07:01
mode: EXECUTE
source: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6205
**Will migrate:** 3
**Will skip:** 6202
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6205 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 0 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 3 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6202 |

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

### `ACKER_BILK - STRANGER_ON_THE_SHORE.md` → `ACKER_BILK - STRANGER_ON_THE_SHORE.md`

```markdown
---
ct_format: '1.3'
song: STRANGER_ON_THE_SHORE
artist: ACKER_BILK
year: 1961
tonic: unknown
mode: unknown
meter: unknown
album: Atco Records / Columbia Records (UK)
legacy_source: general music theory knowledge + British-invasion-precursor historical
  record
legacy_tempo_bpm: 76
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# STRANGER_ON_THE_SHORE — ACKER_BILK (1961)

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

# Stranger on the Shore — Acker Bilk

**Artist:** [[ACKER_BILK]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=stranger+on+the+shore+acker+bilk+1961)
- **Chord Chart:**

## Theoretical Tags
`#era/1960s` `#genre/instrumental-pop` `#genre/mood-music` `#instrument/clarinet` `#form/aaba` `#harmony/extended-chords` `#historical/first-british-number-one-us` `#historical/pre-beatles-british-invasion`

## Concepts Demonstrated

### 1. First British Record to Top the US Billboard Chart → [[01.1 Pop Music, huh?]]

"Stranger on the Shore" holds a specific historical distinction: it was the first recording by a British artist to reach #1 on the US Billboard Hot 100 (May 1962), preceding the Beatles' "I Want to Hold Your Hand" by nearly two years. This is an important detail for reading the "British Invasion" narrative correctly — the standard story treats the Beatles' 1964 arrival as the moment when British music broke through in America, but Bilk's instrumental clarinet piece had already crossed the Atlantic two years e
... [truncated]
```

### `HARVEY_SCHMIDT - TRY_TO_REMEMBER.md` → `HARVEY_SCHMIDT - TRY_TO_REMEMBER.md`

```markdown
---
ct_format: '1.3'
song: TRY_TO_REMEMBER
artist: HARVEY_SCHMIDT
year: 1960
tonic: unknown
mode: unknown
meter: unknown
album: From the off-Broadway musical 'The Fantasticks'
legacy_source: general music theory knowledge + off-Broadway historical record
legacy_tempo_bpm: 108
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# TRY_TO_REMEMBER — HARVEY_SCHMIDT (1960)

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

# Try to Remember — Harvey Schmidt & Tom Jones

**Artist:** [[HARVEY_SCHMIDT]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=try+to+remember+fantasticks+jerry+orbach)
- **Chord Chart:**

## Theoretical Tags
`#era/1960s` `#genre/off-broadway` `#genre/musical-theatre` `#form/aaba` `#meter/3-4-waltz` `#harmony/folk-tinged` `#historical/the-fantasticks` `#historical/longest-running-musical`

## Concepts Demonstrated

### 1. Off-Broadway as a Separate Commercial Category → [[01.1 Pop Music, huh?]]

"Try to Remember" is the opening number of *The Fantasticks*, which premiered off-Broadway in 1960 and ran continuously until 2002 — 42 years, 17,162 performances, making it the longest-running musical in world history. The show's economic model was specifically off-Broadway: a small cast, simple production, intimate venue (Sullivan Street Playhouse, 149 seats). *The Fantasticks* demonstrated that off-Broadway could produce culturally enduring work on dramatically different economics than the big Broadway houses, and its succes
... [truncated]
```

### `THE_SINGING_NUN - DOMINIQUE.md` → `THE_SINGING_NUN - DOMINIQUE.md`

```markdown
---
ct_format: '1.3'
song: DOMINIQUE
artist: THE_SINGING_NUN
year: 1963
tonic: unknown
mode: unknown
meter: unknown
album: Philips Records
legacy_source: general music theory knowledge + novelty-song historical record
legacy_tempo_bpm: 128
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# DOMINIQUE — THE_SINGING_NUN (1963)

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

# Dominique — The Singing Nun

**Artist:** [[THE_SINGING_NUN]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=dominique+singing+nun+1963)
- **Chord Chart:**

## Theoretical Tags
`#era/1960s` `#genre/novelty-song` `#genre/foreign-language-pop` `#form/verse-chorus` `#harmony/primary-chords` `#instrumentation/acoustic-guitar` `#historical/belgian-nun` `#historical/1963-number-one`

## Concepts Demonstrated

### 1. The Foreign-Language Pop Hit → [[01.1 Pop Music, huh?]]

"Dominique" — sung in French by a Belgian Catholic nun (Jeannine Deckers, known publicly as "Soeur Sourire" or "Sister Smile") — reached #1 on the US Billboard Hot 100 in December 1963, spent four weeks at the top, and became one of the most unlikely #1 records in American chart history. A French-language acoustic-guitar song about a 13th-century Dominican saint, performed by a religious sister, topped the chart in a country where the dominant pop was rock and roll and R&B.

Foreign-language pop hits in America are rare but recurring: "Sukiyaki" (Kyu Sakamoto, Japanese, 1963), "Dominique" (French
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*