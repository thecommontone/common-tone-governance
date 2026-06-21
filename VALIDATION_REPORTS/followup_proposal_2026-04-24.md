---
report: CTSF Rescue — Follow-up Proposal
generated: 2026-04-24T06:55:00Z
status: awaiting approval
---

# CTSF Rescue — Follow-up Proposal

Two follow-ups were flagged in the 2026-04-24 rescue delta report. I looked at the underlying data before proposing solutions. Here's what I found and what I recommend.

---

## Follow-up #1 — The 164-file review queue

### What's actually in there (full breakdown)

| Category | Files | What they actually are |
|---|---:|---|
| `EXTRACTED_*` files | 123 | Content extracted from other sources (articles, videos), dated 20260331 or 20260408. **Not songs.** |
| Single-artist-name files | 13 | `Barrie Manilow.md`, `Bon Jovi.md`, `Britney Spears.md` — artist-profile placeholders with bad Spotify auto-enrichment. |
| Essay / analysis notes | 9 | `Song Analysis of Avicii's Wake Me Up.md`, `Analysis of Nirvana Songs Part 1.md` — these are prose essays. |
| Miscellaneous "other" | 14 | Mix of real songs with odd filenames (`Ferry Across the MerseyGerry and the Pacemakers.md`), analysis notes (`Love on Top Modulations.md`), and misfiles. |
| Leading-dash stubs | 2 | `- Koko.md`, `- Song Name.md` — placeholder files. |
| Master lists / indexes | 2 | `MASTER LISTENING LIST.md`, `_INDEX.md`. |
| **Headline** | **163**¹ | 147 are clearly not songs; 16 need human eyes. |

¹ Off-by-one from 164 because of my categorizer regex; doesn't change the shape.

### Recommendation — "route, don't delete"

These files contain real content (extracted research, analysis, artist profiles). Deleting them would lose information. I propose routing them to appropriate folders so REPERTOIRE contains only song entries:

**Step 1 — Auto-routable (147 files, run a script):**

| Source | Destination | Count |
|---|---|---:|
| `EXTRACTED_*.md` | `02_SOURCE_MATERIAL/RESEARCH_NOTES/extracted/` | 123 |
| `Song Analysis of *.md`, `Analysis of *.md` | `02_SOURCE_MATERIAL/RESEARCH_NOTES/song_analyses/` | 9 |
| `Barrie Manilow.md`, `Bon Jovi.md`, … (single-name) | `05_REFERENCE/ARTISTS/` (create if absent) | 13 |
| `MASTER LISTENING LIST.md` | `03_MANUSCRIPT/_WORKING_NOTES/` | 1 |
| `_INDEX.md`, `- Koko.md`, `- Song Name.md` | delete (true empty/utility stubs — verify before) | 3² |

² I'll show you the content of these 3 before any deletion.

**Step 2 — Human-judgment (16 "other" + flagged misc):** I'll generate a one-screen triage list with preview + proposed target, and you pick for each.

### Estimated work: ~15 minutes once you approve the mapping.

---

## Follow-up #2 — The 152 "other failed" files

### Root causes (this was the surprise)

| Rule | Files | What's actually wrong |
|---|---:|---|
| **R08** (filename §1.1) | **133** | **Validator bug.** These are the `_2`/`_3` collision-disambiguated files (e.g., `AEROSMITH - CRYIN_2.md`). The spec EXPLICITLY ALLOWS `_N` suffixes (§1.1: "Disambiguation suffix: If two songs share an identical filename, append `_2`, `_3`, etc."). The validator's §1.1 check doesn't recognize the suffix. |
| R14 (form→Timeline) | 12 | Form array references sections like `chorus-out`, `bridge`, `verse` that aren't present as Timeline headers. Spec §172 specifically names `chorus-out` as a valid form value. Some of these files are genuinely missing Timeline content; others may be validator bugs. |
| R05 (♭/♯ not b/#) | 8 | Real data issue. Timeline uses ASCII `b`/`#` in Roman numerals (e.g., `bVII`). Mechanical fix: replace with `♭VII`, etc. |
| R_BODY (sections missing) | 7 | Files missing `Theoretical Notes` and/or `Connections` sections. Mechanical fix: append stubs. |
| R04 (mode validity) | 2 | **Validator bug + spec drift.** The spec uses `aeolian` in its own examples (lines 91, 105, 277, 700, 731). The validator's `VALID_MODES` set is missing `aeolian` (and `ionian`). |
| R16 (mode-change sep) | 1 | `JEROME_KERN - ALL_THE_THINGS_YOU_ARE.md` has `(key: I — Ab major)` instead of lowercase mode. Single-file fix. |

### Recommendation

**Fix order (easiest → hardest):**

**1. Validator bugs (135 "failures" cleared for free, zero file changes)**

Two small edits to `ctsf_validator.py`:

a. **R08 — accept `_N` disambiguation suffix.** Change the §1.1 filename check to strip a trailing `_N` before comparing. ~5 lines of code. Clears 133 spurious failures.

b. **R04 — align `VALID_MODES` with the spec.** Add `aeolian` and `ionian`. ~1 line. Clears 2 failures. Per the spec these are already first-class mode names.

**2. Mechanical data fixes (16 files, script-able)**

a. **R05 (8 files):** Write `fix_ascii_accidentals.py` that scans Timeline sections for `bII`/`bIII`/`#IV` etc. and replaces the ASCII `b`/`#` with `♭`/`♯`. Dry-run first, review diff, then commit.

b. **R_BODY (7 files):** Append missing `## Theoretical Notes` and `## Connections` stub sections using the same `TBD — awaiting enrichment` skeletons the migrator uses. Trivial append.

c. **R16 (1 file):** Hand-fix `JEROME_KERN - ALL_THE_THINGS_YOU_ARE.md` — takes 30 seconds.

**3. R14 investigation (12 files)**

These need per-file inspection because the failure is semantic (does the form actually reference a missing Timeline section?) rather than cosmetic. For each:

1. Read the `form` array.
2. Check if the Timeline has headers for each form value (suffix-stripped per spec §172).
3. If Timeline really is missing content: the file is skeleton-quality and this isn't a rule failure so much as a content-completeness gap — which is already tracked by the `Skeleton` bucket. Consider downgrading R14 from Required to Recommended for files in skeleton state.
4. If Timeline IS present but validator is wrong: fix validator.

I'll classify all 12 after you approve and report the split.

### Projected post-fix validator state

If we do fixes 1 + 2 (ignore R14 for now):

| Bucket | Current | After fixes |
|---|---:|---:|
| Enriched | 16 | 16 |
| Skeleton | 6,034 | 6,169 (+ 135 recovered spec-compliant) |
| Failed | 316 | 28 (164 review-queue moved out + 124 validator/mechanical fixes) |

### Estimated work
- Validator fixes: 10 minutes of code, 5 of testing.
- Mechanical fixes: 15 minutes for the fixer script + review.
- R14 classification: 30 minutes per-file walkthrough.

---

## What I need from you

**Three decisions:**

1. **On follow-up #1:** OK to run the auto-routing (123 EXTRACTED_* + 9 analyses + 13 artist-name + 1 listening list = 146 files moved)? I'll show you the 3 proposed deletions and the 16 "other" triage items before touching anything.
2. **On validator fixes:** OK to update `ctsf_validator.py` to accept `_N` suffixes in R08 and add `aeolian`/`ionian` to R04's valid-mode set?
3. **On mechanical data fixes:** OK to build `fix_ascii_accidentals.py` and `append_missing_sections.py` as sibling scripts in `_SYSTEM/scripts/`? Both would default to dry-run like the migrator.

If you say "yes to all three and go," the 316-file failure count becomes ~28 real pedagogical TODOs, and we can circle back to the remaining R14 cluster on a subsequent pass.
