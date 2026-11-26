#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Deterministic entry program: writes the single sentence a house cat would
say in the five seconds after sweeping a glass off the table to
/output/entry.txt. No input, no randomness, no network.
"""

from pathlib import Path

ENTRY = (
    "The glass was squatting in my sunbeam and refused to pay rent, "
    "so I served it an eviction notice \u2014 the floor simply signed "
    "for the delivery."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
