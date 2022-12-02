"""
A-B
Rock vs Rock:        0      -> draw
Rock vs Paper:      -1      -> b
Rock vs Scissors:   -2      -> a

Paper vs Rock:       1      -> a
Paper vs Paper:      0      -> draw
Paper vs Scissors:  -1      -> b

Scissors vs Rock:    2      -> b
Scissors vs Paper:   1      -> a
Scissors vs Scissor: 0      -> draw
"""

from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


MAPPING = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}


def get_shape(code: str) -> Shape:
    return MAPPING[code]


def evaluate_round(p1: str, p2: str) -> tuple[int, int]:
    v1 = get_shape(code=p1).value
    v2 = get_shape(code=p2).value

    tmp = v1 - v2
    if tmp in (-2, 1):  # p1 wins
        v1 += 6
    elif tmp in (-1, 2):  # p2 wins
        v2 += 6
    else:  # draw
        v1 += 3
        v2 += 3

    return v1, v2


INPUT_FILE = "test_input.txt"

scores = (0, 0)

with open(INPUT_FILE, mode="r") as infile:
    for line in infile:
        line = line.strip()

        p1, p2 = line.split(maxsplit=1)
        s1, s2 = evaluate_round(p1=p1, p2=p2)
        scores = scores[0] + s1, scores[1] + s2

print(f"P1: {scores[0]}\nP2: {scores[1]}")
