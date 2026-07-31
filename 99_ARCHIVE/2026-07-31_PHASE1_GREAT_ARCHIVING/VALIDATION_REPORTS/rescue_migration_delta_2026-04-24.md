---
report: CTSF Rescue Migration — Delta Report
generated: 2026-04-24T06:42:30Z
migrator_version: v1.1
source: REPERTOIRE_LEGACY/REPERTOIRE_PRE_MIGRATION_2026-04-23
target: 02_SOURCE_MATERIAL/REPERTOIRE
---

# CTSF Rescue Migration — Delta Report

## TL;DR

The v1.0 run (2026-04-23 / 2026-04-24 morning) wrote 6,013 CTSF-compliant skeletons but silently dropped the frontmatter of every file whose YAML failed to parse (4,597 files / 72%). The v1.1 rescue run read from the pre-migration backup, parsed everything with a three-tier lenient parser, re-issued every file with the metadata intact, explicitly logged all collisions, and used frontmatter fallback to rescue 139 previously-unmigrated files whose filenames didn't parse to `Artist - Title`.

## Metadata recovery — v1.0 vs v1.1

Measured over CTSF v1.3 files in main REPERTOIRE after cleanup:

| Field | v1.0 recovery | v1.1 recovery |
|---|---:|---:|
| `year` (non-`unknown`) | ~0% | **97.5%** (6,048 / 6,203) |
| `spotify_link` | ~0% | **89.2%** (5,535) |
| `genre` | ~0% | **66.6%** (4,133) |
| `composers` | ~0% | **59.4%** (3,685) |
| `legacy_source` | ~0% | **98.3%** (6,100) |
| `album` | ~0% | 10.1% (626) |

## Validator — post-rescue

Generated from `ctsf_validator.py` on the main REPERTOIRE folder, 2026-04-24 06:42.

| Bucket | Count | Share |
|---|---:|---:|
| Enriched (compliant + no `unknown`s) | 16 | 0.25% |
| Skeleton (compliant + some `unknown`) | 6,034 | 94.78% |
| Failed (one or more Required rules violated) | 316 | 4.96% |
| **Total** | **6,366** | |

The 16 "Enriched" files retained fully-typed `tonic`/`mode`/`meter` from the pre-migration backup (the CTSF gold standard — these are Doug-authored or previously-analyzed entries).

The 316 "Failed" breaks down roughly as:
- ~164 files with non-compliant filenames that couldn't be rescued (EXTRACTED_* notes, single-artist-name files with bad Spotify auto-enrichment, general junk)
- ~152 other rule failures (R05 ASCII flats/sharps, R_TITLE missing heading, R16 mode-change separator, etc.) — these are legitimate skeleton-level issues to triage separately

## Migrator v1.1 changes

Three targeted improvements:

1. **Lenient three-tier frontmatter parser:** strict YAML → sanitize stray bullets → regex-salvage known scalar fields. Handled 4,362 files via sanitize tier and 238 via regex tier.
2. **Frontmatter fallback for anomalous filenames:** when filename doesn't parse to `Artist - Title`, consult the frontmatter but only if title shares tokens with the filename stem. Rescued 134 files that v1.0 dropped; refused 15 cases where the frontmatter looked like bad auto-enrichment.
3. **Explicit collision logging:** every `_2`/`_3` suffix disambiguation now records winner + loser + original target. 107 real plan-vs-plan collisions flagged in this run.

Plus one orchestration addition:

4. **`--write-target` + `--overwrite-existing`:** allows reading from a backup folder and writing to the main folder, bypassing "existing file" collision detection when the target contains a prior lossy migration to replace.

## Execution summary

Pre-rescue main REPERTOIRE: 6,258 files (after v1.0 migration + orphan cleanup).

Rescue run:
- Wrote 6,146 v1.1 files (read from backup, 2 fd-exhaustion retries written after).
- Added 5 files whose originals existed only in main, not in backup.
- Deleted 155 orphans (150 whose canonical twins got written in the rescue, plus the 5 originals whose new-name versions got written as part of the mop-up).

Post-rescue main REPERTOIRE: 6,366 files.

## Known follow-ups

1. **164 files remain in human-review state.** Filename patterns: `EXTRACTED_*` (these appear to be notes/essays, not songs), single-artist-name files (`Britney Spears.md`, `Kanye West.md`), and files where frontmatter auto-enrichment imported a wrong song that the token-match guard correctly refused. Triage list: `/outputs/v1_1_needs_review.txt`.
2. **The 152 "other failed" files** (non-review rule failures) should be triaged in a follow-up pass. Likely quick wins: normalize ASCII `b`/`#` to `♭`/`♯` in Timeline blocks (R05), synthesize missing `# Title` headings (R_TITLE), fix lowercase for mode-change separators (R16).
3. **Tempo data lost** (`tempo_bpm` shows 0% recovery). Worth investigating whether it survived in any pre-migration files — it may be that the pre-migration source simply didn't have this field populated.

## Artifacts

- Migrator source: `_SYSTEM/scripts/ctsf_migrator.py` (v1.1)
- v1.0 archive: `_SYSTEM/scripts/ctsf_migrator_v1.0_archived_2026-04-24.py`
- Dry-run plan: `VALIDATION_REPORTS/ctsf_migration_plan_2026-04-24-v1.1-rescue-dryrun.md`
- Execute plan + log: `VALIDATION_REPORTS/ctsf_migration_plan_2026-04-24-v1.1-rescue.md`, `VALIDATION_REPORTS/ctsf_migration_log_2026-04-24-v1.1-rescue.md`
- Validator output: `VALIDATION_REPORTS/ctsf_validation_2026-04-24-post-v1.1-rescue.{md,json,csv}`
- Review queues: `/outputs/v1_1_needs_review.txt`, `/outputs/v1_1_orphan_paths.txt`, `/outputs/v1_1_leftover_targets.txt`
