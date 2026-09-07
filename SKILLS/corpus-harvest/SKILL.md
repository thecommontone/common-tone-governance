---
name: corpus-harvest
description: >
  Turn any transcript-bearing source (a YouTube channel, or a local folder of
  transcripts) into fully credited research extractions staged for The Common
  Tone vault. A supervised, resumable workflow: any assistant (Claude/Cowork or
  Codex) continues it mechanically from STATE.json across sessions, but no
  session launches itself, and the workflow always stops at Doug's two approval
  gates. Trigger when Doug says: "harvest [channel/folder]", "run corpus-harvest
  on [source]", "start a harvest program", "resume the [source] harvest", or
  supplies a source URL / transcript folder for extraction into the vault.
metadata:
  version: 0.3.0-build
  status: constructed_not_installed
  plan: 00_WORKSHOP/CORPUS_HARVEST_SKILL_PLAN_2026-08-25.md (v0.3, ratified)
  amendments: "0.2.0: Doug-authorized model-routing/budget policy (2026-08-28). 0.2.1: P0 fixes — state lock, installer containment, unconditional load policy, completion gates (2026-08-28). 0.2.2: round-4 fixes — symlink-safe validated lock, all writers serialize on state_lock, blocking anomalies actually block with recorded resolutions, audits bound to run watermark + artifact digest, lstat drift detection, concrete model identifiers (2026-08-28). 0.2.3: round-5 audit-integrity fixes — audits refuse an empty population; audit digest rehashes current file bytes at audit AND completion, refusing missing/changed/escaped artifacts (2026-08-28). 0.3.0: model inputs are hash-bound at launch; survey and extraction calibration rubrics are separate and machine-scored (2026-09-05)"
---

# corpus-harvest

**The anchor (ratified by Doug, 2026-08-25):** one reusable skill that turns any
transcript-bearing source into fully credited research extractions staged for
The Common Tone vault. Doug supplies a source URL or local transcript folder,
ratifies one proposed directive set, sessions run the pipeline to
staged-and-validated candidate files, and Doug's rulings send them through the
canonical Ingestion Gate (`music-file-intake`).

This skill is **assistant-agnostic**: markdown + plain Python (stdlib only) +
file state. Parallel agents are an optimization, not a requirement.

## Where things live

- **Staging (all of Stages 0–4):** `__MY_BOOK/_CT_RESEARCH_INTAKE/<source_slug>/`
  — `RAW/ SEGMENTS/ TXT/ MANIFEST.csv CHUNKS.csv STATE.json PROGRESS.md
  RUNBOOK.md EXTRACTIONS/`. Nothing under this skill's control ever writes
  `INBOUND_QUARANTINE/` — that folder belongs to `music-file-intake` alone.
- **State:** `STATE.json` is the machine authority (schema:
  `references/STATE.schema.json`). `PROGRESS.md` is generated from it
  (`state.py render`) — never hand-ticked. Single-writer atomic updates; a
  schema-version mismatch is flagged to Doug, never silently migrated.
- **Schemas:** `references/` — STATE, MANIFEST, SEGMENTS, extraction records,
  acquisition receipts, candidate frontmatter.
- **Integrity:** `CHECKSUMS.txt` — verify an installed copy with
  `shasum -a 256 -c CHECKSUMS.txt` (report mismatches; never overwrite).

## The pipeline (6 stages, 2 gates)

Every session: read vault `CLAUDE.md` + `PLAIN_SIGHT_COMPACT.md`, then the
program's `RUNBOOK.md`, then `state.py show --root <staging>` and resume from
the first incomplete stage. Record every run in STATE.json; regenerate
PROGRESS.md; stop at clean chunk boundaries.

**Stage 0 — Acquire.** New program: `scaffold.py` creates the staging tree
(guards refuse forbidden paths and non-empty targets). Then the adapter:
`acquire_youtube.sh <staging> <url>` (strict URL allowlist, capability-based
execution, no raw URL interpolation, dependency/disk checks, acquisition
receipts with hashes) — or, for `local-folder`, Doug's files are **copied**
into `RAW/` (originals untouched) and receipts written the same way.

**Stage 1 — Normalize.** `normalize.py --root <staging>`: canonical-file
selection per adapter; timestamped `SEGMENTS/*.jsonl` sidecars; flowing
`TXT/*.txt`; `MANIFEST.csv` with quality grades (`verbatim/asr/mixed/corrupt`)
and grade provenance; corrupt/doubled/misgraded items become STATE anomalies.
Idempotent — safe to rerun. Report the MEASURED corpus facts.

**GATE 1 — Directive authoring (Doug ratifies).** Propose a directive set +
routing proposal + credit conventions using `assets/DIRECTIVE_PROPOSAL_TEMPLATE.md`.
Inputs: a stratified corpus sample, `01_SPECS/CHAPTER_MAP.md`, a bounded
Lodestone claim/gap index, the Research QUEUE/STATUS, and
`library/DIRECTIVE_LIBRARY.md` (seeded from the 12 ratified 12tone directives).
Record the proposal with `state.py gate1-propose --root <staging>
--proposal-file <file>` (the file must live inside staging); when Doug
ratifies, record it with `state.py gate1-ratify --root <staging>
--ratified-by "Doug"` — ratification requires the recorded proposal and
freezes that exact file's hash; there is no path to `ratified` that skips
`proposed`. Nothing past this point runs while the gate is open
(`state.py set-stage` enforces it). **Gate and stage events are recorded only
through the state.py CLI — STATE.json is never hand-edited.**

**Stage 2 — Survey.** `build_chunks.py --root <staging>` (limit from the frozen
chunk policy; re-chunk only via `--rechunk REASON`, recorded). One pass per
chunk under `assets/PREAMBLE_TEMPLATE.md` discipline → `EXTRACTIONS/INDEX/
chunk_NN.md` (A: item/song index; B: directive relevance table). Merge B-rows
into `EXTRACTIONS/TARGETS.csv` (`item_id, directive, note`). Tier calibration
uses the distinct **survey** rubric in `references/CALIBRATION_RUBRICS.md`;
bounded false-positive routing is allowed, but fabrication and miscredit are
fatal.

**Stage 3 — Deep passes.** One directive at a time, in the ratified priority
order. `parse_targets.py --root <staging> --directive DNN` builds the chunk
map (fails closed on unknown items). One pass per chunk → `EXTRACTIONS/DNN/
chunk_NN.md` **plus** extraction records appended to `EXTRACTIONS/DNN/
records.jsonl` (schema: `references/EXTRACTION_RECORD.schema.json` —
`generated_by_ai: true`; `relation` = quotation/paraphrase/synthesis;
`claim_type: creator_claimed_coinage` for claimed coinages, never global
originality). Tier calibration uses the stricter **extraction** rubric in
`references/CALIBRATION_RUBRICS.md`: zero misroutes and exact quotation
fidelity. **Split merges:** one agent writing a ~30k-word merge hits
output caps and returns nothing (proven in the 12tone program) — merge by
family or section-set.

**Stage 4 — Merge + validate.** Assemble candidate markdown files (frontmatter:
`references/CANDIDATE_FRONTMATTER_SPEC.md`, `rights_status: needs_review`)
plus a routing PROPOSAL — all inside staging. Run
`validate_citations.py --root <staging> --records <records.jsonl>`: every
verbatim quote is matched into SEGMENTS through the **shared prose normalizer**
(`03_ENGINES_AND_TOOLS/web-projection/merge_report.py::norm` — P4, fail-closed:
ambiguous/absent quotes are flagged, never auto-resolved; ASR-origin quotes
stay `approximate` and are barred from print-candidate status).

**GATE 2 — Doug's rulings.** Present candidates + routing proposal + open
anomalies. Record each ruling as Doug gives it: `state.py gate2-rule --root
<staging> --file <candidate.md> --ruling approved|approved_with_edits|rejected|
deferred [--destination …] [--credit-notes …]` (the file's hash is pinned at
ruling time); then `state.py gate2-disposition --root <staging> --disposition
retain|relocate_proposed|deletion_proposed` for the staging folder (deletion
only ever by proposal, Hard Rail #8); then `state.py gate2-close`.

**Stage 5 — Canonical intake.** In order: (1) `state.py verify-intake --root
<staging> --skill-roots <roots>` — if `music-file-intake` is unavailable,
**stop with a handoff; never imitate the Gate.** (2) `state.py
build-allowlist --root <staging>` — derives the allowlist EXACTLY from the
Gate-2 approved rulings, re-verifying every hash (a file changed since its
ruling refuses and must be re-presented). (3) `state.py set-stage --stage
s5_canonical_intake --status in_progress` — enforcement re-checks Markdown-ness,
64-hex digests, staging containment, actual hashes, and exact correspondence
with the rulings. (4) Invoke `music-file-intake` with that allowlist — never a
folder. The Gate creates and manages its own quarantine entries; this skill
only hands over the list.

## Model routing & budget (binding — added by Doug's amendment, 2026-08-28)

Model choice is POLICY, enforced **within the corpus-harvest state
protocol** — state.py refuses non-compliant operations; it cannot prevent an
assistant from launching agents outside the lifecycle, so doing so is a
hard-rail violation, and any artifact without a STATE run entry is treated
as an incident. Follow
`references/MODEL_ROUTING_POLICY.md`; models map to tiers only through
`references/MODEL_TIER_MAP.json` (unknown model = refused). Every model run
goes through the state.py lifecycle — never around it:
`model-run-start --scope … --model … --max-tokens … --input-file …`
requires the supervising assistant to enumerate the exact staged files it will
dispatch, atomically hashes them, and reserves the
run's maximum tokens and REFUSES when the scope has no Doug-approved budget,
the model's tier exceeds the budget's `max_tier` (frontier use exists only
where Doug set `max_tier frontier`, plus a recorded escalation reason), four
model runs are already active, or used + reserved + requested would exceed
the ceiling. `model-run-finish` re-hashes the bound inputs and refuses changed
bytes; it also requires nonnegative actual tokens and at least one hashed
output. `model-run-abort` releases the reservation.
The state protocol cannot inspect an external model transport: adding
unrecorded inline prompt text is a hard-rail violation. Render the complete
prompt bundle to staging where possible, bind it, and dispatch those bytes.
Budgets are set per SCOPE (`set-budget --scope`): the six stages plus
`gate1_proposal`, `calibration`, `audit`, and `orchestration`. Gate-1
ratification records the numerical audit policy (recall threshold,
attribution threshold, sample fraction); an audit sample below threshold
STOPS the stage. Mechanical stages are scripts and burn zero tokens.
Calibrate tiers once against known 12tone chunks before the first full run.
Use `references/CALIBRATION_RUBRICS.json` through
`scripts/score_calibration.py`; preserve original verdicts, and use held-out
transcripts—not studied fixtures—for any confirmation run.

## Hard rails (restated from CLAUDE.md + the ratified plan)

Never modify `RAW/`. Never write `02_SOURCE_MATERIAL/TEXTBOOK/`. Never delete
(stage proposals instead). Never write `INBOUND_QUARANTINE/`. Doug's theories
(Plagal Paradigm, Stream Leading, The Herald, Graded Closure, …): collect
"candidate evidence for [[X]]" only — never complete a theory. Every quote
carries item title + id + date (+ time range once validated). No session
launches itself; no publication; no git side effects from this skill. P3:
every report states what was checked and what was not.

## Failure discipline

Refuse over guess (P7): ambiguity stops the run and asks Doug; the answer is
recorded in STATE.json, never re-derived. Discovery of a materially larger
problem ends the session with a finding + handoff (P2). A check that fails
unexpectedly gets fixed, not dismissed (P4).
