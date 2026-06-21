---
type: vault_policy
scope: OUTER_VAULT
vault_root: /Users/dougsmith/Docs/__MY_BOOK/
created: 2026-04-20
author: Doug Smith (via Claude consultation)
grounded_in:
  - ORG_CONSULTATION_2026-04-20.md (framework)
  - VAULT_MAPS/vault_map_2026-04-18.md (folder inventory)
status: canonical
analog_of: The_Common_Tone_Project/00_CONSTITUTION/CONSTITUTION.md
motto: "Every folder has one role. Every new file has one home."
location_note: "Moved from outer root to GOVERNANCE/ on 2026-05-07 as part of four-bucket reorganization."
---

# OUTER VAULT ROLES

**What this document is.** The canonical policy that classifies every top-level folder in `/Users/dougsmith/Docs/__MY_BOOK/`. It is the outer-vault analog of `The_Common_Tone_Project/00_CONSTITUTION/CONSTITUTION.md` — the document that tells a human (or an AI assistant) where anything belongs, why it is outside the inner sanctum, and what the promotion rule is for moving inward.

**Where this file lives.** `GOVERNANCE/OUTER_VAULT_ROLES.md` — moved here 2026-05-07 during the four-bucket reorganization. The root-level `OUTER_VAULT_ROLES.md` no longer exists.

**What this document is not.** It is not a map — the cartographer-generated snapshot in `GOVERNANCE/VAULT_MAPS/` is the authoritative map. This file is *policy*; the map is *observation*. The two are companions.

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
CT_BUSINESS/          Business operation of The Common Tone brand
DEVELOPMENT/          Active development, incubator, projects, ideas
GOVERNANCE/           Vault infrastructure, maps, renders, this file
EDUCATION/            Douglas College teaching materials
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

- `DEVELOPMENT/_DEV_INCUBATOR/` — The canonical four-stage incubator (Pitch → Build → Prove → Promote). Contains `SALAMI_PROJECT/` (1,242 songs, 126,272 chords in `salami_db.sqlite`; `salami_explorer.py` Flask app at localhost:8765). Run with `cd .../DEVELOPMENT/_DEV_INCUBATOR/SALAMI_PROJECT && python3 salami_explorer.py`.
- `DEVELOPMENT/IDEA_LAB/` — Creative incubator using a folder-per-idea PR model (`IDEA-001` through `IDEA-015+`). AI assistants must check `IDEA_LAB/_INDEX.md` for ideas in `peer-review` status at the start of every session.
- `DEVELOPMENT/PROJECTS/` — Operational CT-prefixed projects: `CT-Control-Center`, `CT-Email`, `CT-Infrastructure`, `CT-Intake`, `CT-Interactive`, `CT-Substack`, `CT-Textbook`, `CT-Vault`, `COMPOSER_FIELD_GUIDES/`, `PROJECT_SETUP_GUIDE.md`.
- `DEVELOPMENT/CT_DIMENSIONS/` — Platform architecture planning docs. Working drafts; not yet operational.
- `DEVELOPMENT/Excalidraw/` — Single working diagram (Apr 27).
- `DEVELOPMENT/NOTATION & XML/` — 97 MusicXML/MXL files (scales, grooves, instructional phrases). Role 2b Dev Incubator — notation tooling exploration.

**The key test:** *"Is this building something for the book, courses, or public surface?"* If yes but not yet operational → it lives here.

---

### GOVERNANCE/ — Vault Infrastructure and Operations

Items that describe, validate, or operate the vault. Not content — they *are* the classification system, the validation surface, and the render target.

- `GOVERNANCE/OUTER_VAULT_ROLES.md` — this file.
- `GOVERNANCE/VAULT_MAPS/` — Cartographer snapshots + `CURRENT_MAP.md` pointer. Owned by the `vault-cartographer` skill.
- `GOVERNANCE/RENDERS/` — Binary render artifact parking lot. **Canonical render target path: `/Users/dougsmith/Docs/__MY_BOOK/GOVERNANCE/RENDERS/`** (updated 2026-05-07; was `__MY_BOOK/RENDERS/`). Contents are frozen build artifacts — canonical `.md` source lives inside the sanctum. Sub-folders: `BrandBrief/`, `PlagalParadigm/`, field guide renders. Do not edit files here; do not promote them back inward.
- `GOVERNANCE/VALIDATION_REPORTS/` — Output of validation, audit, and check scripts. Append-only; rotate quarterly if size becomes a concern.
- `GOVERNANCE/SKILLS/` — Operational skill infrastructure. Contains `composer-instrument-guide/` (YAML specs, Python build scripts, `SKILL.md`). Read at runtime by the Cowork skill.
- `GOVERNANCE/cowork_scheduled_tasks_skills/` — Scheduled-task `.md` shims (morning email, evening email, writer-watch).

**Note on `_SYSTEM/`.** The outer vault's `_SYSTEM/` folder lives at `__MY_BOOK/_SYSTEM/` (root, not inside GOVERNANCE/) because `The_Common_Tone_Project/_SYSTEM` is a symlink pointing to `../_SYSTEM`. Moving `_SYSTEM/` into GOVERNANCE/ would require updating that symlink. Policy: `_SYSTEM/` stays at root. It is Governance Layer infrastructure regardless of physical location.

---

### EDUCATION/ — Douglas College Teaching Materials

Teaching materials produced for or used at Douglas College. Completely separate from the textbook project. Stays outer permanently; never ingested into the Machine.

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

- `__MY COMPOSITION BOOK/`
- `_MY JAZZ-BOOK/`
- `_MY HISTORY BOOK/`

**Rule.** No automation ingests from these into the Machine without explicit human instruction.

### Role 4a — Project Archives

- `_ARCHIVE_BOOK_ITERATIONS/` — Historical drafts. Receives moves-in as the project evolves.
- `WORKBOOK/` — Early workbook draft; candidate for fold-in to `_ARCHIVE_BOOK_ITERATIONS/`.
- `ARCHIVE/` — One-file straggler; candidate for fold-in or removal.
- `ADMIN/` — **⚠️ APFS hardlink** to `The_Common_Tone_Project/01_ADMIN_AND_POLICY/`. Same physical directory confirmed via inode comparison. **Do NOT move or delete** — it would destroy inner-sanctum data simultaneously. Treat as read-only at the outer root.

### Role 4b — Large Reference Corpora (do not move — sizes listed)

- `DATA_FOLDER/` — HDF5 datasets + derived JSON/TXT (3.1 GB). Needs provenance README.
- `RESOURCES_REFERENCE/` — Album art, historical photos, diagrams (5.5 GB).
- `REPERTOIRE_DOCUMENTED_POP_SONGS/` — Pop repertoire scans and transcriptions (15 GB).
- `REPERTOIRE_CLASSICAL_THEORY_EXAMPLES/` — Classical repertoire examples (1 GB).
- `REPERTOIRE_DOUGS_POP_SONGS_FOR_THEORY/` — Doug's pop songs as pedagogical examples (1.1 GB).
- `SIBELIUS_FILES/` — Sibelius-score archive (20 MB).
- `PAGES_DOCS/` — Pages/Word document archive (194 MB).
- `_DOUGS_WRITING_STYLE/` — Reference corpus for brand-voice tooling (187 MB).
- `THE_WRITERS_DEN_ARCHIVE/` — Active reference for `writer-watch` skill (264 KB).

### Role 4c — Legacy / Dormant

- `JazzStandards-main/` — Third-party JSON corpus, vendored (1,186 days cold).
- `SOME INGESTION/` — Old ingest residue, 3 files (742 days cold).
- `GRFX_TEST_FOLDER/` — Graphics sandbox, 11 files (374 days cold).
- `LISTENING_LISTS/` — Curated listening lists (452 days cold).
- `MUSIC_COLLEGE/` — College-era personal material (452 days cold).

### Governance Layer (root-level)

- `_SYSTEM/` — Operational substrate of the inner sanctum. Accessed by both vaults via symlink `The_Common_Tone_Project/_SYSTEM → ../_SYSTEM`. Contains `canonical_projects.yaml`, scripts, scheduled-task definitions, SQLite databases, procedures, logs, templates. **Do not classify as Role 4** — operationally live. Stays at root (symlink dependency).

### Root-Level Files (intentionally at root)

- `Cowork_log_file.md` — Session log; must stay at root.
- `COMMONTONE_FUNCTIONAL_MAP_DESCRIPTION_2026-05-01.md` — Canonical prose description of the entire enterprise; allowed at root per policy.
- `ABC_and_Verovio_Orientation.md` — Active reference (May 2026); fold into `_ARCHIVE_BOOK_ITERATIONS/` when no longer needed.
- `.gitignore` — Version control config.

---

## The Ingestion Gate (restated)

The only authorized path from outer → inner is the `music-file-intake` skill. No human, no AI assistant, and no automation moves material across that boundary without going through intake. The **Promote** stage of `DEVELOPMENT/_DEV_INCUBATOR/` lifecycle is a special case: deliberate, logged, with Markdown conversion at the gate.

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

- `ORG_CONSULTATION_2026-04-20.md` — the consulting memo that established this framework.
- `DEVELOPMENT/_DEV_INCUBATOR/README.md` — the incubator's lifecycle policy.
- `GOVERNANCE/VAULT_MAPS/CURRENT_MAP.md` — the cartographer-generated outer-vault map.
- `The_Common_Tone_Project/00_CONSTITUTION/CONSTITUTION.md` — the inner-sanctum constitution.

---

*Created 2026-04-20. Updated through 2026-05-07.*

*2026-05-07 (four-bucket reorganization):* Outer vault restructured into four top-level buckets — `CT_BUSINESS/`, `DEVELOPMENT/`, `GOVERNANCE/`, `EDUCATION/`. This file moved from `__MY_BOOK/OUTER_VAULT_ROLES.md` to `__MY_BOOK/GOVERNANCE/OUTER_VAULT_ROLES.md`. `CANONICAL_DOCS_REGISTRY.yaml` IDEA_LAB path updated to `DEVELOPMENT/IDEA_LAB`. `MARKDOWN_FIRST_POLICY.md` RENDERS canonical path updated to `GOVERNANCE/RENDERS/`. Stray files cleaned: trumpet renders moved to `GOVERNANCE/RENDERS/`; `Cowork_log_file.md.tmp` and `AGENTS.md` deleted.
