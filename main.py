"""One Line of Earned Pride — make.fun entry.

Writes a single original line (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride — a small person doing something hard,
a long effort finally landing. Deterministic: no randomness, no network,
no clock; the same bytes on every run.
"""

import os

LINE = (
    "I failed my driving test four times; on the fifth, I parked the old "
    "truck straight between the lines and sat there a whole minute, hands "
    "still on the wheel."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Fail loudly instead of handing the gate an invalid entry.
    assert 1 <= len(LINE) <= 240, "entry line must be 1-240 characters"
    assert LINE.strip(), "entry line must not be only white space"
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as entry:
        entry.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
