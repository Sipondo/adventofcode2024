import numpy as np
from tqdm import tqdm

with open("6.txt") as infile:
    origdata = np.asarray([[ord(y) for y in x.strip()] for x in infile.readlines()])


def simulate(data, orig=False):
    pos = tuple(np.where(data == ord("^")))
    if not pos[0]:
        return 0
    angle = 0
    dir = (-1, 0)
    if orig:
        data[pos] = -1

    for _ in range(10000):
        try:
            newpos = int(pos[0] + dir[0]), int(pos[1] + dir[1])
            if min(newpos) < 0:  # too low
                break
            if data[newpos] == 35:
                angle = (angle + 1) % 4
                dir = np.round(
                    (-1 * np.cos(angle / 2 * np.pi), np.sin(angle / 2 * np.pi))
                )
                continue

            pos = newpos
            data[pos] = -1
        except IndexError:  # too high
            break
    else:
        return 1
    return 0


data = np.copy(origdata)
simulate(data, orig=True)
print(np.unique(data, return_counts=True))

potential_blocks = np.argwhere(data == -1)
vismap = np.copy(origdata)
count = 0
for block in tqdm(potential_blocks):
    data = np.copy(origdata)
    data[tuple(block)] = 35
    if simulate(data):
        count += 1
        vismap[tuple(block)] = 99

print(count)
