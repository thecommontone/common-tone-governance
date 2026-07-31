---
report: Quarantine Triage — Final
generated: 2026-04-24T07:15:00Z
tasks: [#23]
---

# REPERTOIRE_QUARANTINE Triage — 2026-04-24

All 32 quarantined files were reviewed individually, content-inspected, and routed.

## Actions taken

| Action | Count | Details |
|---|---:|---|
| Restored to REPERTOIRE | 4 | `_INDEX.md`, `_TEMPLATE.md`, `_TIER_C_NEW_VOCABULARY.md` (utility files), plus `THE_CHI_LITES - HAVE_YOU_SEEN_HER.md` (real 1,018-word analysis; renamed from `THE_CHI-LITES` to comply with §1.1 hyphen-to-underscore rule). |
| Routed to `ESSAYS/` | 6 | Good Vibrations Handout, Love on Top Modulations, Pachelbel Stuff, Single Ladies Analysis, Suspension in Miley Cyrus's Wrecking Ball, Form in Top 20. |
| Routed to `05_REFERENCE/EXTRACTED_MDS/` | 2 | `ETHAN_HEIN_CULTURAL.md`, Taylor Swift blog post extract. |
| Routed to `05_REFERENCE/CONCEPTS/` | 1 | `Songs with unresolved V7sus4.md` — a research-data table about a specific harmonic concept. |
| Routed to `03_MANUSCRIPT/_WORKING_NOTES/` | 1 | `Freq. of Songs in BOOK and CLASS.md` — pedagogical frequency data for the textbook. |
| Routed to `04_ARCHIVE/STUDENT_WORK/` (new subfolder) | 1 | `Good Vibrations Assignments.md` — student essay by Russil Alden. |
| Kept in QUARANTINE for manual merge | 3 | See below. |
| Deleted | 14 | Corrupted files, wrong-song auto-enrichment, copyright-sensitive lyric dumps. Full contents preserved in `quarantine_deletion_manifest_2026-04-24.md` for recovery if ever needed. |

## Still in QUARANTINE (for your manual merge when convenient)

Each has legitimate content but also has an existing CTSF entry in main REPERTOIRE that the notes should be merged into:

1. **`The Ballad of Brenda and Eddie.md`** → merge into `BILLY_JOEL - BALLAD_OF_BRENDA_AND_EDDIE.md`. The quarantine note says Joel wrote it as a short warm-up song that he fused with the other parts into "Scenes from an Italian Restaurant," citing the Abbey Road Medley as influence — real pedagogical fact.

2. **`Obla.md`** → merge into existing `THE_BEATLES - OBLA_DI_OBLA_DA.md`. The quarantine note has form analysis: "intro ABABCAB coda / Passamezzo? / Sentence structure / Main Melodic sequence – rising steps – 8 beat pattern / Cadential Melodic sequence – falling steps – 2 beat pattern / This follows a similar pattern to the Hank Williams song I'm So Lonesome I Could Cry."

3. **`Looking Glass - Brandy Youre A Fine GIRL.md`** → merge into existing `LOOKING_GLASS - BRANDY.md`. The quarantine note has chord-progression sketch (`vi | IV`).

## Deletion manifest

All 14 deleted files had their full contents archived to [quarantine_deletion_manifest_2026-04-24.md](quarantine_deletion_manifest_2026-04-24.md) before deletion. Total archived: 27,976 bytes.

## Validator improvements

As part of this pass, I also taught the validator to match the migrator's behavior on utility files:

- Added `SKIP_FILENAMES = {"_INDEX.md", "_TEMPLATE.md", "_TIER_C_NEW_VOCABULARY.md"}` to `ctsf_validator.py`.
- These files are now correctly excluded from validation (they aren't song entries).
- This stops them from counting as R01/R02/R03/R04/R08/R_BODY failures forever.

## Final state of the vault

| Folder | Files | Change |
|---|---:|---|
| `02_SOURCE_MATERIAL/REPERTOIRE/` | 6,221 | +15 (4 restored + 11 re-migrated non-CTSF stragglers — Acker Bilk, Harvey Schmidt, Winchester Cathedral, Bee Gees, Barry Manilow, etc.) |
| `02_SOURCE_MATERIAL/REPERTOIRE_QUARANTINE/` | 3 | Down from 32 |
| `ESSAYS/` | 18 | +6 |
| `05_REFERENCE/EXTRACTED_MDS/` | 144 | +2 |
| `05_REFERENCE/CONCEPTS/` | 3 | +1 (`Songs with unresolved V7sus4.md`) |
| `03_MANUSCRIPT/_WORKING_NOTES/` | 1 | New folder |
| `04_ARCHIVE/STUDENT_WORK/` | 1 | New folder |

## Validator state

| | Before quarantine triage | After |
|---|---:|---:|
| Total files validated | 6,206 | 6,218 (3 utility files correctly skipped) |
| Enriched | 23 | 23 |
| Skeleton | 6,171 | 6,185 |
| Failed | 12 | **13** — all R14 table-format Timelines (same known validator limitation as before; +1 came from one more non-CTSF file that appeared mid-session and then got re-migrated) |

All 13 remaining failures are the same R14 table-format-Timeline issue — legitimate skeleton entries whose Timelines use table rows instead of `### [section]` headers. Low priority validator upgrade.

## REPERTOIRE is now clean

- 6,221 files
- 3 utility meta-files (skipped by validator)
- 6,185 CTSF v1.3 skeleton entries
- 23 enriched entries
- 13 table-format Timelines needing a future validator upgrade
- 0 non-CTSF content

Zero junk. Zero corrupted stubs. Zero bad-auto-enrichment files. Every file has either valid CTSF v1.3 frontmatter with preserved metadata from the pre-migration backup, or is a recognized utility file.
