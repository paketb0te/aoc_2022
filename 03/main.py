INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"

import string

prio_map = dict(zip(string.ascii_lowercase, range(1, 27))) | dict(
    zip(string.ascii_uppercase, range(27, 53))
)

prio_sum = 0

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        line = line.strip()
        # Get the intersection of the first and second half of the line.
        item_set = set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
        # Get the only element in the set and its priority to the total.
        prio_sum += prio_map[next(iter(item_set))]

print(f"Part 1: {prio_sum}")
