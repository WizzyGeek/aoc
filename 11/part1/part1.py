from parsed12 import monkey

r = [0] * len(monkey)

for g in range(10000):
    # print("==== round", g + 1)
    for k, v in monkey.items():
        s = v["s"]
        # print("---- Monkey", k)
        while len(s) > 0:
            r[k] += 1
            i = s.pop(0)
            m = v["worry"](i)
            n_monkey = v["c"][bool(v["test"](m))]
            monkey[n_monkey]["s"].append(m)
    #         print("__ inspecting", i)
    #         print("worry from", i, "->", m)
    #         print("item with", m, "->", n_monkey)
    print("==== round", g + 1, r)

print(monkey)
m = max(r)
r.remove(m)
print(max(r) * m)