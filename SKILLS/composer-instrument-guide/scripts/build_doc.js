#!/usr/bin/env node
// Build an instrument field-guide handout in Doug's house style from a JSON spec.
// Usage:  node build_doc.js <spec.json> <out_dir>
// The spec.json contains:
//   - everything from the instrument YAML
//   - "_assets":         { range_png, transp_written_png, transp_concert_png }
//   - "_render_size":    1|2|3|4 (max tier to include; 3 = canonical 3-page build)
//   - "_filename_suffix":"" | "_1pg" | "_2pg" | "_3pg" | "_full"
//   - "_family_config":  optional family override of section order / headings / defaults

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  AlignmentType, HeadingLevel, BorderStyle, WidthType, ShadingType,
} = require("docx");

if (process.argv.length < 4) {
  console.error("usage: build_doc.js <spec.json> <out_dir>");
  process.exit(1);
}
const SPEC = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const OUT_DIR = process.argv[3];
const RENDER_SIZE = SPEC._render_size ?? 3;          // tier ceiling
const FAMILY_CONFIG = SPEC._family_config || null;

// --- DOUG'S STYLE CONSTANTS ---
const BODY_FONT = "Gill Sans";
const HEADING_FONT = "Futura Condensed ExtraBold";
const BOX_TITLE_FONT = "Gill Sans";
const PAGE_MARGINS = { top: 540, right: 1080, bottom: 540, left: 1080 };
const CONTENT_WIDTH = 12240 - PAGE_MARGINS.left - PAGE_MARGINS.right;
const SIDEBAR_WIDTH = Math.round(CONTENT_WIDTH * 0.74);

const NO_BORDER = { style: BorderStyle.NONE, size: 0 };
const THIN_GREY  = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const THIN_STEEL = { style: BorderStyle.SINGLE, size: 1, color: "707070" };
const LB_SIZE = 76;
const PURPLE_LEFT = { style: BorderStyle.SINGLE, size: LB_SIZE, color: "7B2D8E" };
const ORANGE_LEFT = { style: BorderStyle.SINGLE, size: LB_SIZE, color: "E67E22" };
const TEAL_LEFT   = { style: BorderStyle.SINGLE, size: LB_SIZE, color: "2C5F7A" };
const GREEN_LEFT  = { style: BorderStyle.SINGLE, size: LB_SIZE, color: "2E8B57" };
const RED_LEFT    = { style: BorderStyle.SINGLE, size: LB_SIZE, color: "C0392B" };
const OCHRE_LEFT  = { style: BorderStyle.SINGLE, size: LB_SIZE, color: "D4A04C" };

const ASIDE_BORDER = {
  pedantry:     PURPLE_LEFT,
  history:      TEAL_LEFT,
  "family-tree": GREEN_LEFT,
};

// =====================================================================
// TIER SYSTEM
// =====================================================================
// Each block has a default tier (1=essential, 2=standard, 3=rich, 4=extended).
// Per-instrument YAML can override via `_tiers: { blockname: N }`.
// Family config (if loaded) can also override default tiers.

const DEFAULT_TIERS = {
  intro:               1,
  voice:               2,
  players_pov:         3,
  reading_writing:     1,    // section header for definition_box + transposition demo
  definition_box:      1,
  transposition_demo:  1,
  asides:              3,
  range:               1,
  articulation:        1,
  mutes:               2,
  phrasing:            2,
  pitfalls:            2,
  listen:              3,
  history:             4,    // textbook-tier; history is rich but expendable for the 3-page canonical
  checklist:           1,
};

const FAMILY_TIERS = (FAMILY_CONFIG && FAMILY_CONFIG.default_tiers) || {};
const SPEC_TIERS = SPEC._tiers || {};

function getTier(blockKey) {
  return SPEC_TIERS[blockKey] ?? FAMILY_TIERS[blockKey] ?? DEFAULT_TIERS[blockKey] ?? 2;
}
function shouldRender(blockKey) {
  return getTier(blockKey) <= RENDER_SIZE;
}

// =====================================================================
// HEADINGS — family config can override
// =====================================================================
const DEFAULT_HEADINGS = {
  voice:           "Voice & character",
  reading_writing: "Reading & writing the part",
  range:           "Range, registers, and danger zones",
  articulation:    "Articulation & playing techniques",
  mutes_brass:     "Mutes — the instrument's wardrobe",
  mutes_other:     "Mutes / accessories",
  phrasing:        "Breath, stamina, and phrasing",
  pitfalls:        "Common pitfalls",
  listen:          "Listen for it in…",
  history:         "A short history",
  players_pov:     "From the player's chair",
  checklist:       "Composer's first-pass checklist",
};
const FAMILY_HEADINGS = (FAMILY_CONFIG && FAMILY_CONFIG.headings) || {};
function heading(key, fallback) {
  return FAMILY_HEADINGS[key] || DEFAULT_HEADINGS[key] || fallback || key;
}

// =====================================================================
// PARAGRAPH HELPERS
// =====================================================================
const body = (text, opts = {}) => new Paragraph({
  style: "Normal",
  spacing: { after: 60, line: 260 },
  children: [new TextRun({ text, font: BODY_FONT, size: 20, ...opts })],
});
const bodyRich = (runs) => new Paragraph({
  style: "Normal",
  spacing: { after: 60, line: 260 },
  children: runs.map(r => new TextRun({ font: BODY_FONT, size: 20, ...r })),
});
const bullet = (text) => new Paragraph({
  style: "Normal",
  bullet: { level: 0 },
  spacing: { after: 0, line: 220 },
  children: [new TextRun({ text, font: BODY_FONT, size: 18 })],
});
const bulletRich = (runs) => new Paragraph({
  style: "Normal",
  bullet: { level: 0 },
  spacing: { after: 0, line: 220 },
  children: runs.map(r => new TextRun({ font: BODY_FONT, size: 18, ...r })),
});
const sidebarPara = (text) => new Paragraph({
  spacing: { after: 20, line: 220 },
  children: [new TextRun({ text, font: BODY_FONT, size: 18 })],
});
const sidebarRich = (runs) => new Paragraph({
  spacing: { after: 20, line: 220 },
  children: runs.map(r => new TextRun({ font: BODY_FONT, size: 18, ...r })),
});
const fullBoxPara = (text) => new Paragraph({
  spacing: { after: 40, line: 240 },
  children: [new TextRun({ text, font: BODY_FONT, size: 20 })],
});

const h2 = (text) => new Paragraph({
  heading: HeadingLevel.HEADING_2,
  spacing: { before: 100, after: 60 },
  children: [new TextRun({ text, font: HEADING_FONT, size: 24 })],
});

// =====================================================================
// BOX BUILDERS
// =====================================================================
function fullBorderBox(title, paras, border, fill) {
  const borders = { top: border, bottom: border, left: border, right: border };
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: [CONTENT_WIDTH],
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        borders, width: { size: CONTENT_WIDTH, type: WidthType.DXA },
        shading: { fill, type: ShadingType.CLEAR },
        margins: { top: 120, bottom: 120, left: 120, right: 120 },
        children: [
          new Paragraph({
            spacing: { after: 80 },
            children: [new TextRun({ text: title, font: BOX_TITLE_FONT, bold: true, size: 26 })],
          }),
          ...paras,
        ],
      })],
    })],
  });
}
function leftBorderBox(title, paras, border, width = SIDEBAR_WIDTH) {
  const borders = { top: NO_BORDER, bottom: NO_BORDER, right: NO_BORDER, left: border };
  return new Table({
    width: { size: width, type: WidthType.DXA },
    columnWidths: [width],
    rows: [new TableRow({
      cantSplit: true,
      children: [new TableCell({
        borders, width: { size: width, type: WidthType.DXA },
        margins: { top: 160, bottom: 160, left: 240, right: 120 },
        children: [
          new Paragraph({
            spacing: { after: 60 },
            children: [new TextRun({ text: title, font: BOX_TITLE_FONT, bold: true, size: 22 })],
          }),
          ...paras,
        ],
      })],
    })],
  });
}
const definitionBox      = (t, p) => fullBorderBox(t, p, THIN_GREY,  "F0F0F0");
const tipBox             = (t, p) => leftBorderBox(t, p, ORANGE_LEFT);
const pitfallsBox        = (t, p) => leftBorderBox(t, p, RED_LEFT);
const playersPovBox      = (t, p) => leftBorderBox(t, p, OCHRE_LEFT);
const asideBox           = (t, p, kind) => leftBorderBox(t, p, ASIDE_BORDER[kind] || PURPLE_LEFT);

// =====================================================================
// IMAGE / TABLE HELPERS
// =====================================================================
const imgRun = (file, w, h) => new ImageRun({
  data: fs.readFileSync(file),
  transformation: { width: w, height: h },
});
const imgPara = (file, w, h, alignment = AlignmentType.CENTER) => new Paragraph({
  alignment, spacing: { after: 80 },
  children: [imgRun(file, w, h)],
});

function transpositionTable(writtenPng, concertPng) {
  const cell = (caption, file) => new TableCell({
    borders: { top: NO_BORDER, bottom: NO_BORDER, left: NO_BORDER, right: NO_BORDER },
    width: { size: CONTENT_WIDTH / 2, type: WidthType.DXA },
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    children: [
      new Paragraph({
        spacing: { after: 40 }, alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: caption, font: BODY_FONT, bold: true, size: 20 })],
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER, spacing: { after: 0 },
        children: [imgRun(file, 280, 70)],
      }),
    ],
  });
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: [CONTENT_WIDTH / 2, CONTENT_WIDTH / 2],
    rows: [new TableRow({ children: [
      cell("WRITTEN  (" + (SPEC.instrument.name) + " part)", writtenPng),
      cell("SOUNDS  (concert pitch)", concertPng),
    ]})],
  });
}

function compactTable(headers, rows, colWidths) {
  const headerRow = new TableRow({ tableHeader: true,
    children: headers.map((h, i) => new TableCell({
      borders: {
        top:    { style: BorderStyle.SINGLE, size: 4, color: "555555" },
        bottom: { style: BorderStyle.SINGLE, size: 4, color: "555555" },
        left: NO_BORDER, right: NO_BORDER,
      },
      width: { size: colWidths[i], type: WidthType.DXA },
      shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
      margins: { top: 30, bottom: 30, left: 80, right: 80 },
      children: [new Paragraph({
        spacing: { after: 0, line: 220 },
        children: [new TextRun({ text: h, font: BODY_FONT, bold: true, size: 18 })],
      })],
    })),
  });
  const dataRows = rows.map(r => new TableRow({
    children: r.map((v, i) => new TableCell({
      borders: {
        top: NO_BORDER,
        bottom: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
        left: NO_BORDER, right: NO_BORDER,
      },
      width: { size: colWidths[i], type: WidthType.DXA },
      margins: { top: 20, bottom: 20, left: 80, right: 80 },
      children: [new Paragraph({
        spacing: { after: 0, line: 220 },
        children: [new TextRun({ text: v, font: BODY_FONT, size: 18 })],
      })],
    })),
  }));
  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: [headerRow, ...dataRows],
  });
}

// =====================================================================
// COMPACT MODE — applied when squeezing to lower-tier output
// =====================================================================
// At tier 1 (1-page) we need to shrink retained blocks. compact: true triggers:
//   articulation: keep top 4 only
//   pitfalls:     keep top 3 only
//   listen:       drop entirely (it's tier 3 anyway)
const COMPACT = RENDER_SIZE <= 1;

function trim(arr, n) { return arr ? arr.slice(0, n) : []; }

// =====================================================================
// BLOCK RENDERERS — each pushes onto `children` if the block exists
//                  AND its tier is in scope.
// =====================================================================
const inst = SPEC.instrument;
const A = SPEC._assets || {};
const children = [];

const RENDERERS = {
  title() {
    children.push(
      new Paragraph({
        heading: HeadingLevel.HEADING_1,
        spacing: { before: 0, after: 40 },
        children: [new TextRun({
          text: `${inst.name} — A Composer's Field Guide`,
          font: HEADING_FONT, size: 32,
        })],
      }),
      new Paragraph({
        style: "Normal",
        spacing: { after: 80, line: 240 },
        children: [new TextRun({
          text: "Everything you need to write idiomatically for the instrument without ever having played one.",
          font: BODY_FONT, italics: true, size: 19, color: "555555",
        })],
      }),
    );
  },

  intro() {
    if (!SPEC.intro || !shouldRender("intro")) return;
    const para = (SPEC.intro.paragraph || "").replace(/\s+$/, "");
    const sep = SPEC.intro.paragraph_emphasis ? ": " : "";
    children.push(bodyRich([
      { text: para + sep },
      ...(SPEC.intro.paragraph_emphasis ? [{ text: SPEC.intro.paragraph_emphasis, bold: true }] : []),
    ]));
  },

  voice() {
    if (!SPEC.voice || !shouldRender("voice")) return;
    children.push(h2(SPEC.voice.heading || heading("voice")));
    if (SPEC.voice.paragraph) children.push(body(SPEC.voice.paragraph));
    if (SPEC.voice.signature_gestures && SPEC.voice.signature_gestures.length) {
      children.push(bodyRich([{ text: "Signature gestures:", bold: true }]));
      for (const g of SPEC.voice.signature_gestures) children.push(bullet(g));
    }
    if (SPEC.voice.archetypal_uses && SPEC.voice.archetypal_uses.length) {
      children.push(bodyRich([{ text: "Archetypal uses:", bold: true }]));
      for (const u of SPEC.voice.archetypal_uses) children.push(bullet(u));
    }
  },

  players_pov() {
    if (!SPEC.players_pov || !shouldRender("players_pov")) return;
    const title = SPEC.players_pov.title || heading("players_pov");
    children.push(playersPovBox(title, [sidebarPara(SPEC.players_pov.paragraph || "")]));
  },

  reading_writing() {
    if (!shouldRender("reading_writing")) return;
    const hasContent = (SPEC.definition_box && shouldRender("definition_box"))
                    || (A.transp_written_png && shouldRender("transposition_demo"));
    if (!hasContent) return;
    if (!COMPACT) children.push(h2(heading("reading_writing")));
    if (SPEC.definition_box && shouldRender("definition_box")) {
      children.push(definitionBox(SPEC.definition_box.title, [fullBoxPara(SPEC.definition_box.body)]));
    }
    if (A.transp_written_png && A.transp_concert_png && shouldRender("transposition_demo")) {
      children.push(new Paragraph({
        spacing: { before: 80, after: 40 },
        children: [new TextRun({ text: "Written vs. sounding — a one-bar demo", font: BODY_FONT, bold: true, size: 22 })],
      }));
      children.push(transpositionTable(A.transp_written_png, A.transp_concert_png));
      if (!COMPACT) {
        children.push(body(
          "Both bars sound the SAME pitches. The transposing part is notated so the player reads what feels natural under the fingers; the score sounds at concert. Notation software handles this automatically — but as a composer you should be able to do it in your head for sketching."
        ));
      }
    }
  },

  asides() {
    if (!shouldRender("asides")) return;
    let asides = SPEC.asides;
    if (!asides && SPEC.pedestal_pedantry) {
      asides = [{ kind: "pedantry", title: SPEC.pedestal_pedantry.title, body: SPEC.pedestal_pedantry.body }];
    }
    if (!asides || !asides.length) return;
    for (const a of asides) {
      children.push(asideBox(a.title, [sidebarPara(a.body)], a.kind));
    }
  },

  range() {
    if (!shouldRender("range") || !A.range_png) return;
    children.push(h2(heading("range")));
    const w = COMPACT ? 480 : 540;
    const h = COMPACT ? 240 : 270;
    children.push(imgPara(A.range_png, w, h));
    if (SPEC.range_caption && !COMPACT) children.push(body(SPEC.range_caption));
  },

  articulation() {
    if (!SPEC.articulation || !SPEC.articulation.length || !shouldRender("articulation")) return;
    children.push(h2(heading("articulation")));
    let items = SPEC.articulation;
    if (COMPACT) items = trim(items, 3);
    for (const a of items) {
      children.push(bulletRich([{ text: a.name, bold: true }, { text: " — " + a.description }]));
    }
  },

  mutes() {
    if (!SPEC.mutes || !SPEC.mutes.length || !shouldRender("mutes")) return;
    const h = inst.family === "brass" ? heading("mutes_brass") : heading("mutes_other");
    children.push(h2(h));
    children.push(compactTable(
      ["Mute", "Sound character", "Notation"],
      SPEC.mutes.map(m => [m.name, m.sound, m.notation]),
      [1900, 5780, 2400]
    ));
    if (SPEC.mute_caveat) children.push(body(SPEC.mute_caveat));
  },

  phrasing() {
    if (!SPEC.phrasing || !SPEC.phrasing.length || !shouldRender("phrasing")) return;
    children.push(h2(heading("phrasing")));
    for (const p of SPEC.phrasing) children.push(bullet(p));
  },

  pitfalls() {
    if (!shouldRender("pitfalls")) return;
    // Merge: per-instrument first, then family defaults (deduped by exact text match).
    const own = SPEC.pitfalls || [];
    const family = (FAMILY_CONFIG && FAMILY_CONFIG.default_pitfalls) || [];
    const seen = new Set(own);
    const merged = [...own, ...family.filter(x => !seen.has(x))];
    if (!merged.length) return;
    let items = merged;
    if (COMPACT) items = trim(items, 3);
    children.push(pitfallsBox(SPEC.pitfalls_title || heading("pitfalls"),
      items.map(item => sidebarRich([{ text: "✗ ", bold: true }, { text: item }]))
    ));
  },

  listen() {
    if (!shouldRender("listen")) return;
    const own = SPEC.listen || [];
    const family = (FAMILY_CONFIG && FAMILY_CONFIG.default_listen) || [];
    const seenPieces = new Set(own.map(L => L.piece));
    const merged = [...own, ...family.filter(L => !seenPieces.has(L.piece))];
    if (!merged.length) return;
    children.push(h2(heading("listen")));
    children.push(compactTable(
      ["Piece", "What it does"],
      merged.map(L => [L.piece, L.role]),
      [4200, 5880]
    ));
  },

  history() {
    if (!SPEC.history || !shouldRender("history")) return;
    children.push(h2(heading("history")));
    if (SPEC.history.origin) children.push(body(SPEC.history.origin));
    if (SPEC.history.timeline && SPEC.history.timeline.length) {
      children.push(compactTable(
        ["Era", "Note"],
        SPEC.history.timeline.map(t => [t.era, t.note]),
        [2200, 7880]
      ));
    }
    if (SPEC.history.family_tree) {
      children.push(bodyRich([
        { text: "Family ties: ", bold: true, italics: true, color: "666666" },
        { text: SPEC.history.family_tree, italics: true, color: "666666" },
      ]));
    }
  },

  checklist() {
    if (!SPEC.checklist || !shouldRender("checklist")) return;
    children.push(tipBox(SPEC.checklist.title || heading("checklist"),
      SPEC.checklist.items.map(item => sidebarRich([{ text: "✓ ", bold: true }, { text: item }]))
    ));
  },

  footer() {
    children.push(new Paragraph({
      spacing: { before: 240, after: 0 },
      alignment: AlignmentType.RIGHT,
      children: [new TextRun({
        text: "— prepared for composition students · D. Smith ·  THE COMMON TONE",
        font: BODY_FONT, italics: true, size: 18, color: "888888",
      })],
    }));
  },
};

// =====================================================================
// SECTION ORDER — family config can override; otherwise this default
// =====================================================================
const DEFAULT_SECTION_ORDER = [
  "title",
  "intro",
  "voice",
  "players_pov",
  "reading_writing",
  "asides",
  "range",
  "articulation",
  "mutes",
  "phrasing",
  "pitfalls",
  "history",
  "listen",
  "checklist",
  "footer",
];

const SECTION_ORDER = (FAMILY_CONFIG && FAMILY_CONFIG.section_order) || DEFAULT_SECTION_ORDER;

for (const section of SECTION_ORDER) {
  const fn = RENDERERS[section];
  if (typeof fn === "function") fn();
  // Unknown section names are silently skipped — family configs can list
  // family-specific sections that this default renderer doesn't implement yet.
}

// =====================================================================
// DOCUMENT
// =====================================================================
const doc = new Document({
  creator: "Doug Smith",
  title: `${inst.name} — A Composer's Field Guide`,
  styles: {
    default: { document: { run: { font: BODY_FONT, size: 20 } } },
    paragraphStyles: [
      { id: "Normal", name: "Normal", quickFormat: true,
        run: { font: BODY_FONT, size: 20 },
        paragraph: { spacing: { after: 60, line: 260 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: false, font: HEADING_FONT },
        paragraph: { spacing: { before: 0, after: 80 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: false, font: HEADING_FONT },
        paragraph: { spacing: { before: 100, after: 60 }, outlineLevel: 1 } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: PAGE_MARGINS } },
    children,
  }],
});

const safe = inst.name.replace(/[^A-Za-z0-9]+/g, "_");
const suffix = SPEC._filename_suffix ?? "";
const fname = `${safe}_Field_Guide${suffix}.docx`;
const out = path.join(OUT_DIR, fname);
Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(out, buf);
  console.log("WROTE", out, buf.length, "bytes");
});
