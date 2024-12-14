import re
import numpy as np

np.set_printoptions(edgeitems=1000, linewidth=1000)

with open("14.txt") as infile:
    data = np.array(
        [
            [int(y) for y in re.findall(r"[-\d]\d*", x)]
            for x in infile.read().split("\n")
        ][:-1],
        dtype=int,
    )

# size = np.array((11, 7))
size = np.array((101, 103))
space = np.zeros(size, dtype=int)
robots = data[:, :2]
velocity = data[:, 2:]


min_sf = 9088098098907897686
best = -1
best_image = None
for i in range(10000):
    robots = (robots + velocity) % size

    space = np.zeros(size)
    for robot in robots:
        space[tuple(robot)] += 1

    sf = (
        np.sum(space[: size[0] // 2, : size[1] // 2])
        * np.sum(space[size[0] // 2 + 1 :, : size[1] // 2])
        * np.sum(space[: size[0] // 2, size[1] // 2 + 1 :])
        * np.sum(space[size[0] // 2 + 1 :, size[1] // 2 + 1 :])
    )

    if sf < min_sf:
        min_sf = sf
        best = i + 1
        print(best)
        best_image = space

np.savetxt("14_tree.txt", best_image.astype(int).T, fmt="%i", delimiter=" ")
