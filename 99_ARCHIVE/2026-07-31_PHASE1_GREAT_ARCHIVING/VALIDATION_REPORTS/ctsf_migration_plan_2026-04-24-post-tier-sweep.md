---
title: "CTSF Migration Plan"
date: 2026-04-24 08:04
mode: EXECUTE
source: "/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (EXECUTE)

**Source:** `/sessions/gracious-peaceful-brown/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6246
**Will migrate:** 19
**Will skip:** 6227
**Needs human review:** 0

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 19 | YAML parsed cleanly on first try |
| `sanitized` | 0 | parsed after stripping stray top-level bullets |
| `regex` | 6224 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 3 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 19 | clean 'Artist - Title' filename — trusted |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format= '1.3' | 6224 |
| utility file (not a song entry) | 3 |

## Renames

- Files keeping current filename: **19**
- Files being renamed:            **0**

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 0 | 0.0% |
| `tonic` | 19 | 100.0% |
| `mode` | 19 | 100.0% |
| `meter` | 19 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `album` | 19 | 100.0% |
| `legacy_source` | 19 | 100.0% |
| `legacy_tempo_bpm` | 19 | 100.0% |

## Sample preview — first 3 migrated files

### `50_CENT - IN_DA_CLUB.md` → `50_CENT - IN_DA_CLUB.md`

```markdown
---
ct_format: '1.3'
song: IN_DA_CLUB
artist: 50_CENT
year: 2003
tonic: unknown
mode: unknown
meter: unknown
album: Shady/Aftermath/Interscope Records — 'Get Rich or Die Tryin''
legacy_source: general music theory knowledge + 2000s hip-hop historical record
legacy_tempo_bpm: 90
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# IN_DA_CLUB — 50_CENT (2003)

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

# In Da Club — 50 Cent

**Artist:** [[50_CENT]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=in+da+club+50+cent+2003)
- **Chord Chart:**

## Theoretical Tags
`#era/2000s` `#genre/hip-hop` `#genre/gangsta-rap` `#form/verse-chorus` `#harmony/minor-key` `#texture/string-hook` `#historical/dr-dre-production` `#historical/shady-aftermath` `#historical/50-cent-breakthrough`

## Concepts Demonstrated

### 1. Hip-Hop Commercial Dominance in 2003 → [[01.1 Pop Music, huh?]]

"In Da Club" reached #1 on the Billboard Hot 100 in February 2003 and stayed there for nine weeks. 50 Cent's *Get Rich or Die Tryin'* album sold 872,000 copies in its first week — then the biggest first-week for any debut album in SoundScan history — and eventually sold over 12 million copies in the US. By 2003, hip-hop had fully completed its transition from niche genre to dominant commercial pop, and "In Da Club" was one of the central artifacts of that dominance.

The 2003 commercial moment is worth teaching. Hip-hop's first commercial peak had been the 1990s (W
... [truncated]
```

### `ADELE - ROLLING_IN_THE_DEEP.md` → `ADELE - ROLLING_IN_THE_DEEP.md`

```markdown
---
ct_format: '1.3'
song: ROLLING_IN_THE_DEEP
artist: ADELE
year: 2010
tonic: unknown
mode: unknown
meter: unknown
album: XL / Columbia — '21'
legacy_source: general music theory knowledge + 2010s pop historical record
legacy_tempo_bpm: 105
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# ROLLING_IN_THE_DEEP — ADELE (2010)

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

# Rolling in the Deep — Adele

**Artist:** [[ADELE]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=rolling+in+the+deep+adele+2011)
- **Chord Chart:**

## Theoretical Tags
`#era/2010s` `#genre/pop-soul` `#form/verse-prechorus-chorus` `#harmony/minor-key` `#historical/adele-breakthrough` `#historical/paul-epworth-production` `#historical/grammy-record-of-year-2012` `#historical/british-soul-revival`

## Concepts Demonstrated

### 1. Adele's Commercial Phenomenon and the British Soul Revival → [[01.1 Pop Music, huh?]]

"Rolling in the Deep" was the lead single from Adele's *21* (January 2011). The album sold over 31 million copies worldwide and remained the best-selling album globally for two consecutive years (2011, 2012). "Rolling in the Deep" itself won the 2012 Grammy Record of the Year plus Song of the Year, and the album swept the 2012 Grammys.

Adele's commercial breakthrough was part of a broader British soul revival that included Amy Winehouse (*Back to Black*, 2006), Duffy (*Rockferry*, 2008), and the ongoing mainstream acceptance of Sam Smith and o
... [truncated]
```

### `BEYONCE - IRREPLACEABLE.md` → `BEYONCE - IRREPLACEABLE.md`

```markdown
---
ct_format: '1.3'
song: IRREPLACEABLE
artist: BEYONCE
year: 2006
tonic: unknown
mode: unknown
meter: unknown
album: Columbia Records — 'B'Day'
legacy_source: general music theory knowledge + 2000s pop historical record
legacy_tempo_bpm: 88
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  strict; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# IRREPLACEABLE — BEYONCE (2006)

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

# Irreplaceable — Beyoncé

**Artist:** [[BEYONCE]]

## Media & Links
- **Audio:** `![[]]`
- **Score / Lead Sheet:** `![[]]`
- **YouTube:** [Watch](https://www.youtube.com/results?search_query=irreplaceable+beyonce+2006)
- **Chord Chart:**

## Theoretical Tags
`#era/2000s` `#genre/r-and-b` `#form/verse-chorus` `#harmony/diatonic` `#texture/acoustic-guitar` `#historical/ne-yo-songwriter` `#historical/stargate-production` `#historical/10-weeks-number-one`

## Concepts Demonstrated

### 1. Ten Weeks at #1 → [[01.1 Pop Music, huh?]]

"Irreplaceable" spent ten consecutive weeks at #1 on the Billboard Hot 100 from December 2006 to March 2007 — one of the longest chart runs of the 2000s. Beyoncé's commercial position was cemented by this run; she had already been commercially successful via Destiny's Child and her solo debut *Dangerously in Love* (2003), but *B'Day* and particularly "Irreplaceable" established her as the dominant female pop/R&B artist of the era.

Beyoncé's 2000s commercial dominance preceded and eventually overlapped with Rihanna's rise (starting 2005) and Lady Gaga's (2008-2009), forming the female-pop triumvirate that dominated late-2000s c
... [truncated]
```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in EXECUTE mode.*