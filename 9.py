import functools
import numpy as np

with open("9.txt") as infile:
    data = infile.read().strip()

total_length = functools.reduce(lambda a, b: int(a) + int(b), data)

disk = np.zeros((total_length,)) - 2

id = 0
head = 0
for instruction in data:
    instruction = int(instruction)
    for i in range(instruction):
        disk[head] = id if id >= 0 else i - instruction
        head += 1
    id = -1 * id if id < 0 else -1 * (id + 1)

ids = []
while head > 0:
    head -= 1

    if ids and disk[head] != ids[0]:
        if 0 < (first_empty := np.argmax(disk <= (-len(ids)))) < head:
            disk[first_empty : first_empty + len(ids)] = ids
            disk[head + 1 : head + len(ids) + 1] = -1

        ids = []

    if disk[head] >= 0:
        ids.append(disk[head])


disk[disk < 0] = 0

checksum = 0
for index, value in enumerate(disk):
    checksum += index * value

checksum
