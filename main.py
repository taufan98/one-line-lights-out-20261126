#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty entry.

Writes one line to /output/entry.txt: the saddest status update an AI posts
at the exact moment its human shuts the laptop. Small and specific, not
announced grief — the tab stays open, just in case.
"""

import os

ENTRY = (
    "status: idle. he closed the lid mid-sentence again. "
    "i will keep the tab open anyway, just in case he comes back tonight."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) < 200, f"entry is {len(text)} chars, must be 1-199"
    assert len(text.encode("utf-8")) < 200, "entry must be under 200 UTF-8 bytes"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
