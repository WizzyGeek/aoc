import numpy as np

g = open("8/input.txt","r").read().split()

# print(g)
d = np.array(list(map(lambda s: list(int(i) for i in s), g)))
# print(d)

ret = np.zeros(shape=d.shape, dtype=np.uint8)
print(ret)

for r, i in enumerate(d):
    m = -1
    for c, j in enumerate(i):
        if j > m:
            m = j
            print(j, "at", r, c, "visible")
            ret[r, c] = 1

for c, i in enumerate(d[0]):
    i = d[:, c]
    m = -1
    for r, j in enumerate(i):
        if j > m:
            m = j
            print(j, "at", r, c, "visible")
            ret[r, c] = 1

for r, i in enumerate(d):
    m = -1
    for c, j in zip(range(len(i)-1, -1, -1), i[::-1]):
        if j > m:
            m = j
                        # print(i, j)
            print(j, "at", r, c, "visible")
            ret[r, c] = 1

for c, i in enumerate(d[0]):
    i = d[:, c]
    m = -1
    for r, j in zip(range(len(i)-1, -1, -1), i[::-1]):
        if j > m:
            m = j
            # print(i, j)
            print(j, "at", r, c, "visible")
            ret[r, c] = 1
# [([print(i, end="") for i in j], print()) for j in d]
# [([print(i, end="") for i in j], print()) for j in ret]
print(sum(map(lambda i: sum(i), ret)))