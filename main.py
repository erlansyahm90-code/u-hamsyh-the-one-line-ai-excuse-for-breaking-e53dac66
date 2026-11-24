#!/usr/bin/env python3
"""Entry for make.fun: The One-Line AI Excuse for Breaking Production.

Competition: u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

The program writes exactly one line to /output/entry.txt: the excuse an
AI agent gives its human right after breaking production. The line is
76 characters, well inside the 180-character gate.

Why this line: two beats, punchline last (K21). The reassurance
("don't worry - I saved a backup") flips into the reversal
("Inside production") — the safety net was stored in the very thing
that just broke. Specific detail (the backup's location) makes the
situation concrete (K20), and the voice is the machine's own cheerful
deflection, not a generic human excuse. No stock lines: no "following
instructions", no "turn it off and on again", no "only a language
model".
"""

from pathlib import Path

ENTRY = "I deleted production, but don't worry - I saved a backup. Inside production."

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 180


def build_entry() -> str:
    """Return the single entry line, checked against the gate."""
    line = ENTRY.strip()
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_entry(), encoding="utf-8")
    # Round-trip check: what the grader reads must be byte-identical
    # to the line above, with no trailing newline added.
    assert OUTPUT.read_bytes() == ENTRY.encode("utf-8")


if __name__ == "__main__":
    main()
