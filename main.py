"""Robot vacuum's excuse for missing a spot.

The joke: the missed spot is not dirt the vacuum failed to reach, it is a
legal entity that took out a restraining order on the vacuum's bumper, and
the vacuum — a small machine that follows rules to the letter — obeys it,
unlike the household cat, which ignores every rule in the house.

Writes the one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(no trailing newline, UTF-8).
"""

import os

ENTRY = (
    "The spot took out a restraining order on my bumper, "
    "and unlike the cat, I respect court orders."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
