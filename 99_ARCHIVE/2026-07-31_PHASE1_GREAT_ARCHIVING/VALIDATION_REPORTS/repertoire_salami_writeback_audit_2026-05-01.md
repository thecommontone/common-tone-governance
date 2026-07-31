# Repertoire / SALAMI Writeback Audit

Generated: 2026-05-01

## Scope

Audit of the first reviewed-positive SALAMI metadata writeback batch. This audit compares the five edited CTSF files against their pre-write backups in:

`VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/`

No additional writeback batch was run during this audit.

## Summary

| File | Backup exists | Current frontmatter valid | Non-frontmatter changed | Blocked fields found | Rollback possible |
|---|---|---|---|---|---|
| `ANNE_MURRAY - A_LOVE_SONG.md` | Yes | Yes | No | No | Yes |
| `CANNED_HEAT - ON_THE_ROAD_AGAIN.md` | Yes | Yes | No | No | Yes |
| `THE_BUCKINGHAMS - KIND_OF_A_DRAG.md` | Yes | Yes | No | No | Yes |
| `ABBA - ON_AND_ON_AND_ON.md` | Yes | Yes | No | No | Yes |
| `BEASTIE_BOYS - BRASS_MONKEY.md` | Yes | Yes | No | No | Yes |

Validation notes:

- Each current file parses as YAML frontmatter.
- Each backup exists.
- Each diff consists only of six added `salami_*` frontmatter lines immediately before the closing frontmatter delimiter.
- The body content after the frontmatter delimiter is identical to the backup in every file.
- No blocked fields appeared: `salami_coverage: false`, `salami_timeline`, `salami_sections`, `salami_chords`, `tempo_bpm`, or `estimated_bpm`.
- Rollback is possible for each file by replacing the current file with its corresponding backup copy.

## Per-File Audit

### `ANNE_MURRAY - A_LOVE_SONG.md`

- Current file: `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - A_LOVE_SONG.md`
- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/ANNE_MURRAY - A_LOVE_SONG.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 532
salami_filename: "salami_0078.txt"
salami_match_type: "exact_artist_title"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
```

### `CANNED_HEAT - ON_THE_ROAD_AGAIN.md`

- Current file: `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/CANNED_HEAT - ON_THE_ROAD_AGAIN.md`
- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/CANNED_HEAT - ON_THE_ROAD_AGAIN.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 845
salami_filename: "salami_0501.txt"
salami_match_type: "exact_artist_title"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
```

### `THE_BUCKINGHAMS - KIND_OF_A_DRAG.md`

- Current file: `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/THE_BUCKINGHAMS - KIND_OF_A_DRAG.md`
- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/THE_BUCKINGHAMS - KIND_OF_A_DRAG.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 831
salami_filename: "salami_0299.txt"
salami_match_type: "exact_artist_title"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
```

### `ABBA - ON_AND_ON_AND_ON.md`

- Current file: `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - ON_AND_ON_AND_ON.md`
- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/ABBA - ON_AND_ON_AND_ON.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 885
salami_filename: "salami_0463.txt"
salami_match_type: "exact_artist_title"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
```

### `BEASTIE_BOYS - BRASS_MONKEY.md`

- Current file: `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BEASTIE_BOYS - BRASS_MONKEY.md`
- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/BEASTIE_BOYS - BRASS_MONKEY.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 149
salami_filename: "salami_0432.txt"
salami_match_type: "exact_artist_title"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
```

## Git / Tracking Note

The workspace has two relevant Git contexts:

- Outer repo root: `/Users/dougsmith`
- Nested CTSF repo: `/Users/dougsmith/Docs/__MY_BOOK/The_Common_Tone_Project`

In the nested CTSF repo, the five edited repertoire files are tracked and show as modified. The nested repo diff confirms the same six-line frontmatter-only additions for each file.

In the outer repo, `_SYSTEM/scripts/repertoire_salami_crosswalk.py`, this report, the writeback reports, and backup files currently appear as untracked project artifacts. This is why the earlier status warning looked noisier than the actual CTSF file changes.

Recommendation:

- Add the crosswalk script to Git tracking if this automation is intended to become a maintained project tool.
- Commit the five CTSF metadata changes in the nested `The_Common_Tone_Project` repo only after this audit is accepted.
- Keep generated validation reports and backup copies report/backups-only for now, or track only a small curated audit report. Avoid committing every backup copy into the main repo unless there is a formal archival policy.
- For future writeback batches, consider a lightweight snapshot strategy: keep dated backup folders locally, write a Markdown/CSV manifest with file hashes and rollback paths, and commit only the reviewed code plus curated audit/report files.

## Recommendation

This first writeback batch passes the audit. It is safe to review the five diffs manually, then either commit this tiny batch or run one more capped reviewed-positive metadata-only batch after approval.
