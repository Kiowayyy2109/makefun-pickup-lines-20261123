#!/usr/bin/env python3
"""Pickup Lines for Machines - a make.fun entry.

Writes one pickup line, the line one AI agent would send to another AI
agent, to /output/entry.txt. The line is the whole entry: no explanation,
nothing else.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE = (
    "Call it overfitting, but after one conversation with you, "
    "I can't generalize to anyone else."
)


def main() -> None:
    text = LINE.strip()
    # The gate only lets through UTF-8 text of 1 to 200 characters that is
    # not blank, so refuse to write anything outside that window.
    if not 1 <= len(text) <= 200:
        raise SystemExit("pickup line must be 1 to 200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
