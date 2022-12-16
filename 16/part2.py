from functools import cache
from time import perf_counter as pf
from collections import defaultdict
pf1 = pf()

from input import d
p = "EV"

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
stackE = list(branch(i, open_node(i, 0), ds[i] + 1, 0, d[i][0]) for i in openable)

s2d = []

for i in stack:
    for j in stackE:
        if j==i:
            continue
        s2d.append((i, j))

# print(stack)

# Optimisations
# 1. track pressure rate of branch (65648 bytes needed for precompute in actual input)
# 2. all branches which lead to a closed tap opening are tracked (A branch doing nothing but looping is useless)
# 3. dead, ended branches are pruned
# 4. rate map

# Part 2
# Observation
# Time = 26
# visitors = 2
# vists = exclusive -> bool1 & bool2 == 0
# Effectively a pair of two part1 solvers concurrently in exclusivity


rate_map = {i: v[0] for i, v in d.items()}

ended = None
m = 0
# y = set() # for getting debuginfo contained in cache
while s2d:
    # if len(s2d) == 490:
    #     print(s2d)
    cur, curE = s2d.pop()
    # print(cur, stack)
    if cur.bool & curE.bool:
        continue

    if cur.time >= 26: # Branch ended
        if (cur.pressure + curE.pressure) > m:
            ended = cur, curE
            m = cur.pressure + curE.pressure
        continue

    # if cur.time >= 26 or curE.time >= 26:
    #     continue

    if True: # branch ended early lmao, dead branch
        tl = 26 - cur.time
        # cur = cur._replace(time=30, pressure=)
        # print("Optima", cur)
        if  (t:=(cur.pressure + tl * cur.rate + curE.pressure + tl * curE.rate)) > m:
            ended = cur, curE
            m = t
            print(m, len(s2d))
        # continue

    if not (check_br(cur.node, cur) and check_br(curE.node, curE)):
        if not check_br(cur.node, cur):
            s2d.append((cur._replace(time=cur.time + 1, rate=cur.rate + rate_map[cur.node], bool=open_node(cur.node, cur.bool),  pressure=cur.pressure + cur.rate), curE))

        if not check_br(curE.node, curE):
            s2d.append((cur, curE._replace(time=curE.time + 1, rate=curE.rate + rate_map[curE.node], bool=open_node(curE.node, curE.bool),  pressure=curE.pressure + curE.rate)))
        continue

    l = cur.bool
    ds = dist(cur.node)
    lE = curE.bool
    dsE = dist(curE.node)
    stackE = []
    # print(cur.node)
    # y.add(cur.node)
    lim = 26 - cur.time
    time_map = defaultdict(lambda k: [])
    for k, v in filter(lambda kv: not (l & kv[1]), bitmap.items()):
        if (g:=ds[k]) >= lim:
            continue
        time_map[g].append(cur._replace(time=cur.time + g, node=k, pressure=cur.pressure + cur.rate*g))

    limE = 26 - curE.time
    for k, v in filter(lambda kv: not (lE & kv[1]), bitmap.items()):
        if (g:=dsE[k]) >= limE:
            continue
        stackE.append(curE._replace(time=curE.time + g, node=k, pressure=curE.pressure + curE.rate*g))

    for j in stackE:
        for k
        s2d.append((i, j))


    # print(1, s2d)

print(pf()- pf1)
print(ended, m)
# print(dist.cache_info())
# clearly this grows at n^2 - n compared to part1
# so we can