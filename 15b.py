import numpy as np
from tqdm import tqdm

with open("15.txt") as infile:
    raw_maze, raw_instr = infile.read().split("\n\n")

origdata = np.asarray([[ord(y) for y in x.strip()] for x in raw_maze.strip().split()])

instructions = [x for x in raw_instr.strip()]


def push(matrix, pos, dir):
    to = pos + dir

    if matrix[tuple(to)] == 46:
        matrix[tuple(to)] = matrix[tuple(pos)]
        matrix[tuple(pos)] = 46
        return True
    elif matrix[tuple(to)] in (64, 79):
        if push(matrix, to, dir):
            matrix[tuple(to)] = matrix[tuple(pos)]
            matrix[tuple(pos)] = 46
            return True
        else:
            return False
    elif matrix[tuple(to)] == 35:
        return False


for instruction in instructions:
    pos = np.argwhere(origdata == 64)[0]

    if instruction == "^":
        dir = np.array((-1, 0))
    elif instruction == "v":
        dir = np.array((1, 0))
    elif instruction == "<":
        dir = np.array((0, -1))
    elif instruction == ">":
        dir = np.array((0, 1))

    push(origdata, pos, dir)

gps = 0
for i, row in enumerate(origdata):
    for j, e in enumerate(row):
        gps += i * 100 + j if e == 79 else 0
print(gps)
