# INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"

map_1 = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

map_2 = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}

with open(INPUT_FILE, mode="r") as infile:
    score_1 = sum(map_1[line.strip()] for line in infile)

print(f"Score for Part 1: {score_1}")

with open(INPUT_FILE, mode="r") as infile:
    score_2 = sum(map_2[line.strip()] for line in infile)

print(f"Score for Part 2: {score_2}")
