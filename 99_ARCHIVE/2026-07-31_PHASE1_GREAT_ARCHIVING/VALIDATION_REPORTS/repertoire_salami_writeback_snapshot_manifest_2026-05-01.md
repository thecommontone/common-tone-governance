# Repertoire / SALAMI Writeback Snapshot Manifest

Generated: 2026-05-01

## Purpose

Preserve the first known-good reviewed-positive SALAMI metadata writeback state without committing backup copies into the repo. The first audit passed and is recorded at:

`VALIDATION_REPORTS/repertoire_salami_writeback_audit_2026-05-01.md`

## Snapshot Table

| CTSF file | Current SHA-256 | Backup file | Backup SHA-256 |
|---|---|---|---|
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - A_LOVE_SONG.md` | `d846e6d3669ce7368b41690c93c8c61ff780579a688318ce3ce676282ac90e1b` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/ANNE_MURRAY - A_LOVE_SONG.pre-salami-writeback.md` | `419d17e3a67c831e00a8d4b64af8d4e94907f720ca0d61005e56e57af79b90c9` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/CANNED_HEAT - ON_THE_ROAD_AGAIN.md` | `e5da8d32b7ac829d45331b9aa05e5fff896fc9822f012adc74ef8ba4ae78bb39` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/CANNED_HEAT - ON_THE_ROAD_AGAIN.pre-salami-writeback.md` | `2d0a4ee987de6fb689a837c2b6ee12d741601b788af048dfb2c092119d424c45` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/THE_BUCKINGHAMS - KIND_OF_A_DRAG.md` | `8a94cec17004c91a0a7bc456ac58047970af15aa0a2ad9ecd9d84eab3bf9e50a` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/THE_BUCKINGHAMS - KIND_OF_A_DRAG.pre-salami-writeback.md` | `50ce54112fcab7ac86bf9f95272643efa79e9d48b0df7e95d67c40bb4a0c1404` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/ABBA - ON_AND_ON_AND_ON.md` | `3560f1327feb6296446ee814e7a411ee7670e12b9ddf9c7a6e9c5507f898b769` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/ABBA - ON_AND_ON_AND_ON.pre-salami-writeback.md` | `0bc25407f091b54fcb6d10d3a0e6c4f2342da4240c4ded23ab6f1ee009ccd13a` |
| `The_Common_Tone_Project/02_SOURCE_MATERIAL/REPERTOIRE/BEASTIE_BOYS - BRASS_MONKEY.md` | `39faf15492c8b327e35e95565f2242c2ec9a65acd78bb9919a0045a2937c9a6c` | `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/BEASTIE_BOYS - BRASS_MONKEY.pre-salami-writeback.md` | `534dcb254b634853e33fc10e14bfc1131d5410d272f39e6a6d5ecad3bd53d38a` |

## Rollback Instruction

To roll back one file, replace the current CTSF file with its corresponding backup file from `VALIDATION_REPORTS/backups/repertoire_salami_writeback_test_2026-05-01/`.

Do not roll back by hand-editing individual lines unless the current file has changed again after this snapshot. If it has changed again, compare current, backup, and this manifest before replacing anything.

## Commit Recommendation

- Do not commit backup copies by default.
- Commit the five CTSF metadata changes in the nested `The_Common_Tone_Project` repo only after accepting the audit.
- Add `_SYSTEM/scripts/repertoire_salami_crosswalk.py` to tracking in the outer project if this script is now a maintained automation tool.
- Keep this manifest and the audit report as the lightweight preservation layer for the first known-good writeback state.
