import re
from sympy.core.numbers import int_valued
from sympy import Matrix

with open("13.txt") as infile:
    data = [
        [int(y) for y in re.findall(r"\d+", x)] for x in infile.read().split("\n\n")
    ]


def solve(machine):
    a = Matrix([machine[0:2], machine[2:4]]).T
    b = Matrix(machine[4:])
    solution = a.solve(b)

    return (
        (int_valued(solution[0]) and int_valued(solution[1]))
        and sum((solution[0] * 3, solution[1]))
        or 0
    )


total = 0
for machine in data:
    machine[4:] = [machine[4] + 10000000000000, machine[5] + 10000000000000]
    total += solve(machine)

print(total)
