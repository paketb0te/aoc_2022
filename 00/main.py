INPUT_FILE = "test_input.txt"

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        line = line.strip()
        ...