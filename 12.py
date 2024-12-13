import numpy as np
from scipy.signal import convolve
from scipy.ndimage import measurements

with open("12_test.txt") as infile:
    data = [x.strip() for x in infile.readlines()]

garden = np.zeros((len(data), len(data[0])))

for i in range(len(data)):
    for j in range(len(data)):
        garden[i][j] = ord(data[i][j])

# A

KERNEL = np.array([[0, 1, 0], [1, 100, 1], [0, 1, 0]])

price = 0
for species in np.unique(garden):
    monoculture, plot_count = measurements.label((garden == species) * 1)

    for plot_id in range(1, plot_count + 1):
        plot = (monoculture == plot_id) * 1

        fencing = convolve(plot, KERNEL)
        fencing[fencing >= 100] = 0

        price += np.sum(plot) * np.sum(fencing)

price

# B

KERNEL = np.array([[0, 8, 0], [4, 100, 1], [0, 2, 0]])

price = 0
for species in np.unique(garden):
    monoculture, plot_count = measurements.label((garden == species) * 1)

    for plot_id in range(1, plot_count + 1):
        plot = (monoculture == plot_id) * 1

        fencing = convolve(plot, KERNEL)
        fencing[fencing >= 100] = 0

        sides = 0
        iterfence = fencing.copy()
        for i in (8, 4, 2, 1):
            sides += measurements.label((iterfence >= i) * 1)[1]
            iterfence = iterfence % i

        price += np.sum(plot) * sides

price
