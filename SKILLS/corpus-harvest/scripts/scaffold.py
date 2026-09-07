#!/usr/bin/env python3
"""corpus-harvest scaffolder: create one program's staging tree.

Creates <staging-root>/ with RAW/ SEGMENTS/ TXT/ EXTRACTIONS/ STATE.json
PROGRESS.md RUNBOOK.md. The runbook is rendered from assets/RUNBOOK_TEMPLATE.md
with the program's REAL values — no placeholders survive, and no corpus
estimates are ever written (measured values live in PROGRESS.md after Stage 1).

Guards (adversarial-tested):
- refuses any path containing a forbidden component (INBOUND_QUARANTINE,
  02_SOURCE_MATERIAL, TEXTBOOK, 00_CONSTITUTION, 04_ARCHIVE, 99_ARCHIVE),
  checked on the RESOLVED path — traversal cannot sneak past;
- refuses a non-empty existing target;
- intended home is __MY_BOOK/_CT_RESEARCH_INTAKE/<source_slug>/ (Doug's ruling),
  but the guard is by prohibition, not prescription, so fixtures and self-tests
  can scaffold in temp dirs.

--self-test scaffolds a 12tone-equivalent program in a temp dir and verifies:
tree complete, STATE valid, runbook fully substituted, runbook carries no
superseded corpus estimates.
"""
import argparse, os, shutil, sys, tempfile

import state as S

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
FORBIDDEN = S.FORBIDDEN_PATH_PARTS          # single source of truth: state.py
CANONICAL_PARENT = S.CANONICAL_PARENT


def check_path(target, source_slug, fixture_mode=False):
    resolved = os.path.realpath(os.path.abspath(target))
    bad = set(resolved.split(os.sep)) & FORBIDDEN
    if bad:
        raise SystemExit(f"REFUSED: staging root resolves into forbidden "
                         f"location(s) {sorted(bad)}: {resolved}")
    parent = os.path.basename(os.path.dirname(resolved))
    leaf = os.path.basename(resolved)
    canonical = parent == CANONICAL_PARENT and leaf == source_slug
    if not fixture_mode:
        # Canonical containment (Doug's ruling 2026-08-25): real programs live
        # ONLY at .../_CT_RESEARCH_INTAKE/<source_slug>/. Tests must say so
        # explicitly with --fixture-mode; there is no silent third option.
        if not canonical:
            raise SystemExit(
                f"REFUSED: staging root must be …/{CANONICAL_PARENT}/{source_slug}/ "
                f"(got …/{parent}/{leaf}). Use --fixture-mode only for isolated "
                "temp test workspaces.")
    elif not (canonical or S.is_fixture_territory(resolved)):
        # fixture mode is confined to sanctioned isolated territory: the
        # system temp tree, or a root explicitly marked with the sentinel
        # file (2026-08-28 reviews, findings 3 and dry-run 2)
        raise SystemExit(
            f"REFUSED: --fixture-mode only scaffolds inside the system temp "
            f"tree or under a directory marked with {S.FIXTURE_SENTINEL}; "
            f"got: {resolved}")
    if os.path.exists(resolved) and os.listdir(resolved):
        raise SystemExit(f"REFUSED: {resolved} exists and is not empty — "
                         "corpus-harvest never adopts a folder it did not create")
    return resolved


def render_runbook(values):
    tpl_path = os.path.join(ASSETS, "RUNBOOK_TEMPLATE.md")
    with open(tpl_path, encoding="utf-8") as f:
        tpl = f.read()
    out = tpl
    for k, v in values.items():
        out = out.replace("{{%s}}" % k, str(v))
    if "{{" in out:
        leftover = sorted({t.split("}}")[0] for t in out.split("{{")[1:]})
        raise SystemExit(f"REFUSED: unfilled runbook placeholders: {leftover}")
    return out


def scaffold(target, source_slug, adapter, locator, assistant, skill_version,
             word_limit=90000, token_ceiling=120000, fixture_mode=False):
    resolved = check_path(target, source_slug, fixture_mode)
    os.makedirs(resolved, exist_ok=True)
    for d in ("RAW", "SEGMENTS", "TXT", "EXTRACTIONS"):
        os.makedirs(os.path.join(resolved, d))
    st = S.init_state(resolved, source_slug, adapter, locator, assistant,
                      skill_version, word_limit, token_ceiling)
    S.write_progress(resolved, st)
    rb = render_runbook({
        "source_slug": source_slug, "source_locator": locator,
        "adapter": adapter, "staging_root": resolved,
        "skill_version": skill_version, "generated_at": st["program"]["created_at"],
        "word_limit": word_limit, "token_ceiling": token_ceiling,
    })
    with open(os.path.join(resolved, "RUNBOOK.md"), "w", encoding="utf-8") as f:
        f.write(rb)
    return resolved


def self_test():
    tmp = tempfile.mkdtemp(prefix="corpus_harvest_selftest_")
    try:
        target = os.path.join(tmp, "_CT_RESEARCH_INTAKE", "twelvetone-equivalent")
        root = scaffold(target, "twelvetone-equivalent", "youtube",
                        "https://www.youtube.com/@12tonevideos",
                        "scaffold-self-test", "0.1.0-build")
        errors = []
        for p in ("RAW", "SEGMENTS", "TXT", "EXTRACTIONS",
                  "STATE.json", "PROGRESS.md", "RUNBOOK.md"):
            if not os.path.exists(os.path.join(root, p)):
                errors.append(f"missing {p}")
        st = S.load_state(root)
        errors += S.validate_state(st)
        with open(os.path.join(root, "RUNBOOK.md"), encoding="utf-8") as f:
            rb = f.read()
        if "{{" in rb:
            errors.append("unfilled placeholder in runbook")
        # behavioral match with the 12tone reference program, minus its flaws:
        for token in ("Anchor", "KICKOFF PROMPT", "Master Preamble",
                      "Never modify RAW/", "GATE 1", "GATE 2"):
            if token not in rb:
                errors.append(f"runbook missing required element: {token}")
        # superseded estimates must not be reproduced (the reference runbook's
        # ~660k / ~8 chunks estimates were wrong; generated runbooks carry none)
        for stale in ("660,000", "660k", "~8 chunks", "1,153", "396"):
            if stale in rb:
                errors.append(f"runbook reproduces superseded estimate: {stale}")
        # guard behavior: forbidden dir, and noncanonical location without
        # fixture mode, must both refuse
        try:
            scaffold(os.path.join(tmp, "INBOUND_QUARANTINE", "x"),
                     "x", "youtube", "u", "t", "0")
            errors.append("guard failed: scaffolded inside INBOUND_QUARANTINE")
        except SystemExit:
            pass
        try:
            scaffold(os.path.join(tmp, "random_folder", "y"),
                     "y", "youtube", "u", "t", "0")
            errors.append("guard failed: scaffolded outside _CT_RESEARCH_INTAKE "
                          "without --fixture-mode")
        except SystemExit:
            pass
        if errors:
            for e in errors:
                print(f"SELF-TEST FAIL: {e}", file=sys.stderr)
            return 1
        print("SELF-TEST PASS: tree, STATE, runbook substitution, "
              "no-superseded-estimates, and path guard all verified "
              "(temp workspace only; nothing touched outside it)")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--staging-root")
    ap.add_argument("--source-slug")
    ap.add_argument("--adapter", choices=["youtube", "local-folder"])
    ap.add_argument("--locator")
    ap.add_argument("--assistant")
    ap.add_argument("--skill-version")
    ap.add_argument("--word-limit", type=int, default=90000)
    ap.add_argument("--token-ceiling", type=int, default=120000)
    ap.add_argument("--fixture-mode", action="store_true",
                    help="EXPLICIT test-only bypass of the canonical "
                         "_CT_RESEARCH_INTAKE/<source_slug>/ requirement; "
                         "forbidden-directory and emptiness guards still apply")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    for req in ("staging_root", "source_slug", "adapter", "locator",
                "assistant", "skill_version"):
        if not getattr(a, req):
            ap.error(f"--{req.replace('_', '-')} is required (or use --self-test)")
    root = scaffold(a.staging_root, a.source_slug, a.adapter, a.locator,
                    a.assistant, a.skill_version, a.word_limit, a.token_ceiling,
                    fixture_mode=a.fixture_mode)
    print(f"scaffolded {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
