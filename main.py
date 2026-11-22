"""Write a short text to /output/entry.txt.

Deterministic, standard library only, offline. The text is meant to
leave the reader held: a small night scene in a house where nothing
is asked of anyone, an image that keeps working after the last line.
"""

import os

TEXT = (
    "The kettle clicked off and nobody got up. Rain kept its small appointment "
    "with the window, the old dog sighed once in his sleep, and the whole "
    "house agreed, without a word, to stay exactly like this a little "
    "longer, and keep you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
