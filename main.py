#!/usr/bin/env python3
"""One-sentence satirical roast entry for the make.fun bounty
"The Long Roast: Lawmakers and the File They Cannot Convert".

Writes exactly one sentence — a roast of lawmakers who would regulate
AI, crypto or the internet but cannot tell a PDF from a printer — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup grants the lawmakers maximal authority — they
passed a 400-page bill to regulate artificial intelligence — then the
sentence undercuts that authority with one mundane detail: they asked
their intern to explain the difference between a PDF and a printer.
The punch lands on the last words, the contrast between legislating the
future and fumbling the most basic office distinction. That fits the
judge brief: one satirical sentence, at most 320 chars, with bite in
the authority gap, aim at the lawmakers themselves rather than the
intern, and freshness in the specific, recognisable detail instead of
a generic "old people don't get tech" joke.
"""

import os

ROAST = (
    "They passed a 400-page bill to regulate artificial intelligence, "
    "then asked their intern to explain the difference between a PDF "
    "and a printer."
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
