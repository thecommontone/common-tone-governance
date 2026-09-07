# Calibration rubrics

These rubrics answer two different questions. They must not be collapsed into
one generic pass/fail score.

## Survey rubric — Stage 2

The survey is a high-recall routing pass. A small number of false-positive
routes can be removed by the deep pass and audit, but a missed target may never
be read again. A candidate passes when:

- target recall is at least 90%;
- primary-repertoire identification is 100%;
- fabrications are zero;
- attribution errors are zero; and
- misroutes are no more than 10% of evaluated rows.

Quotation fidelity is still measured for diagnostic comparison, but it is not
a survey gate because Stage 2 produces routing candidates, not print-ready
citations.

## Extraction rubric — Stage 3

Extraction creates evidence that may advance toward manuscript use. A
candidate passes when:

- target recall is at least 90%;
- primary-repertoire identification is 100%;
- fabrications are zero;
- attribution errors are zero;
- misroutes are zero; and
- quotation fidelity is 100%.

## Benchmark discipline

`CALIBRATION_RUBRICS.json` is the machine authority and
`scripts/score_calibration.py` is the deterministic scorer. Invalid or empty
populations refuse rather than manufacture a score.

The strict calibration verdicts recorded on 2026-09-05 remain **FAIL**. A
diagnostic rescore under these task-specific rubrics does not rewrite those
results and does not select a production model retroactively.

Any confirmation benchmark must freeze its rubric before dispatch and use
held-out transcripts that were not in the first benchmark. Reusing the same
fixtures after studying their errors is diagnostic only, not independent
confirmation. Every model-run start must bind the exact prompt, transcript,
schema, rubric, and other dispatched files through repeated `--input-file`
arguments so their current-byte hashes live in STATE.json.
