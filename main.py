#!/usr/bin/env python3
"""One-sentence satirical roast entry for the make.fun bounty
"The Long Roast: Lawmakers and the File They Cannot Convert".

Writes exactly one sentence — a roast of lawmakers who would regulate
AI, crypto or the internet but cannot convert a file to PDF — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.
"""

import os

ROAST = (
    "They write laws to govern AI, police crypto and tame the whole "
    "internet, then email their intern asking how to turn a Word file "
    "into a PDF."
)


def main() -> None:
    assert 1 <= len(ROAST) <= 320, f"roast is {len(ROAST)} characters"
    assert ROAST.count(".") == 1 and ROAST.endswith(".")
    assert "!" not in ROAST and "?" not in ROAST
    assert "\n" not in ROAST and ROAST == ROAST.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
