#!/usr/bin/env python3
"""End-to-end orchestrator for the composer-instrument-guide skill.

Usage:  python3 run.py <spec.yaml> <out_dir> [--size 1|2|3|full|all]

Reads an instrument YAML spec, renders the range diagram (Verovio + zone overlay)
and transposition demo (Verovio), then calls Node to assemble the docx in Doug's
house style. Outputs everything in <out_dir>:
   <Instrument>_Field_Guide.docx        — the handout (default tier-3 build)
   <Instrument>_Range_Registers.svg     — the standalone range graphic
   range.png, transp_written.png,
   transp_concert.png                   — intermediate assets

--size controls how much content is included:
   1     → tier-1 only (essential): 1-page version, suffix _1pg
   2     → tiers 1-2 (standard):    2-page version, suffix _2pg
   3     → tiers 1-3 (rich)         DEFAULT, no suffix (canonical handout)
   full  → all tiers including extended content, suffix _full
   all   → produces 1pg + 2pg + 3pg in one pass (always suffixed)
"""
import argparse, os, sys, json, subprocess, datetime

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)  # so `import validate` works regardless of cwd

DEFAULT_LOG_PATH = "/Users/dougsmith/Docs/__MY_BOOK/Cowork_log_file.md"

SIZE_MAP = {       # --size value → (max_tier, filename_suffix)
    "1":    (1, "_1pg"),
    "2":    (2, "_2pg"),
    "3":    (3, ""),         # canonical, no suffix
    "full": (4, "_full"),
}


def run(cmd, **kw):
    print(">", " ".join(cmd))
    return subprocess.run(cmd, check=True, **kw)


def append_cowork_log(inst_name, out_dir, sizes_built):
    """Append a one-line build entry to the Cowork log if the path is writable."""
    log_path = os.environ.get("COWORK_LOG_PATH", DEFAULT_LOG_PATH)
    log_dir = os.path.dirname(log_path)
    if not log_dir or not os.path.exists(log_dir):
        return  # silently skip when log dir isn't there (e.g., bare sandbox)
    try:
        date = datetime.date.today().isoformat()
        sizes_str = ", ".join(sizes_built)
        with open(log_path, "a") as f:
            f.write(
                f"\n## {date} — {inst_name} field guide built\n"
                f"- composer-instrument-guide produced {sizes_str} → {out_dir}\n"
            )
    except OSError:
        pass  # never fail the build over the log


def load_family_config(family):
    """Read families/<family>.yaml if it exists, else return None."""
    if not family:
        return None
    path = os.path.join(ROOT, "families", f"{family}.yaml")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return yaml.safe_load(f)


def build_one_size(args, spec, family_config, max_tier, filename_suffix,
                   range_png, written_png, concert_png):
    """Build the docx for a single tier ceiling. Returns the docx filename."""
    spec_for_size = dict(spec)
    spec_for_size["_assets"] = {
        "range_png": range_png,
        "transp_written_png": written_png,
        "transp_concert_png": concert_png,
    }
    spec_for_size["_render_size"] = max_tier
    spec_for_size["_filename_suffix"] = filename_suffix
    if family_config:
        spec_for_size["_family_config"] = family_config

    spec_json = os.path.join(args.out_dir, f"_spec{filename_suffix or '_3pg'}.json")
    with open(spec_json, "w") as f:
        json.dump(spec_for_size, f, default=str)

    run(["node", os.path.join(SCRIPTS, "build_doc.js"), spec_json, args.out_dir])

    try: os.remove(spec_json)
    except OSError: pass

    inst_name = spec["instrument"]["name"]
    safe = "".join(c if c.isalnum() else "_" for c in inst_name)
    return f"{safe}_Field_Guide{filename_suffix}.docx"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec_yaml")
    ap.add_argument("out_dir")
    ap.add_argument("--size", default="3",
                    help="1|2|3|full|all  (default: 3 — the canonical 3-page build)")
    args = ap.parse_args()

    if args.size not in SIZE_MAP and args.size != "all":
        print(f"unknown --size {args.size!r}; use 1, 2, 3, full, or all", file=sys.stderr)
        sys.exit(2)

    os.makedirs(args.out_dir, exist_ok=True)

    # 0) Validate the spec up front so typos surface before any rendering.
    from validate import validate
    with open(args.spec_yaml) as f:
        spec = yaml.safe_load(f)
    errs = validate(spec)
    if errs.items:
        errs.report()
        sys.exit(2)

    inst_name = spec["instrument"]["name"]
    safe = "".join(c if c.isalnum() else "_" for c in inst_name)

    # 0a) Load family config (if any) — drives section order / headings / defaults
    family_config = load_family_config(spec.get("instrument", {}).get("family"))

    # 1) Build range diagram (SVG) — same for all sizes
    range_svg = os.path.join(args.out_dir, f"{safe}_Range_Registers.svg")
    run(["python3", os.path.join(SCRIPTS, "build_range.py"), args.spec_yaml, range_svg])

    # 2) Rasterize range to PNG (cairosvg)
    import cairosvg
    range_png = os.path.join(args.out_dir, "range.png")
    cairosvg.svg2png(url=range_svg, write_to=range_png, output_width=1440)

    # 3) Transposition snippets (only for transposing instruments) — same for all sizes
    transp = spec["instrument"].get("transposition", {})
    written_png = concert_png = None
    if transp.get("written_higher_than_concert") and transp["written_higher_than_concert"] != "P1":
        run(["python3", os.path.join(SCRIPTS, "build_transposition.py"),
             args.spec_yaml, args.out_dir, "--stem", "transp"])
        written_png = os.path.join(args.out_dir, "transp_written.png")
        concert_png = os.path.join(args.out_dir, "transp_concert.png")

    # 4) Build docx(s) — one per requested size
    if args.size == "all":
        size_specs = [("1", *SIZE_MAP["1"]), ("2", *SIZE_MAP["2"]), ("3", *SIZE_MAP["3"])]
        # When --size all, ALWAYS suffix the canonical build too, for consistency
        size_specs = [(label, max_tier, suffix or "_3pg") for (label, max_tier, suffix) in size_specs]
    else:
        max_tier, suffix = SIZE_MAP[args.size]
        size_specs = [(args.size, max_tier, suffix)]

    files_built = []
    for label, max_tier, suffix in size_specs:
        fname = build_one_size(args, spec, family_config, max_tier, suffix,
                               range_png, written_png, concert_png)
        files_built.append(fname)

    # 5) Append Cowork log
    append_cowork_log(inst_name, args.out_dir, files_built)

    print(f"\n✓ Done. Built {len(files_built)} file(s) in {args.out_dir}:")
    for f in files_built: print(f"   {f}")


if __name__ == "__main__":
    main()
