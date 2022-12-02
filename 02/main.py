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

3 > 2 > 1 > 3
"""
from enum import Enum
from typing import Callable

INPUT_FILE = "test_input.txt"
# INPUT_FILE = "input.txt"


class Shape(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


def get_shape(code: str) -> Shape:
    return CODE_MAPPING_PART_1[code]


def get_winning_move(shape: Shape) -> Shape:
    return Shape((shape.value + 1) % 3)


def get_drawing_move(shape: Shape) -> Shape:
    return Shape(shape.value)


def get_losing_move(shape: Shape) -> Shape:
    return Shape((shape.value + 2) % 3)


CODE_MAPPING_PART_1 = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}

CODE_MAPPING_PART_2 = {
    "X": get_losing_move,
    "Y": get_drawing_move,
    "Z": get_winning_move,
}


def get_moves_part_1(code_1: str, code_2: str) -> tuple[Shape, Shape]:
    return get_shape(code=code_1), get_shape(code=code_2)


def get_moves_part_2(code_1: str, code_2: str) -> tuple[Shape, Shape]:
    s1 = get_shape(code=code_1)
    s2 = CODE_MAPPING_PART_2[code_2](shape=s1)
    return s1, s2


def evaluate_round(s1: Shape, s2: Shape) -> tuple[int, int]:
    v1 = s1.value + 1
    v2 = s2.value + 1

    tmp = (v1 - v2 + 3) % 3
    if tmp == 1:  # p1 wins
        v1 += 6
    elif tmp == 2:  # p2 wins
        v2 += 6
    else:  # draw
        v1 += 3
        v2 += 3

    return v1, v2


def get_scores(
    moves_getter: Callable[[str, str], tuple[Shape, Shape]]
) -> tuple[int, int]:
    scores = (0, 0)
    with open(INPUT_FILE, mode="r") as infile:
        for line in infile:
            line = line.strip()

            code_1, code_2 = line.split(maxsplit=1)
            s1, s2 = moves_getter(code_1, code_2)
            score_1, score_2 = evaluate_round(s1=s1, s2=s2)
            scores = scores[0] + score_1, scores[1] + score_2
    return scores


scores = get_scores(moves_getter=get_moves_part_1)

print("-" * 80)
print(f"# Part 2:")
print(f"P1: {scores[0]}\nP2: {scores[1]}")

scores = get_scores(moves_getter=get_moves_part_2)

print("-" * 80)
print(f"# Part 2:")
print(f"P1: {scores[0]}\nP2: {scores[1]}")
