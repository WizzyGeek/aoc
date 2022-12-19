import re
import numpy as np

pat = re.compile(r"Blueprint (.*):\n? *Each ore robot costs (.*) ore\.\n? *Each clay robot costs (.*) ore\.\n? *Each obsidian robot costs (.*) ore and (.*) clay\.\n? *Each geode robot costs (.*) ore and (.*) obsidian\..*")
d = {
    int(b): [np.array([int(o), 0, 0], dtype=np.uint8), np.array([int(c), 0, 0], dtype=np.uint8), np.array([int(obo), int(obc), 0], dtype=np.uint8), np.array([int(go), 0, int(gob)], dtype=np.uint8)] for b, o, c, obo, obc, go, gob in (i.groups() for i in pat.finditer(open("19/example.txt", "r").read()))
}
# print(d)
def add(robots, resources, k = 1):
    for idx, i in enumerate(robots):
        resources[idx] += i * k

 # remember spending resources is always the correct answer, but how you spend them depends you cant be greedy, since you will end up with only ore.
 # So we try out all purchases
def all_vistable_states(resources, robots, s, lt): # which states can current state visit?
    if resources[-1] >= lt:
        return []
    gt = lt + 1

    ret = []
    if (resources[2] >= s[3][2]) and (resources[0] >= s[3][0]):
        tmp = resources.copy()
        tmp[-1] += 1
        if tmp[-1] < gt:
            tmp[2] -= s[3][2]
            tmp[0] -= s[3][0]
            add(robots, tmp)
            tmp2 = robots.copy()
            tmp2[3] += 1
            ret.append((tmp, tmp2))
            return [(tmp, tmp2)]
    elif robots[2] != 0:
        dob, dore = (s[3][2] - resources[2], s[3][0] - resources[0])
        dtob, dtore = (dob // robots[2]) + 1, (dore // robots[0]) + 1
        dt = max(dtob, dtore)
        tmp = resources.copy()
        tmp[-1] += dt
        if tmp[-1] < gt:
            tmp[0] -= s[3][0]
            tmp[2] -= s[3][2]
            add(robots, tmp, dt)
            tmp2 = robots.copy()
            tmp2[3] += 1
            ret.append((tmp, tmp2))
            # return ret

    if (resources[1] >= s[2][1]) and (resources[0] >= s[2][0]):
        tmp = resources.copy()
        tmp[1] -= s[2][1]
        tmp[0] -= s[2][0]
        tmp[-1] += 1
        if tmp[-1] < gt:
            add(robots, tmp)
            tmp2 = robots.copy()
            tmp2[2] += 1
            ret.append((tmp, tmp2))
            # return ret # all others are bad
    elif robots[1] != 0:
        dclay, dore = (s[2][1] - resources[1], s[2][0] - resources[0])
        dtclay, dtore = dclay // robots[1] + 1, dore // robots[0] + 1
        dt = max(dtclay, dtore)
        tmp = resources.copy()
        tmp[-1] += dt
        if tmp[-1] < gt:
            tmp[0] -= s[2][0]
            tmp[1] -= s[2][1]
            add(robots, tmp, dt)
            tmp2 = robots.copy()
            tmp2[2] += 1
            ret.append((tmp, tmp2))

    if resources[0] >= s[1][0]:
        tmp = resources.copy()
        tmp[0] -= s[1][0]
        tmp[-1] += 1
        if tmp[-1] < gt:
            add(robots, tmp)
            tmp2 = robots.copy()
            tmp2[1] += 1
            ret.append((tmp, tmp2))
    elif robots[0] != 0:
        tmp = resources.copy()
        dt = (s[1][0] - tmp[0]) // robots[0] + 1
        tmp[-1] += dt
        if tmp[-1] < gt:
            tmp[0] -= s[1][0]
            add(robots, tmp, dt)
            tmp2 = robots.copy()
            tmp2[1] += 1
            ret.append((tmp, tmp2))

    if resources[0] >= s[0][0]:
        tmp = resources.copy()
        tmp[0] -= s[0][0]
        tmp[-1] += 1
        if tmp[-1] < (gt):
            add(robots, tmp)
            tmp2 = robots.copy()
            tmp2[0] += 1
            ret.append((tmp, tmp2))
    elif robots[0] != 0:
        tmp = resources.copy()
        k = (s[0][0] - tmp[0]) // robots[0] + 1
        tmp[-1] += k
        if tmp[-1] < gt:
            add(robots, tmp, k)
            tmp[0] -= s[0][0]
            tmp2 = robots.copy()
            tmp2[0] += 1
            ret.append((tmp, tmp2))

    tmp = resources.copy()
    tmp[-1] += 1
    add(robots, tmp)
    ret.append((tmp, robots.copy()))

    return ret

# We have the costs, we can calculate time when we get these robots and left over resources after making them
def get_geodes(s, lt):
    resources = [1, 0, 0, 0, 1] # ore, clay, obsidian, geode, the minute at which the state
    robots = [1, 0, 0, 0] #r rate of each resource
    # state = (resources, robots) # you get the idea
    # now we have a decision problem, let's bruteforce!

    stack = [(resources, robots)]
    m = 0
    first_g = float("inf")

    while stack:
        res, robo = stack.pop(0)
        if res[3] == 0 and first_g != float("inf"):
            continue
        tmp = all_vistable_states(res, robo, s, lt)
        # from pprint import pprint
        # pprint(tmp)
        # input()
        for R, ro in tmp:
            if (k := R[-1] >= lt) and R[-2] > m:
                assert R[-1] == lt, R[-1]
                m = R[-2]
            elif not k:
                if R[3] >= 1 and R[-1] < first_g:
                    first_g = R[-1]
                stack.append((R, ro))
    print(m, first_g, res, robo)
    return m

# all_vistable_states([49, 41, 1, 0, 17], [6, 5, 1, 1], [[4, 0, 0], [2, 0, 0],[ 3, 14,  0],[2, 0, 7],], 24)
# print(all_vistable_states([1, 0, 13, 0, 23], [1, 0, 1, 0], [[2, 0, 0], [4, 0, 0], [2, 4, 0], [4, 0, 13]]))
# q = 0
# for k, v in d.items():
#     s = get_geodes(v, 24)
#     print(s, v)
#     q += k * s

# print(q)
print(d)