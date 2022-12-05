from collections import deque
from copy import deepcopy

INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"

reading_map: bool = True
map_lines: list[str] = []
instruction_lines: list[str] = []

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        line = line.strip("\n")
        # Marks the break between map and instructions.
        if not line:
            reading_map = False
            continue
        # Handle map lines
        if reading_map:
            map_lines.append(line)
        # Handle instruction lines
        else:
            instruction_lines.append(line)

# Remove '[', ']' and ' ' and drop the bottom row (numbering).
map_lines = [line[1::4] for line in map_lines[:-1]]
# split into single characters
map_lists = [list(line) for line in map_lines]
# Zip up the lists in reverse order so the "bottom crate" will be the first element in each stack.
# This allows us to easier use deque because we can just append() and pop().
crate_map = [deque(stack) for stack in zip(*map_lists[::-1])]
# Remove the "air" above crates (elements not containg a character).
for stack in crate_map:
    while not stack[-1].isalpha():
        stack.pop()

instructions = [line.split()[1::2] for line in instruction_lines]
instructions = [tuple(int(char) for char in instr) for instr in instructions]

# Part 1
crate_map_part_1 = deepcopy(crate_map)
for cnt, src, dst in instructions:
    for i in range(cnt):
        crate = crate_map_part_1[src - 1].pop()
        crate_map_part_1[dst - 1].append(crate)

top_crates_1 = "".join(stack.pop() for stack in crate_map_part_1)

# Part 2
crate_map_part_2 = deepcopy(crate_map)
for cnt, src, dst in instructions:
    crates: deque[str] = deque()
    for i in range(cnt):
        crates.append(crate_map_part_2[src - 1].pop())
    crate_map_part_2[dst - 1].extend(reversed(crates))

top_crates_2 = "".join(stack.pop() for stack in crate_map_part_2)

print(f"Part 1: {top_crates_1}")
print(f"Part 2: {top_crates_2}")
