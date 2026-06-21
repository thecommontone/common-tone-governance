# Repertoire / SALAMI Reviewed-Positive Writeback Test

Generated: 2026-05-01

## Command

```bash
python3 _SYSTEM/scripts/repertoire_salami_crosswalk.py --writeback-reviewed-positive --reviewed-positive-offset 10 --limit 5 --dry-run --backup --report-stem repertoire_salami_writeback_batch2_2026-05-01
```

## Summary

- Mode: dry-run
- Reviewed-positive rows in allow-list: 18
- Reviewed-positive rows skipped by offset: 10
- Files considered under limit: 5
- Files changed: 0
- Files that would change: 5
- Rows skipped: 0
- CSV companion: `VALIDATION_REPORTS/repertoire_salami_writeback_batch2_2026-05-01_dry_run.csv`

## Changed / Would Change Files

| Action | CTSF file | SALAMI | Fields added | Backup |
|---|---|---|---|---|
| `would_change` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/AEROSMITH - LAST_CHILD.md` | `114` / `salami_1117.txt` | `salami_coverage: true`<br>`salami_song_id: 114`<br>`salami_filename: "salami_1117.txt"`<br>`salami_match_type: "duplicate_salami_versions_canonicalized"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"`<br>`salami_duplicate_policy: "identical_chord_signature_lowest_id"` | - |
| `would_change` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - DAYDREAM_BELIEVER.md` | `567` / `salami_0330.txt` | `salami_coverage: true`<br>`salami_song_id: 567`<br>`salami_filename: "salami_0330.txt"`<br>`salami_match_type: "duplicate_salami_versions_canonicalized"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"`<br>`salami_duplicate_policy: "identical_chord_signature_lowest_id"` | - |
| `would_change` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BB_KING - THE_THRILL_IS_GONE.md` | `227` / `salami_0437.txt` | `salami_coverage: true`<br>`salami_song_id: 227`<br>`salami_filename: "salami_0437.txt"`<br>`salami_match_type: "duplicate_salami_versions_canonicalized"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"`<br>`salami_duplicate_policy: "identical_chord_signature_lowest_id"` | - |
| `would_change` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.md` | `98` / `salami_0625.txt` | `salami_coverage: true`<br>`salami_song_id: 98`<br>`salami_filename: "salami_0625.txt"`<br>`salami_match_type: "duplicate_salami_versions_canonicalized"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"`<br>`salami_duplicate_policy: "identical_chord_signature_lowest_id"` | - |
| `would_change` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BILL_WITHERS - AINT_NO_SUNSHINE.md` | `580` / `salami_0640.txt` | `salami_coverage: true`<br>`salami_song_id: 580`<br>`salami_filename: "salami_0640.txt"`<br>`salami_match_type: "duplicate_salami_versions_canonicalized"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"`<br>`salami_duplicate_policy: "identical_chord_signature_lowest_id"` | - |

## Skipped Rows

| CTSF / Row | Reason |
|---|---|
| - | None |

## Warnings

| CTSF file | Warning |
|---|---|
| - | None |

## Safety Notes

- No negative coverage fields are written.
- No SALAMI timeline, section, chord, tempo, or musical content fields are written.
- Writeback is limited to reviewed-positive rows from the pilot review file.
- Actual writeback requires `--backup` and `--execute-writeback`.

## Recommended Next Step

Inspect the changed files and backups. If clean, keep the next run capped and boring: either another reviewed-positive batch of 5 or a dedicated import-preview report for one timeline candidate.
