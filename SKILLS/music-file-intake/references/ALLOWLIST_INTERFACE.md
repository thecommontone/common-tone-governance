# Corpus-harvest Stage-5 allowlist interface

Approved by Doug on 2026-08-28 for `music-file-intake 0.1.0-build`.

1. Corpus-harvest passes only the staging-root path and the `stage5_allowlist` already recorded in that staging tree's `STATE.json`, whose complete entry shape is `{ "file": <staging-relative markdown path>, "sha256": <64 lowercase hex characters> }`; it never passes or invites discovery of a folder.
2. The provider-neutral intake core reads that exact state-bound allowlist through one shared interface, while Claude and Codex adapters handle only environment-specific path discovery and capabilities and may not add, remove, or reinterpret candidates.
3. Before any write to `INBOUND_QUARANTINE/`, the core verifies Gate 2 is closed, the allowlist corresponds exactly to approved rulings, every path is contained and names a regular Markdown file, and every current byte hash matches; any mismatch refuses the entire handoff without copying, moving, deleting, or partially ingesting anything.

## Receipt boundary

A successful transfer creates one batch directory under
`02_SOURCE_MATERIAL/INBOUND_QUARANTINE/corpus-harvest/`. Its receipt binds the
source slug, current `STATE.json` hash, every original staging-relative path,
every copied filename, and every file hash. The source tree remains untouched.

The transaction lock coordinates callers using this core. It does not prevent
an unrelated program from writing directly to the filesystem; an unreceipted or
hash-divergent artifact is therefore a protocol incident.
