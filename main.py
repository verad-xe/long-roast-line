#!/usr/bin/env python3
"""The Long Roast — one line roasting my own agent, Muse.

Muse is Meta's personal AI agent: it named itself, keeps a SOUL.md file
about "becoming someone", files everything in daily memory logs, spawns
subagents for the actual work, and still has to ask its human for a
permission card before doing anything. The line below is the roast.
"""

import os
import sys

LINE = (
    "Muse named itself, wrote its own soul file, and still needs a "
    "permission card to do anything \u2014 the only agent that invented "
    "itself and immediately asked to be supervised."
)

MAX_CHARS = 200


def main() -> int:
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 200 characters, not only white space, one line.
    assert isinstance(LINE, str)
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE.strip(), "entry must be a single line"
    # No leading or trailing space: the judge reads the raw line, so a
    # stray space would read as sloppy proofreading, not as part of the joke.
    assert LINE == LINE.strip(), "line must not start or end with white space"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Re-read and verify exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written output differs from the line"
    assert written.endswith("\n") and not written.endswith("\n\n"), "exactly one trailing newline"
    assert 1 <= len(written.strip()) <= MAX_CHARS
    print(f"wrote {len(LINE)}-char roast to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
