from parsed import monkey, l

r = [0] * len(monkey)

y = open("debug.txt", "w")

for g in range(10000):
    for k, v in monkey.items():
        s = v["s"]
        # print("---- Monkey", k, file=y)
        while len(s) > 0:
            r[k] += 1
            i = s.pop(0)
            m = v["worry"](i)
            n_monkey = v["c"][bool(v["test"](m))]
            monkey[n_monkey]["s"].append(m)
    #         print("__ inspecting", i, file=y)
    #         print("worry from", i, "->", m, file=y)
    #         print("item with", m, "->", n_monkey, file=y)
    # print("==== round", g + 1, r, file=y)

m = max(r)
r.remove(m)
print(max(r) * m)
y.close()