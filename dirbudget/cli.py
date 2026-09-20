"""Command-line interface for directory byte budgets."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import measure_directory


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dir-budget",
        description="Fail when a directory's regular files exceed a byte budget.",
    )
    parser.add_argument("directory", type=Path)
    parser.add_argument("--max-bytes", type=int, required=True, metavar="BYTES")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        report = measure_directory(args.directory, args.max_bytes)
    except (NotADirectoryError, ValueError) as exc:
        print(f"dir-budget: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({
        "directory": str(report.directory),
        "total_bytes": report.total_bytes,
        "budget_bytes": report.budget_bytes,
        "files": report.files,
        "exceeded": report.exceeded,
    }, indent=2))
    return 1 if report.exceeded else 0


if __name__ == "__main__":
    raise SystemExit(main())
