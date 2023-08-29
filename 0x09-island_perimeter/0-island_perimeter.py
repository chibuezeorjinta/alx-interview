#!/usr/bin/python3
"""Find the perimeter of a given island"""


def island_perimeter(grid):
    """
    A 2d array is provided.
    count the 0's around the 1's

    Args:
        grid: list[list[int]]
    Return:
        int
    """
    rows, cols = len(grid), len(grid[0])

    # Create a larger grid with padding of 0s around the original grid
    bigGrid = [
        [0] * (cols + 2)
    ]
    for row in grid:
        bigGrid.append([0] + row + [0])
    bigGrid.append([0] * (cols + 2))

    perimeter = 0

    # Calculate the perimeter by checking the neighbors of each land cell
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if bigGrid[i][j] == 1:  # If it's land
                perimeter += 4 - (
                    bigGrid[i - 1][j] + bigGrid[i + 1][j] +
                    bigGrid[i][j - 1] + bigGrid[i][j + 1]
                )

    return perimeter
