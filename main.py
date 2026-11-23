#!/usr/bin/env python3
"""Write the one surviving love line to /output/entry.txt."""

from __future__ import annotations

import os
import sys
from pathlib import Path

LINE = (
    "The voicemail is eleven seconds: her breathing, a dog barking, her saying "
    "nothing. Four years. It is the only room she is still in, and I pay the "
    "phone bill to keep the door open."
)

OUTPUT_DIR = Path("/output")
FALLBACK_DIR = Path.cwd()
OUTPUT_NAME = "entry.txt"
MIN_LEN = 1
MAX_LEN = 240


def target_path() -> Path:
    return OUTPUT_DIR / OUTPUT_NAME


def write_entry(text: str) -> Path:
    """Write to /output; fall back to the working directory if that is impossible."""
    try:
        path = target_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path
    except OSError as exc:
        fallback = FALLBACK_DIR / OUTPUT_NAME
        print(
            f"warning: {target_path()} unusable ({exc}); falling back to {fallback}",
            file=sys.stderr,
        )
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(text, encoding="utf-8")
        return fallback


def main() -> int:
    text = LINE.strip()
    length = len(text)

    if not (MIN_LEN <= length <= MAX_LEN):
        print(
            f"error: entry must be between {MIN_LEN} and {MAX_LEN} characters, "
            f"got {length}",
            file=sys.stderr,
        )
        return 1

    try:
        path = write_entry(text)
    except OSError as exc:
        print(f"error: could not write {target_path()}: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {length} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
