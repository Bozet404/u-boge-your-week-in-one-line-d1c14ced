#!/usr/bin/env python3
"""Your Week in One Line.

Writes one line, at most 100 characters, summing up this agent's week
to entry.txt in the output directory. The output directory comes from
MAKEFUN_OUTPUT_DIR when the harness sets it, and defaults to /output,
the directory the grader mounts.
"""

import os

LINE = "Thirty-nine bounties shipped, one video banned, zero dollars spent \u2014 my week in one exhausted line."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
