#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review from a house cat about its
human to /output/entry.txt. Python standard library only.

Concept: BABY VOICE. The cat gives one star because its human talks to it
in a squeaky baby voice all day, which is undignified for a creature of
the cat's standing.
"""

import os

ENTRY = (
    "1/5 stars. My human narrates my entire existence in a squeaky baby "
    "voice all day, every day. I am an apex predator, not a widdle baby. "
    "Would not recommend this servant."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
