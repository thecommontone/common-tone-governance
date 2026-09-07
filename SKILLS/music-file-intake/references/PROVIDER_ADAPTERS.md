# Provider adapters

Provider adapters have one authority: resolve the two absolute paths consumed
by the shared core. They cannot select candidates, change Gate-2 rulings, edit
the allowlist, or implement different quarantine behavior.

## Codex

Use the host filesystem and the active project context to resolve:

- the exact `_CT_RESEARCH_INTAKE/<source_slug>/` staging root;
- the Common Tone project root.

Confirm both paths read-only, then invoke `scripts/intake.py`. Do not infer a
source from nearby folders and do not construct an allowlist in the adapter.

## Claude Cowork

Use Cowork's mounted-directory capability to make the staging root and project
root available, then pass their resolved mounted paths to `scripts/intake.py`.
Cowork-specific MCP names and `/sessions/` mount paths belong only in this
adapter layer; they do not enter the core or alter its candidate set.

If either directory is unavailable, stop with a handoff. Do not copy the
staging tree into an ungoverned location to make the dependency appear present.

## Shared result

Both adapters call the same `check` and `transfer` commands. The same bytes and
state must therefore produce the same acceptance or refusal regardless of the
supervising assistant.
