with open("7.txt") as infile:
    data = [
        [int(z) for y in x.split() if (z := y.strip().replace(":", ""))]
        for x in infile.readlines()
    ]


def elephant(target, ropes):
    if not ropes:
        return False
    elif [target] == ropes:
        return True

    if not target % ropes[-1]:
        if elephant(target // ropes[-1], ropes[:-1]):
            return True

    if str(target).endswith(str(ropes[-1])):  # B
        try:
            if elephant(int(str(target)[: -len(str(ropes[-1]))]), ropes[:-1]):
                return True
        except ValueError:
            pass

    if target < ropes[-1]:
        return False
    return elephant(target - ropes[-1], ropes[:-1])


sum = 0
for row in data:
    if elephant(row[0], row[1:]):
        sum += row[0]

sum
