INPUT_FILE = "test_input.txt"
# INPUT_FILE = "input.txt"

from collections import deque

with open(INPUT_FILE, mode="r") as infile:
    line = infile.read().strip()


def get_marker(datastream: str, marker_size: int) -> int | None:
    fifo = deque(datastream[0 : marker_size - 1])
    for idx, char in enumerate(datastream[marker_size - 1 :]):
        fifo.append(char)
        # If all characters are different, return index + offset
        # (we are iterating over a slice, not the original list).
        if len(set(fifo)) == marker_size:
            return idx + marker_size
        fifo.popleft()


print(f"Part 1: {get_marker(datastream=line, marker_size=4)}")
print(f"Part 2: {get_marker(datastream=line, marker_size=14)}")
