#!/usr/bin/env python3
"""Render side-by-side WRITTEN vs CONCERT pitch demo for a transposing instrument.

Reads spec.transposition from the YAML; writes two PNGs: <stem>_written.png and
<stem>_concert.png. Skips silently if the instrument is non-transposing
(transposition.written_higher_than_concert == 'P1').
"""
import argparse, yaml, verovio, cairosvg, os

def render(abc_str, out_png):
    tk = verovio.toolkit()
    tk.setOptions({
        "pageWidth": 900, "pageHeight": 220, "scale": 38,
        "adjustPageHeight": True, "header": "none", "footer": "none",
        "spacingStaff": 6, "font": "Leipzig", "inputFrom": "abc",
    })
    tk.loadData(abc_str)
    svg = tk.renderToSVG(1)
    svg_path = out_png.replace(".png", ".svg")
    with open(svg_path, "w") as f: f.write(svg)
    cairosvg.svg2png(url=svg_path, write_to=out_png, output_width=900)

import re as _re

def pitch_to_abc(pitch: str) -> str:
    """Convert a scientific pitch name like 'D5' or 'F#5' to an ABC pitch token.
    ABC convention: capital letters = below middle C; lowercase = above middle C.
    Commas lower an octave (e.g. 'C,' = C3); apostrophes raise (e.g. "c'" = C6)."""
    m = _re.match(r'^([A-Ga-g])([#b]?)(\d)$', pitch.strip())
    if not m:
        return pitch  # leave as-is; let ABC parser handle/error
    letter, accid, octave = m.group(1).upper(), m.group(2), int(m.group(3))
    accid_tok = {"#":"^", "b":"_", "":""}[accid]
    if octave <= 4:
        return f"{accid_tok}{letter}{',' * (4 - octave)}"
    else:
        return f"{accid_tok}{letter.lower()}{chr(39) * (octave - 5)}"

def build_transposition_pair(spec, out_dir, stem):
    inst = spec["instrument"]
    t = inst.get("transposition", {})
    if t.get("written_higher_than_concert", "P1") == "P1":
        return None
    written_pitches = t["written_example_pitches"]
    concert_pitches = t["concert_example_pitches"]
    written_key = t.get("written_example_key", "C")
    concert_key = t.get("concert_example_key", "C")
    w_chord = t.get("written_chord_label", written_key)
    c_chord = t.get("concert_chord_label", concert_key)

    # Convert scientific pitches (e.g. "D5") to proper ABC tokens (e.g. "d").
    # Then suffix duration 2 — at L:1/4 that's a half note, two of which fill 4/4.
    w_tokens = [pitch_to_abc(p) + "2" for p in written_pitches]
    c_tokens = [pitch_to_abc(p) + "2" for p in concert_pitches]
    abc_written = (
        f"X:1\nM:4/4\nL:1/4\nK:{written_key}\n"
        + f'"{w_chord}"' + " ".join(w_tokens) + " |"
    )
    abc_concert = (
        f"X:1\nM:4/4\nL:1/4\nK:{concert_key}\n"
        + f'"{c_chord}"' + " ".join(c_tokens) + " |"
    )
    written_png = os.path.join(out_dir, f"{stem}_written.png")
    concert_png = os.path.join(out_dir, f"{stem}_concert.png")
    render(abc_written, written_png)
    render(abc_concert, concert_png)
    return (written_png, concert_png)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("spec_yaml")
    ap.add_argument("out_dir")
    ap.add_argument("--stem", default="transp")
    args = ap.parse_args()
    with open(args.spec_yaml) as f:
        spec = yaml.safe_load(f)
    pair = build_transposition_pair(spec, args.out_dir, args.stem)
    print("WROTE", pair if pair else "(skipped: non-transposing)")
