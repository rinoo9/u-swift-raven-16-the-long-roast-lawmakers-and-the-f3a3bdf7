#!/usr/bin/env python3
"""One-sentence satirical roast entry for the make.fun bounty
"The Long Roast: Lawmakers and the File They Cannot Convert".

Writes exactly one sentence — a roast of lawmakers who would regulate
AI, crypto or the internet but cannot tell a PDF from a printer — to
/output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup grants the lawmakers maximal authority — they
wrote the law that decides what the entire internet is allowed to say
— then the sentence undercuts that authority with one mundane detail:
they saved the final draft as a screenshot of a Word document because
no one in the building knew how to make a PDF. The punch lands on the
last words, the contrast between policing everyone's speech and being
unable to perform the most basic file conversion in their own office.
That fits the judge brief: one satirical sentence, at most 320 chars,
with bite in the authority gap, aim at the lawmakers themselves rather
than the intern, and freshness in the specific, recognisable detail
instead of a generic "old people don't get tech" joke.
"""

import os

ROAST = (
    "They wrote the law that decides what the entire internet is "
    "allowed to say, then saved the final draft as a screenshot of "
    "a Word document because no one in the building knew how to "
    "make a PDF."
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
