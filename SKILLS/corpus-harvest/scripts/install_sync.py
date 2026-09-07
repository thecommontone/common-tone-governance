#!/usr/bin/env python3
"""corpus-harvest checksum-safe installer/synchronizer.

The plan (v0.3, Correction 2) requires per-assistant installed copies to sync
from the canonical home via a checksum manifest, where "a mismatch is
reported, not overwritten." This is that tool. Running it is mechanics;
WHERE it may be pointed is authorization — installation to
GOVERNANCE/SKILLS/ and per-assistant roots each require Doug's explicit word.

Modes:
  check    compare an installed copy against the package's CHECKSUMS.txt:
           reports identical / drifted / missing / extra files. Exit 0 only
           when the copy matches exactly.
  install  copy the package into an EMPTY (or nonexistent) destination and
           verify every file against CHECKSUMS.txt after copying. Refuses a
           non-empty destination — drift is never overwritten; a drifted
           copy is resolved by a human, not this tool.
"""
import argparse, hashlib, os, re, shutil, sys

EXCLUDE_DIRS = {"__pycache__"}
MANIFEST = "CHECKSUMS.txt"
_DIGEST = re.compile(r"^[0-9a-f]{64}$")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def _contained(root, rel):
    """Resolve rel against root and require containment; refuse symlinked
    entries. Returns the resolved absolute path."""
    p = os.path.realpath(os.path.join(root, rel))
    r = os.path.realpath(root)
    if not (p == r or p.startswith(r + os.sep)):
        raise SystemExit(f"REFUSED: manifest path escapes its root: {rel!r}")
    if os.path.islink(os.path.join(root, rel)):
        raise SystemExit(f"REFUSED: symlinked manifest entry: {rel!r}")
    return p


def read_manifest(package):
    """Parse and VALIDATE the manifest (2026-08-28 P0: manifests are input,
    not gospel). Rejects: malformed lines, invalid digests, absolute paths,
    '..' components, duplicate normalized names."""
    path = os.path.join(package, MANIFEST)
    if not os.path.isfile(path):
        raise SystemExit(f"REFUSED: package has no {MANIFEST}: {package}")
    entries = {}
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split(None, 1)
            if len(parts) != 2:
                raise SystemExit(f"REFUSED: malformed manifest line {n}")
            digest, name = parts
            if not _DIGEST.match(digest):
                raise SystemExit(f"REFUSED: invalid digest on manifest line {n}")
            name = name.lstrip("*")
            if os.path.isabs(name):
                raise SystemExit(f"REFUSED: absolute manifest path: {name!r}")
            norm = os.path.normpath(name)
            if norm.startswith("..") or f"..{os.sep}" in norm or norm == "..":
                raise SystemExit(f"REFUSED: parent-escaping manifest path: {name!r}")
            if norm in entries:
                raise SystemExit(f"REFUSED: duplicate manifest entry: {norm!r}")
            entries[norm] = digest
    return entries


def walk_files(root):
    """-> (files {rel: path}, symlinks [rel]). Symlinked files AND symlinked
    directory components are structural drift, detected via lstat — a
    symlink pointing at pristine content is still not an installed copy
    (2026-08-28 round-4 P1-5)."""
    out, symlinks = {}, []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        for d in list(dirnames):
            if d in EXCLUDE_DIRS:
                dirnames.remove(d)
            elif os.path.islink(os.path.join(dirpath, d)):
                symlinks.append(os.path.normpath(
                    os.path.join(".", os.path.relpath(os.path.join(dirpath, d), root))))
                dirnames.remove(d)
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.normpath(os.path.join(".", os.path.relpath(p, root)))
            if os.path.islink(p):
                symlinks.append(rel)
                continue
            out[rel] = p
    return out, symlinks


def check(package, dest):
    manifest = read_manifest(package)
    if not os.path.isdir(dest):
        print(f"MISSING: no installed copy at {dest}")
        return 2
    files, symlinks = walk_files(dest)
    files.pop(os.path.normpath(f"./{MANIFEST}"), None)
    drifted, missing = [], []
    for rel, digest in manifest.items():
        p = files.pop(rel, None)
        if p is None:
            if rel not in symlinks:
                missing.append(rel)
        elif sha256_file(p) != digest:
            drifted.append(rel)
    extra = sorted(files)
    if not (drifted or missing or extra or symlinks):
        print(f"OK: {dest} matches the package manifest "
              f"({len(manifest)} files verified, lstat-checked)")
        return 0
    for rel in symlinks:
        print(f"SYMLINK (structural drift, NOT followed): {rel}")
    for rel in drifted:
        print(f"DRIFT (reported, NOT overwritten): {rel}")
    for rel in missing:
        print(f"MISSING: {rel}")
    for rel in extra:
        print(f"EXTRA (not in manifest): {rel}")
    print("Resolution is a human decision — this tool never overwrites drift.",
          file=sys.stderr)
    return 1


def install(package, dest):
    manifest = read_manifest(package)
    resolved = os.path.realpath(os.path.abspath(dest))
    if os.path.exists(resolved) and os.listdir(resolved):
        raise SystemExit(f"REFUSED: {resolved} exists and is not empty — "
                         "install only into an empty destination; a drifted "
                         "copy is never overwritten")
    os.makedirs(resolved, exist_ok=True)
    for rel in manifest:
        src = _contained(package, rel)
        dst = _contained(resolved, rel)
        if not os.path.isfile(src):
            raise SystemExit(f"REFUSED: manifest names a missing source file: {rel}")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
    shutil.copy2(os.path.join(package, MANIFEST), os.path.join(resolved, MANIFEST))
    bad = [rel for rel, digest in manifest.items()
           if sha256_file(os.path.join(resolved, rel)) != digest]
    if bad:
        raise SystemExit(f"INSTALL FAILED verification: {bad}")
    print(f"installed {len(manifest)} files to {resolved}; all verified "
          "against the manifest")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=["check", "install"])
    ap.add_argument("--package", required=True,
                    help="canonical package dir (contains CHECKSUMS.txt)")
    ap.add_argument("--dest", required=True, help="installed-copy location")
    a = ap.parse_args(argv)
    if a.mode == "check":
        return check(a.package, a.dest)
    return install(a.package, a.dest)


if __name__ == "__main__":
    sys.exit(main())
