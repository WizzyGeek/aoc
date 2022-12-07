# No repl first day
g = list(filter(bool, open("7/example.txt", "r").read().split("\n")))
# print(g)

cd = ""
tree: dict[str, list[int | list[str]]] = {}
stack: list[str] = []
c = 0
# print(g)
crd: list[int | list[str]] = [0, []]
while c < len(g):  # type: ignore
    i = g[c]
    if i == "$ cd ..":
        cd = stack.pop()
    elif i.startswith("$ cd "):
        stack.append(cd)
        cd = i[5:]
        tree.setdefault(cd, [0, []])
    elif i == "$ ls":
        c += 1
        i = g[c]
        crd = tree[cd]
        while i[0] != "$":
            p = i.split()
            if i.startswith("dir"):
                n = p[1]
                crd[1].append(n)  # type: ignore
                tree.setdefault(n, [0, []])
            else:
                # print(c,p[0])
                crd[0] += int(p[0]) # type: ignore
            c += 1
            try:
                i = g[c]
            except:
                break
        c -= 1 # compensate one element look ahead for exit
    else:
        print(i);
        raise ValueError

    c += 1

root = tree["/"]
s = 0
ds = root[1]

f = {}

stack = ["/"]
cd = "/"
while stack:
    leaf = tree[cd]
    if not leaf[1]:
        tree[stack[-1]][0] += leaf[0]  # type: ignore
        try:
            cd = tree[stack[-1]][1].pop()
        except:
            cd = stack.pop()
    else:
        stack.append(cd)
        cd = leaf[1].pop()

print(tree)
print(sum((i[0] < 100_000) * i[0] for i in tree.values()))