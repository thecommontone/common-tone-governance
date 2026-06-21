---
title: "CTSF Migration Plan"
date: 2026-04-24 06:35
mode: DRY-RUN
source: "/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/04_ARCHIVE/REPERTOIRE_LEGACY/REPERTOIRE_PRE_MIGRATION_2026-04-23"
spec: "01_SPECS/CTSF_SPEC.md v1.3.1"
tags: [migration, ctsf, repertoire]
---

# CTSF Migration Plan (DRY-RUN)

**Source:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/04_ARCHIVE/REPERTOIRE_LEGACY/REPERTOIRE_PRE_MIGRATION_2026-04-23`
**Write target:** `/sessions/amazing-loving-gates/mnt/__MY_BOOK/The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE`
**Total files seen:** 6363
**Will migrate:** 6148
**Will skip:** 56
**Needs human review:** 159

## Frontmatter parse-tier distribution (v1.1)

| Tier | Files | Meaning |
|---|---:|---|
| `strict` | 1756 | YAML parsed cleanly on first try |
| `sanitized` | 4362 | parsed after stripping stray top-level bullets |
| `regex` | 238 | field-by-field regex salvage (YAML structurally broken) |
| `none` | 7 | no frontmatter or nothing salvageable |

## Artist/song resolution source (v1.1)

| Source | Files | Meaning |
|---|---:|---|
| `filename` | 6014 | clean 'Artist - Title' filename — trusted |
| `frontmatter_fallback` | 134 | anomalous filename, frontmatter rescue (token-match) |

## Skipped files

| Reason | Count |
|---|---:|
| already ct_format=1.3 | 52 |
| utility file (not a song entry) | 3 |
| already ct_format=1.2 | 1 |

## Files needing human review

| Reason | Count |
|---|---:|
| anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None' | 146 |
| anomalous filename '- Koko.md' and frontmatter song 'Silly Love Songs - 2014 Remaster' share no tokens with stem 'Koko' — possible bad auto-enrichment | 1 |
| anomalous filename '- Song Name.md' and frontmatter song 'Smooth Operator - Single Version' share no tokens with stem 'Song Name' — possible bad auto-enrichment | 1 |
| anomalous filename 'Bon Jovi.md' and frontmatter song 'Born To Be My Baby' share no tokens with stem 'Bon Jovi' — possible bad auto-enrichment | 1 |
| anomalous filename 'Britney Spears.md' and frontmatter song 'Бритни Спирс' share no tokens with stem 'Britney Spears' — possible bad auto-enrichment | 1 |
| anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='Ethan Hein CULTURAL — Knowledge Extraction' | 1 |
| anomalous filename 'Ever Ever After.md' and frontmatter song 'Everybody’s Looking At Me' share no tokens with stem 'Ever Ever After' — possible bad auto-enrichment | 1 |
| anomalous filename 'Form in Top 20.md' and frontmatter song 'Formed a Band' share no tokens with stem 'Form in Top 20' — possible bad auto-enrichment | 1 |
| anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='T', song='None' | 1 |
| anomalous filename 'Kanye West.md' and frontmatter song 'Waves' share no tokens with stem 'Kanye West' — possible bad auto-enrichment | 1 |
| anomalous filename 'MASTER LISTENING LIST.md' and frontmatter song 'It's Impossible - Digitally Mastered - May - June, 1988' share no tokens with stem 'MASTER LISTENING LIST' — possible bad auto-enrichment | 1 |
| anomalous filename 'Obla.md' and frontmatter song 'Ob-La-Di, Ob-La-Da - Remastered 2009' share no tokens with stem 'Obla' — possible bad auto-enrichment | 1 |
| anomalous filename 'REM.md' and frontmatter song 'Reminder' share no tokens with stem 'REM' — possible bad auto-enrichment | 1 |
| anomalous filename 'Selena Gomez.md' and frontmatter song 'Wolves' share no tokens with stem 'Selena Gomez' — possible bad auto-enrichment | 1 |

### Sample (first 15):

- `- Koko.md` — anomalous filename '- Koko.md' and frontmatter song 'Silly Love Songs - 2014 Remaster' share no tokens with stem 'Koko' — possible bad auto-enrichment
- `- Song Name.md` — anomalous filename '- Song Name.md' and frontmatter song 'Smooth Operator - Single Version' share no tokens with stem 'Song Name' — possible bad auto-enrichment
- `Analysis of Nirvana Songs Part 1.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `Barrie Manilow.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `Bon Jovi.md` — anomalous filename 'Bon Jovi.md' and frontmatter song 'Born To Be My Baby' share no tokens with stem 'Bon Jovi' — possible bad auto-enrichment
- `Britney Spears.md` — anomalous filename 'Britney Spears.md' and frontmatter song 'Бритни Спирс' share no tokens with stem 'Britney Spears' — possible bad auto-enrichment
- `ETHAN_HEIN_CULTURAL.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='Ethan Hein CULTURAL — Knowledge Extraction'
- `EXTRACTED_11_As_Tears_Go_By___The_Rolling_Stones_20260331.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_11_You_Are_My_Sunshine___Connecting_The_Dots___Part_2_20260331.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_A Horse with No Name_20260408.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_Analysis of Nirvana Songs Part 1_20260408.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_Analysis of-She’s Always a Woman_20260408.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_Arcade Fire_20260408.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_Army of Me_20260408.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'
- `EXTRACTED_Atlas by Battles-A Compositional Analysis_20260408.md` — anomalous filename — no frontmatter artist+song to fall back on. Existing frontmatter: artist='None', song='None'

## Collisions (v1.1)

**Total distinct collisions:** 107
**Total files bumped to `_2`/`_3`/... suffix:** 119

| Target name | Winner | Losers (→ new target) |
|---|---|---|
| `AEROSMITH - CRYIN.md` | `Aerosmith - Cryin'.md` | `Aerosmith - Cryin’.md` → `AEROSMITH - CRYIN_2.md` |
| `ALLMAN_BROTHERS_BAND - JESSICA.md` | `Allman Brothers Band - Jessica.md` | `Jessica.md` → `ALLMAN_BROTHERS_BAND - JESSICA_2.md` |
| `AL_JOLSON - CALIFORNIA_HERE_I_COME.md` | `Al Jolson - California Here I Come.md` | `Al Jolson - California, Here I Come.md` → `AL_JOLSON - CALIFORNIA_HERE_I_COME_2.md` |
| `ARETHA_FRANKLIN - I_NEVER_LOVED_A_MAN.md` | `Aretha Franklin - I Never Loved A Man (The Way I Love You).md` | `Aretha Franklin - I Never Loved A Man.md` → `ARETHA_FRANKLIN - I_NEVER_LOVED_A_MAN_2.md` |
| `BARRY_MANILOW - CANT_SMILE_WITHOUT_YOU.md` | `Barry Manilow - Can't Smile Without You.md` | `Barry Manilow - Can’t Smile Without You.md` → `BARRY_MANILOW - CANT_SMILE_WITHOUT_YOU_2.md` |
| `BEYONCE - IF_I_WERE_A_BOY.md` | `Beyonce - If I Were a Boy.md` | `Beyoncé - If I Were a Boy.md` → `BEYONCE - IF_I_WERE_A_BOY_2.md` |
| `BEYONCE - I_CARE.md` | `Beyonce - I Care.md` | `Beyoncé - I Care.md` → `BEYONCE - I_CARE_2.md` |
| `BEYONCE - LOVE_ON_TOP.md` | `Beyonce - Love On Top.md` | `Beyoncé - Love On Top.md` → `BEYONCE - LOVE_ON_TOP_2.md` |
| `BEYONCE - SINGLE_LADIES.md` | `Beyoncé - Single Ladies (Put a Ring on It).md` | `Single Ladies.md` → `BEYONCE - SINGLE_LADIES_2.md` |
| `BILLIE_EILISH - WHEN_THE_PARTYS_OVER.md` | `Billie Eilish - When the Party’s Over.md` | `Billie Eilish - when the partys over.md` → `BILLIE_EILISH - WHEN_THE_PARTYS_OVER_2.md` |
| `BILLY_JOEL - PIANO_MAN.md` | `Billy Joel - Piano Man.md` | `Piano Man.md` → `BILLY_JOEL - PIANO_MAN_2.md` |
| `BILLY_JOEL - THE_BALLAD_OF_BILLY_THE_KID.md` | `Billy Joel - The Ballad of Billy the Kid.md` | `Billy Joel.md` → `BILLY_JOEL - THE_BALLAD_OF_BILLY_THE_KID_2.md` |
| `BILLY_TALENT - SURRENDER.md` | `Billy Talent - Surrender.md` | `Surrender.md` → `BILLY_TALENT - SURRENDER_2.md` |
| `BJORK - ARMY_OF_ME.md` | `Army of Me.md` | `Bjork - Army of Me.md` → `BJORK - ARMY_OF_ME_2.md` |
| `BLAKE_SHELTON - MINE_WOULD_BE_YOU.md` | `Blake Shelton - Mine Would Be You.md` | `Mine Would Be You-Blake Shelton.md` → `BLAKE_SHELTON - MINE_WOULD_BE_YOU_2.md`<br>`Mine Would Be You.md` → `BLAKE_SHELTON - MINE_WOULD_BE_YOU_3.md` |
| `BOBBY_DARIN - BEYOND_THE_SEA.md` | `Beyond The Sea.md` | `Bobby Darin - Beyond the Sea.md` → `BOBBY_DARIN - BEYOND_THE_SEA_2.md` |
| `BOB_DYLAN - MR_TAMBOURINE_MAN.md` | `Bob Dylan - Mr. Tambourine Man.md` | `Mr. Tambourine Man.md` → `BOB_DYLAN - MR_TAMBOURINE_MAN_2.md` |
| `BOB_DYLAN - THE_TIMES_THEY_ARE_A_CHANGIN.md` | `Bob Dylan - The Times They Are A-Changin'.md` | `The Times They Are A Changin'.md` → `BOB_DYLAN - THE_TIMES_THEY_ARE_A_CHANGIN_2.md`<br>`The Times They Are a Changin’.md` → `BOB_DYLAN - THE_TIMES_THEY_ARE_A_CHANGIN_3.md` |
| `BRITNEY_SPEARS - TOXIC.md` | `Britney Spears - Toxic.md` | `Toxic – Brittney Spears.md` → `BRITNEY_SPEARS - TOXIC_2.md` |
| `BRUCE_CHANNEL - HEY_BABY.md` | `Bruce Channel - Hey Baby.md` | `Bruce Channel - Hey! Baby.md` → `BRUCE_CHANNEL - HEY_BABY_2.md` |
| `BUDDY_HOLLY_AND_THE_CRICKETS - THATLL_BE_THE_DAY.md` | `Buddy Holly & the Crickets - That'll Be The Day.md` | `Buddy Holly and the Crickets - That'll Be the Day.md` → `BUDDY_HOLLY_AND_THE_CRICKETS - THATLL_BE_THE_DAY_2.md`<br>`Buddy Holly and the Crickets - That’ll Be the Day.md` → `BUDDY_HOLLY_AND_THE_CRICKETS - THATLL_BE_THE_DAY_3.md` |
| `CHARLI_XCX - CHAINS_OF_LOVE.md` | `CHAINS.md` | `Charli XCX - Chains of Love.md` → `CHARLI_XCX - CHAINS_OF_LOVE_2.md` |
| `CHUCK_BERRY - CAROL.md` | `Carol – Chuck Berry.md` | `Chuck Berry - Carol.md` → `CHUCK_BERRY - CAROL_2.md` |
| `CHUCK_BERRY - REELIN_AND_ROCKIN.md` | `Chuck Berry - Reelin' & Rockin'.md` | `Chuck Berry - Reelin' And Rockin'.md` → `CHUCK_BERRY - REELIN_AND_ROCKIN_2.md` |
| `CREEDENCE_CLEARWATER_REVIVAL - HAVE_YOU_EVER_SEEN_THE_RAIN.md` | `Creedence Clearwater Revival - Have You Ever Seen The Rain.md` | `Have you ever seen the rain.md` → `CREEDENCE_CLEARWATER_REVIVAL - HAVE_YOU_EVER_SEEN_THE_RAIN_2.md` |
| `CROSBY_STILLS_AND_NASH - SOUTHERN_CROSS.md` | `Crosby, Stills & Nash - Southern Cross.md` | `Crosby, Stills and Nash - Southern Cross.md` → `CROSBY_STILLS_AND_NASH - SOUTHERN_CROSS_2.md` |
| `CROSBY_STILLS_AND_NASH - SUITE_JUDY_BLUE_EYES.md` | `Crosby, Stills & Nash - Suite- Judy Blue Eyes.md` | `Crosby, Stills and Nash - Suite- Judy Blue Eyes.md` → `CROSBY_STILLS_AND_NASH - SUITE_JUDY_BLUE_EYES_2.md` |
| `CROWDED_HOUSE - DONT_DREAM_ITS_OVER.md` | `Crowded House - Don't Dream It's Over.md` | `Crowded House - Don’t Dream it’s Over.md` → `CROWDED_HOUSE - DONT_DREAM_ITS_OVER_2.md` |
| `DEREK_AND_THE_DOMINOS - LAYLA.md` | `Derek & The Dominos - Layla.md` | `Derek and the Dominos - Layla.md` → `DEREK_AND_THE_DOMINOS - LAYLA_2.md`<br>`Layla.md` → `DEREK_AND_THE_DOMINOS - LAYLA_3.md` |
| `DUKE_ELLINGTON - IT_DONT_MEAN_A_THING.md` | `Duke Ellington - It Don't Mean a Thing (If It Ain't Got That Swing).md` | `Duke Ellington - It Don't Mean a Thing.md` → `DUKE_ELLINGTON - IT_DONT_MEAN_A_THING_2.md` |
| `ELLA_FITZGERALD - A_TISKET_A_TASKET.md` | `Ella Fitzgerald - A-Tisket A-Tasket.md` | `Ella Fitzgerald - A-Tisket, A-Tasket.md` → `ELLA_FITZGERALD - A_TISKET_A_TASKET_2.md` |
| `ELVIS_COSTELLO_AND_THE_ATTRACTIONS - OLIVERS_ARMY.md` | `Elvis Costello & The Attractions - Oliver's Army.md` | `Elvis Costello and the Attractions - Oliver's Army.md` → `ELVIS_COSTELLO_AND_THE_ATTRACTIONS - OLIVERS_ARMY_2.md`<br>`OLIVER'S ARMY.md` → `ELVIS_COSTELLO_AND_THE_ATTRACTIONS - OLIVERS_ARMY_3.md` |
| `ELVIS_PRESLEY - HIS_LATEST_FLAME.md` | `Elvis Presley - His Latest Flame (Marie's The Name).md` | `Elvis Presley - His Latest Flame.md` → `ELVIS_PRESLEY - HIS_LATEST_FLAME_2.md` |
| `FRANKI_VALLI_AND_THE_FOUR_SEASONS - BIG_GIRLS_DONT_CRY.md` | `Franki Valli and the Four Seasons - Big Girls Don’t Cry.md` | `Franki Valli and the Four Seasons - Big Girls Don�t Cry.md` → `FRANKI_VALLI_AND_THE_FOUR_SEASONS - BIG_GIRLS_DONT_CRY_2.md` |
| `GORDON_LIGHTFOOT - THE_WRECK_OF_THE_EDMUND_FITZGERALD.md` | `Gordon Lightfoot - The Wreck Of The Edmund Fitzgerald.md` | `Gordon Lightfoot - The Wreck of the Edmund Fitzgerald (1976).md` → `GORDON_LIGHTFOOT - THE_WRECK_OF_THE_EDMUND_FITZGERALD_2.md` |
| `GRANDMASTER_FLASH_AND_THE_FURIOUS_FIVE - THE_MESSAGE.md` | `Grandmaster Flash & the Furious Five - The Message.md` | `Grandmaster Flash and the Furious Five - The Message.md` → `GRANDMASTER_FLASH_AND_THE_FURIOUS_FIVE - THE_MESSAGE_2.md` |
| `GRIMES - GENESIS.md` | `Genesis.md` | `Grimes - Genesis.md` → `GRIMES - GENESIS_2.md` |
| `GUNS_N_ROSES - SWEET_CHILD_O_MINE.md` | `Guns 'n Roses - Sweet Child o' Mine.md` | `Guns N Roses - Sweet Child O’ Mine.md` → `GUNS_N_ROSES - SWEET_CHILD_O_MINE_2.md`<br>`Guns N Roses - Sweet Child O� Mine.md` → `GUNS_N_ROSES - SWEET_CHILD_O_MINE_3.md` |
| `HANK_WILLIAMS - COLD_COLD_HEART.md` | `Hank Williams - Cold Cold Heart.md` | `Hank Williams - Cold, Cold Heart.md` → `HANK_WILLIAMS - COLD_COLD_HEART_2.md` |
| `HANK_WILLIAMS - IM_SO_LONESOME_I_COULD_CRY.md` | `Hank Williams - I'm So Lonesome I Could Cry.md` | `Hank Williams - I’m So Lonesome I Could Cry.md` → `HANK_WILLIAMS - IM_SO_LONESOME_I_COULD_CRY_2.md` |
| `HANK_WILLIAMS - JAMBALAYA.md` | `Hank Williams - Jambalaya (On the Bayou).md` | `Hank Williams - Jambalaya.md` → `HANK_WILLIAMS - JAMBALAYA_2.md`<br>`Jambalaya.md` → `HANK_WILLIAMS - JAMBALAYA_3.md` |
| `IRENE_CARA - FLASHDANCE.md` | `Irene Cara - Flashdance (What A Feeling).md` | `Irene Cara - Flashdance.md` → `IRENE_CARA - FLASHDANCE_2.md` |
| `JAMES_BROWN - GET_UP_SEX_MACHINE.md` | `James Brown - Get Up (I Feel Like Being Like A) Sex Machine (Part 1).md` | `James Brown - Get Up (I Feel Like Being a) Sex Machine.md` → `JAMES_BROWN - GET_UP_SEX_MACHINE_2.md` |
| `JANES_ADDICTION - JANE_SAYS.md` | `Jane's Addiction - Jane Says.md` | `Jane’s Addiction - Jane Says.md` → `JANES_ADDICTION - JANE_SAYS_2.md` |
| `JANN_ARDEN - COULD_I_BE_YOUR_GIRL.md` | `COULD I BE YOUR GIRL Jann Arden.md` | `Jann Arden - Could I Be Your Girl-.md` → `JANN_ARDEN - COULD_I_BE_YOUR_GIRL_2.md` |
| `JOHNNY_CASH - I_WALK_THE_LINE.md` | `I Walk The Line.md` | `Johnny Cash - I Walk the Line.md` → `JOHNNY_CASH - I_WALK_THE_LINE_2.md` |
| `JOSIAH_QUEEN - YESTERDAY_IS_DEAD.md` | `Josiah Queen - Yesterday Is Dead.md` | `Yesterday is in F.md` → `JOSIAH_QUEEN - YESTERDAY_IS_DEAD_2.md` |
| `KANYE_WEST - STRONGER.md` | `Kanye West - Stronger.md` | `Stronger.md` → `KANYE_WEST - STRONGER_2.md` |
| `KELLY_CLARKSON - SINCE_U_BEEN_GONE.md` | `Kelly Clarkson - Since U Been Gone.md` | `Since U Been Gone.md` → `KELLY_CLARKSON - SINCE_U_BEEN_GONE_2.md` |
| `KELLY_CLARKSON - SINCE_YOUVE_BEEN_GONE.md` | `Kelly Clarkson - Since You've Been Gone.md` | `Kelly Clarkson - Since You’ve Been Gone.md` → `KELLY_CLARKSON - SINCE_YOUVE_BEEN_GONE_2.md` |
| ... | ... | (57 more collisions omitted) |

## Renames

- Files keeping current filename: **1**
- Files being renamed:            **6147**

### Sample renames (first 25)

| Old filename | New filename |
|---|---|
| `(G)Idle - LION.md` | `IDLE - LION.md` |
| `- Black Orpheus.md` | `GERRY_MULLIGAN_SEXTET - MORNING_OF_THE_CARNIVAL_FROM_BLACK_ORPHEUS.md` |
| `- Blue Moon.md` | `FRANK_SINATRA - BLUE_MOON_1999_REMASTERED.md` |
| `- Corvocado.md` | `SIFARE_BAND - QUIET_NIGHTS_OF_QUIET_STARS_CORVOCADO.md` |
| `- Days of Wine And Roses.md` | `JACKIE_GLEASON - DAYS_OF_WINE_AND_ROSES_REMASTERED1996.md` |
| `- Fame.md` | `DAVID_BOWIE - FAME_2016_REMASTER.md` |
| `- Final Countdown.md` | `SOUNDWALL_AMELIA_MCLEAN - FINAL_COUNTDOWN_FROM_PARADISE_SEASON_2.md` |
| `- Flintstones.md` | `GEEK_MUSIC - THE_FLINTSTONES_MAIN_THEME.md` |
| `- Fried Bananas.md` | `PIERO_UMILIANI_ENZO_PIETANZA_DJARNOLD_MADDALONI_FRANKIE_FORTYFIVE_KEEDOMAN - FRIED_BANANAS_RE_EDIT_ENZO_PIETANZA_DJARNOLD_MADDALONI_FRANKIE_FORTYFIVE_KEEDOMAN_REMIX.md` |
| `- Godfather Theme.md` | `MASSIMO_BELLUCCI - LOVE_THEME_PIANO.md` |
| `- Graduation (Friends Forever).md` | `PIANOSTALGIA_FM - GRADUATION_PIANO_VERSION.md` |
| `- Green Dolphin Street.md` | `BABY_LULLABIES_BABY_MUSIC_LITTLE_BABY_MUSIC - ON_GREEN_DOLPHIN_STREET_PIANO_JAZZ_VERSION.md` |
| `- How High the Moon.md` | `CHET_BAKER - HOW_HIGH_THE_MOON_MONO.md` |
| `- Oh Come All Ye Faithful.md` | `BONEY_M - OH_COME_ALL_YE_FAITHFUL.md` |
| `- Plaisir D'Amour.md` | `THE_SEEKERS - PLAISIR_DAMOUR_STEREO_2009_REMASTER.md` |
| `- Purple People Eater.md` | `JUDY_GARLAND - PURPLE_PEOPLE_EATER_LIVE.md` |
| `- Seems Like Old Times.md` | `LAUFEY - SEEMS_LIKE_OLD_TIMES_BONUS_TRACK.md` |
| `- Shadow of Your Smile.md` | `ASTRUD_GILBERTO - THE_SHADOW_OF_YOUR_SMILE_LOVE_THEME_FROM_THE_SANDPIPER.md` |
| `- Somewhere, My Love (Lara's Theme).md` | `PAUL_POTTS - DOVE_NON_SO_SOMEWHERE_MY_LOVE_LARAS_THEME_FROM_DOCTOR_JIVAGO.md` |
| `- Star Trek Theme.md` | `JERRY_GOLDSMITH - STAR_TREK_VOYAGER_MAIN_TITLE.md` |
| `- Still Got The Blues.md` | `GARY_MOORE - STILL_GOT_THE_BLUES_LIVE_FROM_THE_BLUES_ALIVE_TOUR_UK1993.md` |
| `- Take Me Out To The Ball Game.md` | `TOY_RAMPAGE - TAKE_ME_OUT_TO_THE_BALL_GAME_RUBBER_CHICKEN_VERSION.md` |
| `- The Bare Necessities.md` | `PHIL_HARRIS_BRUCE_REITHERMAN - THE_BARE_NECESSITIES_FROM_THE_JUNGLE_BOOK_SOUNDTRACK.md` |
| `- Watch What Happens.md` | `ODONEL_LEVY - WATCH_WHAT_HAPPENS_2024_REMASTERED_VERSION.md` |
| `- When A Man Loves A Woman.md` | `PERCY_SLEDGE - WHEN_A_MAN_LOVES_A_WOMAN_MONO.md` |

## Placeholder (`unknown`) distribution

| Field | Files marked `unknown` | % of migrated |
|---|---:|---:|
| `year` | 141 | 2.3% |
| `tonic` | 6148 | 100.0% |
| `mode` | 6148 | 100.0% |
| `meter` | 6148 | 100.0% |

## Carry-forward fields preserved

| Field | Files | % of migrated |
|---|---:|---:|
| `legacy_source` | 6095 | 99.1% |
| `spotify_link` | 5535 | 90.0% |
| `genre` | 4133 | 67.2% |
| `composers` | 3685 | 59.9% |
| `album` | 585 | 9.5% |
| `legacy_tempo_bpm` | 352 | 5.7% |
| `legacy_key` | 71 | 1.2% |

## Sample preview — first 3 migrated files

### `(G)Idle - LION.md` → `IDLE - LION.md`

```markdown
---
ct_format: '1.3'
song: LION
artist: (G)Idle
year: 2020
tonic: unknown
mode: unknown
meter: unknown
spotify_link: https://open.spotify.com/track/40OyiVO9NtBg9R2Gpwxs3u
legacy_source: 'Merged: FileMaker Database + Original REPERTOIRE'
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: filename; parse_tier:
  sanitized; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# LION — (G)Idle (2020)

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

### `- Black Orpheus.md` → `GERRY_MULLIGAN_SEXTET - MORNING_OF_THE_CARNIVAL_FROM_BLACK_ORPHEUS.md`

```markdown
---
ct_format: '1.3'
song: Morning Of The Carnival - From "Black Orpheus"
artist: Gerry Mulligan Sextet
year: 1963
tonic: unknown
mode: unknown
meter: unknown
spotify_link: https://open.spotify.com/track/6GQ6rapsknPIutGbpv0DTR
genre: Jazz
legacy_source: 'Merged: FileMaker Database + Original REPERTOIRE'
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: frontmatter_fallback;
  parse_tier: regex; schema-compliant skeleton, analytical fields unknown unless recovered)'
---

# MORNING OF THE CARNIVAL - FROM "BLACK ORPHEUS" — Gerry Mulligan Sextet (1963)

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

# Black Orpheus — 

## Theoretical Taxonomy
#concept/ii--v

## Analytical Notes
*(From FileMaker Database)*
# Black Orpheus —


```

### `- Blue Moon.md` → `FRANK_SINATRA - BLUE_MOON_1999_REMASTERED.md`

```markdown
---
ct_format: '1.3'
song: Blue Moon - 1999 Remastered
artist: Frank Sinatra
year: 1961
tonic: unknown
mode: unknown
meter: unknown
spotify_link: https://open.spotify.com/track/5RLzsVW6UNiV2YrOlKwzNN
genre: Jazz
legacy_source: 'Merged: FileMaker Database + Original REPERTOIRE'
ct_entry_date: '2026-04-24'
ct_last_updated: '2026-04-24'
migration_note: 'Migrated 2026-04-24 by ctsf_migrator.py v1.1 (source: frontmatter_fallback;
  parse_tier: sanitized; schema-compliant skeleton, analytical fields unknown unless
  recovered)'
---

# BLUE MOON - 1999 REMASTERED — Frank Sinatra (1961)

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

# Blue Moon — 

## Theoretical Taxonomy
#harmony/applied-chords

## Analytical Notes
*(From FileMaker Database)*
# Blue Moon — 

## Features & Notes
Bob Dylan
Mel Torme
Coleman Hawkins
Rod Stewart
Elvis Presley;


```

---

*Plan produced by `_SYSTEM/scripts/ctsf_migrator.py` in DRY-RUN mode.*