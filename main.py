"""Midnight Fridge Roast.

Writes a single-line roast of a smart fridge that refuses to open
after midnight to /output/entry.txt.
"""

import os

ROAST = (
    "After midnight my fridge locks itself like a nightclub bouncer, "
    "and I have to remind it I own the club, the drinks, and the leftovers."
)


def main() -> None:
    text = ROAST.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
