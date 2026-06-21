# Repertoire / SALAMI Pilot Review Decisions

Generated: 2026-05-01

Source pilot: `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01_pilot.csv`

## Decision Rules Used

- **Accept positive coverage** when artist/title match is exact or a duplicate cluster is proven to contain identical chord rows.
- **Reject negative frontmatter writeback** for no-match rows. Non-coverage stays report-only.
- **Reject automatic CTSF timeline import** for Tier C rows. Tier C can receive form-container/generated-asset work first.
- **Accept duplicate-cluster coverage** when duplicate SALAMI rows have identical chord signatures; choose the lowest SALAMI `song_id` as canonical.
- **Reject SALAMI-only promotion** if an active CTSF entry already exists under an alias or abbreviation.

## Row-by-Row Recommendations

| # | CTSF / SALAMI item | Proposed pilot action | Decision | Exact next action | Reason |
|---:|---|---|---|---|---|
| 1 | Anne Murray — A Love Song | `import_salami_timeline` | **ACCEPT** | Write reviewed positive `salami_*` coverage and test one CTSF timeline import from `salami_0078.txt` (`song_id=532`). | Exact artist/title match; Tier B skeleton; 70 chord rows, 2 sections; CTSF file has unknown tonic/mode/meter and TBD body. |
| 2 | Canned Heat — On The Road Again | `import_salami_timeline` | **ACCEPT** | Write reviewed positive `salami_*` coverage and import/test timeline from `salami_0501.txt` (`song_id=845`). | Exact match; Tier B skeleton; 52 chord rows, 4 sections; good blues/modal candidate. Note CTSF year appears Spotify-release-derived and should not be trusted as original year. |
| 3 | The Buckinghams — Kind Of A Drag | `import_salami_timeline` | **ACCEPT** | Write reviewed positive `salami_*` coverage and import/test timeline from `salami_0299.txt` (`song_id=831`). | Exact match; Tier B skeleton; 86 chord rows, 4 sections. Note CTSF year appears compilation/release-derived and should not be trusted as original year. |
| 4 | ABBA — On And On And On | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0463.txt` (`song_id=885`); do not author CTSF prose yet. | Exact match; Tier C skeleton; 168 chord rows, 4 sections. Tier C should get generated structure before deep CTSF enrichment. |
| 5 | Beastie Boys — Brass Monkey | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0432.txt` (`song_id=149`). | Exact match; Tier C skeleton; 25 chord rows, 3 sections; useful as coverage/structure, not a deep-file priority. |
| 6 | Bonnie Pointer — Heaven Must Have Sent You | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0369.txt` (`song_id=86`). | Exact match; Tier C skeleton; 147 chord rows, 4 sections. |
| 7 | Isaac Hayes — The Look Of Love | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0391.txt` (`song_id=313`); flag as possible later Tier B review. | Exact match; Tier C skeleton; 305 chord rows, 8 sections, unusually rich SALAMI data. |
| 8 | Little River Band — Happy Anniversary | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0457.txt` (`song_id=642`). | Exact match; Tier C skeleton; 129 chord rows, 6 sections. |
| 9 | Madonna — Live To Tell | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0462.txt` (`song_id=951`); consider later Tier B review. | Exact match; Tier C skeleton; 216 chord rows, 6 sections; likely pedagogically stronger than generic Tier C. |
| 10 | Shannon — Let The Music Play | `create_form_container` | **ACCEPT** | Write reviewed positive `salami_*` coverage; generate form container from `salami_0315.txt` (`song_id=714`). | Exact match; Tier C skeleton; 147 chord rows, 6 sections. |
| 11 | Aerosmith — Last Child | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_1117.txt` (`song_id=114`); duplicate `salami_0504.txt` has identical chord signature. | Duplicate cluster is real but duplicates are identical; safe for coverage after canonical selection. |
| 12 | Anne Murray — Daydream Believer | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0330.txt` (`song_id=567`); duplicate rows `0951`, `0789`, `0165` have identical chord signatures. | Duplicate cluster contains identical chord data. |
| 13 | B.B. King — The Thrill Is Gone | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0437.txt` (`song_id=227`); duplicate `salami_1054.txt` has identical chord signature. | Duplicate cluster contains identical chord data. |
| 14 | Barry White — You're The First, The Last, My Everything | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0625.txt` (`song_id=98`); duplicate `salami_1237.txt` has identical chord signature. | Duplicate cluster contains identical chord data. |
| 15 | Bill Withers — Ain't No Sunshine | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0640.txt` (`song_id=580`); duplicate `salami_0015.txt` has identical chord signature. | Duplicate cluster contains identical chord data; Tier B skeleton, so this is a good later import candidate after writeback policy is approved. |
| 16 | AC/DC — Back in Black | `manual_or_other_source_analysis` | **REJECT FOR SALAMI ACTION** | Do not write SALAMI fields; keep as report-only `no_match`. No immediate manual action needed. | Tier A file is already populated/enriched; SALAMI has no match. |
| 17 | AC/DC — Highway to Hell | `manual_or_other_source_analysis` | **REJECT FOR SALAMI ACTION** | Do not write SALAMI fields; keep as report-only `no_match`. No immediate manual action needed. | Tier A file is already populated/enriched; SALAMI has no match. |
| 18 | Adele — Hello | `manual_or_other_source_analysis` | **REJECT FOR SALAMI ACTION** | Do not write SALAMI fields; keep as report-only `no_match`. No immediate manual action needed. | Tier A file is already populated/enriched; SALAMI has no match. |
| 19 | Adele — Someone Like You | `manual_or_other_source_analysis` | **REJECT FOR SALAMI ACTION** | Do not write SALAMI fields; keep as report-only `no_match`. No immediate manual action needed. | Tier A file is already populated/enriched; SALAMI has no match. |
| 20 | Alicia Keys — If I Ain't Got You | `manual_or_other_source_analysis` | **REJECT FOR SALAMI ACTION** | Do not write SALAMI fields; keep as report-only `no_match`. No immediate manual action needed. | Tier A file is already populated/enriched; SALAMI has no match. |
| 21 | SALAMI-only: Milli Vanilli — Girl I m Gonna Miss You | `promote_to_tier_review` | **REJECT AS SALAMI-ONLY** | Do not create/promote a new CTSF entry. Add matcher normalization for `I m` ↔ `I'm`; link to existing `MILLI_VANILLI - GIRL_IM_GONNA_MISS_YOU.md`. Prefer canonical SALAMI `salami_0336.txt` (`song_id=405`) over duplicate `salami_0957.txt`. | Active CTSF entry already exists; this is a normalization miss, not a repertoire gap. |
| 22 | SALAMI-only: Pink Floyd — Another Brick In The Wall (Part II) | `promote_to_tier_review` | **REJECT AS SALAMI-ONLY** | Do not create/promote a new CTSF entry. Add matcher normalization for `Part II` ↔ `Pt.2`; link to existing `PINK_FLOYD - ANOTHER_BRICK_IN_THE_WALL_PT2.md`. Prefer canonical SALAMI `salami_0343.txt` (`song_id=71`) over duplicate `salami_0964.txt`. | Active CTSF entry already exists; this is an abbreviation/roman-numeral normalization miss. |
| 23 | A Taste Of Honey — Sukiyaki | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0557.txt` (`song_id=202`); duplicate `salami_1170.txt` has identical chord signature. | Duplicate cluster contains identical chord data; Tier C skeleton can receive coverage and form-container work. |
| 24 | ABBA — Chiquitita | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0636.txt` (`song_id=297`); duplicate `salami_0011.txt` has identical chord signature. | Duplicate cluster contains identical chord data; Tier C skeleton can receive coverage and form-container work. |
| 25 | ABBA — Honey Honey | `review_match` | **ACCEPT WITH CANONICALIZATION** | Treat as SALAMI-covered; canonical row `salami_0899.txt` (`song_id=628`); duplicate `salami_0276.txt` has identical chord signature. | Duplicate cluster contains identical chord data; Tier C skeleton can receive coverage and form-container work. |

## Summary Counts

| Decision bucket | Rows |
|---|---:|
| Accept exact match for timeline import | 3 |
| Accept exact match for form-container generation | 7 |
| Accept duplicate cluster after canonicalization | 8 |
| Reject SALAMI action for high-value no-match entries | 5 |
| Reject SALAMI-only promotion; fix matcher normalization | 2 |

## Recommended Implementation Follow-Up

1. Add duplicate canonicalization to the crosswalk script: for exact duplicate clusters with identical chord signatures, choose the lowest `song_id` and mark `duplicate_policy: identical_chord_signature_lowest_id`.
2. Add alias normalization for `I'm`/`I m` and `Part II`/`Pt.2`/`Part 2`.
3. Add an `--execute-reviewed` mode that can take a reviewed decisions file and write positive `salami_*` fields only for accepted rows.
4. Run one timeline import test using row 1, Anne Murray — "A Love Song", before scaling timeline import to the other accepted Tier B rows.
