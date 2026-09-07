---
name: music-file-intake
description: Use when Doug asks to ingest, route, file, extract, or catalog research material for the Common Tone project, including a corpus-harvest Stage-5 allowlist handoff. This skill is the sole Ingestion Gate for material entering the project from the outer vault or an assistant workspace.
---

# Music File Intake

Build identity: `music-file-intake 0.1.0-build` (`constructed_not_installed`)

Turn incoming research into governed Common Tone material without bypassing
Doug's approvals, inventing candidates, or writing textbook prose. This skill is
the single Ingestion Gate; provider adapters resolve paths, but the rules and the
Stage-5 transfer implementation are shared.

## Start here

1. Read the live project `README.md`, `CLAUDE.md`,
   `PLAIN_SIGHT_COMPACT.md`, `00_CONSTITUTION/CONSTITUTION.md`, and the
   relevant Domain Charter. Declare the CONTENT / Pipeline lane.
2. Read the current handoff when mounted. Treat chat history as continuity,
   not current authority.
3. Read `references/PROVIDER_ADAPTERS.md`. Use the relevant adapter only to
   obtain the staging root and project root.
4. Choose the mode below. If the request is ambiguous, inspect read-only and
   present the smallest concrete routing recommendation before any write.

## Hard rails

- Never write to `02_SOURCE_MATERIAL/TEXTBOOK/`.
- Never delete source material. Duplicates and deletions are proposals for Doug.
- Never paraphrase or complete Doug's original theory or voice.
- Outer-vault material enters the project only through this skill.
- A corpus-harvest handoff uses only `STATE.json.stage5_allowlist`; never scan
  the staging folder for additional candidates.
- `approved_by`, `invoked_by`, and similar fields are recorded protocol
  assertions, not cryptographic proof of Doug's identity.
- The scripts enforce rules for cooperating assistants. An out-of-band write is
  not physically prevented; an artifact without a valid receipt is an incident.

## Choose a mode

- **Mode A — route an existing file.** Read
  `references/INTAKE_MODES.md#mode-a--file-routing`.
- **Mode B — extract a source document to Markdown.** Read
  `references/INTAKE_MODES.md#mode-b--document-extraction`.
- **Mode C — process a Consensus research synthesis.** Read
  `references/INTAKE_MODES.md#mode-c--consensus-research-synthesis`.
- **Mode D — accept a corpus-harvest Stage-5 allowlist.** Follow the mechanical
  protocol below. This is the only mode that writes to
  `INBOUND_QUARANTINE/` through the included transfer script.

## Mode D — corpus-harvest Stage 5

Read `references/ALLOWLIST_INTERFACE.md` before running the scripts.

### 1. Obtain paths without choosing candidates

Resolve exactly two inputs:

- `staging_root`: the source's `_CT_RESEARCH_INTAKE/<source_slug>/` tree;
- `vault_root`: the Common Tone project root.

Do not pass a candidate path, a directory to scan, or an edited allowlist.

### 2. Check without writing

From this skill directory:

```bash
python3 scripts/intake.py check \
  --staging-root "/absolute/path/to/staging" \
  --vault-root "/absolute/path/to/The_Common_Tone_Project"
```

The command exits `0` with JSON only when Gate 2 is ruled, Stage 5 is in
progress, the allowlist exactly matches Doug-approved rulings, every path is a
contained non-symlink regular `.md` file, every current hash matches, and no
relevant blocking anomaly is open. It performs no write.

Present the source slug, candidate count, state hash, and batch ID. Treat the
check and transfer as separate gates: do not transfer until Doug explicitly
authorizes the quarantine write.

### 3. Transfer one atomic batch

```bash
python3 scripts/intake.py transfer \
  --staging-root "/absolute/path/to/staging" \
  --vault-root "/absolute/path/to/The_Common_Tone_Project" \
  --invoked-by "<assistant/session assertion>"
```

The core serializes cooperating transfers, validates again under the lock,
copies current bytes into a private transaction directory, writes
`INTAKE_RECEIPT.json`, revalidates, and exposes the batch with one rename. It
never moves or deletes the staging files. Any refusal returns exit `2` and must
leave no partial visible batch.

### 4. Stop at the gate boundary

Report the receipt and exact destination. Do not route files onward, alter the
corpus-harvest state, mark Stage 5 complete, commit, or push unless separately
authorized. Downstream classification is a new intake decision.

## General intake conventions

Read `references/INTAKE_MODES.md` and the live canonical specs before creating
frontmatter or choosing a destination. Chapter identifiers, status values, and
repertoire schemas change over time; never substitute a cached list for the
current project files.

On completion, append the required Cowork log entry and update the one current
handoff when work remains open, but only when those bookkeeping writes are in
the authorized scope.
