def mk_c(d):
    k = d.split()
    # print(d, k)
    r = 0 + 0j
    if k[0] == "U":
        r = complex(0, int(k[1]))
    elif k[0] == "D":
        r = complex(0, -1 * int(k[1]))
    elif k[0] == "R":
        r = complex(int(k[1]))
    elif k[0] == "L":
        r = complex(-1 * int(k[1]))
    else:
        raise ValueError()
    return r

g = list(map(mk_c, open("9/input.txt", "r").read().split("\n")))
# print(g)

Hv = 0 + 0j
tails = [0] * 9

visited = [
    (0+0j),
]


def compute_closet(h, t):
    if h.imag == t.imag:
        p = set([h + 1, h, h - 1]) & set([t + 1, t, t-1])
        assert len(p) == 1, f"{h} {t} {p}"
        return p.pop()
    if h.real == t.real:
        p = set([h + 1j, h, h - 1j]) & set([t + 1j, t, t-1j])
        assert len(p) == 1, f"{h} {t} {p}"
        return p.pop()
    p = set([h, h + 1, h - 1, h + 1j, h - 1j, h + (1 + 1j), h + (-1 + 1j), h + (1 - 1j), h - (1 + 1j)]) & set([t + (1 + 1j), t + (-1 + 1j), t + (1 - 1j), t - (1 + 1j)])
    assert len(p) == 1, f"{h} {t} {p}"
    return p.pop()


def break_movement(m):
    if m.real == 0.0:
        step = m * -1j
        step = round(step.real / abs(step.real))
        y = step * 1j

        for i in range(round((step * m * -1j).real)):
            yield y
    else:
        step = round(m.real / abs(m.real))
        for i in range(round(abs(m.real))):
            yield step

for j in g:
    for i in break_movement(j):
        Hv += i
        f = Hv
        c = 0
        while c < len(tails):
            if tails[c] not in [f, f + 1, f - 1, f + 1j, f - 1j, f + (1 + 1j), f + (-1 + 1j), f + (1 - 1j), f - (1 + 1j)]:
                tails[c] = compute_closet(f, tails[c])
            f = tails[c]
            c += 1
        if c >= len(tails):
            visited.append(f)

print(tails, visited, len(set(visited)))