#!/usr/bin/python3
""" Rotation of a 2D matrix """


def rotate_2d_matrix(matrix):
    """
    Rotate a given matrix

    Args:
        matrix: List of lists
    """
    n = len(matrix)
    # for each row
    for x in range(n):
        reversedRow = []
        # Collect the values from back as a list
        for y in range((n - 1), -1, -1):
            reversedRow.append(matrix[y][x])
        matrix.append(reversedRow)
    # Remove the rows original matrix
    for i in range(n):
        matrix.pop(0)
