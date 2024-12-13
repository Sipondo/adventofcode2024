import numpy as np
from tqdm import tqdm

with open("8.txt") as infile:
    origdata = np.asarray([[ord(y) for y in x.strip()] for x in infile.readlines()])

options = np.unique(origdata, return_counts=True)[0]
canvas = np.zeros(origdata.shape)

for option in options:
    if option == 46:
        continue

    antennas = np.argwhere(origdata == option)
    antenna_pairs = [
        (a, b) for idx, a in enumerate(antennas) for b in antennas[idx + 1 :]
    ]

    for antenna_pair in antenna_pairs:
        diff = antenna_pair[0] - antenna_pair[1]
        antenna_pair = [tuple(x) for x in antenna_pair]

        nodes = [
            tuple(x + y)
            for x in antenna_pair
            for z in range(50)  # =1 for A, high for B
            for y in (-diff * z, diff * z)
            # if tuple(x + y) not in antenna_pair # omit for B
        ]

        for node in nodes:
            if (
                node[0] >= 0
                and node[1] >= 0
                and node[0] < canvas.shape[0]
                and node[1] < canvas.shape[1]
            ):
                canvas[node] += 1
