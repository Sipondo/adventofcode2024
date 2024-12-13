rocks = {}
with open("11.txt") as infile:
    for rock in map(int, infile.read().split()):
        rocks[rock] = rocks[rock] + 1 if rock in rocks else 1


def iterate(old):
    rocks = {}
    for rock, count in old.items():
        if rock == 0:
            rocks[1] = rocks[1] + count if 1 in rocks else count
        elif not ((l := len(s := str(rock))) % 2):
            r1, r2 = int(s[: l // 2]), int(s[l // 2 :])
            rocks[r1] = rocks[r1] + count if r1 in rocks else count
            rocks[r2] = rocks[r2] + count if r2 in rocks else count
        else:
            rocks[rock * 2024] = (
                rocks[rock * 2024] + count if rock * 2024 in rocks else count
            )
    return rocks


for i in range(1, 75 + 1):
    rocks = iterate(rocks)
    # print(rocks)
    print(i, "Stones:", sum(rocks.values()))
