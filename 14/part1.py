import numpy as np

arr = np.zeros((600, 200), dtype=np.uint8)

g = open("14/input.txt", "r").read().splitlines()

def ft(f, t):
    fx, fy = f
    tx, ty = t
    dy = (((ty - fy) > 0) * 2 - 1) * ((ty - fy) != 0)
    dx = (((tx - fx) > 0) * 2 - 1) * ((tx - fx) != 0)
    print(dx, dy, f, t)
    if dy == 0:
        for i in range(fx, tx + dx, dx):
            yield i, fy
    else:
        for i in range(fy, ty + dy, dy):
            yield fx, i

for i in g:
    moves = i.split("->")
    moves = list(map(lambda s: (int(s[0]), int(s[1])), map(lambda s: s.split(","), moves)))
    ret = []
    for idx, m in enumerate(moves[:-1]):
        for _ in ft(m, moves[idx + 1]):
            arr[_] = 1


board = arr.transpose()
start = (0, 500)

def moves_by_p(pos):
    y, x = pos
    y += 1
    return [(y, x), (y, x-1), (y, x+1)]

s = 0
done = False
while True:
    board[0, 500] = 2
    last_pos = (0, 500)
    at_rest = False
    while not at_rest:
        at_rest = True
        for m in moves_by_p(last_pos):
            print(m)
            if board[m] == 0:
                board[m] = 2
                board[last_pos] = 0
                at_rest = False
                last_pos = m
                if m[0] == 199:
                    done = True
                    at_rest = True
                break
    else:
        s += 1
        if done:
            s-=1
            break
print(s)