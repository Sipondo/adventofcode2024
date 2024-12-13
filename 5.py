with open("5.txt", "r") as infile:
    raw = [x.strip() for x in infile.readlines()]


rules = set()
updates = []

for line in raw:
    if "|" in line:
        rules.add(tuple([int(x.strip()) for x in line.split("|")]))
    else:
        if not line:
            continue
        updates.append([int(x.strip()) for x in line.split(",")])

good_updates = []
bad_updates = []
for update in updates:
    for i, e_i in enumerate(update):
        for j, e_j in enumerate(update[i:]):
            if (e_j, e_i) in rules:
                bad_updates.append(update)
                break
        else:
            continue
        break
    else:
        good_updates.append(update)


print(sum([update[len(update) // 2] for update in good_updates]))

for update in bad_updates:
    sorting = True
    while sorting:
        sorting = False
        for i, e_i in enumerate(update):
            for j, e_j in enumerate(update[i:]):
                if (e_j, e_i) in rules:
                    sorting = True
                    update[i], update[i + j] = update[i + j], update[i]

print(sum([update[len(update) // 2] for update in bad_updates]))
