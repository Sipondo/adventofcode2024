import numpy as np

with open("2.txt", "r") as infile:
    data = [[int(y) for y in x.strip().split()] for x in infile.readlines()]


def is_safe(report):
    diffs = list(map(lambda x: x[0] - x[1], zip(report, report[1:])))
    plus = all([x >= 0 for x in diffs])
    min = all([x <= 0 for x in diffs])
    three = all([1 <= abs(x) <= 3 for x in diffs])
    return (plus or min) and three


def is_sort_of_safe(report, dampened=False):
    slope = 0
    for i, new in enumerate(report):
        if i == 0:
            old = report[i]
            continue
        new = report[i]
        if 1 <= abs(old - new) <= 3:
            if slope == 0:
                slope = -1 if old > new else 1

            if old - new < 0 and slope == 1 or old - new > 0 and slope == -1:
                old = report[i]
                continue
        if dampened:
            return False
        else:
            dampened = True
    return True


print(sum([is_safe(x) for x in data]))
print(
    sum(
        [
            is_sort_of_safe(x)
            or is_sort_of_safe(x[1:], True)
            or is_sort_of_safe([x[0]] + x[2:], True)
            for x in data
        ]
    )
)
