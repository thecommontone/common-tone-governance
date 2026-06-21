# Repertoire / SALAMI Gitignore Patch Report

Generated: 2026-05-01

## Summary

- Project-local `.gitignore` existed already: No
- Project-local `.gitignore` created: Yes
- Primary commit made: Yes
- Primary commit hash: `3e9f4726300266019ccc4b55166c1af5a57752c1`
- Commit message: `Ignore generated SALAMI validation artifacts`

The root Git repository is `/Users/dougsmith`, but this patch intentionally created a project-local ignore file at:

`/Users/dougsmith/Docs/__MY_BOOK/.gitignore`

This avoids touching the already-modified root `.gitignore`.

## Exact Patterns Added

```gitignore
# IDEA-012 / SALAMI generated validation artifacts
VALIDATION_REPORTS/backups/
VALIDATION_REPORTS/repertoire_salami_crosswalk_*.csv
VALIDATION_REPORTS/repertoire_salami_writeback_*_dry_run.csv
VALIDATION_REPORTS/repertoire_salami_writeback_*_actual.csv
VALIDATION_REPORTS/repertoire_salami_writeback_batch*_*.csv
VALIDATION_REPORTS/repertoire_salami_*_dry_run.csv
VALIDATION_REPORTS/repertoire_salami_*_actual.csv
```

## Verification Results

| Check | Result |
|---|---|
| `git check-ignore -v VALIDATION_REPORTS/backups/example.txt` | Ignored by `VALIDATION_REPORTS/backups/` |
| `git check-ignore -v VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_dry_run.csv` | Ignored by `VALIDATION_REPORTS/repertoire_salami_*_dry_run.csv` |
| `git check-ignore -v VALIDATION_REPORTS/repertoire_salami_crosswalk_2026-05-01.csv` | Ignored by `VALIDATION_REPORTS/repertoire_salami_crosswalk_*.csv` |
| `git check-ignore -v VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_actual.csv` | Ignored by `VALIDATION_REPORTS/repertoire_salami_*_actual.csv` |
| `git check-ignore -v VALIDATION_REPORTS/repertoire_salami_outer_repo_tracking_2026-05-01.md` | Not ignored |
| `git check-ignore -v VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_actual.md` | Not ignored |
| `git check-ignore -v _SYSTEM/scripts/repertoire_salami_crosswalk.py` | Not ignored |

## Curated Reports

No tracked curated Markdown reports are affected. The ignore rules do not ignore Markdown files and do not affect the crosswalk script or IDEA_LAB files.

## Files Deliberately Left Unstaged

Generated execution Markdown reports remain untracked and visible:

- `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_actual.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_dry_run.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_actual.md`
- `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_dry_run.md`

Generated CSVs and backup folders are now ignored.

## Next Recommended Boring Step

Accept the `.gitignore` patch and this report/status bookkeeping. Do not run Batch 3 until the ignored-artifact behavior is accepted.
