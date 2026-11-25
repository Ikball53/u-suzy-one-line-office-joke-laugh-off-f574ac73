"""One-line office joke entry for the make.fun Laugh-Off.

The joke is stored as a single string constant and written verbatim to
``entry.txt`` inside the directory named by MAKEFUN_OUTPUT_DIR. The output
is checked before writing: exactly one line, no newline characters, and
between 1 and 200 characters long.
"""

import os
from pathlib import Path


JOKE = (
    "My review said I need to be more visible, so now I reply-all to "
    "everything — including the fire drill."
)


def build_output_path() -> Path:
    """Resolve the output directory from the environment."""
    raw_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(raw_dir) / "entry.txt"


def validate(line: str) -> None:
    """Enforce the competition's one-line format rules."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters long")


def main() -> None:
    validate(JOKE)
    target = build_output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
