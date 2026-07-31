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
**Total files seen:** 6223
**Will migrate:** 1
**Will skip:** 6222
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6220 | YAML parsed cleanly on first try |
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
| already ct_format=1.3 | 6219 |
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

### `BARRY_MANILOW - COPACABANA.md` → `BARRY_MANILOW - COPACABANA.md`

```markdown
---
ct_format: '1.3'
song: COPACABANA
artist: BARRY_MANILOW
year: 1978
tonic: unknown
mode: unknown
meter: unknown
album: Arista Records — 'Even Now'
legacy_source: general music theory knowledge + narrative-pop historical record
legacy_tempo_bpm: 128
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# COPACABANA — BARRY_MANILOW (1978)

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

# Copacabana (At the Copa) — Barry Manilow

**Artist:** [[BARRY_MANILOW]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=copacabana+barry+manilow+1978)
- **Chord Chart:**

## Theoretical Tags
`#era/1970s` `#genre/narrative-pop` `#genre/disco-era-adjacent` `#form/narrative-verse-chorus` `#harmony/minor-to-major` `#rhythm/latin-flavored` `#historical/barry-manilow` `#historical/grammy-1978`

## Concepts Demonstrated

### 1. The Narrative Pop Hit in the Disco Era → [[04.6 Advanced Form]]

"Copacabana" tells a complete three-act story: Lola the showgirl and Tony the bartender fall in love at the Copacabana nightclub in the 1940s; a rival, Rico, arrives and starts a fight over Lola; Tony is killed in the brawl; decades later, an aging Lola still sits at the Copa drinking and mourning. Manilow, Sussman, and Feldman crafted a self-contained short story in approximately four and a half minutes of song.

This narrative-pop approach was distinctive in 1978, when most chart-topping pop was disco dance music or rock material that typically didn't carry complet
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*