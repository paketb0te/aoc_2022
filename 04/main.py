INPUT_FILE = "test_input.txt"
# INPUT_FILE = "input.txt"

import re

fully_contained_assignments = 0
overlapping_assignment_pairs = 0

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        line = line.strip()
        ass_tuple = tuple(int(i) for i in re.split(r",|-", line, maxsplit=3))
        r1 = range(ass_tuple[0], ass_tuple[1] + 1)
        r2 = range(ass_tuple[2], ass_tuple[3] + 1)
        # Part 1:
        # Check if first assignment is contained in the second
        # or vice versa (just comparing start and end values).
        if (r1[0] in r2 and r1[-1] in r2) or (r2[0] in r1 and r2[-1] in r1):
            fully_contained_assignments += 1
        # Part 2:
        # Check if first and second assignment overlap.
        if r1[0] in r2 or r1[-1] in r2 or r2[0] in r1 or r2[-1] in r1:
            overlapping_assignment_pairs += 1

print(f"Part 1: {fully_contained_assignments}")
print(f"Part 2: {overlapping_assignment_pairs}")
