#!/usr/bin/env python3
"""Validate an instrument YAML spec before the build pipeline runs.

Catches typos and schema drift in ~50ms instead of after a partial build.
Exit code 0 = clean; non-zero = errors printed.

Usage:  python3 validate.py <spec.yaml>
"""
from __future__ import annotations
import argparse, re, sys, yaml

PITCH_RE = re.compile(r"^[A-Ga-g][#b]?\d$")
HEX_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
VALID_CLEFS = {"treble", "bass"}
VALID_DANGER = {"✓", "!", "!!", "!!!", "x"}
VALID_INTERVALS = {  # interval label → (semitones, diatonic steps)
    "P1": (0, 0),
    "m2": (1, 1), "M2": (2, 1),
    "m3": (3, 2), "M3": (4, 2),
    "P4": (5, 3), "A4": (6, 3),
    "d5": (6, 4), "P5": (7, 4),
    "m6": (8, 5), "M6": (9, 5),
    "m7": (10, 6), "M7": (11, 6),
    "P8": (12, 7),
}

DIATONIC_LADDER = [
    f"{n}{o}" for o in range(0, 9) for n in ["C","D","E","F","G","A","B"]
]
SEMITONE_VALUES = {"C":0, "D":2, "E":4, "F":5, "G":7, "A":9, "B":11}


def pitch_to_midi(pitch: str) -> int:
    m = re.match(r"^([A-G])([#b]?)(\d)$", pitch.upper().replace("B♭","Bb").replace("♯","#").replace("♭","b"))
    if not m:
        raise ValueError(f"unparseable pitch: {pitch}")
    letter, accid, octave = m.group(1), m.group(2), int(m.group(3))
    semis = SEMITONE_VALUES[letter] + (1 if accid == "#" else -1 if accid == "b" else 0)
    return (octave + 1) * 12 + semis  # MIDI: C-1=0, C4=60


class Errors:
    def __init__(self):
        self.items: list[str] = []

    def add(self, msg: str):
        self.items.append(msg)

    def fatal(self, msg: str):
        self.items.append(f"FATAL: {msg}")
        self.report()
        sys.exit(1)

    def report(self):
        if not self.items:
            print("✓ spec validates clean")
            return
        print(f"✗ {len(self.items)} issue(s):")
        for it in self.items:
            print(f"  • {it}")


def check_pitch(p, where, errs: Errors):
    if not isinstance(p, str) or not PITCH_RE.match(p):
        errs.add(f"{where}: invalid pitch {p!r} (expected like 'F#3' or 'Bb4')")


def check_hex(c, where, errs: Errors):
    if not isinstance(c, str) or not HEX_RE.match(c):
        errs.add(f"{where}: invalid hex color {c!r} (expected '#RRGGBB')")


def validate(spec: dict) -> Errors:
    errs = Errors()

    # --- instrument ---
    inst = spec.get("instrument") or {}
    if not isinstance(inst, dict):
        errs.fatal("`instrument` block missing or not a mapping")
    for key in ("name", "family", "clef"):
        if not inst.get(key):
            errs.add(f"instrument.{key} required")
    clef = inst.get("clef", "treble")
    if clef not in VALID_CLEFS:
        errs.add(f"instrument.clef: {clef!r} not in {VALID_CLEFS}")

    # --- transposition (optional but if present, validate arithmetic) ---
    t = inst.get("transposition") or {}
    if t:
        interval = t.get("written_higher_than_concert")
        if interval and interval != "P1":
            if interval not in VALID_INTERVALS:
                errs.add(f"transposition.written_higher_than_concert: unknown interval {interval!r}")
            wp = t.get("written_example_pitches") or []
            cp = t.get("concert_example_pitches") or []
            if len(wp) != len(cp):
                errs.add(f"transposition: written/concert pitch counts differ ({len(wp)} vs {len(cp)})")
            for p in wp: check_pitch(p, "transposition.written_example_pitches", errs)
            for p in cp: check_pitch(p, "transposition.concert_example_pitches", errs)
            if interval in VALID_INTERVALS and len(wp) == len(cp):
                expected_semis = VALID_INTERVALS[interval][0]
                for w, c in zip(wp, cp):
                    if PITCH_RE.match(w) and PITCH_RE.match(c):
                        try:
                            diff = pitch_to_midi(w) - pitch_to_midi(c)
                            if diff != expected_semis:
                                errs.add(
                                    f"transposition: {w} → {c} is {diff} semitones, "
                                    f"but interval {interval} expects {expected_semis}"
                                )
                        except ValueError:
                            pass  # check_pitch already flagged

    # --- zones ---
    zones = spec.get("zones") or []
    if not zones:
        errs.add("zones: at least one zone required")
    for i, z in enumerate(zones):
        where = f"zones[{i}]"
        for k in ("name", "written_range", "color", "danger", "blurb"):
            if k not in z:
                errs.add(f"{where}.{k} required")
        rng = z.get("written_range")
        if not (isinstance(rng, list) and len(rng) == 2):
            errs.add(f"{where}.written_range: expected [low, high]")
        else:
            for p in rng: check_pitch(p, f"{where}.written_range", errs)
        if "color" in z: check_hex(z["color"], f"{where}.color", errs)
        if "border" in z: check_hex(z["border"], f"{where}.border", errs)
        d = z.get("danger")
        if d is not None and d not in VALID_DANGER:
            errs.add(f"{where}.danger: {d!r} not in {VALID_DANGER}")

    # --- new optional blocks (light validation) ---
    for block in ("voice", "listen", "pitfalls", "asides", "players_pov", "history"):
        if block in spec and spec[block] is None:
            errs.add(f"{block}: present but empty (omit the key instead)")

    pov = spec.get("players_pov")
    if pov and not isinstance(pov, dict):
        errs.add("players_pov: expected a mapping with 'paragraph'")

    hist = spec.get("history")
    if hist:
        if not isinstance(hist, dict):
            errs.add("history: expected a mapping with optional origin/timeline/family_tree")
        else:
            tl = hist.get("timeline")
            if tl is not None:
                if not isinstance(tl, list):
                    errs.add("history.timeline: expected a list of {era, note}")
                else:
                    for i, item in enumerate(tl):
                        if not isinstance(item, dict) or "era" not in item or "note" not in item:
                            errs.add(f"history.timeline[{i}]: missing 'era' or 'note'")

    voice = spec.get("voice")
    if voice and not isinstance(voice, dict):
        errs.add("voice: expected a mapping with 'paragraph' and optional 'signature_gestures'/'archetypal_uses'")

    listen = spec.get("listen")
    if listen:
        if not isinstance(listen, list):
            errs.add("listen: expected a list of {piece, role}")
        else:
            for i, item in enumerate(listen):
                if not isinstance(item, dict) or "piece" not in item or "role" not in item:
                    errs.add(f"listen[{i}]: missing 'piece' or 'role'")

    pitfalls = spec.get("pitfalls")
    if pitfalls and not isinstance(pitfalls, list):
        errs.add("pitfalls: expected a list of strings")

    asides = spec.get("asides")
    if asides:
        if not isinstance(asides, list):
            errs.add("asides: expected a list")
        else:
            for i, a in enumerate(asides):
                if not isinstance(a, dict):
                    errs.add(f"asides[{i}]: expected a mapping")
                    continue
                for k in ("kind", "title", "body"):
                    if k not in a:
                        errs.add(f"asides[{i}].{k} required")
                if a.get("kind") and a["kind"] not in {"pedantry", "history", "family-tree"}:
                    errs.add(f"asides[{i}].kind: {a['kind']!r} not in pedantry|history|family-tree")

    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec_yaml")
    args = ap.parse_args()
    with open(args.spec_yaml) as f:
        spec = yaml.safe_load(f)
    errs = validate(spec)
    errs.report()
    sys.exit(0 if not errs.items else 2)


if __name__ == "__main__":
    main()
