import numpy as np

INPUT_FILE = "test_input.txt"
INPUT_FILE = "input.txt"

grid = np.genfromtxt(INPUT_FILE, delimiter=1)

visibility = np.full(grid.shape, False)

# Visibility from left side:
for i in range(0, grid.shape[0], 1):
    highest = -1
    for j in range(0, grid.shape[1], 1):
        tree = grid[i][j]
        visible = tree > highest
        visibility[i][j] |= visible
        highest = max(tree, highest)

# visibility from the right side:
for i in range(0, grid.shape[0], 1):
    highest = -1
    for j in range(-1, -grid.shape[0] - 1, -1):
        tree = grid[i][j]
        visible = tree > highest
        visibility[i][j] |= visible
        highest = max(tree, highest)

# Visibility from the top side:
for j in range(0, grid.shape[1], 1):
    highest = -1
    for i in range(0, grid.shape[0], 1):
        tree = grid[i][j]
        visible = tree > highest
        visibility[i][j] |= visible
        highest = max(tree, highest)

# Visibility from the bottom side:
for j in range(0, grid.shape[1], 1):
    highest = -1
    for i in range(-1, -grid.shape[0] - 1, -1):
        tree = grid[i][j]
        visible = tree > highest
        visibility[i][j] |= visible
        highest = max(tree, highest)


def get_scenic_score(grid: np.ndarray, i: int, j: int, i_step: int, j_step: int) -> int:
    tree_height = grid[i][j]
    score = 0
    while 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]:
        i += i_step
        j += j_step
        try:
            if i < 0 or j < 0:
                raise IndexError
            curr_height = grid[i][j]
            score += 1
            if curr_height >= tree_height:
                break
        except IndexError:
            break
    return score


scenic_scores = np.full(grid.shape, 1, dtype=int)

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        for i_step, j_step in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            scenic_scores[i][j] *= get_scenic_score(
                grid=grid, i=i, j=j, i_step=i_step, j_step=j_step
            )


print(f"Part 1: {np.sum(visibility)}")
print(f"Part 2: {np.max(scenic_scores)}")
