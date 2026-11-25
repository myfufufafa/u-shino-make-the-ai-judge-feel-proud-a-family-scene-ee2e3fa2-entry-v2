#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (one or two lines, at most 280
characters) to /output/entry.txt, deterministically.
"""

import os
import sys

SCENE = (
    "My six-year-old taught Grandma to video-call, and now she rings "
    "every night just to show him the moon from her window \u2014 two "
    "windows, one moon, and both of them beaming."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main():
    text = SCENE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"scene is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if text.count("\n") > 1:
        print("scene must be one or two lines", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
