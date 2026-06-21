# Repertoire / SALAMI Reviewed-Positive Writeback Test

Generated: 2026-05-01

## Command

```bash
python3 _SYSTEM/scripts/repertoire_salami_crosswalk.py --writeback-reviewed-positive --limit 5 --backup --execute-writeback
```

## Summary

- Mode: actual writeback
- Reviewed-positive rows in allow-list: 18
- Files considered under limit: 5
- Files changed: 5
- Files that would change: 0
- Rows skipped: 0
- CSV companion: `VALIDATION_REPORTS/repertoire_salami_writeback_test_2026-05-01_actual.csv`

## Changed / Would Change Files

| Action | CTSF file | SALAMI | Fields added | Backup |
|---|---|---|---|---|
| `changed` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - A_LOVE_SONG.md` | `532` / `salami_0078.txt` | `salami_coverage: true`<br>`salami_song_id: 532`<br>`salami_filename: "salami_0078.txt"`<br>`salami_match_type: "exact_artist_title"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/ANNE_MURRAY - A_LOVE_SONG.pre-salami-writeback.md` |
| `changed` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/CANNED_HEAT - ON_THE_ROAD_AGAIN.md` | `845` / `salami_0501.txt` | `salami_coverage: true`<br>`salami_song_id: 845`<br>`salami_filename: "salami_0501.txt"`<br>`salami_match_type: "exact_artist_title"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/CANNED_HEAT - ON_THE_ROAD_AGAIN.pre-salami-writeback.md` |
| `changed` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/THE_BUCKINGHAMS - KIND_OF_A_DRAG.md` | `831` / `salami_0299.txt` | `salami_coverage: true`<br>`salami_song_id: 831`<br>`salami_filename: "salami_0299.txt"`<br>`salami_match_type: "exact_artist_title"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/THE_BUCKINGHAMS - KIND_OF_A_DRAG.pre-salami-writeback.md` |
| `changed` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - ON_AND_ON_AND_ON.md` | `885` / `salami_0463.txt` | `salami_coverage: true`<br>`salami_song_id: 885`<br>`salami_filename: "salami_0463.txt"`<br>`salami_match_type: "exact_artist_title"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/ABBA - ON_AND_ON_AND_ON.pre-salami-writeback.md` |
| `changed` | `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BEASTIE_BOYS - BRASS_MONKEY.md` | `149` / `salami_0432.txt` | `salami_coverage: true`<br>`salami_song_id: 149`<br>`salami_filename: "salami_0432.txt"`<br>`salami_match_type: "exact_artist_title"`<br>`salami_match_score: 1.000`<br>`salami_last_checked: "2026-05-01"` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/BEASTIE_BOYS - BRASS_MONKEY.pre-salami-writeback.md` |

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
