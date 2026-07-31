---
title: "CTSF Migration Plan"
date: 2026-04-24 06:12
mode: DRY-RUN
source: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (DRY-RUN)

**Source:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6361
**Will migrate:** 6101
**Will skip:** 56
**Needs human review:** 204

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 52 |
| utility file (not a song entry) | 3 |
| already ct_format=1.2 | 1 |

## Files needing human review

| Reason | Count |
|---|---:|
| cannot determine artist+song from frontmatter or filename | 194 |
| frontmatter song 'Smooth Operator - Single Version' does not match filename stem 'Song Name' — possible bad auto-enrichment | 1 |
| frontmatter song 'Born To Be My Baby' does not match filename stem 'Bon Jovi' — possible bad auto-enrichment | 1 |
| frontmatter song 'Бритни Спирс' does not match filename stem 'Britney Spears' — possible bad auto-enrichment | 1 |
| frontmatter song 'Everybody’s Looking At Me' does not match filename stem 'Ever Ever After' — possible bad auto-enrichment | 1 |
| frontmatter song 'Formed a Band' does not match filename stem 'Form in Top 20' — possible bad auto-enrichment | 1 |
| frontmatter song 'Waves' does not match filename stem 'Kanye West' — possible bad auto-enrichment | 1 |
| frontmatter song 'It's Impossible - Digitally Mastered - May - June, 1988' does not match filename stem 'MASTER LISTENING LIST' — possible bad auto-enrichment | 1 |
| frontmatter song 'Ob-La-Di, Ob-La-Da - Remastered 2009' does not match filename stem 'Obla' — possible bad auto-enrichment | 1 |
| frontmatter song 'Reminder' does not match filename stem 'REM' — possible bad auto-enrichment | 1 |
| frontmatter song 'Wolves' does not match filename stem 'Selena Gomez' — possible bad auto-enrichment | 1 |

### Sample (first 15):

- `- Black Orpheus.md` — cannot determine artist+song from frontmatter or filename
- `- Blue Moon.md` — cannot determine artist+song from frontmatter or filename
- `- Days of Wine And Roses.md` — cannot determine artist+song from frontmatter or filename
- `- Final Countdown.md` — cannot determine artist+song from frontmatter or filename
- `- Fried Bananas.md` — cannot determine artist+song from frontmatter or filename
- `- Godfather Theme.md` — cannot determine artist+song from frontmatter or filename
- `- Graduation (Friends Forever).md` — cannot determine artist+song from frontmatter or filename
- `- How High the Moon.md` — cannot determine artist+song from frontmatter or filename
- `- Koko.md` — cannot determine artist+song from frontmatter or filename
- `- Oh Come All Ye Faithful.md` — cannot determine artist+song from frontmatter or filename
- `- Shadow of Your Smile.md` — cannot determine artist+song from frontmatter or filename
- `- Song Name.md` — frontmatter song 'Smooth Operator - Single Version' does not match filename stem 'Song Name' — possible bad auto-enrichment
- `- Star Trek Theme.md` — cannot determine artist+song from frontmatter or filename
- `- Take Me Out To The Ball Game.md` — cannot determine artist+song from frontmatter or filename
- `- The Bare Necessities.md` — cannot determine artist+song from frontmatter or filename

## Renames

- Files keeping current filename: **1**
- Files being renamed:            **6100**

### Sample renames (first 25)

| Old filename | New filename |
|---|---|
| `(G)Idle - LION.md` | `IDLE - LION.md` |
| `- Corvocado.md` | `SIFARE_BAND - QUIET_NIGHTS_OF_QUIET_STARS_CORVOCADO.md` |
| `- Fame.md` | `DAVID_BOWIE - FAME_2016_REMASTER.md` |
| `- Flintstones.md` | `GEEK_MUSIC - THE_FLINTSTONES_MAIN_THEME.md` |
| `- Green Dolphin Street.md` | `BABY_LULLABIES_BABY_MUSIC_LITTLE_BABY_MUSIC - ON_GREEN_DOLPHIN_STREET_PIANO_JAZZ_VERSION.md` |
| `- Plaisir D'Amour.md` | `THE_SEEKERS - PLAISIR_DAMOUR_STEREO_2009_REMASTER.md` |
| `- Purple People Eater.md` | `JUDY_GARLAND - PURPLE_PEOPLE_EATER_LIVE.md` |
| `- Seems Like Old Times.md` | `LAUFEY - SEEMS_LIKE_OLD_TIMES_BONUS_TRACK.md` |
| `- Somewhere, My Love (Lara's Theme).md` | `PAUL_POTTS - DOVE_NON_SO_SOMEWHERE_MY_LOVE_LARAS_THEME_FROM_DOCTOR_JIVAGO.md` |
| `- Still Got The Blues.md` | `GARY_MOORE - STILL_GOT_THE_BLUES_LIVE_FROM_THE_BLUES_ALIVE_TOUR_UK1993.md` |
| `- Watch What Happens.md` | `ODONEL_LEVY - WATCH_WHAT_HAPPENS_2024_REMASTERED_VERSION.md` |
| `- When A Man Loves A Woman.md` | `PERCY_SLEDGE - WHEN_A_MAN_LOVES_A_WOMAN_MONO.md` |
| `- Where Do I Begin (Love Story).md` | `SHIRLEY_BASSEY - LOVE_STORY_1994_REMASTER.md` |
| `- Woodchopper's Ball.md` | `TEN_YEARS_AFTER - WOODCHOPPERS_BALL_LIVE.md` |
| `- Yesterday When I Was Young.md` | `SHIRLEY_BASSEY - YESTERDAY_WHEN_I_WAS_YOUNG_1994_REMASTER.md` |
| `10,000 Maniacs - Candy Everybody Wants.md` | `10000_MANIACS - CANDY_EVERYBODY_WANTS.md` |
| `10cc - I'm Not In Love.md` | `10CC - IM_NOT_IN_LOVE.md` |
| `2 Live Crew - C'mon Babe.md` | `2_LIVE_CREW - CMON_BABE.md` |
| `2 Live Crew - Me So Horny.md` | `2_LIVE_CREW - ME_SO_HORNY.md` |
| `25 or 6 to 4 - Chicago.md` | `25_OR_6_TO_4 - CHICAGO.md` |
| `2Pac & Dr. Dre - California Love.md` | `2PAC_AND_DR_DRE - CALIFORNIA_LOVE.md` |
| `2Pac - Brenda's Got A Baby.md` | `2PAC - BRENDAS_GOT_A_BABY.md` |
| `2Pac - Changes.md` | `2PAC - CHANGES.md` |
| `2Pac - Dear Mama.md` | `2PAC - DEAR_MAMA.md` |
| `2Pac - Hit 'Em Up.md` | `2PAC - HIT_EM_UP.md` |

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 4556 | 74.7% |
| `tonic` | 6101 | 100.0% |
| `mode` | 6101 | 100.0% |
| `meter` | 6101 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `legacy_source` | 1608 | 26.4% |
| `spotify_link` | 1399 | 22.9% |
| `composers` | 953 | 15.6% |
| `album` | 388 | 6.4% |
| `legacy_tempo_bpm` | 279 | 4.6% |
| `genre` | 148 | 2.4% |
| `legacy_key` | 68 | 1.1% |

## Sample preview — first 3 migrated files

### `(G)Idle - LION.md` → `IDLE - LION.md`

```markdown
---
ct_format: '1.3'
song: LION
artist: (G)Idle
year: unknown
tonic: unknown
mode: unknown
meter: unknown
ct_entry_date: '2026-04-11'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.0 (source: filename; schema-compliant
  skeleton, analytical fields unknown)'
---

# LION — (G)Idle

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

# LION — (G)Idle

**Artist:** [[(G)Idle]]

## Analytical Notes
*(From FileMaker Database)*
# LION — (G)Idle


```

### `- Corvocado.md` → `SIFARE_BAND - QUIET_NIGHTS_OF_QUIET_STARS_CORVOCADO.md`

```markdown
---
ct_format: '1.3'
song: Quiet Nights of Quiet Stars - Corvocado
artist: Sifare Band
year: 2012
tonic: unknown
mode: unknown
meter: unknown
spotify_link: https://open.spotify.com/track/79FYkHPGtNnFeJw6jlO4XX
genre: Latin Jazz
legacy_source: 'Merged: FileMaker Database + Original REPERTOIRE'
ct_entry_date: '2026-04-11'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.0 (source: frontmatter;
  schema-compliant skeleton, analytical fields unknown)'
---

# QUIET NIGHTS OF QUIET STARS - CORVOCADO — Sifare Band (2012)

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

# Corvocado — 

## Analytical Notes
*(From FileMaker Database)*
# Corvocado —


```

### `- Fame.md` → `DAVID_BOWIE - FAME_2016_REMASTER.md`

```markdown
---
ct_format: '1.3'
song: Fame - 2016 Remaster
artist: David Bowie
year: 1975
tonic: unknown
mode: unknown
meter: unknown
spotify_link: https://open.spotify.com/track/1PehfITh0TTRx3LkDdV4h3
genre: TV Theme
legacy_source: 'Merged: FileMaker Database + Original REPERTOIRE'
ct_entry_date: '2026-04-11'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.0 (source: frontmatter;
  schema-compliant skeleton, analytical fields unknown)'
---

# FAME - 2016 REMASTER — David Bowie (1975)

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

# Fame — 

## Analytical Notes
*(From FileMaker Database)*
# Fame —


```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in DRY-RUN mode.*