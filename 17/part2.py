import numpy as np

n = 1000000000000
board = np.zeros(20000, dtype=np.uint8)

MAGIC = 61
g = list(map(lambda s: ord(s) - MAGIC, open("17/input.txt", "r").read()))
# print(g, board)

def set_index(c, r):
    board[r] = board[r] | (1 << c)

def check_intersection(mask, r):
    # r = (r % (4 * 2667))
    for i in reversed(mask):
        if i & board[r]:
            return True
        r += 1
        assert r < board.shape[0], r
    return False

def set_mask(mask, r):
    # r = (r % (4 * 2667))
    for i in reversed(mask):
        board[r] = board[r] | i
        r += 1

class Shape:
    def __init__(self, indices, right, mask_arr):
        self.indices = indices
        self.rightmost_index = right
        self.topmost_index = max(map(lambda s: s[1], indices))
        self.mask_arr = mask_arr
        self.mask_arrs = m = []
        for c in range(7):
            m.append(list(map(lambda s: s << c, self.mask_arr)))

    def indices_to_set(self, c, r):
        return list(map(lambda s: (s[0] + c, s[1] + r), self.indices))

    def mask(self, c):
        return self.mask_arrs[c]

    def can_move_right(self, c):
        return c + 1 <= self.rightmost_index

shapes = [
    Shape([(0, 0), (1, 0), (2, 0), (3, 0)], 3, [
        0b1111
    ]),
    Shape([(1, 0), (1, 1), (1, 2), (0, 1), (2, 1)], 4, [
        0b010,
        0b111,
        0b010,
    ]),
    Shape([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], 4, [
        0b100,
        0b100,
        0b111
    ]),
    Shape([(0, 0), (0, 1), (0, 2), (0, 3)], 6, [1, 1, 1, 1]),
    Shape([(0,0), (1, 0), (0, 1), (1, 1)], 5, [0b11, 0b11])
]

fallen = 0
cur_y = 0
ls = len(shapes)
lg = len(g)
c = 0
searching = True

been_states = {}
acur_y = 0
while fallen < n:
    shape = shapes[fallen % ls]
    idx = [2, 3 + cur_y]
    # if not searching:
    #     idx = [2, (3 + cur_y) % board.shape[0] + rem]
    at_rest = False
    # print("s",idx, end=" ")
    while not at_rest:
        move = g[c % lg]
        # print(move, end=" ")
        if move > 0 and shape.can_move_right(idx[0]) and not check_intersection(shape.mask(idx[0] + 1), idx[1]):
            idx[0] += 1
        if move < 0 and idx[0] > 0 and not check_intersection(shape.mask(idx[0] - 1), idx[1]):
            idx[0] -= 1
        c += 1

        # print(idx, end=" ")
        if check_intersection(shape.mask(idx[0]), idx[1] - 1) or idx[1] <= 0:
            at_rest = True
        else:
            idx[1] -= 1
        # print(idx, end=" ")
        assert idx[1] >= 0

    fallen += 1
    # print("Fallen(", idx,")", sep = "")
    set_mask(shape.mask(idx[0]), idx[1])
    cur_y = max(cur_y, shape.topmost_index + 1 + idx[1])

    if fallen < 2023: # I assume this is because of cycles detected here being "unsteady"
        continue

    ch = (fallen % ls, c % lg)
    if ch in been_states and searching:
        dfallen = fallen - been_states[ch][0] # 1 cycle change
        dcury = cur_y - been_states[ch][1]
        cycles = (n - fallen) // dfallen # how many floored cycles for n?
        print(cur_y, dcury, cycles)
        acur_y = dcury * cycles
        fallen += dfallen * cycles
        been_states.clear()
        searching = False
    if searching:
        been_states[ch] = (fallen, cur_y)

print(acur_y + cur_y)