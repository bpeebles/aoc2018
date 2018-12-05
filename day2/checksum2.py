#!/usr/bin/env python3
import sys

ids = [id.strip() for id in (l.strip() for l in open('input.txt', 'r').readlines()) if id]

for id in ids:
    for id2 in ids:
        diff = set()
        pos = set()
        for i in range(len(id)):
            if id[i] != id2[i]:
                diff.add(id[i])
                diff.add(id2[i])
                pos.add(i)
        if len(diff) == 2:
            print(id)
            print(id2)
            print(''.join(c for c in id if c not in diff))
            print(''.join(id[i] for i in range(len(id)) if i not in pos))
            sys.exit(0)
