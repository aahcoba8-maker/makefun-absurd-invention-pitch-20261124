"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching an absurd invention to entry.txt.
Stdlib only. Output goes to $MAKEFUN_OUTPUT_DIR when set, else /output,
else the script directory.
"""

import os

SENTENCE = (
    "A toaster that launches your toast with a tiny parachute so it never "
    "lands butter-side down, then bills you for air traffic control."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(f"wrote {path} ({len(SENTENCE)} chars)")


if __name__ == "__main__":
    main()
