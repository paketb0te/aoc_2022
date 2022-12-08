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

# print(visibility)

print(f"Part 1: {np.sum(visibility)}")
print(f"Part 2: {2}")
