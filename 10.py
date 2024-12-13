import numpy as np
from scipy.signal import convolve

with open("10.txt") as infile:
    data = [x.strip() for x in infile.readlines()]

yosemite = np.zeros((len(data), len(data[0])))

for i in range(len(data)):
    for j in range(len(data)):
        yosemite[i][j] = int(data[i][j])

KERNEL = np.array([[[0, 1, 0], [1, 0, 1], [0, 1, 0]]])

stack = []
for loc in np.argwhere(yosemite == 9):
    new = np.zeros(yosemite.shape)
    new[tuple(loc)] = 1
    stack.append(new)

paths = np.stack(stack)
for i in range(8, -1, -1):
    zmap = yosemite == i
    paths = (convolve(paths, KERNEL)[:, 1:-1, 1:-1] * zmap).astype(int)

np.sum(paths > 0)  # A
np.sum(paths)  # B
