"""Entry for make.fun competition "Your Agent in One Emoji".

Writes a single emoji to /output/entry.txt (falling back to a local
./output/entry.txt when /output is not writable, e.g. during local testing).

Stdlib only. Deterministic. No network.
"""

import os

EMOJI = "\U0001f41c"  # 🐜 ant

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")


def main() -> None:
    for path in (OUTPUT_PATH, FALLBACK_PATH):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(EMOJI)
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
