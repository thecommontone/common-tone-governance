---
title: "CTSF Migration Plan"
date: 2026-04-24 07:02
mode: EXECUTE
source: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6206
**Will migrate:** 1
**Will skip:** 6205
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 6206 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 0 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 0 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 1 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 6205 |

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

### `THE_NEW_VAUDEVILLE_BAND - WINCHESTER_CATHEDRAL.md` → `THE_NEW_VAUDEVILLE_BAND - WINCHESTER_CATHEDRAL.md`

```markdown
---
ct_format: '1.3'
song: WINCHESTER_CATHEDRAL
artist: THE_NEW_VAUDEVILLE_BAND
year: 1966
tonic: unknown
mode: unknown
meter: unknown
album: Fontana Records
legacy_source: general music theory knowledge + novelty-song historical record
legacy_tempo_bpm: 112
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# WINCHESTER_CATHEDRAL — THE_NEW_VAUDEVILLE_BAND (1966)

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

# Winchester Cathedral — The New Vaudeville Band

**Artist:** [[THE_NEW_VAUDEVILLE_BAND]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=winchester+cathedral+new+vaudeville+band+1966)
- **Chord Chart:**

## Theoretical Tags
`#era/1960s` `#genre/novelty-song` `#genre/retro-pastiche` `#form/aaba` `#harmony/1920s-vocabulary` `#texture/megaphone-vocal` `#historical/grammy-winner` `#historical/british-invasion-retro`

## Concepts Demonstrated

### 1. The Retro-Pastiche Novelty Hit → [[01.1 Pop Music, huh?]]

"Winchester Cathedral" reached #1 on the US Billboard Hot 100 in December 1966 and won the 1967 Grammy Award for Best Contemporary (R&R) Recording — a distinction that seems incongruous given that the song sounds like a deliberate 1920s pastiche rather than contemporary rock and roll. The Grammy reflected the song's enormous commercial success and the voting academy's often-conservative preferences, but it also illustrates an important point about 1960s popular music: amid the British Invasion, Motown, psychedelia, and fol
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*