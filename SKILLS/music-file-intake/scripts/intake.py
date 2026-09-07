#!/usr/bin/env python3
"""Command-line boundary for the provider-neutral music-file-intake core."""

from __future__ import annotations

import argparse
import json
import sys

sys.dont_write_bytecode = True

from intake_core import (  # noqa: E402 - bytecode policy must precede local import
    SKILL_VERSION,
    IntakeError,
    transfer_handoff,
    validate_handoff,
)


def _root_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--staging-root",
        required=True,
        help="Exact corpus-harvest staging root containing STATE.json",
    )
    parser.add_argument(
        "--vault-root",
        required=True,
        help="Common Tone project root containing 02_SOURCE_MATERIAL",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="music-file-intake",
        description="Validate and atomically transfer a corpus-harvest Stage-5 allowlist.",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="Validate without writing")
    _root_arguments(check)
    transfer = commands.add_parser("transfer", help="Copy one validated atomic batch")
    _root_arguments(transfer)
    transfer.add_argument(
        "--invoked-by",
        required=True,
        help="Recorded protocol assertion identifying the supervising session",
    )
    commands.add_parser("version", help="Print the fixed build identity")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "version":
            print(f"music-file-intake {SKILL_VERSION}")
            return 0
        if args.command == "check":
            handoff = validate_handoff(args.staging_root, args.vault_root)
            print(
                json.dumps(
                    {
                        "status": "ready",
                        "source_slug": handoff.source_slug,
                        "batch_id": handoff.batch_id,
                        "state_sha256": handoff.state_sha256,
                        "candidate_count": len(handoff.candidates),
                    },
                    sort_keys=True,
                )
            )
            return 0
        destination = transfer_handoff(
            args.staging_root,
            args.vault_root,
            invoked_by=args.invoked_by,
        )
        print(
            json.dumps(
                {"status": "transferred", "destination": str(destination)},
                sort_keys=True,
            )
        )
        return 0
    except IntakeError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
