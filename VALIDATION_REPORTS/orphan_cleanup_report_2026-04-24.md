---
report: Orphan Cleanup Report
generated: 2026-04-24T06:20:00Z
task: "#15 Clean up orphaned pre-migration filenames"
scope: 02_SOURCE_MATERIAL/REPERTOIRE/
---

# Orphan Cleanup Report — 2026-04-24

## Summary

The 2026-04-23 CTSF v1.3 migration successfully wrote 6,013 normalized files but could not unlink their pre-migration originals (Operation not permitted — cowork delete guard). This left REPERTOIRE with ~12,256 files: every song present in both the old (Title Case, spaces) and new (UPPERCASE_UNDERSCORED) form.

This cleanup pass parsed `ctsf_migration_log_2026-04-23-migration.md`, extracted the 6,012 old paths it had been unable to unlink, and deleted them after safety checks. One edge case — George Shearing — Canadian Sunset — was identified where the new file was 0 bytes (fd-exhaustion during migration); the old file was kept and the zero-byte husk removed instead.

## Numbers

| Stage                                            | Count  |
| ------------------------------------------------ | -----: |
| REPERTOIRE files before cleanup                  | 12,256 |
| Orphan paths parsed from migration log           |  6,012 |
| Orphan paths excluded to prevent data loss (Canadian Sunset) | 1 |
| Orphan paths deleted                             |  6,012 |
| 0-byte failed-migration files deleted            |      1 |
| REPERTOIRE files after cleanup                   |  6,244 |
| Cleanup errors                                   |      0 |

## Post-state classification

Of 6,244 remaining files:

- **5,939** CTSF v1.3 normalized files (UPPERCASE_UNDERSCORED — `ABBA - DANCING_QUEEN.md` etc.) — successfully migrated.
- **303** unmigrated files — pre-existing filenames the migrator's `Artist - Title` parser rejected. Examples: `- Black Orpheus.md`, `Army of Me.md`, `Complicated by Avril Lavigne.md`, `EXTRACTED_A Horse with No Name_20260408.md`. These files were never touched by the migration and retain their original frontmatter.
- **1** deliberately kept: `George Shearing - Canadian Sunset.md`. Migration's new file was 0 bytes (Errno 23 — too many open files); the old file (441 B, intact content) is retained and needs a targeted re-run of the migrator on this one file.

## Safety measures taken

1. **Path confinement.** Every deletion path was verified to start with the REPERTOIRE directory prefix.
2. **Edge-case protection.** The 1 migrator entry with a non-standard error (Errno 23 vs. Errno 1) was excluded from the deletion list automatically, and the corresponding old file was confirmed on disk before proceeding.
3. **Audit log.** Every deletion outcome is recorded in `/outputs/orphan_cleanup_log.txt` and this report.

## Known issues surfaced (out of scope for cleanup, flagged for follow-up)

1. **CTSF v1.3 rewrite loses metadata.** Spot-checked samples show new-format frontmatter drops fields the old frontmatter carried — `year`, `spotify_link`, `composers`, `source` — replacing them with `unknown` sentinels. The Y:M:T of `2_LIVE_CREW - CMON_BABE.md` is `unknown/unknown/unknown` even though that information may be recoverable from the old file or upstream sources. **Recommend re-running the migrator with a metadata-preserving pass before closing CTSF migration.**
2. **303 files skipped by the migrator's parser.** Filenames without a clean `Artist - Title` pattern were not normalized. These need either (a) manual renaming to match the pattern and a targeted re-migration, or (b) an enriched migrator that can consult frontmatter `artist`/`song` fields as a fallback.
3. **74-file arithmetic gap.** Log summary says "wrote 6013" but only 5,939 UPPERCASE-pattern files exist post-cleanup. Likely causes: writes that collided on an identical normalized filename (silent overwrite), or new files whose shapes don't match the UPPERCASE regex. Worth an explicit count from the migrator's own accounting rather than post-hoc regex.

## Artifacts

- Orphan path list: `/outputs/orphan_paths.txt`
- Per-file deletion log: `/outputs/orphan_cleanup_log.txt`
- Source migration log: `VALIDATION_REPORTS/ctsf_migration_log_2026-04-23-migration.md`
