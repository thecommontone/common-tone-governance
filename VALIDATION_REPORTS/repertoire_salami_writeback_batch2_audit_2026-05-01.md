# Repertoire / SALAMI Batch 2 Writeback Audit

Generated: 2026-05-01

## Scope

Audit of the second tiny reviewed-positive SALAMI metadata writeback batch. This batch targeted accepted canonicalized duplicate matches only, using:

```bash
python3 _SYSTEM/scripts/repertoire_salami_crosswalk.py --writeback-reviewed-positive --reviewed-positive-offset 10 --limit 5 --backup --execute-writeback --report-stem repertoire_salami_writeback_batch2_2026-05-01
```

No timelines, sections, chords, tempo fields, or negative coverage fields were written.

## Candidate Files

| CTSF file | SALAMI song_id | SALAMI file | Duplicate policy |
|---|---:|---|---|
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/AEROSMITH - LAST_CHILD.md` | 114 | `salami_1117.txt` | `identical_chord_signature_lowest_id` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - DAYDREAM_BELIEVER.md` | 567 | `salami_0330.txt` | `identical_chord_signature_lowest_id` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BB_KING - THE_THRILL_IS_GONE.md` | 227 | `salami_0437.txt` | `identical_chord_signature_lowest_id` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.md` | 98 | `salami_0625.txt` | `identical_chord_signature_lowest_id` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILL_WITHERS - AINT_NO_SUNSHINE.md` | 580 | `salami_0640.txt` | `identical_chord_signature_lowest_id` |

## Summary

| File | Backup exists | Frontmatter valid | Duplicate policy added | Non-frontmatter changed | Blocked fields found | Rollback possible |
|---|---|---|---|---|---|---|
| `AEROSMITH - LAST_CHILD.md` | Yes | Yes | Yes | No | No | Yes |
| `ANNE_MURRAY - DAYDREAM_BELIEVER.md` | Yes | Yes | Yes | No | No | Yes |
| `BB_KING - THE_THRILL_IS_GONE.md` | Yes | Yes | Yes | No | No | Yes |
| `BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.md` | Yes | Yes | Yes | No | No | Yes |
| `BILL_WITHERS - AINT_NO_SUNSHINE.md` | Yes | Yes | Yes | No | No | Yes |

Validation notes:

- Each backup exists in `VALIDATION_REPORTS/backups/repertoire_salami_writeback_batch2_2026-05-01/`.
- Each current file parses as YAML frontmatter.
- Each diff consists only of seven added `salami_*` frontmatter lines immediately before the closing frontmatter delimiter.
- `salami_duplicate_policy: "identical_chord_signature_lowest_id"` was added in all five files.
- The body content after the frontmatter delimiter is identical to the backup in every file.
- No blocked fields appeared: `salami_coverage: false`, `salami_timeline`, `salami_sections`, `salami_chords`, `tempo_bpm`, or `estimated_bpm`.
- Rollback is possible for each file by replacing the current file with its corresponding backup copy.

## Per-File Audit

### `AEROSMITH - LAST_CHILD.md`

- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_batch2_2026-05-01/AEROSMITH - LAST_CHILD.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- `salami_duplicate_policy` added: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 114
salami_filename: "salami_1117.txt"
salami_match_type: "duplicate_salami_versions_canonicalized"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
salami_duplicate_policy: "identical_chord_signature_lowest_id"
```

### `ANNE_MURRAY - DAYDREAM_BELIEVER.md`

- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_batch2_2026-05-01/ANNE_MURRAY - DAYDREAM_BELIEVER.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- `salami_duplicate_policy` added: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 567
salami_filename: "salami_0330.txt"
salami_match_type: "duplicate_salami_versions_canonicalized"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
salami_duplicate_policy: "identical_chord_signature_lowest_id"
```

### `BB_KING - THE_THRILL_IS_GONE.md`

- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_batch2_2026-05-01/BB_KING - THE_THRILL_IS_GONE.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- `salami_duplicate_policy` added: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 227
salami_filename: "salami_0437.txt"
salami_match_type: "duplicate_salami_versions_canonicalized"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
salami_duplicate_policy: "identical_chord_signature_lowest_id"
```

### `BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.md`

- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_batch2_2026-05-01/BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- `salami_duplicate_policy` added: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 98
salami_filename: "salami_0625.txt"
salami_match_type: "duplicate_salami_versions_canonicalized"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
salami_duplicate_policy: "identical_chord_signature_lowest_id"
```

### `BILL_WITHERS - AINT_NO_SUNSHINE.md`

- Backup file: `VALIDATION_REPORTS/backups/repertoire_salami_writeback_batch2_2026-05-01/BILL_WITHERS - AINT_NO_SUNSHINE.pre-salami-writeback.md`
- Backup exists: Yes
- Current frontmatter valid: Yes
- `salami_duplicate_policy` added: Yes
- Non-frontmatter content changed: No
- Blocked fields appear: No
- Rollback possible: Yes

Exact lines added:

```yaml
salami_coverage: true
salami_song_id: 580
salami_filename: "salami_0640.txt"
salami_match_type: "duplicate_salami_versions_canonicalized"
salami_match_score: 1.000
salami_last_checked: "2026-05-01"
salami_duplicate_policy: "identical_chord_signature_lowest_id"
```

## Recommendation

Batch 2 passes the same audit standard as batch 1 and additionally verifies the duplicate-policy metadata path. Do not scale further until these ten CTSF diffs and both audit reports are accepted.
