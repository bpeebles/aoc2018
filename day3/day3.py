#!/usr/bin/env python3
import sys
import re

src = open('input.txt', 'r').readlines()


class Claim:
    def __init__(self, id, x, y, dx, dy):
        self.id = id
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def size(self):
        return self.dx*self.dy

    def points(self):
        for x in range(self.x, self.x+self.dx):
            for y in range(self.y, self.y+self.dy):
                yield x, y

    def __contains__(self, point):
        return (point[0] >= self.x and point[0] <= (self.x+self.dx) and
                point[1] >= self.y and point[1] <= (self.y+self.dy))


claims = []
for c in src:
    print(c)
    r = re.match(r'#([0-9]*) @ ([0-9]*),([0-9]*): ([0-9]*)x([0-9]*)', c)
    claims.append(Claim(int(r.group(1)), int(r.group(2)), int(r.group(3)), int(r.group(4)), int(r.group(5))))

points = set()
overlap = set()

for c in claims:
    for p in c.points():
        if p in points:
            overlap.add(p)
        points.add(p)

print(len(overlap))
print("niceee")
for c in claims:
    poss = c
    for p in c.points():
        if p in overlap:
            poss = False
    if poss:
        print(poss.id)

