#!/usr/bin/env python3

adjs = """
"""


def calcuate_freq(match_second=False):
    adj = 0
    seen = set()
    loops = 0
    tries = 0
    while True:
        loops += 1
        for line in adjs.splitlines():
            if line is not None and line.strip():
                seen.add(adj)
                tries += 1
                a = int(line)
                adj += a
                print(a, " -> ", adj)
                if match_second and adj in seen:
                    print("found first duplicate match after", tries, "tries and", loops, "loops")
                    print(adj)
                    return adj

    print(adj)
    return adj


if __name__ == "__main__":
    calcuate_freq(match_second=False)
    calcuate_freq(match_second=True)
