#!/usr/bin/env python3
"""Print a deterministic CHECKSUMS.txt body without modifying the package."""

from __future__ import annotations

import hashlib
import os
import stat
import sys
from pathlib import Path, PurePosixPath


MANIFEST = "CHECKSUMS.txt"


class ManifestError(RuntimeError):
    pass


def _read_regular(path: Path) -> bytes:
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(path, flags)
    except OSError as exc:
        raise ManifestError(
            f"cannot open without following symlinks: {path}: {exc}"
        ) from exc
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise ManifestError(f"not a regular file: {path}")
        chunks = []
        while True:
            chunk = os.read(fd, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(fd)


def generate(root_value: os.PathLike[str] | str) -> str:
    root = Path(os.path.abspath(os.fspath(root_value)))
    try:
        root_info = os.lstat(root)
    except FileNotFoundError as exc:
        raise ManifestError(f"package root is missing: {root}") from exc
    if stat.S_ISLNK(root_info.st_mode) or not stat.S_ISDIR(root_info.st_mode):
        raise ManifestError(f"package root must be a real directory: {root}")

    files: list[tuple[str, str]] = []
    stack = [(root, PurePosixPath())]
    while stack:
        directory, relative_dir = stack.pop()
        for entry in sorted(
            os.scandir(directory), key=lambda item: item.name, reverse=True
        ):
            relative = relative_dir / entry.name
            name = relative.as_posix()
            info = entry.stat(follow_symlinks=False)
            if stat.S_ISLNK(info.st_mode):
                raise ManifestError(f"symlink in package: {name}")
            if stat.S_ISDIR(info.st_mode):
                stack.append((Path(entry.path), relative))
                continue
            if not stat.S_ISREG(info.st_mode):
                raise ManifestError(f"non-regular entry in package: {name}")
            if name == MANIFEST:
                continue
            digest = hashlib.sha256(_read_regular(Path(entry.path))).hexdigest()
            files.append((name, digest))
    return "".join(f"{digest}  {name}\n" for name, digest in sorted(files))


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        print("usage: generate_manifest.py [skill-root]", file=sys.stderr)
        return 2
    root = Path(args[0]) if args else Path(__file__).resolve().parents[1]
    try:
        sys.stdout.write(generate(root))
    except ManifestError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
