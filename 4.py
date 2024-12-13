import numpy as np
from skimage.util import view_as_windows

with open("4.txt", "r") as infile:
    raw = [x.strip() for x in infile.readlines()]

CONVERT_DICT = {"-": -1, "X": 0, "M": 1, "A": 2, "S": 3}

A = ["XMAS"]
B = ["SAMX"]
C = ["X", "M", "A", "S"]
D = ["S", "A", "M", "X"]
E = ["X---", "-M--", "--A-", "---S"]
F = ["S---", "-A--", "--M-", "---X"]
G = ["---S", "--A-", "-M--", "X---"]
H = ["---X", "--M-", "-A--", "S---"]

I = ["M-S", "-A-", "M-S"]
J = ["S-M", "-A-", "S-M"]
K = ["S-S", "-A-", "M-M"]
L = ["M-M", "-A-", "S-S"]


def xmax_to_np(raw: list):
    data = np.zeros((len(raw), len(raw[0])))
    for i, line in enumerate(raw):
        line = line.strip()
        for j, c in enumerate(line):
            if c not in CONVERT_DICT:
                continue
            data[i, j] = CONVERT_DICT[c]
    return data


def count_occurences(data, pattern):
    windows = view_as_windows(data, pattern.shape)
    return np.logical_or(windows == pattern, pattern == -1).all(axis=(2, 3)).sum()


data = xmax_to_np(raw)
sum(count_occurences(data, xmax_to_np(x)) for x in (A, B, C, D, E, F, G, H))
sum(count_occurences(data, xmax_to_np(x)) for x in (I, J, K, L))
