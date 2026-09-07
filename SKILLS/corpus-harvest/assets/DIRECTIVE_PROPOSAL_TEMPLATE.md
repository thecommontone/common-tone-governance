---
type: directive_proposal
program: "corpus-harvest: {{source_slug}}"
status: awaiting_doug_ratification
date: "{{date}}"
---

# Gate 1 — Directive proposal: {{source_slug}}

**Anchor restated:** {{anchor_one_sentence}}

*Doug: this is the one ratification the program needs before extraction starts.
Everything below is a proposal; strike, edit, add, and the set freezes on your
word. Per the Plain Sight Compact: plain language, and each directive says
what it feeds.*

## What the corpus sample showed

{{three_to_six_plain_sentences_on_the_sample — measured facts only}}

## Proposed directives (from library/DIRECTIVE_LIBRARY.md + corpus fit)

| # | Directive (one line) | Feeds (chapter/theory/folder) | Why this corpus supports it |
|---|---|---|---|
| D01 | {{...}} | {{...}} | {{...}} |

## Proposed routing

| Directive | Primary destination folder | Split condition |
|---|---|---|
| D01 | {{...}} | {{...}} |

## Proposed credit conventions

- Creator credited as: {{name, the way the book credits Temperley/Schmalfeldt/Belkin}}
- Claimed coinages labeled: `creator_claimed_coinage` (claim, not originality)
- Relayed frameworks credited to their named originators, verbatim from the corpus
- {{source-specific conventions}}

## Priority order if time is short

{{ordered list}}

## Proposed audit policy (numbers Doug ratifies with the set)

- Recall threshold: {{e.g. 0.90 — audit sample must find ≥90% of reference-verifiable targets}}
- Attribution threshold: {{e.g. 0.95 — ≥95% of sampled credits correct}}
- Duplicate-audit sample fraction: {{0.10–0.15}}
- Sample definition: {{how audit items are drawn, e.g. stratified by chunk and grade}}

*(Recorded in STATE.json at gate1-ratify; below-threshold audits STOP the
stage per MODEL_ROUTING_POLICY.md.)*

## What ratification freezes

The directive set (hash recorded in STATE.json), the routing proposal as the
working default (Gate 2 still rules on every file), and the credit conventions.
Adding or rewording a directive later = a new Gate 1.
