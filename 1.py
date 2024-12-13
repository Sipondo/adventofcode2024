import numpy as np

data = np.loadtxt("1.txt")

data[:, 0] = sorted(data[:, 0])
data[:, 1] = sorted(data[:, 1])

print(sum(np.abs(data[:, 0] - data[:, 1])))  # A

sum([x * list(data[:, 1]).count(x) for x in data[:, 0]])
