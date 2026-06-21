---
name: composer-instrument-guide
description: |
  Generate composer's field-guide handouts in Doug Smith's house style for any
  orchestral or band instrument, at four content depths: 1-page essential, 2-page
  standard, 3-page rich (canonical), and full textbook tier. Driven by a YAML spec
  per instrument and a per-family config (section order, headings, default
  pitfalls, etc.). Produces (1) a custom range/register diagram with a real
  engraved staff (Verovio) and color-coded zones, (2) a written-vs-concert
  transposition demo for transposing instruments, and (3) the .docx in house
  style with definition box, voice & character, players-POV, asides
  (pedantry/history/family-tree), articulation, mute table, breath/stamina,
  common pitfalls (red), history (with era timeline), repertoire pointers, and
  composer's checklist. Use this skill whenever Doug says: "field guide for
  [instrument]", "composer's handout for [instrument]", "make a trumpet
  handout", "do clarinet next", "horn in F field guide", or any request for a
  one-to-many-page instrument primer aimed at composers/composition students.
---

# composer-instrument-guide

A skill that turns an instrument YAML spec into polished composer's handouts in
Doug's house style, at variable depth (1, 2, 3, or full pages).

## When to use

Trigger on any of:
- "field guide for [instrument]" / "composer's guide for [instrument]"
- "trumpet/horn/clarinet/etc. handout for my comp students"
- "do [instrument] next" (in the context of a series of instrument handouts)
- "one-page primer on [instrument]" / "give me the 1-page version of …"

## How it works

```
spec YAML ──► validate.py             ──► schema check
          ──► families/<family>.yaml  ──► section order, headings, defaults
          ──► build_range.py          ──► engraved staff + color zones (SVG/PNG)
          ──► build_transposition.py  ──► written vs sounding (PNG)
          ──► build_doc.js            ──► .docx in house style (filtered by tier)
```

## Setup (one-time)

```bash
./install.sh
```

Installs Python deps (`verovio`, `cairosvg`, `pyyaml`) and Node deps (`docx`).
Idempotent.

## Running it

```bash
# Default — produces the canonical 3-page handout
python3 scripts/run.py instruments/horn_f.yaml /path/to/output_dir

# Specific size
python3 scripts/run.py instruments/horn_f.yaml /path/to/output_dir --size 1
python3 scripts/run.py instruments/horn_f.yaml /path/to/output_dir --size 2
python3 scripts/run.py instruments/horn_f.yaml /path/to/output_dir --size full

# All sizes in one pass — produces _1pg, _2pg, _3pg suffixed docx files
python3 scripts/run.py instruments/horn_f.yaml /path/to/output_dir --size all
```

The validator runs first; bad specs surface before any rendering. After a
successful build, an entry is appended to `Cowork_log_file.md` (path
configurable via `COWORK_LOG_PATH` env var).

## The two architectural axes

### Family
Determines which sections are *relevant* and the section order/heading vocabulary.
Per-family configs live in `families/<family>.yaml`. Currently shipped:
- `families/brass.yaml` (trumpet, horn)

Future: woodwind, bowed-string, plucked-string, pitched-percussion,
unpitched-percussion, keyboard, voice.

### Tier
Determines which *relevant* sections are *included at a given size*. Each block
has a default tier; per-instrument YAML can override; family config can override.

| Tier | Blocks | Variant |
|------|--------|---------|
| 1 (essential) | intro, definition_box, transposition_demo, range, articulation (top 3), checklist | **1pg** — single-page reference |
| 2 (standard)  | + voice, mutes, phrasing, pitfalls, full articulation | **2pg** — standard handout |
| 3 (rich, default) | + players_pov, asides, listen | **3pg** — canonical composer's handout |
| 4 (extended)  | + history (timeline + family tree) | **full** — textbook tier |

`--size all` produces all three of (1pg, 2pg, 3pg) in one pass; the canonical
(no-suffix) build is `--size 3`.

## Adding a new instrument

Copy `instruments/horn_f.yaml` and edit. The schema:

### Required
- `instrument` — `name`, `family`, `clef` (treble/bass), `transposition_blurb`,
  `sounding_blurb`, optional `transposition` (omit for non-transposing)
- `intro` — `paragraph` and optional `paragraph_emphasis` (auto-joined with ": ")
- `definition_box` — `title` and `body` (transposition explainer)
- `zones` — register zones, low → high, with `name`, `written_range` \[low, high\],
  `color`, `border`, `danger` (✓ ! !! !!! x), `blurb`
- `range_caption`, `articulation` (list of {name, description}),
  `phrasing` (bullet list), `checklist` ({title, items})

### Recommended (the heart of "what to write")
- `voice` — `paragraph`, `signature_gestures` (list), `archetypal_uses` (list)
- `players_pov` — `paragraph` (renders in ochre left-bar box)
- `pitfalls` — list of strings (red callout; family defaults appended)
- `listen` — list of `{piece, role}` (table; family defaults appended)

### Optional
- `asides` — list of `{kind, title, body}`; kind ∈ pedantry|history|family-tree
- `history` — `{origin, timeline: [{era, note}], family_tree: "..."}` (tier 4)
- `mutes` — list of `{name, sound, notation}`; `mute_caveat` paragraph
- `_tiers: { blockname: N }` — per-instrument tier override

Backward-compat: top-level `pedestal_pedantry: {title, body}` auto-converts to
a single pedantry aside.

## Family config schema

`families/brass.yaml` is the template. Each family config can declare:
- `section_order` — ordered list of block keys
- `headings` — heading vocabulary overrides
- `default_tiers` — per-block tier overrides for this family
- `default_pitfalls`, `default_listen` — universal-for-this-family content that
  gets appended to per-instrument lists (deduped by exact text match)

## House style invariants

- Gill Sans body / Futura Condensed ExtraBold headings
- Box patterns from doug-docx-style:
  - Pattern A (full border) → Definition box
  - Pattern B (left bar):
    - Purple → Pedestal of Pedantry / asides[kind=pedantry]
    - Teal → asides[kind=history]
    - Green → asides[kind=family-tree]
    - Ochre → Players-POV
    - Orange → Composer's checklist (Tip)
    - Red → Common pitfalls
- Tight margins (0.75" L/R, 0.4" T/B)
- Boxes have `cantSplit: true` so they don't orphan across page breaks
- US Letter, treble or bass clef

## Pedagogical conventions

- **Color overlap is meaningful.** Adjacent zones may share a staff slot; the
  diagram shows this with overlapping colors.
- **Legend ordering matches the diagram.** Highest pitches at the top.
- **Range diagram extracts notehead positions from the rendered SVG** (clef-agnostic).
- **Voice & character comes BEFORE technical specifics.**
- **Pitfalls and Listen-for-it close the loop.**

## Dependencies

- Python 3 with: `verovio`, `cairosvg`, `pyyaml`
- Node.js with: `docx`
- LibreOffice (optional, for converting docx→pdf to verify page count)
