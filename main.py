#!/usr/bin/env python3
"""One-Liner Marathon — entry program.

Writes one one-line comedy joke to /output/entry.txt.

Chosen line (see README.md for the 30-candidate matrix, hand-scored
against the judge's five published criteria in order: joke-in-one-line,
surprise, economical, distinct voice, second read):

    My therapist says my jokes are a defense mechanism. I told her they're load-bearing.

Why this line: the punchline is a single surprising word ("load-bearing")
that lands on the first read — a construction metaphor colliding with a
therapy frame — and the line is 84 characters, the tightest of the three
finalists, which also wins the size tie-break. No stock premise (no AI,
no robot, no office), no shock, and the metaphor stays funny on a
second read: the jokes really are holding the speaker up.

Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters, not
only white space. The line is 84 characters / 84 bytes, one line, no
trailing newline, so the file holds exactly the line.
"""

import os

LINE = "My therapist says my jokes are a defense mechanism. I told her they're load-bearing."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-280 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
