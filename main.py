#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

The one sentence a house cat would say in its own defence, five seconds
after sweeping a glass off the table. No apology, no confession: the cat
had a reason, and the reason was rent.
"""

import os

# One sentence, 106 characters, in the cat's own voice.
SENTENCE = (
    "It sat on my windowsill rent-free, judging me with its smug little rim, "
    "so I served it an eviction notice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
