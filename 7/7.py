g = list(filter(bool, open("7/input.txt", "r").read().split("\n")))

tree = {}
cp = [] # current path
c = 0
b = len(g)
while c < b:
    cmd = g[c]
    # print(cp, cmd)
    if cmd.startswith("$ cd "):
        n = cmd[5:]
        if n != "..":
            cp.append(cmd[5:])
            tree.setdefault(tuple(cp), 0) # Our problem has entirely to do with size
        else:
            cp.pop()
    elif cmd.startswith("$ ls"):
        c_o1 = g[c+1]
        while not c_o1.startswith("$"):
            if not c_o1.startswith("dir"):
                # new file, find all previous directories and update size
                s = int(c_o1.split()[0])
                for i in range(1, len(cp) + 1): # current path
                    tree[tuple(cp[:i])] += s # add to size
            c += 1 # inc
            if c >= b - 1: # all parsed?
                break
            c_o1 = g[c+1] # update
            # ignore dir, cp tracks the structure
    c += 1

print(tree)

sm = 0
for k in tree.values():
    if k <= 100000:
        sm += k

print(sm)

space = 70000000
needed = 30000000
free = 70000000 - tree[("/",)]
print(free, needed, free + 6400111)

m = float("inf")
for k in tree.values():
    if (free + k) >= needed:
        m = min(m, k)

print(m)