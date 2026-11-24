"""The Funniest Toaster Error Message.

A kitchen toaster that has had enough: it reports the one error it can
no longer keep quiet about, in a single deadpan line, and writes that
line to $MAKEFUN_OUTPUT_DIR/entry.txt (at most 120 characters).
"""

import os

MESSAGE = (
    "ERROR 451: The bread has unionised. "
    "Browning suspended until the heat is addressed in writing."
)


def main() -> None:
    # The gate accepts 1 to 120 characters; refuse to ship an over-long line.
    assert 1 <= len(MESSAGE) <= 120, f"entry is {len(MESSAGE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(MESSAGE)
    print(MESSAGE)


if __name__ == "__main__":
    main()
