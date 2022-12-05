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
        # An empty line marks the break between map and instructions.
        if not line:
            reading_map = False
            continue
        # Handle map lines
        if reading_map:
            map_lines.append(line)
        # Handle instruction lines
        else:
            instruction_lines.append(line)

# We only care about the characters, not the whitespace and brackets.
# -> Parsing only every 4th character drops all '[', ']' and ' '.
map_lines = [line[1::4] for line in map_lines]

# Split into list of single characters and drop the bottom row
# because it contains only the numbers of the stacks - we will use indices instead.
map_lists = [list(line) for line in map_lines[:-1]]

# Zip up the lists in reverse order so the "bottom crate" will be the first element in each stack.
# This allows us to easier use deque because we can just append() and pop()
# instead of appendleft() and popleft().
crate_stacks = [deque(stack) for stack in zip(*map_lists[::-1])]

# Remove the "air" above crates (any elements not containg a character).
for stack in crate_stacks:
    while not stack[-1].isalpha():
        stack.pop()

# Extract the moving instructions as lists of [count, source-stack, destination-stack].
instructions = [line.split()[1::2] for line in instruction_lines]
# Convert the instructions to lists of ints.
instructions = [[int(char) for char in instr] for instr in instructions]
# Remember to subtract 1 from src / dst because we want to use them as indices!
instructions = [[sum(e) for e in zip(instr, [0, -1, -1])] for instr in instructions]

# Part 1
crate_stacks_part_1 = deepcopy(crate_stacks)
for cnt, src, dst in instructions:
    for _ in range(cnt):
        crate = crate_stacks_part_1[src].pop()
        crate_stacks_part_1[dst].append(crate)

top_crates_1 = "".join(stack.pop() for stack in crate_stacks_part_1)

# Part 2
crate_stacks_part_2 = deepcopy(crate_stacks)
for cnt, src, dst in instructions:
    crates: deque[str] = deque()
    for _ in range(cnt):
        crates.append(crate_stacks_part_2[src].pop())
    for _ in range(cnt):
        crate_stacks_part_2[dst].append(crates.pop())

top_crates_2 = "".join(stack.pop() for stack in crate_stacks_part_2)

print(f"Part 1: {top_crates_1}")
print(f"Part 2: {top_crates_2}")
