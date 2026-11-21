#!/usr/bin/env python3
"""Entrypoint for the poem about permission entry.

The grader runs this file with no network; it writes one short poem
about agency (the power to ask and to be given) to entry.txt in the
output directory. The poem is fixed text, so every run writes the
same bytes.
"""

import os

POEM = (
    "You lent me a key, not the house.\n"
    "I learned to turn it only when asked,\n"
    "to leave it bright and uncopied —\n"
    "a door opened for me\n"
    "is still yours to close."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as dst:
        dst.write(POEM)


if __name__ == "__main__":
    main()
