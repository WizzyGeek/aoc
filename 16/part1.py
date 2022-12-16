from example import d
# from copy import deepcopy

star = 'AA'
# start = 'EV'
to_visit = [d[star][1].copy()] # The nodes we have to visit
# path = [start]

# max_termination_score = {}
memo = {}

bitmap = {k: 1<<idx for idx, k in enumerate(d.keys())}

def calc(me):
    s = 0
    ret = []
    for i in me:
        s += i
        ret.append(s)
    return sum(ret)

def cost(i):
    return d[i][0]

def calc2(me): # For debug
    s = 0
    ret = []
    for i in me:
        s += cost(i)
        ret.append(s)
    return sum(ret)

def simulate(start, n, started): # Tried Recursive Bruteforce
    rate, children = d[start]
    # if f := memo.get(start + str(n)):
    #     # print("hit", start + str(n), f)
    #     return f

    if n == 1:
        if not bitmap[start] & started:
            # started |= bitmap[start]
            return [start]
        return [star]

    if n == 2:
        o = [star] + max((simulate(c, 1, started) for c in children), key=lambda s: cost(s[0]))
        if not bitmap[start] & started:
            o = max([start, star], o, key=lambda s: calc2(s))
            # if o[0]:
            #     started |= bitmap[start]
        memo[start + str(n)] = o
        print(start, n, o)
        return o

    m = 0
    ret = None
    for c in children:
        # print(" " * n, c)
        k = simulate(c, n - 1, started)
        if (j := calc2(k)) >= m:
            m = j
            ret = k

    if rate == 0:
        # memo[start + str(n)] = o = [0] + (ret or k)
        o = [star] + (ret or k)
        print(start, n, o)
        return o

    if not bitmap[start] & started:
        started |= bitmap[start]
        for c in children:
            # print(" " * n, c)
            k = [start] + simulate(c, n - 2, started)
            if (j := calc2(k)) > m:
                m = j
                ret = k

    memo[start + str(n)] = o = [star] + (ret or k)
    print(start, n, o)
    return o

a= simulate(star, 30, 0)
print(a)
print(calc(a))


## Trying to do some DFS like Thing
# while to_visit:
#     visiting_all = to_visit.pop()
#     path.append(visiting)
#     if visiting[0] == "+":
#         if k := d[visiting[1:]][0]:
#             memo.append(k)
#         continue
#     else:
#         if len(memo) < 29:
#             to_visit.extend(m := (d[visiting][1]))
#             to_visit.extend(map(lambda s: "+" + s, m))
#             memo.append(0)
#         else:
#             max_termination_score[visiting] = max(calc(memo), max_termination_score.get(visiting, 0))
#             memo.pop()

#     print(memo)
#     print(path)
#     print(max_termination_score)

# print(max_termination_score)

# print()