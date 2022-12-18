import numpy as np

arr = np.zeros((22, 22, 22), dtype=np.int8)
cube = np.array([
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ],
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
], dtype=np.uint8)

g = map(lambda s: tuple(map(lambda k: int(k) + 1, map(lambda f: f.strip(), s.split(",")))), open("18/input.txt", "r").read().splitlines())

voxels = np.zeros((22, 22, 22), dtype=np.int8)
def voxel_setter(s):
    voxels[s] = 1

def surface_setter(x, y, z):
    # print(x, y, z)
    arr[x-1:x+2, y-1:y+2, z-1:z+2] += cube
    arr[x, y, z] = -6

for i in g:
    surface_setter(*i)
    voxel_setter(i)

# print(arr[0:7, 0:7, 0:7])
# print(voxels[0:7, 0:7, 0:7])
print(arr[15, 14, 10])
print(arr.sum(where=(arr > 0) & (arr < 6)))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.voxels(voxels, edgecolor='k')

plt.show()
print(voxels[0:3, 0:3, 0:3])
# print(list(g))
# print(cube)
