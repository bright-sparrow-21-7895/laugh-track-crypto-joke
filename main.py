"""Write a one-line crypto trading joke to /output/entry.txt.

The joke is a single line about crypto and trading life,
kept under the 200-character gate for the Laugh Track contest.
Running this module writes the entry file and prints it back.
"""

import os

JOKE = "My trading strategy is simple: buy high, panic-sell low, then tell the group chat I meant to do that."


def main():
    assert 1 <= len(JOKE) <= 200, "entry must be 1-200 characters"
    assert JOKE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"{JOKE} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
