# Repertoire / SALAMI Outer Repo Tracking Report

Generated: 2026-05-01

## Outer Repo Status Summary

The outer Git repository root is `/Users/dougsmith`, not `/Users/dougsmith/Docs/__MY_BOOK`. A full `git status --short` from the project folder is therefore noisy and includes unrelated home-directory material.

For IDEA-012, the relevant path-scoped status was reviewed for:

- `_SYSTEM/scripts/repertoire_salami_crosswalk.py`
- `IDEA_LAB/IDEA-012_Unified-Repertoire-SALAMI-Crosswalk/`
- `VALIDATION_REPORTS/repertoire_salami*`

## Proposed Tracked Files

Tracked in primary outer commit `38e249446df40484c82a5aa49f817ee64989b6ba`:

- `_SYSTEM/scripts/repertoire_salami_crosswalk.py`
- `IDEA_LAB/IDEA-012_Unified-Repertoire-SALAMI-Crosswalk/01-PITCH.md`
- `IDEA_LAB/IDEA-012_Unified-Repertoire-SALAMI-Crosswalk/02-REVIEWS.md`
- `IDEA_LAB/IDEA-012_Unified-Repertoire-SALAMI-Crosswalk/03-STATUS.md`
- `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01.md`
- `VALIDATION_REPORTS/repertoire_salami_pilot_review_2026-05-01.md`
- `VALIDATION_REPORTS/repertoire_salami_timeline_import_test_2026-05-01.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_audit_2026-05-01.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_audit_2026-05-01.md`
- `VALIDATION_REPORTS/repertoire_salami_repo_hygiene_2026-05-01.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_snapshot_manifest_2026-05-01.md`

This report and the status addendum were created after the primary commit so they could record the primary commit hash.

## Files Deliberately Left Untracked

Generated CSVs:

- `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01.csv`
- `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01_pilot.csv`
- `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_actual.csv`
- `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_dry_run.csv`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_actual.csv`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_dry_run.csv`

Generated execution reports left untracked because curated audits/manifest capture the durable evidence:

- `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_actual.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_dry_run.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_actual.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_dry_run.md`

Backup artifacts:

- `VALIDATION_REPORTS/backups/`

All unrelated modified or untracked files outside IDEA-012 were left untouched.

## CSV Classification

| File | Classification | Reason |
|---|---|---|
| `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01.csv` | do_not_track: generated bulk CSV | 1.1 MB full generated crosswalk; Markdown summary is tracked. |
| `VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01_pilot.csv` | do_not_track: generated CSV | Pilot decisions are preserved in the curated Markdown review. |
| `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_actual.csv` | do_not_track: generated CSV | Batch 1 audit/report evidence is tracked in Markdown. |
| `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_dry_run.csv` | do_not_track: generated CSV | Dry-run execution artifact. |
| `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_actual.csv` | do_not_track: generated CSV | Batch 2 audit/report evidence is tracked in Markdown. |
| `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_dry_run.csv` | do_not_track: generated CSV | Dry-run execution artifact. |

## .gitignore Recommendation

No `.gitignore` changes were made. A narrow future change is recommended, especially because the current outer repo has a modified root `.gitignore` outside this project scope.

Suggested patterns:

```gitignore
Docs/__MY_BOOK/VALIDATION_REPORTS/backups/
Docs/__MY_BOOK/VALIDATION_REPORTS/*_dry_run.csv
Docs/__MY_BOOK/VALIDATION_REPORTS/*_actual.csv
Docs/__MY_BOOK/VALIDATION_REPORTS/repertoire_salami_crosswalk_*.csv
Docs/__MY_BOOK/VALIDATION_REPORTS/repertoire_salami_writeback_batch*.csv
```

Avoid a broad `VALIDATION_REPORTS/` ignore pattern because curated Markdown reports are useful project evidence.

## Commit Result

- Primary commit made: Yes
- Primary commit hash: `38e249446df40484c82a5aa49f817ee64989b6ba`
- Commit message: `Track SALAMI crosswalk tool and IDEA-012 reports`
- Files in primary commit: 11
- Staged-file verification: clean; no CSVs, backups, backup folders, or unrelated files were staged.

## Remaining Cautions

- Do not run Batch 3 until this outer tracking state is accepted.
- Do not import SALAMI timelines into CTSF files.
- Do not write negative coverage.
- Do not commit generated backups wholesale.
- Treat the outer repo carefully because its root is the user home directory and status is noisy by default.

## Next Recommended Boring Step

Accept the outer tracking commits, then consider a narrow `.gitignore` patch for SALAMI backup and generated CSV artifacts.
