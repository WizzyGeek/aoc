import numpy as np
from string import ascii_lowercase
from math import inf

d = {i: idx for idx, i in enumerate(ascii_lowercase)}
d["S"] = -1
d["E"] = 26

g = open("12/input.txt", "r").read().split()
r = np.array(list(map(lambda s: list(map(lambda i: d[i], s)), g)), dtype=np.int8)
# print(r.shape)

inx = [0, 0]
end = [0, 0]

for ro, i in enumerate(r):
    for c, j in enumerate(i):
        if j == -1:
            inx = [ro, c]
            r[ro, c] = 0
        if j ==  26:
            end = [ro, c]
            r[ro, c] = 25

ret = list(map(lambda _: [inf] * r.shape[1], range(r.shape[0])))

from pprint import pprint
# pprint(ret)
ret[inx[0]][inx[1]] = 0
pprint(ret)

acc = lambda p: ret[p[0]][p[1]]
acR = lambda p: r[p[0]][p[1]]

# needs_value = [end]
# nv = set(map(tuple, needs_value))
# nvx = 0
# gv = False


# while needs_value:
#     cur = needs_value[nvx]
#     fr = cur
#     ro, co = cur
#     moveup = (ro != 0) and ((ro -1, co) not in nv) and (acR(cur) - acR([ro - 1, co])) < 2
#     movedown = (ro != r.shape[0] - 1) and (ro +1, co) not in nv and (acR(cur) - acR([ro + 1, co])) < 2
#     moveleft = co != 0 and (ro, co -1) not in nv and (acR(cur) - acR([ro, co -1])) < 2
#     moveright = (co != r.shape[1] - 1) and (ro, co+1) not in nv and (acR(cur) - acR([ro, co +1])) < 2
#     if moveup:
#         if acc([ro - 1, co]) != inf:
#             ret[cur[0]][cur[1]] = acc([ro - 1, co]) + 1
#             break
#         else:
#             needs_value.append([ro - 1, co])
#             nv.add((ro -1, co))

#     if movedown:
#         if acc([ro + 1, co]) != inf:
#             ret[cur[0]][cur[1]] = acc([ro + 1, co]) + 1
#             break
#         else:
#             needs_value.append([ro + 1, co])
#             nv.add((ro +1, co))

#     if moveleft:
#         if acc([ro, co -1]) != inf:
#             print(1)
#             ret[cur[0]][cur[1]] = acc([ro, co -1]) + 1
#             break
#         else:
#             needs_value.append([ro, co -1])
#             nv.add((ro, co-1))

#     if moveright:
#         if acc([ro, co+1]) != inf:
#             ret[cur[0]][cur[1]] = acc([ro, co +1]) + 1
#             break
#         else:
#             needs_value.append([ro, co +1])
#             nv.add((ro, co+1))

#     # print(needs_value, movedown, moveup, moveleft, moveright)
#     nvx += 1

# pprint(needs_value)
# pprint(ret)
# print(len(needs_value))

# def recurse(ro, co):
#     if acc((ro, co)) != inf:
#         return acc((ro,co))
#     cur = (ro, co)
#     moveup = (ro != 0) and (acR(cur) - acR([ro - 1, co])) < 2
#     movedown = (ro != r.shape[0] - 1) and (acR(cur) - acR([ro + 1, co])) < 2
#     moveleft = co != 0 and (ro, co -1) and (acR(cur) - acR([ro, co -1])) < 2
#     moveright = (co != r.shape[1] - 1) and (acR(cur) - acR([ro, co +1])) < 2

#     s = inf
#     if moveup:
#         s = min(s, recurse(ro-1, co) + 1)
#     if movedown:
#         s = min(s, recurse(ro+1, co) + 1)
#     if moveleft:
#         s = min(s, recurse(ro, co-1) + 1)
#     if moveright:
#         s = min(s, recurse(ro, co+1) + 1)
#     return s

# print(end)
# print(recurse(end[0], end[1]))

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
    # pprint(ret)
    if acc(end) != inf:
        break

print(acc(end))