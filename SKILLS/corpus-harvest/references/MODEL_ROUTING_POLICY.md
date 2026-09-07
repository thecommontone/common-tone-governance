# Model routing & budget policy (corpus-harvest)

*Adopted by Doug's amendment authorization, 2026-08-28, after joint
Claude/Codex review. Binding on every supervising assistant. Provider-neutral:
the skill speaks in CAPABILITY TIERS; the mapping table below is the only
provider-specific text and is updated without touching the rest of the skill.*

## Tiers and provider mapping

| Tier | Meaning | Codex | Claude |
|---|---|---|---|
| **none** | deterministic scripts; zero model tokens | Python | Python |
| **economy** | high-volume, well-specified, schema-checked work | Luna | Haiku |
| **balanced** | default production reasoning | Terra | Sonnet |
| **frontier** | hardest judgment, used narrowly and never silently | Sol | Opus |

## Routing table

| Work | Tier | Escalate to next tier when |
|---|---|---|
| Acquisition, normalization, chunking, targeting maps, exact-quote/timestamp validation | **none** | never — these are scripts (`validate_citations.py` already verifies quote presence, ambiguity, and time ranges deterministically) |
| Orchestration + STATE management | balanced | state anomaly or conflicting instructions |
| Stage 2 survey (chunk passes) | cheapest tier independently passing the survey rubric; balanced until selected | low confidence, or audit disagreement |
| D12-style index assembly, mechanical formatting | economy | schema or completeness failure |
| Ordinary Stage 3 deep-pass extraction | cheapest tier independently passing the extraction rubric; balanced until selected | ambiguous meaning, attribution, or evidence |
| Credit/coinage ledger (D11-style), contested attribution history | **frontier**, narrowly | this is the default for the sensitive passage only — not the whole directive run |
| Stage 4 semantic merging | balanced | conflicting interpretations between chunks |
| Gate-1 proposal drafting | balanced | frontier review only for novel/contested directives |
| Independent contextual audit (context-use + credit correctness — NOT quote matching, which is scripted) | economy or balanced | any disagreement triggers frontier adjudication of that item |

## What "enforced" means here (stated plainly)

These controls are enforced **within the corpus-harvest state protocol**:
state.py refuses non-compliant operations for any assistant that runs the
harvest through it — which the SKILL binds every supervising assistant to
do. state.py cannot physically prevent an assistant from launching an agent
outside this lifecycle; that act would violate the skill's hard rails and
Doug's authorization, and leaves no STATE record — an unexplained
extraction artifact with no run entry is itself the audit signal. Likewise,
`approved_by` is a **recorded protocol assertion, not cryptographic proof**:
the protocol requires that only Doug's word be recorded there, and the
record makes any violation inspectable after the fact; it does not make one
impossible.

Input binding has the same explicit protocol boundary. `state.py` proves the
identity and continued integrity of every file named at launch; it cannot
inspect an external provider request and prove that the supervising assistant
sent no extra inline text. The assistant MUST render the complete prompt to a
staging file where possible, enumerate every dispatched file with
`--input-file`, and send exactly those bound bytes. Unrecorded prompt material
is a hard-rail violation and makes the run unauditable.

## Cost controls (binding, enforced within the state protocol by state.py)

Models map to tiers only through `MODEL_TIER_MAP.json`; an unknown model is
refused, never guessed. Every model run passes through the lifecycle
`model-run-start` → `model-run-finish`/`model-run-abort`:

1. **Ceilings, pre-dispatch:** budgets are set per SCOPE (the six stages plus
   `gate1_proposal`, `calibration`, `audit`, `orchestration`) by Doug via
   `set-budget --scope … --ceiling … --max-tier …`. `model-run-start`
   requires one or more repeatable `--input-file` arguments, rejects missing,
   outside-staging, duplicate, non-regular, or symlinked inputs, and records
   each staging-relative path with its current-byte SHA-256 before it
   atomically reserves the run's maximum tokens. It REFUSES when
   used + active reservations + requested would exceed the ceiling — the
   ceiling stops spending *before* dispatch, not after. No ceiling, no launch.
2. **Tier authority is Doug's:** a run's tier (from the map) may not exceed
   the scope budget's `max_tier`. Frontier use exists only where Doug set
   `max_tier frontier`, and additionally requires a recorded escalation
   reason. A launching assistant's reason alone never authorizes frontier.
3. **Concurrency:** at most **4 active model runs** program-wide;
   `model-run-start` refuses a fifth. Work in waves.
4. **Completion honesty:** `model-run-finish` first re-hashes every bound input
   and refuses if any byte changed after launch, then requires nonnegative
   actual token counts and at least one hashed output file;
   `model-run-abort` releases the reservation and records why.
5. **Audit sampling + stop rule:** duplicate-audit **10–15%** of survey and
   deep-pass items for context-use and credit correctness. The numerical
   thresholds (recall, attribution, sample fraction) are REQUIRED at Gate-1
   ratification and recorded in STATE; a sample below threshold STOPS the
   stage and the finding goes to Doug — never quietly re-run.
6. **Reporting:** `budget-status` shows used + reserved vs ceiling and max
   tier per scope, and exits nonzero (logging a blocking anomaly) on any
   excess.

## Calibration before the first full run (required once)

Benchmark economy / balanced / frontier on a few known 12tone chunks —
the completed program's routed extractions are the answer key. Measure
recall, quotation fidelity, targeting quality, and credit discipline. Stage 2
uses the high-recall **survey** rubric; Stage 3 uses the stricter
**extraction** rubric. The exact thresholds live in machine-readable
`CALIBRATION_RUBRICS.json`, are explained in `CALIBRATION_RUBRICS.md`, and are
applied by `scripts/score_calibration.py`. Use **the cheapest tier that meets
the relevant rubric** and record the chosen defaults (with the benchmark
results) in the program's STATE notes. Calibration beats guessing; the
reference corpus makes it nearly free.

Existing verdicts remain historical facts: later diagnostic rescoring never
rewrites them or opens a gate. Any confirmation freezes its rubric before
dispatch and uses held-out transcripts, not fixtures whose errors have already
been studied.

## Preflight (before any live Stage 0)

`yt-dlp` present · **the channel actually serves accessible captions in the
required language** (yt-dlp alone guarantees nothing) · disk space · shared
prose normalizer reachable · `music-file-intake` verified.
