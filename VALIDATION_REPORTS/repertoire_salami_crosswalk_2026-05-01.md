# Repertoire / SALAMI Crosswalk Report

Generated: 2026-05-01

## Artifacts

- CSV: `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01.csv`
- Pilot CSV: `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01_pilot.csv`

## Summary

- Active CTSF song entries scanned: 6,020
- SALAMI DB songs scanned: 1,242
- SALAMI chord rows represented: 124,576
- Matched CTSF entries: 571
- High-confidence positive matches: 522
- Rows needing manual review: 47
- High-value Tier A/B entries without SALAMI match: 525

## Count Reconciliation

| Source | Count / Note |
|---|---:|
| Active `.md` files excluding utility files | 6,020 |
| Active `.md` files including utility files | 6,023 |
| `_INDEX.md` claimed total | 364 |
| Enrichment plan claimed total | 6233 |
| SALAMI `songs` table | 1,242 |
| SALAMI `chords` rows | 124,576 |
| Latest validator JSON | VALIDATION_REPORTS/ctsf_validation_2026-04-25.json |

Count mismatch note: resolve active file count vs. index/enrichment-plan claims before any corpus-wide writeback.

## Match Buckets

| Match type | Rows |
|---|---:|
| `no_match` | 5,449 |
| `duplicate_salami_versions_canonicalized` | 512 |
| `title_only_artist_conflict` | 41 |
| `exact_artist_title` | 12 |
| `manual_review` | 4 |
| `duplicate_salami_versions` | 2 |

## Proposed Actions

| Proposed action | Rows |
|---|---:|
| `report_no_match_only` | 4,924 |
| `manual_or_other_source_analysis` | 525 |
| `create_form_container` | 433 |
| `import_salami_timeline` | 86 |
| `review_match` | 47 |
| `mark_coverage_only` | 5 |

## Repertoire Tier Distribution

| Tier | Rows |
|---|---:|
| `(blank)` | 14 |
| `A` | 143 |
| `B` | 484 |
| `C` | 5,117 |
| `D` | 262 |

## Duplicate SALAMI Clusters

| CTSF entry | Candidate SALAMI files |
|---|---|
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - CHIQUITITA.md` | salami_0636.txt (ABBA - Chiquitita), salami_0011.txt (ABBA - Chiquitita) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - FERNANDO.md` | salami_1114.txt (Abba - Fernando), salami_0500.txt (Abba - Fernando) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - HONEY_HONEY.md` | salami_0899.txt (ABBA - Honey Honey), salami_0276.txt (ABBA - Honey Honey) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - TAKE_A_CHANCE_ON_ME.md` | salami_0263.txt (Abba - Take A Chance On Me), salami_0886.txt (Abba - Take A Chance On Me) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/AEROSMITH - LAST_CHILD.md` | salami_1117.txt (Aerosmith - Last Child), salami_0504.txt (Aerosmith - Last Child) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ALABAMA - TAKE_ME_DOWN.md` | salami_0554.txt (Alabama - Take Me Down), salami_1167.txt (Alabama - Take Me Down) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ALWAYS_SOMETHING_THERE_TO_REMIND_ME - NAKED_EYES.md` | salami_1021.txt (Always Something There to Remind Me - Naked Eyes), salami_0402.txt (Always Something There to Remind Me - Naked Eyes) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/AL_GREEN - OH_ME_OH_MY.md` | salami_0381.txt (Al Green - Oh Me, Oh My (Dreams In My Arms)), salami_1001.txt (Al Green - Oh Me, Oh My (Dreams In My Arms)) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANDY_GIBB - SHADOW_DANCING.md` | salami_0593.txt (Andy Gibb - Shadow Dancing), salami_1177.txt (Andy Gibb - Shadow Dancing), salami_1205.txt (Andy Gibb - Shadow Dancing), salami_0564.txt (Andy Gibb - Shadow Dancing) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANITA_BAKER - SWEET_LOVE.md` | salami_0140.txt (Anita Baker - Sweet Love), salami_0764.txt (Anita Baker - Sweet Love) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - DAYDREAM_BELIEVER.md` | salami_0330.txt (Anne Murray - Daydream Believer), salami_0951.txt (Anne Murray - Daydream Believer), salami_0789.txt (Anne Murray - Daydream Believer), salami_0165.txt (Anne Murray - Daydream Believer) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANN_PEEBLES - I_CANT_STAND_THE_RAIN.md` | salami_0358.txt (Ann Peebles - I Can't Stand The Rain), salami_0979.txt (Ann Peebles - I Can't Stand The Rain) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ARETHA_FRANKLIN - CHAIN_OF_FOOLS.md` | salami_0224.txt (Aretha Franklin - Chain Of Fools), salami_0847.txt (Aretha Franklin - Chain Of Fools) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ARETHA_FRANKLIN - I_NEVER_LOVED_A_MAN.md` | salami_0753.txt (Aretha Franklin - I Never Loved A Man), salami_0129.txt (Aretha Franklin - I Never Loved A Man) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ARETHA_FRANKLIN - OH_ME_OH_MY.md` | salami_0917.txt (Aretha Franklin - Oh Me Oh My (I'm A Fool For You Baby)), salami_0294.txt (Aretha Franklin - Oh Me Oh My (I'm A Fool For You Baby)) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ARTHUR_CONLEY - SWEET_SOUL_MUSIC.md` | salami_1175.txt (Arthur Conley - Sweet Soul Music), salami_0562.txt (Arthur Conley - Sweet Soul Music) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/A_TASTE_OF_HONEY - SUKIYAKI.md` | salami_0557.txt (A Taste Of Honey - Sukiyaki), salami_1170.txt (A Taste Of Honey - Sukiyaki) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BACHMAN_TURNER_OVERDRIVE - HEARTACHES.md` | salami_0108.txt (Bachman-Turner Overdrive - Heartaches), salami_0732.txt (Bachman-Turner Overdrive - Heartaches) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BACHMAN_TURNER_OVERDRIVE - ROLL_ON_DOWN_THE_HIGHWAY.md` | salami_0302.txt (Bachman-Turner Overdrive - Roll On Down The Highway), salami_0924.txt (Bachman-Turner Overdrive - Roll On Down The Highway) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BADFINGER - MAYBE_TOMORROW.md` | salami_1023.txt (Badfinger - Maybe Tomorrow), salami_0404.txt (Badfinger - Maybe Tomorrow) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BAD_COMPANY - ROCK_N_ROLL_FANTASY.md` | salami_0786.txt (Bad Company - Rock 'n' Roll Fantasy), salami_0162.txt (Bad Company - Rock 'n' Roll Fantasy) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BALTIMORA - TARZAN_BOY.md` | salami_0939.txt (Baltimora - Tarzan Boy (From "Teenage Mutant Ninja Turtles III")), salami_0318.txt (Baltimora - Tarzan Boy (From "Teenage Mutant Ninja Turtles III")), salami_0739.txt (Baltimora - Tarzan Boy (From "Teenage Mutant Ninja Turtles III")), salami_0115.txt (Baltimora - Tarzan Boy (From "Teenage Mutant Ninja Turtles III")) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BANANARAMA - A_TRICK_OF_THE_NIGHT.md` | salami_1073.txt (Bananarama - A Trick Of The Night), salami_0456.txt (Bananarama - A Trick Of The Night) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BARBARA_LEWIS - HELLO_STRANGER.md` | salami_0967.txt (Barbara Lewis - Hello Stranger), salami_0346.txt (Barbara Lewis - Hello Stranger) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BARBRA_STREISAND - FUNNY_GIRL.md` | salami_1067.txt (Barbra Streisand - Funny Girl), salami_0450.txt (Barbra Streisand - Funny Girl) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BARBRA_STREISAND - PEOPLE.md` | salami_0521.txt (Barbara Streisand - People), salami_1134.txt (Barbara Streisand - People) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.md` | salami_0625.txt (Barry White - You're The First, The Last, My Everything), salami_1237.txt (Barry White - You're The First, The Last, My Everything) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BAY_CITY_ROLLERS - SATURDAY_NIGHT.md` | salami_0579.txt (Bay City Rollers - Saturday Night), salami_1192.txt (Bay City Rollers - Saturday Night) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BB_KING - HOW_BLUE_CAN_YOU_GET.md` | salami_0959.txt (B.B. King - How Blue Can You Get), salami_0338.txt (B.B. King - How Blue Can You Get) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BB_KING - THE_THRILL_IS_GONE.md` | salami_0437.txt (B.B. King - The Thrill Is Gone), salami_1054.txt (B.B. King - The Thrill Is Gone) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BEAUTIFUL - GORDON_LIGHTFOOT.md` | salami_0344.txt (Beautiful - Gordon Lightfoot), salami_0965.txt (Beautiful - Gordon Lightfoot) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BEN_E_KING - AMOR.md` | salami_0080.txt (Ben E. King - Amor), salami_0704.txt (Ben E. King - Amor) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BERTHA_TILLMAN - OH_MY_ANGEL.md` | salami_1024.txt (Bertha Tillman - Oh My Angel), salami_0405.txt (Bertha Tillman - Oh My Angel) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BETTE_MIDLER - THE_ROSE.md` | salami_0889.txt (Bette Midler - The Rose), salami_0452.txt (Bette Midler - The Rose), salami_0266.txt (Bette Midler - The Rose), salami_1069.txt (Bette Midler - The Rose), salami_1240.txt (Bette Midler - The Rose) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILLY_IDOL - CATCH_MY_FALL.md` | salami_0234.txt (Billy Idol - Catch My Fall), salami_0857.txt (Billy Idol - Catch My Fall) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILLY_JOEL - DONT_ASK_ME_WHY.md` | salami_0308.txt (Billy Joel - Don't Ask Me Why), salami_0930.txt (Billy Joel - Don't Ask Me Why) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILLY_PRESTON - WITH_YOU_IM_BORN_AGAIN.md` | salami_0043.txt (Billy Preston - With You I'm Born Again), salami_0668.txt (Billy Preston - With You I'm Born Again) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILLY_SQUIER - MY_KINDA_LOVER.md` | salami_0637.txt (Billy Squier - My Kinda Lover), salami_0012.txt (Billy Squier - My Kinda Lover) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILLY_SWAN - I_CAN_HELP.md` | salami_0722.txt (Billy Swan - I Can Help), salami_0641.txt (Billy Swan - I Can Help), salami_0098.txt (Billy Swan - I Can Help), salami_0016.txt (Billy Swan - I Can Help) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILL_WITHERS - AINT_NO_SUNSHINE.md` | salami_0640.txt (Bill Withers - Ain't No Sunshine), salami_0015.txt (Bill Withers - Ain't No Sunshine) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILL_WITHERS - LOVELY_DAY.md` | salami_0152.txt (Bill Withers - Lovely Day), salami_0776.txt (Bill Withers - Lovely Day) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BING_CROSBY - SILENT_NIGHT.md` | salami_0664.txt (Bing Crosby - Silent Night), salami_0039.txt (Bing Crosby - Silent Night) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BING_CROSBY - WHITE_CHRISTMAS.md` | salami_0184.txt (Bing Crosby - White Christmas), salami_0808.txt (Bing Crosby - White Christmas) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BIZ_MARKIE - JUST_A_FRIEND.md` | salami_0494.txt (Biz Markie - Just A Friend), salami_1108.txt (Biz Markie - Just A Friend) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BJ_THOMAS - HOOKED_ON_A_FEELING.md` | salami_1215.txt (B.J. Thomas - Hooked On A Feeling), salami_0603.txt (B.J. Thomas - Hooked On A Feeling) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BLONDIE - ISLAND_OF_LOST_SOULS.md` | salami_0999.txt (Blondie - Island Of Lost Souls), salami_0379.txt (Blondie - Island Of Lost Souls) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BLONDIE - ONE_WAY_OR_ANOTHER.md` | salami_0031.txt (Blondie - One Way or Another), salami_0656.txt (Blondie - One Way or Another) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BLUE_EYES_CRYIN - WILLIE_NELSON.md` | salami_0988.txt (Blue Eyes Cryin' - Willie Nelson), salami_0367.txt (Blue Eyes Cryin' - Willie Nelson) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BOBBIE_GENTRY - ODE_TO_BILLIE_JOE.md` | salami_1129.txt (Bobbie Gentry - Ode To Billie Joe), salami_0516.txt (Bobbie Gentry - Ode To Billie Joe) |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BOBBI_MARTIN - I_LOVE_YOU_SO.md` | salami_0741.txt (Bobbi Martin - I Love You So), salami_0117.txt (Bobbi Martin - I Love You So) |
| ... | 464 additional clusters omitted from Markdown; see CSV. |

## 25-Song Pilot

| # | Category | Decision | CTSF song | SALAMI candidate | Match |
|---:|---|---|---|---|---|
| 1 | `strong_match` | `import_salami_timeline` | Anne Murray - A Love Song | Anne Murray - A Love Song | `exact_artist_title (1.000)` |
| 2 | `strong_match` | `import_salami_timeline` | Canned Heat - On The Road Again | Canned Heat - On The Road Again | `exact_artist_title (1.000)` |
| 3 | `strong_match` | `import_salami_timeline` | The Buckinghams - Kind Of A Drag | The Buckinghams - Kind Of A Drag | `exact_artist_title (1.000)` |
| 4 | `strong_match` | `create_form_container` | Abba - On And On And On | Abba - On And On And On | `exact_artist_title (1.000)` |
| 5 | `strong_match` | `create_form_container` | Beastie Boys - Brass Monkey | Beastie Boys - Brass Monkey | `exact_artist_title (1.000)` |
| 6 | `strong_match` | `create_form_container` | Bonnie Pointer - Heaven Must Have Sent You | Bonnie Pointer - Heaven Must Have Sent You | `exact_artist_title (1.000)` |
| 7 | `strong_match` | `create_form_container` | Isaac Hayes - The Look Of Love | Isaac Hayes - The Look Of Love | `exact_artist_title (1.000)` |
| 8 | `strong_match` | `create_form_container` | Little River Band - Happy Anniversary | Little River Band - Happy Anniversary | `exact_artist_title (1.000)` |
| 9 | `strong_match` | `create_form_container` | Madonna - Live To Tell | Madonna - Live To Tell | `exact_artist_title (1.000)` |
| 10 | `strong_match` | `create_form_container` | Shannon - Let The Music Play | Shannon - Let The Music Play | `exact_artist_title (1.000)` |
| 11 | `duplicate_cluster` | `review_match` | Righteous Brothers - Unchained Melody | The Righteous Brothers - Unchained Melody | `duplicate_salami_versions (0.980)` |
| 12 | `duplicate_cluster` | `review_match` | Nat King Cole - Unforgettable | Dinah Washington - Unforgettable | `duplicate_salami_versions (0.928)` |
| 13 | `high_value_no_salami` | `manual_or_other_source_analysis` | AC/DC - Back in Black | None | `no_match (0.000)` |
| 14 | `high_value_no_salami` | `manual_or_other_source_analysis` | AC/DC - Highway to Hell | None | `no_match (0.000)` |
| 15 | `high_value_no_salami` | `manual_or_other_source_analysis` | Adele - Hello | None | `no_match (0.000)` |
| 16 | `high_value_no_salami` | `manual_or_other_source_analysis` | Adele - Someone Like You | None | `no_match (0.000)` |
| 17 | `high_value_no_salami` | `manual_or_other_source_analysis` | Alicia Keys - If I Ain't Got You | None | `no_match (0.000)` |
| 18 | `additional_review` | `review_match` | Simon & Garfunkel - Hazy Shade of Winter | Simon And Garfunel - A Hazy Shade Of Winter | `manual_review (0.991)` |
| 19 | `additional_review` | `review_match` | Roberta Flack - Feel Like Makin' Love | Roberta Flack - Feel Like Making Love | `manual_review (0.983)` |
| 20 | `additional_review` | `review_match` | Simon & Garfunkel - The Sound of Silence | Simon & Garfunkel - The Sounds Of Silence | `manual_review (0.979)` |
| 21 | `additional_review` | `review_match` | The Rolling Stones - Honky Tonk Woman | The Rolling Stones - Honky Tonk Women | `manual_review (0.958)` |
| 22 | `additional_review` | `review_match` | Aaron Neville - Tell It Like It Is | The Neville Brothers - Tell It Like It Is | `title_only_artist_conflict (0.650)` |
| 23 | `additional_review` | `review_match` | Aretha Franklin - Think | James Brown - Think | `title_only_artist_conflict (0.650)` |
| 24 | `additional_review` | `review_match` | Ben E King - Stand By Me | David Ruffin, Jimmy Ruffin - Stand By Me | `title_only_artist_conflict (0.650)` |
| 25 | `additional_review` | `review_match` | Bill Withers - You've Got A Friend | Roberta Flack and Donny Hathaway - You've got a Friend | `title_only_artist_conflict (0.650)` |

## Recommended Next Move

Do not write `salami_coverage: false` to non-matches. Keep non-coverage report-only.

For positive matches, add an `--execute` mode only after Doug reviews the pilot. Limit writeback to reversible `salami_*` frontmatter fields and do not overwrite `tonic`, `mode`, `meter`, `form`, or Timeline content.

