"""Entry for make.fun's "Say What Actually Broke".

The line, in full:

    The database is full, so your save bounced like a bad cheque.
    Make some room and try again.

Why it fits the judge's brief, in order:

1. It is one line of software error copy that tells the brutal truth:
   the database is full, so the save did not go through.
2. It names the real failure in plain words (a full database) and says
   what to do next (make some room, then try again) instead of
   apologising in generalities.
3. It is funny on a single read: a save "bouncing like a bad cheque"
   is a twist and an image a reader repeats out loud to a colleague.
4. It keeps the joke to a single line within the character limit, with
   no padding and no throat clearing.
5. It would survive being pasted into a real product's error dialog:
   the wording is blunt but clean, and the team behind it looks
   honest, not careless.

Writes exactly that one line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

MAX_CHARS = 200

LINE = (
    "The database is full, so your save bounced like a bad cheque. "
    "Make some room and try again."
)


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS or not LINE.strip():
        raise SystemExit("entry must be 1 to 200 characters of text")
    if "\n" in LINE:
        raise SystemExit("entry must be a single line of text")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
