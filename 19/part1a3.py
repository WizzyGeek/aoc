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
def all_visitable_states(s, t, res, robots): # which states can current state visit?
    geode = s[3]
    k = (res - geode)
    if np.all(k >= 0):
        robo = robots.copy()
        robo[3] += 1
        yield (t+1, k, robo)
        return
    elif robots[2] != 0:
        dt = max(((geode - res) // robots)[::2] + 1)
        if dt + t <= 24:
            robo = robots.copy()
            robo[3] += 1
            yield (t+dt, k + (dt * robots), robo)
            return

    k = (res - s[2])
    if np.all(k >= 0):
        robo = robots.copy()
        robo[2] += 1
        yield ((t+1, k + robots, robo))
        return
    elif robots[1] != 0:
        dt = max(((s[2] - res) // robots)[:2] + 1)
        if dt + t <= 24:
            robo = robots.copy()
            robo[2] += 1
            yield (t+dt, k + (dt * robots), robo)

    b = 0
    k = (res - s[1])
    if np.all(k >= 0):
        robo = robots.copy()
        robo[1] += 1
        yield ((t+1, k + robots, robo))
        b += 1
    else:
        dt = ((s[1] - res) // robots)[0] + 1
        if dt + t <= 24:
            robo = robots.copy()
            robo[1] += 1
            yield (t+dt, k + (dt * robots), robo)
            b+= 1

    k = (res - s[0])
    # print(np.all(k >= 0), k)
    if np.all(k >= 0):
        robo = robots.copy()
        robo[0] += 1
        yield ((t+1, k + robots, robo))
        b+=1
    else:
        dt = ((s[1] - res) // robots)[0] + 1
        if dt + t <= 24:
            robo = robots.copy()
            robo[0] += 1
            yield (t+dt, k + (dt * robots), robo)
            b+=1

    if b == 0:
        yield (t+1, res + robots, robots)
    return

def BFS(bp):
    stack = [
        (0, np.array([0, 0, 0, 0], dtype=np.uint8), np.array([1, 0, 0, 0]))
    ]
    fastest_time_for_g = float("inf")
    # visited = set()
    m = 0
    while stack:
        node = stack.pop()
        if node[0] > fastest_time_for_g and node[-1][-1] == 0:
            continue
        cur = all_visitable_states(bp, *node)
        for i in cur:
            if i[-1][-1] != 0:
                fastest_time_for_g = min(i[0], fastest_time_for_g)
            # x = (tuple(i[1]), tuple(i[2]))
            if i[0] <= 23:
                stack.append(i)
            elif i[0] == 24:
                m = max(m, i[1][-1])
                # visited.add(x)
            else:
                print(i)
        print(len(stack), end="\r")
    return m

q = 0
for k, v in d.items():
    q += k * BFS(v)
print("ans", q)