import numpy as np

arr = np.zeros((700, 200), dtype=np.uint8)

g = open("14/input.txt", "r").read().splitlines()

def ft(f, t):
    fx, fy = f
    tx, ty = t
    dy = (((ty - fy) > 0) * 2 - 1) * ((ty - fy) != 0)
    dx = (((tx - fx) > 0) * 2 - 1) * ((tx - fx) != 0)
    # print(dx, dy, f, t)
    if dy == 0:
        for i in range(fx, tx + dx, dx):
            yield i, fy
    else:
        for i in range(fy, ty + dy, dy):
            yield fx, i

my = 0
for i in g:
    moves = i.split("->")
    moves = list(map(lambda s: (int(s[0]), int(s[1])), map(lambda s: s.split(","), moves)))
    my = max(max(map(lambda s: s[1], moves)), my)
    ret = []
    for idx, m in enumerate(moves[:-1]):
        for _ in ft(m, moves[idx + 1]):
            arr[_] = 1

print(my)


board = arr.transpose()
board[my + 2] = 1

start = (0, 500)

def moves_by_p(pos):
    y, x = pos
    y += 1
    return [(y, x), (y, x-1), (y, x+1)]

def fb(b):
    ch = [".", "@", "o"]
    r = ""
    for i in b:
        for j in i:
            r += ch[j]
        r+="\n"
    return r

s = 0
# a = open("debug.txt", "w")
while True:
    board[0, 500] = 2
    last_pos = (0, 500)
    at_rest = False
    # print(fb(board[0:169, 430:590]), file=a)
    while not at_rest:
        at_rest = True
        for m in moves_by_p(last_pos):
            if board[m] == 0:
                board[m] = 2
                board[last_pos] = 0
                at_rest = False
                last_pos = m
                break
    else:
        s += 1
        if last_pos == (0, 500):
            break

print(s)
