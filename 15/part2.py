import re

pat = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

def compute_manhattan(x, y, h, k):
    return abs(x-h) + abs(y-k)

g = open("15/input.txt", "r").read().splitlines()

points = []
beacons = {}
for i in g:
    x, y, h, k = pat.match(i).groups()
    x, y, h, k = int(x), int(y), int(h), int(k)
    beacons.setdefault(k, [])
    beacons[k].append(h)
    points.append(((x, y), compute_manhattan(x, y, h, k), k))

class Interval:
    def __init__(self, start, stop):
        self.s = start
        self.t = stop

    def __lt__(self, o):
        # print(self, o, self.t < o.s)
        return self.s < o.s

    def __or__(self, o):
        if self.s >= 4000_000 or self.t <= 0:
            return o
        if 0 >= self.s and 4000_000 <= self.t:
            return self
        if isinstance(o, Interval):
            os = o.s
            ot = o.t
            if 0 >= os and 4000_000 <= ot:
                return o
            if os >= 4000_000 or ot <= 0:
                return self
            if self.s > ot:
                if self.s == ot + 1:
                    return Interval(os, self.t)
                return [o, self]
            if self.t < os:
                if os == self.t + 1:
                    return Interval(self.s, ot)
                return [self, o]
            if ot >= self.t:
                return Interval(min(self.s, os), ot)
            return Interval(min(self.s, os), self.t)
        elif isinstance(o, list):
            if not o:
                return self
            o.append(self)
            return o

    def __bool__(self):
        if 0 >= self.s and 4000_000 <= self.t:
            return False
        return True

    def __str__(self):
        return f"Interval[{self.s}, {self.t}]"

    def __repr__(self):
        return f"Interval[{self.s}, {self.t}]"

def merge_intervals(a):
    a.sort(key=lambda i: i.s)
    output = [a[0]]
    for i in a[1:]:
        last = output[-1]
        if last.t >= i.s or (i.s + 1 == last.t):
            output[-1] = Interval(last.s, max(last.t, i.t))
        else:
            output.append(i)
    if len(output) == 1:
        return output[0]
    else:
        return output

# ry = 10
notable_rows = {}
x = ["|", "/", "-", "\\"]
for ry in range(3000_000, 4000_001): # range is from past failure data
    print(" ", ry, len(notable_rows), end="\r")
    added = []
    for i in points:
        h1 = i[0][0] - i[1] + abs(i[0][1] - ry)
        if compute_manhattan(i[0][0], i[0][1], h1, ry) > i[1]:
            continue
        h2 = i[0][0] + i[1] - abs(i[0][1] - ry)
        # print(h1, h2, i, compute_manhattan(i[0][0], i[0][1], h1, ry))
        if max(h1, h2) <= 0:
            continue

        if h1 == h2:
            added = Interval(h1, h2) | added
            # added.append(range(h1, h2 + 1))
        else:
            added = Interval(min(h1, h2), max(h1, h2)) | added
            # added.append(range(min(h1, h2), max(h1, h2) + 1))
    if added:
        if isinstance(added, list):
            m = merge_intervals(added)
            if m:
                print(m, ry)
                notable_rows[ry] = m
        else:
            print(added, ry)
            notable_rows[ry] = added

f = open("debug.txt", "w")
print(notable_rows)
print(notable_rows, file=f)
# added -= set(beacons.get(ry, []))
# print(beacons.get(ry, []))
# print(len(added))

# Output:

# [Interval[-1192342, 2889464], Interval[2889466, 4276084]] 3040754
# ^CTraceback (most recent call last):
#   File "/home/WizzyGeek/code/aoc/15/part1.py", line 101, in <module>
#     added = Interval(min(h1, h2), max(h1, h2)) | added
#   File "/home/WizzyGeek/code/aoc/15/part1.py", line 51, in __or__
#     elif isinstance(o, list):
# KeyboardInterrupt

# x = 2889465, y=3040754