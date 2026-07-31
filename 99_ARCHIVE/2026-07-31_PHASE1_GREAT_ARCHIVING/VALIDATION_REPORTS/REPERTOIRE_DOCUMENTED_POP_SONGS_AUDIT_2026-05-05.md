# Repertoire Documented Pop Songs Audit And Harvest Map - 2026-05-05

## Scope

This is a read-only audit of `/Users/dougsmith/Docs/__MY_BOOK/REPERTOIRE_DOCUMENTED_POP_SONGS` as an outer-vault Role 4b reference asset. Source files were not moved, renamed, deleted, promoted, or edited. The goal is to identify practical harvesting lanes for The Common Tone project, with the first pass biased toward theory-rich analyses rather than bulk import.

## Corpus Summary

- Total files, including system metadata: 5126
- Auditable non-`.DS_Store` files: 4989
- Directories, including root: 800
- Total size: 14.5 GB (15,600,807,474 bytes)
- Existing inner CTSF repertoire files checked for overlap: 6020
- Rough outer/inner overlap keys: 787
- Explicit theory/analysis-named files: 258
- Notation/source-named files: 2139
- Media sidecars: 213
- Working project artifacts: 329

## Format Mix

| Item | Count |
|---|---:|
| `.pdf` | 2277 |
| `.tif` | 1703 |
| `.tiff` | 312 |
| `.sib` | 273 |
| `[no extension]` | 155 |
| `.mp3` | 124 |
| `.mid` | 63 |
| `.jpg` | 57 |
| `.svg` | 25 |
| `.pages` | 24 |
| `.mp4` | 22 |
| `.txt` | 13 |
| `.gif` | 13 |
| `.jpeg` | 11 |
| `.doc` | 10 |
| `.rtf` | 10 |
| `.docx` | 4 |
| `.tscproj` | 3 |
| `.plist` | 3 |
| `.mxl` | 3 |
| `.png` | 3 |
| `.html` | 2 |
| `.xlsx` | 1 |
| `.m4a` | 1 |

## Top-Level Folder Weight

| Item | Count |
|---|---:|
| `_COLLECTIONS-AND-ANTHOLOGIES` | 2366 |
| `_ARCHIVE` | 699 |
| `13-T` | 230 |
| `00-THE-BEATLES` | 227 |
| `12-S` | 208 |
| `02-B` | 194 |
| `06-G-H-I` | 187 |
| `11-O-P-Q-R` | 161 |
| `05-E-F` | 144 |
| `03-C` | 124 |
| `10-M-N` | 114 |
| `14-U-V-W-X-Y-Z` | 104 |
| `07-J` | 97 |
| `09-L` | 91 |
| `01-A` | 65 |
| `04-D` | 61 |
| `08-K` | 26 |
| `_LEAD-SHEETS-SIBELIUS` | 24 |
| `[root]` | 4 |

## Modified-Year Range

| Year | Files |
|---:|---:|
| 1996 | 19 |
| 1999 | 44 |
| 2001 | 842 |
| 2002 | 1262 |
| 2003 | 55 |
| 2004 | 162 |
| 2007 | 3 |
| 2008 | 1 |
| 2009 | 62 |
| 2010 | 12 |
| 2011 | 17 |
| 2012 | 30 |
| 2013 | 9 |
| 2014 | 35 |
| 2015 | 8 |
| 2016 | 1848 |
| 2017 | 131 |
| 2018 | 47 |
| 2019 | 18 |
| 2020 | 57 |
| 2021 | 52 |
| 2022 | 103 |
| 2023 | 28 |
| 2024 | 158 |
| 2025 | 57 |
| 2026 | 66 |

## Harvest Lanes

1. Theory-rich analyses - highest immediate value. These are files already naming analysis, harmony, chord progressions, modulation, phrase rhythm, form, chromaticism, production analysis, or related theory topics. They should be distilled into private source notes first, then reviewed for CTSF enrichment or concept linkage.
2. Existing CTSF overlaps - use the outer file as corroborating source material for songs already present in `02_SOURCE_MATERIAL/REPERTOIRE/`. These should enrich existing entries after review, not create duplicates.
3. Unrepresented songs - candidates with no inner exact match should become queue/intake candidates only after title/artist confirmation.
4. Anthology indexes and fake-book collections - useful discovery and repertoire breadth surfaces, but not all scans are equally actionable. Treat collection-level PDFs/TIF directories as reference shelves unless a specific song or concept makes them relevant.
5. Source scans and notation projects - Sibelius, image scans, and low-text PDFs can support verification, graphics, MusicXML export, or human review, but are not first-pass Markdown sources.

## First-Pass Harvest Candidates

The machine-readable manifest is here: `REPERTOIRE_DOCUMENTED_POP_SONGS_HARVEST_MANIFEST_2026-05-05.csv`. The table below shows the top 30 of 50 deduplicated ranked candidates. `title_only_review_needed` means the title exists in the inner repertoire but the artist/title identity needs human review before enrichment.

| Rank | Candidate | Lane | Match | Recommended action |
|---:|---|---|---|---|
| 1 | The Beach Boys - Good Vibrations<br>`13-T/THE BEACH BOYS/GOOD VIBRATIONS - THE BEACH BOYS/GOOD VIBRATIONS ASSIGNMENTS/Good Vibrations Formal Analysis - Ana-Rose Till.pdf` | theory-rich analysis | `THE_BEACH_BOYS - GOOD_VIBRATIONS.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 2 | Adele - Hello<br>`01-A/ADELE/Seventh and Ninth Chords in Adele's "Hello" - Pop Music Theory.pdf` | theory-rich analysis | `ADELE - HELLO.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 3 | Bruno Mars - When I Was Your Man<br>`02-B/BRUNO MARS/Chromatic Chords in "When I Was Your Man" by Bruno Mars - Pop Music Theory.pdf` | theory-rich analysis | `BRUNO_MARS - WHEN_I_WAS_YOUR_MAN.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 4 | Grizzly Bear - Ready, Able<br>`11-O-P-Q-R/Ready, Able by Grizzly Bear-A Compositional Analysis.pages` | theory-rich analysis | `GRIZZLY_BEAR - READY_ABLE.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 5 | Bob Dylan - Blowin in the Wind<br>`02-B/BOB DYLAN.pdf/20-Blowing in The Wind Analysis.doc` | theory-rich analysis | `BOB_DYLAN - BLOWIN_IN_THE_WIND.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 6 | The Beach Boys - Good Vibrations<br>`13-T/THE BEACH BOYS/GOOD VIBRATIONS - THE BEACH BOYS/GOOD VIBRATIONS ASSIGNMENTS/Theory analysis.pdf` | theory-rich analysis | `THE_BEACH_BOYS - GOOD_VIBRATIONS.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 7 | Avicii - Wake Me Up<br>`01-A/Song Analysis of Avicii’s Wake Me Up.pages` | theory-rich analysis | `AVICII - WAKE_ME_UP.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 8 | The Lumineers - Ho Hey<br>`09-L/Song Analysis of The Lumineers’ Ho Hey.pages` | theory-rich analysis | `THE_LUMINEERS - HO_HEY.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 9 | The Emotions - Blind Alley<br>`02-B/Blind Alley-RB Chord Stream Supreme.txt` | theory-rich analysis | `THE_EMOTIONS - BLIND_ALLEY.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 10 | Seal - Kiss From a Rose<br>`08-K/Kiss From a Rose - Phrase Rhythm Seal.txt` | theory-rich analysis | `SEAL - KISS_FROM_A_ROSE.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 11 | Irving Berlin - Puttin on the Ritz<br>`11-O-P-Q-R/Putting on the Ritz - Hemiola-polyrhythm.pages` | theory-rich analysis | `IRVING_BERLIN - PUTTIN_ON_THE_RITZ.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 12 | Seal - Kiss From a Rose<br>`08-K/Kiss From a Rose - Phrase Rhythm Seal.pages` | theory-rich analysis | `SEAL - KISS_FROM_A_ROSE.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 13 | Lady Gaga - Paparazzi<br>`09-L/LADY GAGA/Modulation in Pop Music-Lady Gaga=Paparazzi.pages` | theory-rich analysis | `LADY_GAGA - PAPARAZZI.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 14 | The Beatles - Oh! Darling<br>`00-THE-BEATLES/OH DARLING/Oh Darling Analysis.pdf` | theory-rich analysis | `THE_BEATLES - OH_DARLING.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 15 | Daft Punk - Get Lucky<br>`04-D/DAFT PUNK/Technical analysis of Get Lucky by Daft Punk.pdf` | theory-rich analysis | `DAFT_PUNK - GET_LUCKY.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 16 | Lady Gaga - G.U.Y.<br>`09-L/LADY GAGA/Neapolitan Chord in Lady Gaga G.U.Y. - Pop Music Theory.pdf` | theory-rich analysis | `none found (none)` | distill_to_private_source_note_then_intake_review |
| 17 | The Drifters - Under the Boardwalk<br>`13-T/THE DRIFTERS/UNDER THE BOARDWALK/Under the Boardwalk-piano analysis.sib` | theory-rich analysis | `THE_DRIFTERS - UNDER_THE_BOARDWALK.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 18 | Miley Cyrus - Wrecking Ball<br>`10-M-N/MILEY CYRUS/Suspension in Miley Cyrus's Wrecking Ball - Pop Music Theory.pdf` | theory-rich analysis | `MILEY_CYRUS - WRECKING_BALL.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 19 | Miley Cyrus - Wrecking Ball<br>`10-M-N/MILEY CYRUS/Suspension in Miley Cyrus’s Wrecking Ball.pages` | source/reference | `MILEY_CYRUS - WRECKING_BALL.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 20 | Beyonce - Love On Top<br>`02-B/BEYONCE/LOVE ON TOP/Decoding the Love on Top Modulations.pages` | theory-rich analysis | `none found (none)` | distill_to_private_source_note_then_intake_review |
| 21 | Seal - Kiss From a Rose<br>`12-S/SEAL/Seal - Kiss From A Rose.pdf` | source/reference | `SEAL - KISS_FROM_A_ROSE.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 22 | Katy Perry - Firework<br>`08-K/KATY PERRY/Katy Perry "Firework" Production Analysis - Bobby Owsinski's Music Production Blog.pdf` | theory-rich analysis | `KATY_PERRY - FIREWORK.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 23 | Katy Perry - Dark Horse<br>`08-K/KATY PERRY/The Seventh Scale Degree in Katy Perry's Dark Horse - Pop Music Theory.pdf` | theory-rich analysis | `KATY_PERRY - DARK_HORSE.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 24 | Lady Gaga - Paparazzi<br>`09-L/LADY GAGA/Modulation in Music: Lady Gaga "Paparazzi" Example - Pop Music Theory.pdf` | theory-rich analysis | `LADY_GAGA - PAPARAZZI.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 25 | The Emotions - Blind Alley<br>`02-B/Blind Alley-RB Chord Stream Supreme.pages` | theory-rich analysis | `THE_EMOTIONS - BLIND_ALLEY.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 26 | Meghan Trainor - All About That Bass<br>`10-M-N/MEAGAN TRAINOR/ALL ABOUT THE BASS/Chord Progression in Meghan Trainor's "All About that Bass".pdf` | theory-rich analysis | `MEGHAN_TRAINOR - ALL_ABOUT_THAT_BASS.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 27 | Non-Diatonic Chord in Kurt Vile - Wakin' on a Pretty Day<br>`08-K/KATY PERRY/Non-Diatonic Chord in Kurt Vile - Wakin' on a Pretty Day - Pop Music Theory.pdf` | theory-rich analysis | `none found (none)` | distill_to_private_source_note_then_intake_review |
| 28 | The Beatles - Oh! Darling<br>`00-THE-BEATLES/OH DARLING/Oh Darling Analysis.sib` | theory-rich analysis | `THE_BEATLES - OH_DARLING.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 29 | Eric Clapton - Tears In Heaven<br>`05-E-F/ERIC CLAPTON/Eric Clapton - Tears In Heaven.doc` | source/reference | `ERIC_CLAPTON - TEARS_IN_HEAVEN.md (exact_artist_title)` | enrich_existing_ctsf_after_review |
| 30 | Led Zeppelin - Stairway to Heaven<br>`09-L/LED ZEPPELIN/Led Zepplin, Stairway to Heaven.doc` | source/reference | `LED_ZEPPELIN - STAIRWAY_TO_HEAVEN.md (exact_artist_title)` | enrich_existing_ctsf_after_review |

## Concrete Suggestions For Common Tone

- Start a "theory-rich source note" lane outside the inner repertoire: one distilled Markdown note per high-value source, with provenance and candidate Common Tone concepts, before any CTSF entry is touched.
- Use exact artist/title matches against existing CTSF entries as the first enrichment wave. This avoids duplicate repertoire entries and lets strong files like `Oh Darling Analysis.pdf`, `Blowin in The Wind Analysis.doc`, and popmusictheory PDFs deepen songs already in the corpus.
- Promote concept clusters, not files. The first clusters worth harvesting are chromaticism/modal mixture, phrase rhythm/hypermeter, modulation/key change, diatonic-harmonized-scale pedagogy, and Beatles-style mixture/secondary-dominant analysis.
- Treat `.pages` files as high editorial value but medium automation risk. They are often Doug-like analytic notes, but extraction may require Pages export or visual preview rather than plain text tools.
- Keep anthologies as discovery shelves. Their value is in indexes, repertoire breadth, and verification, not wholesale conversion.
- Add a future pointer README for this Role 4b folder if one does not already exist, recording provenance, consuming tools, and the rule that harvested material enters through intake rather than direct movement.

## Extraction Spot Checks

| Sample | Type | Result | Notes |
|---|---|---|---|
| `02-B/Blind Alley-RB Chord Stream Supreme.txt` | `.txt` | extractable_text (516 sample words/items) | direct text read |
| `02-B/BOB DYLAN.pdf/20-Blowing in The Wind Analysis.doc` | `.doc` | extractable_text (1331 sample words/items) | textutil conversion to text |
| `00-THE-BEATLES/OH DARLING/Oh Darling Analysis.pdf` | `.pdf` | extractable_text (457 sample words/items) | pdftotext first pass; OCR if text yield is low |
| `02-B/BRUNO MARS/Chromatic Chords in "When I Was Your Man" by Bruno Mars - Pop Music Theory.pdf` | `.pdf` | extractable_text (366 sample words/items) | pdftotext first pass; OCR if text yield is low |
| `02-B/BEYONCE/LOVE ON TOP/Decoding the Love on Top Modulations.pages` | `.pages` | package_readable_text_not_direct (295 sample words/items) | Pages package export/preview; preserve provenance before Markdown distillation |

## Verification Notes

- File count and extension totals were regenerated during this run.
- Candidate matching checked title guesses against existing inner CTSF Markdown filenames and labels exact artist/title matches separately from title-only matches.
- Text extraction was sampled across direct text, legacy Word, text PDF, notation PDF, and Pages package material.
- No CTSF files, queue files, status files, or source archive files were modified.
- Future promotion should use the Common Tone ingestion path and validate CTSF output with `_SYSTEM/scripts/ctsf_validator.py`.

## Next Work Packet

1. Review the top 10 manifest rows and mark which source notes should be distilled first.
2. For rows with exact CTSF matches, compare the current inner entry before drafting enrichment.
3. For rows without an exact match, confirm title/artist identity before adding any repertoire queue item.
4. If `.pages` notes are selected, export them to text/PDF through Pages or a controlled conversion workflow, then preserve the original source path in provenance.
