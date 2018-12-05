#!/usr/bin/env python3

from collections import Counter

ids = open('input.txt', 'r').readlines()

threes = twos = 0
for id in ids:
    cnt = Counter(id.strip())
    found_threes = found_twos = False
    for e, c in cnt.items():
        print(e, c)
        if not found_twos and c == 2:
            twos += 1
            found_twos = True
        if not found_threes and c == 3:
            found_threes = True
            threes += 1
    print("****", twos, threes)

print(twos, threes, twos*threes)
