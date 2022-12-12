import numpy as np
from string import ascii_lowercase
from math import inf

d = {i: idx for idx, i in enumerate(ascii_lowercase)}
d["S"] = -1
d["E"] = 26

g = open("12/input.txt", "r").read().split()
r = np.array(list(map(lambda s: list(map(lambda i: d[i], s)), g)), dtype=np.int8)
# print(r.shape)

idx = [0, 0]
end = [0, 0]

for ro, i in enumerate(r):
    for c, j in enumerate(i):
        if j == -1:
            idx = [ro, c]
            r[ro, c] = 0
        if j ==  26:
            end = [ro, c]
            r[ro, c] = 25

acR = lambda p: r[p[0]][p[1]]
def solve(inx):
    ret = list(map(lambda _: [inf] * r.shape[1], range(r.shape[0])))

    from pprint import pprint
    # pprint(ret)
    ret[inx[0]][inx[1]] = 0
    # pprint(ret)

    acc = lambda p: ret[p[0]][p[1]]

    to_find = [inx]
    tmp = []
    while True:
        while to_find:
            cur = (ro, co) = to_find.pop()
            mu = (ro != 0) and (acR(cur) - acR([ro - 1, co])) > -2 and acc((ro -1, co)) == inf
            md = (ro != r.shape[0] - 1) and (acR(cur) - acR([ro + 1, co])) > -2 and acc((ro +1, co)) == inf
            ml = co != 0 and (ro, co -1) and (acR(cur) - acR([ro, co -1])) > -2 and acc((ro, co-1)) == inf
            mr = (co != r.shape[1] - 1) and (acR(cur) - acR([ro, co +1])) > -2 and acc((ro, co +1)) == inf
            steps = acc(cur)
            if mu:
                ret[ro -1][co] = min(acc(cur) + 1, ret[ro -1][co])
                tmp.append([ro-1, co])
            if md:
                ret[ro +1][co] = min(acc(cur) + 1, ret[ro +1][co])
                tmp.append([ro+1, co])
            if ml:
                ret[ro][co -1] = min(acc(cur) + 1, ret[ro][co -1])
                tmp.append([ro, co -1])
            if mr:
                ret[ro][co +1] = min(acc(cur) + 1, ret[ro][co +1])
                tmp.append([ro, co +1])
        to_find = tmp
        tmp = []
        # print(to_find)
        if acc(end) != inf or not to_find:
            break

    print(acc(end))
    return ret

solved = solve(idx)
print(1)

m = solved[end[0]][end[1]]

for ro, i in enumerate(solved):
    for co, j in enumerate(i):
        if acR((ro, co)) == 0 and j != inf:
            solved = solve((ro, co))
            print(solved[end[0]][end[1]])
            if solved[end[0]][end[1]] == 0:
                print(ro, co)
                exit()
            m = min(m, solved[end[0]][end[1]])

print(m, idx)

# solved = solve(idx)
# print(solved[idx[0]][idx[1]])