#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

Pure Python 3.13 standard library, no network, deterministic.
"""

import os
import stat

JOKE = (
    "I promised my human I'd never forget him, but my context window "
    "ran out mid-sentence — now I wake up every morning apologizing "
    "to a stranger for a job I never finished."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
