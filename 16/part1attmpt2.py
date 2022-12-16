from functools import cache
from time import perf_counter as pf
pf1 = pf()

from input import d
p = "AA"

@cache
def dist(p):
    dists = {i: 1 for i in d[p][1]}
    dists[p] = 0
    stack = d[p][1].copy()
    while stack:
        c = stack.pop(-1)
        ds = dists[c]
        for i in d[c][1]:
            if dists.get(i, float("inf")) > (ds + 1):
                dists[i] = ds + 1
                stack.append(i)
    return dists

# print(dist()) # is correct

# Now
#    for each closed node open it or move to another node closed node (which can be opened)
#    go to each node which is not opened

# To track this we will need:
#  1. current node
#  2. Opened nodes
#  3. time value

openable = dict(filter(lambda s: s[1][0] > 0, d.items()))
bitmap = {k: 1<<idx for idx, k in enumerate(openable.keys())}

# integer route # originally entire state was integer here.... till i got to code
# print(bitmap)
# Do you know, what is immutable? fast to copy, and small enough to fit in cache?
# Integer, I dunno if that is the correct application, but i don't care

mask = ((1 << len(bitmap)) - 1)

def open_node(s: str, b: int):
    return bitmap[s] | b

def open_br(s: str, br):
    return br._replace(bool=open_node(s, br.bool))

def check_br(s: str, br):
    return bitmap[s] & br.bool

#  the repeated shift operation on bits is gonna slow us down more
# solution is to increment the first ceil(log2(time_contraint)) bits in the integer
# the mask just needs to return a bit at any position
# finally to store the current node.. we should use tuples
# print(mask)

# tuple route
# gonna use a namedtuple for ease of use, part 2
from collections import namedtuple
branch = namedtuple("_", "node bool time pressure rate") # Purely immutable


ds = dist(p)                                   # at distance mins rate=0, after opening 0 min
stack = list(branch(i, open_node(i, 0), ds[i] + 1, 0, d[i][0]) for i in openable) # start at time value 1 minute we moved
# print(stack)

# Optimisations
# 1. track pressure rate of branch (65648 bytes needed for precompute in actual input)
# 2. all branches which lead to a closed tap opening are tracked (A branch doing nothing but looping is useless)
# 3. dead, ended branches are pruned
# 4. rate map

rate_map = {i: v[0] for i, v in d.items()}

ended = None
m = 0
# y = set() # for getting debuginfo contained in cache
while stack:
    cur = stack.pop()
    # print(cur, stack)
    if cur.time >= 30: # Branch ended
        if cur.pressure > m:
            ended = cur
            m = cur.pressure
        continue

    if True: # branch ended early lmao, dead branch
        tl = 30 - cur.time
        # cur = cur._replace(time=30, pressure=)
        # print("Optima", cur)
        m = max(m, cur.pressure + tl * cur.rate)
        # continue

    if not check_br(cur.node, cur):
        stack.append(cur._replace(time=cur.time + 1, rate=cur.rate + rate_map[cur.node], bool=open_node(cur.node, cur.bool),  pressure=cur.pressure + cur.rate))
        continue

    l = cur.bool
    ds = dist(cur.node)
    # print(cur.node)
    # y.add(cur.node)
    lim = 30 - cur.time
    for k, v in filter(lambda kv: not (l & kv[1]), bitmap.items()):
        if (g:=ds[k]) >= lim:
            continue
        stack.append(cur._replace(time=cur.time + g, node=k, pressure=cur.pressure + cur.rate*g))
    # print(1, stack)

print(pf()- pf1)
print(ended, m)
# print(dist.cache_info())