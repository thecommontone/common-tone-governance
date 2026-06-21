#!/usr/bin/env python3
"""Build a range/register diagram for any instrument from a YAML spec.

Strategy:
  1. Render a stacked CHORD (all boundary pitches at one x position) via Verovio.
     This gives us a real engraved staff + clef + ledger lines + noteheads.
  2. Extract the ACTUAL y-coordinates of the rendered noteheads. Verovio adjusts
     staff position to fit content, so we cannot predict y from a fixed formula —
     we read it from the SVG. This makes the diagram clef-agnostic.
  3. Wrap the Verovio output inside a larger SVG; place color zones and labels
     using the extracted positions.
  4. Build a right-side legend in HIGH→LOW order so it spatially mirrors the diagram.
"""
from __future__ import annotations
import re, yaml, argparse
import verovio

# ----- Pitch helpers (clef-independent natural-name ladder) -----

PAGE_MARGIN_X = 500
PAGE_MARGIN_Y = 500
DIATONIC_STEP_INTERNAL = 90  # constant across clefs in Verovio at scale 40

DIATONIC_LADDER = [
    f"{n}{o}" for o in range(0, 9) for n in ["C","D","E","F","G","A","B"]
]

def natural_index(pitch: str) -> int:
    """Position on the diatonic ladder, ignoring accidentals (F3 == F#3 == Fb3)."""
    natural = pitch.replace("#","").replace("b","")
    if natural not in DIATONIC_LADDER:
        raise KeyError(f"unknown pitch: {pitch}")
    return DIATONIC_LADDER.index(natural)

def pitch_to_abc(pitch: str) -> str:
    """Convert 'F#3'/'Bb4'/'C5' to ABC pitch token (used inside chord brackets)."""
    m = re.match(r'^([A-Ga-g])([#b]?)(\d)$', pitch)
    if not m: raise ValueError(f"bad pitch: {pitch}")
    letter, accid, octave = m.group(1).upper(), m.group(2), int(m.group(3))
    accid_tok = {"#":"^", "b":"_", "":""}[accid]
    if octave <= 4:
        commas = "," * (4 - octave)
        return f"{accid_tok}{letter}{commas}"
    else:
        apos = "'" * (octave - 5)
        return f"{accid_tok}{letter.lower()}{apos}"

# ----- Verovio render -----

def render_chord_staff(boundary_pitches, clef: str = "treble"):
    """Render a chord containing all boundary pitches. Returns (svg, viewBox tuple)."""
    abc_chord = " ".join(pitch_to_abc(p) for p in boundary_pitches)
    abc = f"X:1\nM:none\nL:1/1\nK:C clef={clef}\n[{abc_chord}] |\n"
    tk = verovio.toolkit()
    tk.setOptions({
        "pageWidth": 320, "pageHeight": 400, "scale": 40,
        "adjustPageHeight": True, "header": "none", "footer": "none",
        "spacingStaff": 6, "font": "Leipzig", "inputFrom": "abc",
    })
    tk.loadData(abc)
    svg = tk.renderToSVG(1)
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    vb_parts = [float(x) for x in vb.split()]
    return svg, vb_parts

def strip_outer_svg(svg_str: str) -> str:
    """Strip BOTH the outer <svg> wrapper AND the inner <svg class='definition-scale'>
    wrapper that Verovio inserts. Without this the nested svg's own viewBox would
    fill the parent canvas, blowing up the staff to fit the entire outer area."""
    inner = re.sub(r'^.*?<svg[^>]*>', '', svg_str, count=1, flags=re.DOTALL)
    inner = re.sub(r'<svg [^>]*class="definition-scale"[^>]*>', '', inner, count=1)
    inner = re.sub(r'</svg>\s*</svg>\s*$', '', inner, count=1)
    inner = re.sub(r'</svg>\s*$', '', inner, count=1)
    return inner

def extract_pitch_y_map(inner_staff: str, pitches_low_to_high: list[str]) -> dict[str, float]:
    """Extract actual notehead y-positions and pair them with pitches.

    Verovio renders chord noteheads at distinct staff slots. After we dedupe
    boundary pitches by natural_index, every entry in `pitches_low_to_high`
    occupies a unique staff slot, so the count of unique notehead ys matches.
    We pair sorted-ascending-pitch with sorted-descending-y (low pitch = high y).
    """
    notehead_ys = [
        float(y) + PAGE_MARGIN_Y for y in re.findall(
            r'class="notehead"[^>]*>\s*<use[^>]*transform="translate\([\d.-]+,\s*([\d.-]+)\)',
            inner_staff,
        )
    ]
    if not notehead_ys:
        raise RuntimeError("no noteheads found in Verovio output")
    unique_ys_desc = sorted(set(notehead_ys), reverse=True)  # high y first = low pitch first
    if len(unique_ys_desc) != len(pitches_low_to_high):
        raise RuntimeError(
            f"notehead count mismatch: expected {len(pitches_low_to_high)} unique ys, "
            f"got {len(unique_ys_desc)}. Pitches: {pitches_low_to_high}"
        )
    return dict(zip(pitches_low_to_high, unique_ys_desc))

def pitch_to_y(pitch: str, pitch_y_map: dict[str, float]) -> float:
    """Look up a pitch's y. If not in the map, interpolate by diatonic step
    from the nearest known pitch."""
    if pitch in pitch_y_map:
        return pitch_y_map[pitch]
    target = natural_index(pitch)
    nearest = min(pitch_y_map.keys(), key=lambda p: abs(natural_index(p) - target))
    return pitch_y_map[nearest] - (target - natural_index(nearest)) * DIATONIC_STEP_INTERNAL

def extract_chord_x(inner_staff: str) -> float:
    note_xforms = re.findall(
        r'class="notehead"[^>]*>\s*<use[^>]*transform="translate\(([\d.-]+),\s*([\d.-]+)\)',
        inner_staff,
    )
    if not note_xforms:
        raise RuntimeError("no noteheads found in Verovio output")
    return float(note_xforms[0][0]) + PAGE_MARGIN_X

# ----- Helpers -----

def _xml_escape(s: str) -> str:
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def _pretty_pitch(p: str) -> str:
    return p.replace("#","♯").replace("b","♭")

# ----- Main builder -----

def build_range_svg(spec: dict, out_path: str):
    inst = spec["instrument"]
    clef = inst.get("clef", "treble")
    zones = spec["zones"]                                         # YAML order: low → high

    # Pick boundary pitches for the chord. Two zones with adjacent edges (like
    # "ends at C4" / "starts at C♯4") share a staff slot, so we'd prefer the
    # natural — easier to read on the staff. Add HIGH edges first, then LOW edges,
    # then dedupe by natural_index so the natural (which usually appears as a high
    # edge) wins.
    spec_anchors = spec.get("range_anchors")  # optional explicit override
    if spec_anchors:
        candidates = list(spec_anchors)
    else:
        candidates = [z["written_range"][1] for z in zones] + [z["written_range"][0] for z in zones]
    boundary_pitches = []
    seen = set()
    for p in candidates:
        idx = natural_index(p)
        if idx not in seen:
            boundary_pitches.append(p); seen.add(idx)

    # Sort low to high so we can pair with extracted ys.
    boundary_pitches.sort(key=natural_index)

    staff_svg, (vbx, vby, vbw, vbh) = render_chord_staff(boundary_pitches, clef=clef)
    inner_staff = strip_outer_svg(staff_svg)

    pitch_y = extract_pitch_y_map(inner_staff, boundary_pitches)
    chord_x = extract_chord_x(inner_staff)
    note_ys = {p: pitch_y[p] for p in boundary_pitches}

    # ----- Outer canvas geometry (uses Verovio internal coords) -----
    title_h_int  = 700
    legend_w_int = 9000
    pad_int      = 200

    # Legend content sets a minimum vertical extent: it has a header, then
    # per-zone (label-line + blurb-line) blocks. We compute its bottom so the
    # footer can sit safely below.
    LEGEND_HEADER_GAP = 460
    LEGEND_BLOCK_H    = 720           # per zone (label + blurb)
    legend_bottom_int = vby + 60 + LEGEND_HEADER_GAP + LEGEND_BLOCK_H * len(zones)

    staff_bottom_int = vby + vbh
    content_bottom = max(staff_bottom_int, legend_bottom_int)
    footer_h_int   = 700              # space reserved below the bottom of content

    canvas_x = vbx - pad_int - 1200
    canvas_y = vby - title_h_int
    canvas_w = (vbw + 1200) + pad_int + legend_w_int + pad_int
    canvas_h = (content_bottom - vby) + title_h_int + footer_h_int

    legend_x = vbx + vbw + pad_int

    # Display size in pixels — pick a width that maps internal units cleanly.
    display_w = 720
    display_h = round(display_w * canvas_h / canvas_w)

    # Color zone bands (drawn behind staff)
    zone_x_left  = canvas_x + 1200            # roughly a bit to the right of pitch labels
    zone_x_right = vbx + vbw - 80
    zone_rects = []
    for z in zones:
        lo, hi = z["written_range"]
        zone_rects.append({
            "y_top":    pitch_to_y(hi, pitch_y) - DIATONIC_STEP_INTERNAL/2,
            "y_bottom": pitch_to_y(lo, pitch_y) + DIATONIC_STEP_INTERNAL/2,
            "fill": z["color"],
            "stroke": z.get("border", "#888"),
            "data": z,
        })

    out = []
    out.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{display_w}" height="{display_h}" '
        f'viewBox="{canvas_x:.0f} {canvas_y:.0f} {canvas_w:.0f} {canvas_h:.0f}">'
    )
    out.append(
        f'  <rect x="{canvas_x:.0f}" y="{canvas_y:.0f}" '
        f'width="{canvas_w:.0f}" height="{canvas_h:.0f}" fill="#FAFAFA"/>'
    )

    # Title
    title = f"{inst['name']} — Written Range &amp; Registers"
    out.append(
        f'  <text x="{canvas_x + pad_int + 200:.0f}" y="{vby - 240:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="280" font-weight="bold" fill="#222">{title}</text>'
    )
    sub = f"{clef} clef · {inst.get('transposition_blurb','')}"
    out.append(
        f'  <text x="{canvas_x + canvas_w - pad_int:.0f}" y="{vby - 240:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="200" font-style="italic" fill="#666" text-anchor="end">{_xml_escape(sub)}</text>'
    )

    # Color zones
    for zr in zone_rects:
        out.append(
            f'  <rect x="{zone_x_left:.0f}" y="{zr["y_top"]:.0f}" '
            f'width="{zone_x_right - zone_x_left:.0f}" height="{zr["y_bottom"] - zr["y_top"]:.0f}" '
            f'fill="{zr["fill"]}" opacity="0.55"/>'
        )

    # Verovio engraved staff (clef + lines + ledgers + chord noteheads)
    out.append('  <g class="engraved-staff">')
    out.append(inner_staff)
    out.append('  </g>')

    # Pitch labels next to each notehead (to the right of the stacked chord).
    # Notehead glyph is ~200 internal units wide; push labels past its right edge.
    label_x = chord_x + 380
    for p, y in note_ys.items():
        out.append(
            f'  <text x="{label_x:.0f}" y="{y + 70:.0f}" '
            f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
            f'font-size="200" font-weight="bold" fill="#222">{_pretty_pitch(p)}</text>'
        )

    # Right-side legend — HIGH to LOW (top of diagram corresponds to top of legend)
    legend_zones = sorted(zone_rects, key=lambda z: z["y_top"])
    ly = vby + 60
    out.append(
        f'  <text x="{legend_x:.0f}" y="{ly:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="240" font-weight="bold" fill="#222">Registers (written) — high to low</text>'
    )
    ly += 460
    for zr in legend_zones:
        z = zr["data"]
        out.append(
            f'  <rect x="{legend_x:.0f}" y="{ly - 200:.0f}" width="280" height="240" '
            f'fill="{zr["fill"]}" stroke="{zr["stroke"]}" opacity="0.85"/>'
        )
        lo, hi = z["written_range"]
        rng = f'({_pretty_pitch(lo)}–{_pretty_pitch(hi)})'
        label = f"{_xml_escape(z['name'])}  {rng}"
        out.append(
            f'  <text x="{legend_x + 360:.0f}" y="{ly:.0f}" '
            f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
            f'font-size="200" font-weight="bold" fill="#222">{label}</text>'
        )
        danger = z.get("danger","")
        d_color = "#777" if danger == "✓" else ("#D33" if "!" in danger else "#888")
        out.append(
            f'  <text x="{canvas_x + canvas_w - pad_int:.0f}" y="{ly:.0f}" '
            f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
            f'font-size="200" font-weight="bold" fill="{d_color}" text-anchor="end">{_xml_escape(danger)}</text>'
        )
        ly += 260
        out.append(
            f'  <text x="{legend_x + 360:.0f}" y="{ly:.0f}" '
            f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
            f'font-size="170" fill="#444">{_xml_escape(z["blurb"])}</text>'
        )
        ly += 460

    # Footer — placed below the deeper of (staff bottom, legend bottom)
    fy = content_bottom + 320
    sounding = inst.get("sounding_blurb", "")
    out.append(
        f'  <line x1="{canvas_x + pad_int:.0f}" y1="{fy - 240:.0f}" '
        f'x2="{canvas_x + canvas_w - pad_int:.0f}" y2="{fy - 240:.0f}" '
        f'stroke="#CCC" stroke-width="12"/>'
    )
    out.append(
        f'  <text x="{canvas_x + pad_int + 200:.0f}" y="{fy:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="190" font-weight="bold" fill="#222">Sounding range:</text>'
    )
    out.append(
        f'  <text x="{canvas_x + pad_int + 2100:.0f}" y="{fy:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="190" fill="#333">{_xml_escape(sounding)}</text>'
    )
    out.append(
        f'  <text x="{canvas_x + pad_int + 200:.0f}" y="{fy + 280:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="180" font-weight="bold" fill="#666">Legend:</text>'
    )
    out.append(
        f'  <text x="{canvas_x + pad_int + 1100:.0f}" y="{fy + 280:.0f}" '
        f'font-family=\'Gill Sans, "Helvetica Neue", Helvetica, Arial, sans-serif\' '
        f'font-size="180" fill="#666">✓ idiomatic     ! costs stamina     !! treat with care     !!! specialist     x rare/effect only</text>'
    )

    out.append('</svg>')
    svg_str = "\n".join(out)
    with open(out_path, "w") as f:
        f.write(svg_str)
    return svg_str

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("spec_yaml")
    ap.add_argument("out_svg")
    args = ap.parse_args()
    with open(args.spec_yaml) as f:
        spec = yaml.safe_load(f)
    build_range_svg(spec, args.out_svg)
    print("WROTE", args.out_svg)
