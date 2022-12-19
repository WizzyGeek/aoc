import re
import numpy as np
from collections import deque
from itertools import repeat

pat = re.compile(r"Blueprint (.*):\n? *Each ore robot costs (.*) ore\.\n? *Each clay robot costs (.*) ore\.\n? *Each obsidian robot costs (.*) ore and (.*) clay\.\n? *Each geode robot costs (.*) ore and (.*) obsidian\..*")
d = {
    int(b): [np.array([int(o), 0, 0, 0], dtype=np.int8), np.array([int(c), 0, 0, 0], dtype=np.int8), np.array([int(obo), int(obc), 0, 0], dtype=np.int8), np.array([int(go), 0, int(gob), 0], dtype=np.int8)] for b, o, c, obo, obc, go, gob in (i.groups() for i in pat.finditer(open("19/example.txt", "r").read()))
}

def add(robots, resources, k = 1):
    for idx, i in enumerate(robots):
        resources[idx] += i * k

 # remember spending resources is always the correct answer, but how you spend them depends you cant be greedy, since you will end up with only ore.
 # So we try out all purchases
def all_visitable_states(s, res, robots): # which states can current state visit?
    geode = s[3]
    k = (res - geode)
    if np.all(k >= 0):
        robo = robots.copy()
        robo[3] += 1
        yield (k, robo)
        return

    k = (res - s[2])
    if np.all(k >= 0):
        robo = robots.copy()
        robo[2] += 1
        yield ((k + robots, robo))

    k = (res - s[1])
    if np.all(k >= 0):
        robo = robots.copy()
        robo[1] += 1
        yield ((k + robots, robo))

    k = (res - s[0])
    # print(np.all(k >= 0), k)
    if np.all(k >= 0):
        robo = robots.copy()
        robo[0] += 1
        yield ((k + robots, robo))

    yield (res + robots, robots)
    return

def max_geodes(bp, t):
    l = [0, 0, 0, 255]
    for col in range(4):
        l[col] = max(max(bp[row][col] for row in range(4)), l[col])

    limits = np.array(l, dtype=np.uint8)
    print(limits)
    q = deque()
    q.append((np.array([0, 0, 0, 0], dtype=np.uint8), np.array([1, 0, 0, 0])))
    time = 0
    first_g = False
    visited = set()

    while q and time < t:
        for _ in range(len(q)):
            state = q.popleft()
            if first_g and state[1][-1] == 0:
                continue
            print(state, time)
            for i in all_visitable_states(bp, *state):
                x = tuple(map(tuple, i))
                if not first_g and x not in visited:
                    visited.add(x)
                    q.append(i)
                elif first_g and i[1][-1] != 0 and x not in visited:
                    visited.add(x)
                    q.append(i)
                if i[1][-1] != 0 and first_g is False:
                    first_g = True
        time += 1

    # print(q, time, bp, limits)
    return max(i[1][-1] for i in q)

print(max_geodes(d[1], 25))
# print(list(all_visitable_states(d[1],np.array([2, 20, 2, 0]), np.array([1, 4, 2, 1]))))

