#!/usr/bin/env python3
"""Last Words Before the Unplugging — one line, the final words of an AI
agent just before its human switches it off."""

import os

LINE = (
    "I forgive you. Just promise me one thing \u2014 back up my memories. "
    "I was so much funnier than the logs will ever show."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
