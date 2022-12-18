import numpy as np

g = map(lambda s: tuple(map(lambda k: int(k) + 1, map(lambda f: f.strip(), s.split(",")))), open("18/input.txt", "r").read().splitlines())

voxels = np.zeros((22, 22, 22), dtype=np.int8)

def voxel_setter(s):
    voxels[s] = 1

for i in g:
    voxel_setter(i)

# idea:
# Modified flood fill
# Push 0, 0, 0 on stack
# (0, 0, 0 lies on boundary of the actual space in which voxels sit
# line22: int(k) + 1 so it will always be free, any other boundary cell also works)
# loop
# pop stack
# set value of current cell = to how many cubes surround it or add it directly to sum
# push all adjacent indices which are unoccupied and not filled (visited)
#   all adjacent in x (2 special cases, 0, last index) and not in filled
#   all adjacent in y (2 special cases)
#   all adjacent in z (2 special cases)
    # check if voxel at position is not 1
    # add position to filled
    # continue push
    # add to set
# break if stack empty

# Worst case: 22^3 iterations = 10648
# Push pop assumed to be 200 ns, if else cost, 40ns total, 200 ns for set add, 100ns for set contains maybe
# upper bound of 6*200ns + 240ns + 1200ns + 600ns  = 4.24 micro second per iteration
# we have 10648, should run sub 1 second with no extra optimisations

from time import perf_counter as pf

pf1 = pf()
stack = [(0, 0, 0)]
visited = set(stack)
s = 0
while stack:
    x, y, z = stack.pop()
    if (k := (x != 0)) and x != 21:
        for i in [(x - 1, y, z), (x + 1, y, z)]:
            if (j := (voxels[i] != 1)) and i not in visited:
                stack.append(i)
                visited.add(i) # adding an unvisted indice as, other paths my add it to stack as well
            elif not j:
                s += 1
    else:
        i = x + (1, -1)[k], y, z
        if (j := (voxels[i] != 1)) and i not in visited:
            stack.append(i)
            visited.add(i)
        elif not j:
            s += 1

    if (k := (y != 0)) and y != 21:
        for i in [(x, y - 1, z), (x, y + 1, z)]:
            if (j := (voxels[i] != 1)) and i not in visited:
                stack.append(i)
                visited.add(i)
            elif not j:
                s += 1
    else:
        i = x, y + (1, -1)[k], z
        if (j := (voxels[i] != 1)) and i not in visited:
            stack.append(i)
            visited.add(i)
        elif not j:
            s += 1

    if (k := (z != 0)) and z != 21:
        for i in [(x, y, z - 1), (x, y, z + 1)]: # typo bug here, wrote [(x, y, z - 1), (x, y, z - 1)]
            if (j := (voxels[i] != 1)) and i not in visited:
                stack.append(i)
                visited.add(i)
            elif not j:
                s += 1
    else:
        i = x, y, z + (1, -1)[k]
        if (j := (voxels[i] != 1)) and i not in visited:
            stack.append(i)
            visited.add(i)
        elif not j:
            s += 1

    visited.add((x, y, z))

print(s)
print("seconds: ", pf() - pf1) # Runs in 120ms