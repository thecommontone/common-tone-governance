# Repertoire / SALAMI Repository Hygiene Report

Generated: 2026-05-01

## Summary

- Nested repo: `/Users/dougsmith/Docs/__MY_BOOK/The_Common_Tone_Project`
- Commit made: Yes
- Commit: `dd1e3dcdfe1e01cec89e8063125025ac3bcbb613`
- Commit message: `Add reviewed SALAMI metadata to pilot repertoire files`
- Files committed: 10
- Commit stat: 10 files changed, 65 insertions

## Files Staged And Committed

- `02_SOURCE_MATERIAL/REPERTOIRE/ABBA - ON_AND_ON_AND_ON.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/AEROSMITH - LAST_CHILD.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - A_LOVE_SONG.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/ANNE_MURRAY - DAYDREAM_BELIEVER.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/BARRY_WHITE - YOURE_THE_FIRST_THE_LAST_MY_EVERYTHING.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/BB_KING - THE_THRILL_IS_GONE.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/BEASTIE_BOYS - BRASS_MONKEY.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/BILL_WITHERS - AINT_NO_SUNSHINE.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/CANNED_HEAT - ON_THE_ROAD_AGAIN.md`
- `02_SOURCE_MATERIAL/REPERTOIRE/THE_BUCKINGHAMS - KIND_OF_A_DRAG.md`

## Diff Verification

Before staging, each of the ten intended files was inspected with `git diff -- <path>`.

After staging, the cached diff was verified with:

```bash
git diff --cached --stat
git diff --cached
git status --short
```

Machine guard result:

- Staged paths: 10
- Added lines: 65
- Removed lines: 0
- Unexpected added lines: none
- Unexpected keys: none
- Blocked fields found: none

Allowed metadata committed:

- `salami_coverage: true`
- `salami_song_id`
- `salami_filename`
- `salami_match_type`
- `salami_match_score`
- `salami_duplicate_policy: "identical_chord_signature_lowest_id"`
- `salami_last_checked`

Blocked fields absent:

- `salami_coverage: false`
- `salami_timeline`
- `salami_sections`
- `salami_chords`
- `tempo_bpm`
- `estimated_bpm`

Only frontmatter metadata was committed. No SALAMI timelines, sections, chords, tempo fields, or musical-content imports were committed.

## Unrelated Files Left Alone

The following nested-repo files were present before the commit and were not staged:

- `05_REFERENCE/CONCEPTS/Harmony/Dominant 7th Chord Family.md`
- `Cowork_log_file.md`
- `VOICE_ARCHIVE/DOUG_LEXICON/opinions.md`
- `VOICE_ARCHIVE/DOUG_LEXICON/pedagogical_moves.md`
- `VOICE_ARCHIVE/DOUG_LEXICON/phrases.md`
- `_PROJECTS/CT-Email/CT-Email-project-cowork-log.md`
- `_PROJECTS/CT-Email/email-activity-log.md`
- `05_REFERENCE/CONCEPTS/Harmony/Dominant Complex.md`
- `VOICE_ARCHIVE/INGESTION_REPORTS/INGESTION_2026-04-30_1941_dominant-complex.md`
- `VOICE_ARCHIVE/META/dominant-complex-recording-as-score.md`
- `VOICE_ARCHIVE/VERBATIM/2026-04-30_1941_dominant-complex.md`

## Post-Commit Status

The ten intended CTSF files are no longer listed as modified in the nested repo. The unrelated files above remain modified or untracked and were intentionally left alone.

## Recommended Next Boring Step

Do not run batch 3 yet. First accept the repository-hygiene report and decide whether to track the outer-project automation/report artifacts, especially `_SYSTEM/scripts/repertoire_salami_crosswalk.py`, the IDEA-012 status file, and the curated audit/manifest reports.
