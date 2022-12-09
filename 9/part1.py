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
Tv = 0 + 0j

visited = [
    (0+0j),
]

def compute_closet(h, t):
    if h.imag == t.imag:
        p = set([h + 1, h, h - 1]) & set([t + 1, t, t-1])
        assert len(p) == 1
        return p.pop()
    if h.real == t.real:
        p = set([h + 1j, h, h - 1j]) & set([t + 1j, t, t-1j])
        assert len(p) == 1
        return p.pop()
    possible = set([h, h + 1, h - 1, h + 1j, h - 1j, h + (1 + 1j), h + (-1 + 1j), h + (1 - 1j), h - (1 + 1j)]) & set([t + (1 + 1j), t + (-1 + 1j), t + (1 - 1j), t - (1 + 1j)])
    assert len(possible) == 1, f"{h} {t} {possible}"
    return possible.pop()

    # m = abs(h - t)
    # i = possible[0]
    # for H in possible:
    #     f = abs(H-t)
    #     if f < m:
    #         m = f
    #         i = H
    return i

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

s=0

for j in g:
    for i in break_movement(j):
        s+=i
        Hv += i
        a = Tv not in [Hv, Hv + 1, Hv - 1, Hv + 1j, Hv - 1j, Hv + (1 + 1j), Hv + (-1 + 1j), Hv + (1 - 1j), Hv - (1 + 1j)]
        # print(Tv, Hv, Hv - Tv, visited, a, i, j)
        if a:
            Tv = compute_closet(Hv, Tv)
            visited.append(Tv)
    # print("====")

assert s == sum(g)

print(Hv, Tv, len(set(visited)), visited)