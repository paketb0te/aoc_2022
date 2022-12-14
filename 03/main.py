INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"

import string

prio_map = dict(zip(string.ascii_lowercase, range(1, 27))) | dict(
    zip(string.ascii_uppercase, range(27, 53))
)

prio_sum = 0
badge_prio_sum = 0
elf_group = []

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        line = line.strip()

        # Part 1
        # Get the intersection of the first and second half of the line.
        item_set = set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
        # Get the only element in the set and its priority to the total.
        prio_sum += prio_map[next(iter(item_set))]

        # Part 2
        # Add an elf to the group
        elf_group.append(set(line))
        # process in groups of three
        if len(elf_group) >= 3:
            badge_set = set.intersection(*elf_group)
            badge_prio_sum += prio_map[next(iter(badge_set))]
            elf_group.clear()

print(f"Part 1: {prio_sum}")
print(f"Part 2: {badge_prio_sum}")
