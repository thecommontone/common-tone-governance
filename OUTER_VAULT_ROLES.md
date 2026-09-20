---
type: vault_policy
scope: OUTER_VAULT
vault_root: /Users/dougsmith/Docs/__MY_BOOK/
created: 2026-04-20
author: Doug Smith (via Claude consultation)
grounded_in:
 - ADMIN/STRATEGIC_PLANS/ORG_CONSULTATION_2026-04-20.md (framework)
 - VAULT_MAPS/vault_map_2026-04-18.md (folder inventory)
status: canonical
analog_of: The_Common_Tone_Project/00_CONSTITUTION/CONSTITUTION.md
motto: "Every folder has one role. Every new file has one home."
location_note: "Moved from outer root to GOVERNANCE/ on 2026-05-07 as part of four-bucket reorganization."
---

# OUTER VAULT ROLES

**What this document is.** The canonical policy that classifies every top-level folder in `/Users/dougsmith/Docs/__MY_BOOK/`. It is the outer-vault analog of `The_Common_Tone_Project/00_CONSTITUTION/CONSTITUTION.md` — the document that tells a human (or an AI assistant) where anything belongs, why it is outside the inner sanctum, and what the promotion rule is for moving inward.

**Where this file lives.** `GOVERNANCE/OUTER_VAULT_ROLES.md` — moved here 2026-05-07 during the four-bucket reorganization. The root-level `OUTER_VAULT_ROLES.md` no longer exists.

**What this document is not.** It is not a map. This file is *policy*. The cartographer-generated snapshots in `GOVERNANCE/VAULT_MAPS/` were the observation half, but the skill that made them was retired 2026-07-31 and they are now historical.

---

## The Two Framing Principles (read these first)

Both apply to every decision below.

**Principle 1 — The inner sanctum is a Compile Target.** `The_Common_Tone_Project/` is not storage. It is the engine that compiles the book, the courses, the website, the databases, and the public-facing work. Every file inside it serves one of three purposes: source material the engine consumes, governance the engine obeys, or a build artifact the engine produces. Material that does not serve one of these three purposes belongs in the outer vault.

**Principle 2 — Markdown is the lingua franca of the vault's prose and governance layer.** The inner sanctum's automation runs cleanly because chapter prose, REPERTOIRE entries, domain charters, specs, and concept files are all `.md`. When material is *promoted* into the sanctum, it is *converted* — distilled to Markdown at the gate. Binary originals (PDFs, audio, datasets, images) are allowed in the sanctum only in their defined housing folders.

---

## Outer Vault Structure — The Big Picture

The outer vault is organized in two layers:

**Layer 1 — The Four Buckets** (created 2026-05-07): four top-level folders that group related outer-vault material by purpose.

```
CT_BUSINESS/     Business operation of The Common Tone brand
DEVELOPMENT/     Active development, incubator, projects, ideas
GOVERNANCE/      Vault infrastructure, maps, renders, this file
EDUCATION/      teaching materials
```

**Layer 2 — Root-level folders** (ungrouped): folders that live directly at `__MY_BOOK/` root because they are too large to move, are permanently adjacent works, are live feeder pipelines with hardcoded paths, or are the inner sanctum itself.

---

## The Four Buckets

### CT_BUSINESS/ — Common Tone Business Operation

The operational business layer of The Common Tone brand. Anything that would live in a business folder if Common Tone were a small company: registration, banking, taxes, contracts, licences, branding, and brand-voice assets.

- `CT_BUSINESS/BUSINESS/` — `01_REGISTRATION`, `02_BANKING`, `03_SUBSCRIPTIONS`, `04_TAXES`, `05_VENDORS_AND_CONTRACTS`, `06_LICENCES`, `07_REFERENCE_DOCS`, `BUSINESS_USE_DECLARATIONS.md`, `MASTER_LEDGER.md`.
- `CT_BUSINESS/GRFX/` — Logo concepts (4 PNGs), style guide board, SVG exercises, HTML infographic. Brand visual assets.

**Rule.** No automation ingests from here into the Machine without explicit human instruction.

---

### DEVELOPMENT/ — Active Development, Incubator, Projects

In-progress development efforts: code, interactive tools, platform architecture, creative ideas, and operational CT-prefixed projects. These build or incubate outside the sanctum and migrate in only when proven.

- `DEVELOPMENT/_DEV_INCUBATOR/` — The canonical four-stage incubator (Pitch → Build → Prove → Promote). Contains `SALAMI_PROJECT/` (1,242 songs, 126,272 chords in `salami_db.sqlite`; `salami_explorer.py` Flask app at localhost:8765). Run with `cd.../DEVELOPMENT/_DEV_INCUBATOR/SALAMI_PROJECT && python3 salami_explorer.py`.
- `DEVELOPMENT/IDEA_LAB/` — the **project** incubator, folder-per-idea (23 folders as of 2026-09-07). Ideas themselves live in `The_Common_Tone_Project/IDEA_LEDGER.md`; an idea that graduates gets a folder here. *(The startup obligation to check for `peer-review` items is in `CLAUDE.md` §1 step 6 — not restated here.)*
- `DEVELOPMENT/PROJECTS/` — Operational CT-prefixed projects: `CT-Control-Center`, `CT-Email`, `CT-Infrastructure`, `CT-Intake`, `CT-Interactive`, `CT-Substack`, `CT-Textbook`, `CT-Vault`, `COMPOSER_FIELD_GUIDES/`, `PROJECT_SETUP_GUIDE.md`.
- `DEVELOPMENT/CT_DIMENSIONS/` — Platform architecture planning docs. Working drafts; not yet operational.
- `DEVELOPMENT/Excalidraw/` — Single working diagram (Apr 27).
- `DEVELOPMENT/NOTATION & XML/` — 97 MusicXML/MXL files (scales, grooves, instructional phrases). Role 2b Dev Incubator — notation tooling exploration.

**The key test:** *"Is this building something for the book, courses, or public surface?"* If yes but not yet operational → it lives here.

---

### GOVERNANCE/ — Vault Infrastructure and Operations

Items that describe, validate, or operate the vault. Not content — they *are* the classification system, the validation surface, and the render target.

- `GOVERNANCE/OUTER_VAULT_ROLES.md` — this file.
- `GOVERNANCE/VAULT_MAPS/` — Cartographer snapshots + `CURRENT_MAP.md` pointer. **Unowned since 2026-07-31**, when the `vault-cartographer` skill was retired; the snapshots are historical and nothing regenerates them. A second `CURRENT_MAP.md` exists at `ADMIN/VAULT_MAPS/`; neither is being maintained.
- `GOVERNANCE/RENDERS/` — Binary render artifact parking lot. **Canonical render target path: `/Users/dougsmith/Docs/__MY_BOOK/GOVERNANCE/RENDERS/`** (updated 2026-05-07; was `__MY_BOOK/RENDERS/`). Contents are frozen build artifacts — canonical `.md` source lives inside the sanctum. Sub-folders: `BrandBrief/`, `PlagalParadigm/`, field guide renders. Do not edit files here; do not promote them back inward.
- *(There is no `GOVERNANCE/VALIDATION_REPORTS/`. Validation output lives at `The_Common_Tone_Project/VALIDATION_REPORTS/`; audit output at `ADMIN/AUDITS/`. Corrected 2026-09-07.)*
- `GOVERNANCE/SKILLS/` — Operational skill source copies. Four as of 2026-09-07: `burin-notation/`, `composer-instrument-guide/`, `corpus-harvest/`, `music-file-intake/`. Read at runtime by the Cowork skill. *(Most Cowork skills have no source copy here — Doug's Claude account is the registry of record.)*

**Note on `_SYSTEM/`.** The outer vault's `_SYSTEM/` folder lives at `__MY_BOOK/_SYSTEM/` (root, not inside GOVERNANCE/) because `The_Common_Tone_Project/_SYSTEM` is a symlink pointing to `../_SYSTEM`. Moving `_SYSTEM/` into GOVERNANCE/ would require updating that symlink. Policy: `_SYSTEM/` stays at root. It is Governance Layer infrastructure regardless of physical location.

---

### EDUCATION/ — Teaching Materials

Teaching materials produced for or used. Completely separate from the textbook project. Stays outer permanently; never ingested into the Machine.

- `EDUCATION/EDUCATION_FOLDER/` — Core DC teaching materials: exercises, assessments, theory lectures, rudiments, acoustics, `_ADMIN`. Active reference for teaching use.
- `EDUCATION/DC ADMIN HISTORY/` — Historical DC administration: class lists, grades, course outlines, admin, posters, sight-singing, ESL music lecture. Role 4c (455+ days cold).
- `EDUCATION/SYLLABI/` — Old teaching syllabi and PDFs. Role 4c (712+ days cold).

---

## Root-Level Folders (not in any bucket)

### Role 1 — The Machine

- `The_Common_Tone_Project/` — The single member. Nothing else is classified here.

### Role 2a — Research Feeders (active pipeline)

- `_CT_RESEARCH_INTAKE/` — Canonical intake queue. `music-file-intake` routes from here to `02_SOURCE_MATERIAL/`.
- `OTHER_UNINGESTED/` — Residual pile; fold into `_CT_RESEARCH_INTAKE/` at next intake pass.
- `__ARCHIVE_EXAMINATION/` — Working review space for older material.
- `TIER TALK/` — Four voice transcripts awaiting promotion via `music-file-intake` → sanctum `VOICE_NOTES/`.
- `GRFX_STAGING/` — Graphics staging (`EXTRACTED/`, `IN_PROGRESS/`, `READY/`).

### Role 2c — Pending Verification

- `INGESTED/` — Verify: residue (→ 4a) or ready-to-ingest (→ 2a)?
- `WHISPERS_PROJECT/` — Verify: already in sanctum's narrative? If yes → 4a. If partial → 2a.
- `FILEMAKER_DATABASE_PROJECT/` — Verify: still in active use? If yes → 4b. If no → 4c.

### Role 3 — Adjacent (permanently at root)

*(Empty as of the 2026-09-07 re-review: `__MY COMPOSITION BOOK/`, `_MY JAZZ-BOOK/` and `_MY HISTORY BOOK/` are no longer on disk. The role is kept for future adjacent books.)*

**Rule.** No automation ingests from these into the Machine without explicit human instruction.

### Role 4a — Project Archives

- `_ARCHIVE_BOOK_ITERATIONS/` — Historical drafts. Receives moves-in as the project evolves.
- `WORKBOOK/` — Doug's pitch-and-interval workbook exercises: 45 Sibelius files, 11 PDFs, 6 spreadsheets, 2023–24 (3 MB). **Stays where it is** *(reclassified 2026-09-19 on Doug's yes: it was described as an early draft and a fold-in candidate; it is original exercise material, not a superseded draft).*
- `ARCHIVE/` — the outer archive tree (`ARCHIVE/99_ARCHIVE/…`), **read-only** under `CLAUDE.md` rail 3. Never loaded into an active session. *(Reclassified 2026-09-07: it was described as a one-file straggler and a removal candidate; it is neither.)*
- `ADMIN/` — **the real outer-vault governance repository** (its own Git repo). The inner sanctum's `The_Common_Tone_Project/01_ADMIN_AND_POLICY` is a **symlink pointing here** (`01_ADMIN_AND_POLICY →../ADMIN`). *(Corrected 2026-07-01: an earlier note described this relationship backwards, as an APFS hardlink from ADMIN to the inner folder.)* **Do NOT move, rename, or delete** — the inner symlink and every `../ADMIN/...` reference in CLAUDE.md and the canonical-docs registry depend on it. This is an **active** layer, not read-only: handoffs, audits, `PROJECT_STATUS.md` and `DASHBOARD/` write here constantly. *(The `ceo-daily-report` skill was retired 2026-07-31; there is no `CEO_REPORTS/` folder.)*

### Role 4b — Large Reference Corpora (do not move — sizes listed)

- `DATA_FOLDER/` — Song databases, song-analysis sets and downloaded research datasets (3.3 GB). Provenance note: `DATA_FOLDER/README.md` *(written 2026-09-19 from the folder's own evidence; unknowns are marked).*
- `RESOURCES_REFERENCE/` — Album art, historical photos, diagrams (5.5 GB).
- `REPERTOIRE_DOCUMENTED_POP_SONGS/` — Pop repertoire scans and transcriptions (15 GB).
- `EDUCATION/REPERTOIRE_CLASSICAL_THEORY_EXAMPLES/` — Classical repertoire examples (1 GB). *(Path corrected 2026-07-01: lives under `EDUCATION/`, not at root.)*
- `REPERTOIRE_DOUGS_POP_SONGS_FOR_THEORY/` — Doug's pop songs as pedagogical examples (1.1 GB).
- `SIBELIUS_FILES/` — Sibelius-score archive (20 MB).
- `PAGES_DOCS/` — Pages/Word document archive (194 MB).
- `_DOUGS_WRITING_STYLE/` — Reference corpus for brand-voice tooling (187 MB).
- `_DOUGS_VOICE/` — The unified voice database (created 2026-09-17): raw verbatim, lexicon, pedagogy, tangents, staged insertions, and the pontificate/voice-compass skill workflow. A reference database consulted when "Doug's voice" is needed, not a compile target — the three former inner voice folders (VOICE/VOICE_NOTES/VOICE_ARCHIVE) were merged here and retired. The pontificate and voice-compass skills write here. Companion to [[_DOUGS_WRITING_STYLE]].
- `THE_WRITERS_DEN_ARCHIVE/` — Writers' Den reference corpus (264 KB). *(Its `writer-watch` skill was retired 2026-07-31; a `writer-watch-weekly` skill is installed for Claude Code, and whether it is the same tool has not been established. The corpus stands on its own.)*

### Role 4c — Legacy / Dormant

- `SOME INGESTION/` — Old ingest residue, 3 files (742 days cold).
- `GRFX_TEST_FOLDER/` — Graphics sandbox, 11 files (374 days cold).
- `LISTENING_LISTS/` — Curated listening lists (452 days cold).
- `EDUCATION/MUSIC_COLLEGE/` — College-era personal material (452 days cold). *(Path corrected 2026-07-01: lives under `EDUCATION/`, not at root.)*

### Role 2b (dev/incubator) and Role 4 — folders classified in the 2026-09-07 re-review

Twelve outer-root folders were named nowhere in this file. Classified from what each demonstrably
contains, measured 2026-09-07:

| Folder | Role | Note |
|---|---|---|
| `CLAUDE_DESIGN_KIT/` | **Governance Layer** — its own git repo (`common-tone-design-kit`, added 2026-08-10) | 112 files. Design brief, prompts, and the design system Claude works from. Listed in the `PROJECT_STATUS.md` repo table. |
| `CLAUDEX_FOLDER/` | **Governance Layer** — shared AI workbench | Created 2026-09-07 (ruling A4). The Claude ⇄ Codex whiteboard named by `INNER_CONSCIOUSNESS.md` §4; log is `COLLAB_LOG.md`. **Not a git repo**, and not a source of truth — anything here that matters gets written into its proper home. |
| `_NEW_SKILLS/` | Role 2b — Dev Incubator | 417 files. Skill development staging (e.g. `music-theory-handout`), outside the installed skill set. |
| `claudex-loop-main/` | Role 2b — Dev Incubator | 37 files. Upstream source of the `claudex-loop` skill. Not a git repo; not the installed copy (that is `~/.claude/skills/claudex-loop/`). |
| `SCRAPE_INFO/` | Role 2b — Dev Incubator (acquisition working state) | Wave 1/Wave 2 YouTube caption-acquisition queues, live reports and run records. Acquisition state, not research content; the transcripts themselves live in `_CT_RESEARCH_INTAKE/`. |
| `CHORD_ROSETTA_AUDIT_2026-09-04/`, `CHORD_ROSETTA_AUDIT_2026-09-05/` | Role 4a — Project Archives | Dated audit working folders (scripts, repair plans, notation gallery). Self-dating; fold into `ARCHIVE/99_ARCHIVE/` when cold. |
| `AliceinWonderland/` | Role 2b — Dev Incubator | 73 files. Autonovel/Alice chamber-pilot assets and briefs; companion to `The_Common_Tone_Project/_PROJECTS/AUTONOVEL_CHROMATIC_UNIVERSE/`. |
| `CHANNEL STINGER FOLDER/` | Role 4b — media assets | 31 MB. Channel stinger project files, audio and video renders. Binary; do not promote inward. |
| `SIBELIUS_FILES/TEMPLATE_EXPORTS/` *(consolidated 2026-09-17)* | Role 4b — Large Reference Corpora (notation exports) | The three former `SIBELIUS TEMPLATES-->EXPORTS` batches were folded into `SIBELIUS_FILES/TEMPLATE_EXPORTS/` (`Templates-1/`, `Templates-2/`, `Basic-12-Bar-Blues/`) on Doug's decision, 2026-09-17. Root now holds one Sibelius folder. |
| `LINES AND DOTS AND BLOBS PROJECT/` *(classified 2026-09-19)* | Role 4b — media assets | 45 MB. Camtasia video project for the Chapter 1.2 video, renders and chapter cover images. Binary; do not promote inward. Sits beside `CHANNEL STINGER FOLDER/`. |
| `RESEARCH_OBSERVATORY/` *(classified 2026-09-19)* | Role 2b — research inbox (outside the Machine) | Weekly research digests, source records and an index, arriving as dated ZIP exports Doug reviews before merging. Its own `README.md` is the protocol. Nothing here is promoted inward without Doug's approval. |
| `READER_RESOURCE_COMPENDIUM/` *(classified 2026-09-19)* | Role 2b — Dev Incubator (parked idea) | Reader Resources pilot and Unit I expansion; picks approved by Doug 2026-09-14 and 2026-09-19, publication not authorized. Parked in `IDEA_LEDGER.md` on 2026-09-18. |
| `CLAUDE_DESIGN_KIT/CT_FIGURE_INDEX.html`, `CT_LOGO_INDEX.html` *(moved 2026-09-19)* | Governance Layer — design kit | Two self-contained browse-by-eye index pages (figures and notation; logos and brand), generated 2026-09-18. Moved in from the outer root. Untracked in the design-kit repo; 18 MB together. |

*(`common-tone-site/` was the twelfth. It was a self-marked archived prototype and moved
2026-09-07 to `ARCHIVE/99_ARCHIVE/2026-09-07_common-tone-site-prototype/`, ruling B6. The
canonical, deployed site repo is `~/Code/common-tone-site` — deploy is Doug only.)*

### Governance Layer (root-level)

- `_SYSTEM/` — Operational substrate of the inner sanctum. Accessed by both vaults via symlink `The_Common_Tone_Project/_SYSTEM →../_SYSTEM`. Contains `canonical_projects.yaml`, scripts, scheduled-task definitions, SQLite databases, procedures, logs, templates. **Do not classify as Role 4** — operationally live. Stays at root (symlink dependency).

### Root-Level Files (intentionally at root)

- `AGENTS.md` — four-line pointer for Codex-style agents: the project root is `The_Common_Tone_Project/`, read its `CLAUDE.md`; outer folder roles are in this file. *(Rewritten 2026-09-07; it had been nothing but a `claude-mem` memory dump. The plugin's Codex context now writes to `~/.claude-mem/CODEX_CONTEXT.md` instead, and the freshness auditor has a blocker check that fails if a memory block reappears in it.)*

- *(`Cowork_log_file.md` is **not** at the outer root — the single live session log is at the **vault** root, `The_Common_Tone_Project/Cowork_log_file.md`, per `CLAUDE.md` §3. Corrected 2026-09-07.)*
- *(`COMMONTONE_FUNCTIONAL_MAP_DESCRIPTION_2026-05-01.md` was archived 2026-09-07 to `ARCHIVE/99_ARCHIVE/2026-09-07_ONE_CHOIR_BOOK/` — historical, not maintained, and no longer described as canonical.)*
- `ABC_and_Verovio_Orientation.md` — Active reference (May 2026); fold into `_ARCHIVE_BOOK_ITERATIONS/` when no longer needed.
- `.gitignore` — Version control config.

---

## The Ingestion Gate

The rule is `CLAUDE.md` rail 4 and is not restated here. One outer-vault specific note: the
**Promote** stage of the `DEVELOPMENT/_DEV_INCUBATOR/` lifecycle is a special case — deliberate,
logged, with Markdown conversion at the gate.

---

## Procedure — What to Do When a New Folder Appears at the Outer Root

1. **Decide its bucket.** Does it belong in `CT_BUSINESS/`, `DEVELOPMENT/`, `GOVERNANCE/`, or `EDUCATION/`? If yes, move it in.
2. **If it doesn't fit a bucket**, assign it a Role and add it to "Root-Level Folders" above.
3. **Add a one-line role declaration** to the appropriate section of this file.
4. **If the folder has no README**, create one.
5. **Never** leave a new outer folder unclassified.

---

## Decommissioned Folders (do not re-create)

- The legacy top-level master research wrapper folder (decommissioned 2026-05-01).

---

## Counter-flow — What Belongs Outside That Currently Lives Inside

- **ABC-notation tooling** and any **alternative notation-system** work → `DEVELOPMENT/_DEV_INCUBATOR/` under a per-system subfolder when ready to migrate.
- **Any other inner-sanctum folders that are development rather than operational** — to be identified in the Inner Vault Audit.

---

## Cross-References

- `ADMIN/STRATEGIC_PLANS/ORG_CONSULTATION_2026-04-20.md` — the consulting memo that established this framework. *(Path corrected 2026-09-07; it is not at the GOVERNANCE root.)*
- `DEVELOPMENT/_DEV_INCUBATOR/README.md` — the incubator's lifecycle policy.
- `GOVERNANCE/VAULT_MAPS/CURRENT_MAP.md` — the last cartographer-generated outer-vault map (historical; the skill was retired 2026-07-31).
- `The_Common_Tone_Project/00_CONSTITUTION/CONSTITUTION.md` — the inner-sanctum constitution.

---

*Created 2026-04-20. Updated through 2026-09-07.*

*2026-05-07 (four-bucket reorganization):* Outer vault restructured into four top-level buckets — `CT_BUSINESS/`, `DEVELOPMENT/`, `GOVERNANCE/`, `EDUCATION/`. This file moved from `__MY_BOOK/OUTER_VAULT_ROLES.md` to `__MY_BOOK/GOVERNANCE/OUTER_VAULT_ROLES.md`. `CANONICAL_DOCS_REGISTRY.yaml` IDEA_LAB path updated to `DEVELOPMENT/IDEA_LAB`. `MARKDOWN_FIRST_POLICY.md` RENDERS canonical path updated to `GOVERNANCE/RENDERS/`. Stray files cleaned: trumpet renders moved to `GOVERNANCE/RENDERS/`; `Cowork_log_file.md.tmp` and `AGENTS.md` deleted. *(An outer-root `AGENTS.md` returned 2026-09-05, written by the claude-mem plugin; as of 2026-09-07 it is a four-line pointer to the vault's `CLAUDE.md` — see the Governance Layer entry above.)*

---
*Review log: 2026-09-07 — dated re-review (One Choir Book, ruling B8; authority `ADMIN/AUDITS/2026-09-07_ONE_CHOIR_BOOK_DECISIONS.md`). Removed ownerships by skills retired 2026-07-31 (`vault-cartographer`, `ceo-daily-report`, `writer-watch`, and the `cowork_scheduled_tasks_skills/` shims); removed four folders no longer on disk (`__MY COMPOSITION BOOK/`, `_MY JAZZ-BOOK/`, `_MY HISTORY BOOK/`, `JazzStandards-main/`); corrected the `Cowork_log_file.md` location (vault root, not outer root), the `ORG_CONSULTATION` path, the `GOVERNANCE/VALIDATION_REPORTS/` claim and the `GOVERNANCE/SKILLS/` contents; reclassified `ARCHIVE/` as the protected read-only archive tree; recorded the outer `AGENTS.md` as a pointer and the functional map as archived; classified the twelve previously unclassified root folders plus the new `CLAUDEX_FOLDER/`. Dropped the restated startup obligation and made the "(restated)" Ingestion Gate section a pointer to `CLAUDE.md` rail 4 — this file is policy for the outer vault, and the rules live in the rulebook. Freshness timer reset by this review.*

*Review log: 2026-07-01 — substantive review completed (Doug-commissioned). Corrections: ADMIN hardlink description reversed to symlink reality (§Role 4a); two Role 4b/4c paths re-homed under EDUCATION/. Full path reconciliation run against the live tree; all other directory references verified correct in context. Open observation for Doug: two VOICE_NOTES folders exist in the inner sanctum (root-level and 02_SOURCE_MATERIAL/) — consolidation is a Doug decision, not attempted here. Freshness timer reset by this review.*
