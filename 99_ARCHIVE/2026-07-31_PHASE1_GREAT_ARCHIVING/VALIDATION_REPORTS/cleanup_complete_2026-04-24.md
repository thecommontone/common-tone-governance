---
report: CTSF Cleanup — Final Delta Report
generated: 2026-04-24T07:02:00Z
tasks_completed: [#19, #20, #21, #22]
---

# CTSF Cleanup — Final Delta Report

## TL;DR

From 316 validation failures to **12** — a 96% reduction. Of the 12 remaining, all are the same validator/table-format-Timeline tension (R14) on legitimate entries that use table-style Timelines instead of `### [section]` headers. Zero real data-quality issues remain.

## Numbers across the day

| Stage | Files in REPERTOIRE | Enriched | Skeleton | Failed |
|---|---:|---:|---:|---:|
| Baseline (pre-v1.0) | 6,364 (backup) | — | — | — |
| After v1.0 migration + orphan cleanup | 6,244 | 16 | 5,919 | 309 |
| After v1.1 rescue migration | 6,366 | 16 | 6,034 | 316 |
| After validator bug fixes (R08, R04) | 6,366 | 16 | 6,167 | 183 |
| After auto-routing 164 non-songs | 6,202 | 23 | — | — |
| After R05 + R_BODY mechanical fixes | 6,204 | 23 | 6,167 | 14 |
| After R16 hand-fix + in-place rescue | 6,206 | 23 | 6,170 | 13 |
| **After final Winchester Cathedral catch** | **6,206** | **23** | **6,171** | **12** |

## What shipped

### Code changes (reusable)

1. **`ctsf_validator.py` fixes.**
   - R08 now accepts `_N` disambiguation suffix per spec §1.1.
   - `VALID_MODES` now includes `aeolian` and `ionian` — the spec uses these in its own examples but the validator's set was out of sync.

2. **`_SYSTEM/scripts/fix_ascii_accidentals.py`** (new).
   - Replaces ASCII `b`/`#` with Unicode `♭`/`♯` in Timeline Roman numerals.
   - Dry-run by default. Scope: only touches substrings matching Roman-numeral boundaries inside Timeline sections — won't corrupt prose or letter-name chord symbols.

3. **`_SYSTEM/scripts/append_missing_sections.py`** (new).
   - Appends missing CTSF Required body sections (Summary, Timeline, Chord Vocabulary, Theoretical Notes, Connections) to files that have frontmatter but lack one or more.
   - Never reorders or rewrites existing content — append-only.
   - Dry-run by default.

4. **`_SYSTEM/scripts/repertoire_auto_router.py`** (new).
   - Moves non-song files out of REPERTOIRE to appropriate homes elsewhere in the vault.
   - Destinations: `EXTRACTED_*` → `05_REFERENCE/EXTRACTED_MDS/`, `Song Analysis of X` → `ESSAYS/`, everything else → `02_SOURCE_MATERIAL/REPERTOIRE_QUARANTINE/`.
   - Dry-run by default. Handles destination collisions by routing to `_collisions/` subfolders.

### Data changes

- **164 non-song files routed out of REPERTOIRE:**
  - 123 `EXTRACTED_*` → `05_REFERENCE/EXTRACTED_MDS/` (existing home, now has 142 files total).
  - 9 `Song Analysis of …` → `ESSAYS/` (existing home, now 12 files).
  - 32 artist-name stubs / misc → `02_SOURCE_MATERIAL/REPERTOIRE_QUARANTINE/` (new folder) — **awaits your triage**.

- **8 files:** ASCII `b`/`#` → Unicode `♭`/`♯` in Timeline sections (36 surgical replacements).

- **7 files:** appended missing `## Theoretical Notes` and `## Connections` stubs.

- **1 file:** hand-edited `JEROME_KERN - ALL_THE_THINGS_YOU_ARE.md` — `(key: I — Ab major)` → `(key: I / major) — Ab as local tonic` for three section headers, to satisfy R16's mode-change separator syntax while preserving the annotation as trailing prose.

- **3 files:** caught by re-running the v1.1 migrator on main REPERTOIRE (picked up `ACKER_BILK - STRANGER_ON_THE_SHORE.md`, `HARVEY_SCHMIDT - TRY_TO_REMEMBER.md`, `THE_NEW_VAUDEVILLE_BAND - WINCHESTER_CATHEDRAL.md` — each had older-schema frontmatter with `title`/`key_note`/`tempo_bpm` and was added to main after the 06:13 backup).

## The 12 remaining failures — all R14, all table-format Timelines

Every remaining failure is the same pattern: files with `form: [intro, verse, chorus, bridge, chorus-out]` in frontmatter whose Timeline is in **table format** rather than `### [section]` header format. Examples:

- `BILL_WITHERS - USE_ME.md`
- `AL_GREEN - I'M STILL IN LOVE WITH YOU.md`
- `CURTIS_MAYFIELD - SUPERFLY.md`
- `EARTH_WIND_AND_FIRE - THATS_THE_WAY_OF_THE_WORLD.md`
- (and 8 more — all in the soul/funk/R&B corpus, suggesting a single early authoring style)

These files contain the form information — it's just in the Timeline's "Section" column rather than as a level-3 header. R14's current implementation only scans for `### [section]` headers, so it can't see the data.

**Recommendation:** extend R14 in a follow-up pass to also check table-format Timelines. That's a validator upgrade, not a file fix. Low priority — these are all otherwise-compliant skeleton entries.

## REPERTOIRE_QUARANTINE — the 32 files needing your eye

The quarantine contains the stubs, artist-name files, and assorted misc the auto-router couldn't confidently place. Many are bad-Spotify-auto-enrichment victims (e.g., `Britney Spears.md` contains a Russian song by Платина). Many are legitimate research notes that might want real homes (e.g., `Single Ladies Analysis.md`, `Pachelbel Stuff.md`, `The Ballad of Brenda and Eddie.md`).

Suggested follow-up (new session): a skill-assisted walk-through of the 32 files — for each, decide delete / keep in quarantine / move to a better home. I'll generate a per-file proposal deck when you're ready.

## Artifacts

Scripts (all in `_SYSTEM/scripts/`):
- `ctsf_migrator.py` (v1.1 — current)
- `ctsf_migrator_v1.0_archived_2026-04-24.py` (v1.0 archive)
- `ctsf_validator.py` (v1.3.1 with today's R08/R04 patches)
- `fix_ascii_accidentals.py` (new)
- `append_missing_sections.py` (new)
- `repertoire_auto_router.py` (new)

Reports:
- `rescue_migration_delta_2026-04-24.md` (v1.0 vs v1.1)
- `followup_proposal_2026-04-24.md` (this session's plan)
- `cleanup_complete_2026-04-24.md` (this report)
- `ctsf_validation_2026-04-24-FINAL.{md,json,csv}` (final validator output)
- `fix_ascii_accidentals_2026-04-24-exec.md`
- `append_missing_sections_2026-04-24-exec.md`
- `repertoire_auto_router_plan_2026-04-24.md` + `_log_2026-04-24.md`
- `ctsf_migration_log_2026-04-24-inplace-cleanup.md`, `…-catch-winchester.md`

Folder changes:
- REPERTOIRE: 6,366 → 6,206 files (164 moved out, 4 added back after re-migration)
- New: `02_SOURCE_MATERIAL/REPERTOIRE_QUARANTINE/` (32 files — your triage queue)
- EXTRACTED_MDS: 19 → 142 files (+123 routed)
- ESSAYS: 3 → 12 files (+9 routed)
