#!/usr/bin/python3
""" 2D Matrix Rotation by 90 degrees
"""


def rotate_2d_matrix(matrix: list) -> list:
    """Rotate n x n matrix in place
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(map(lambda l: len(l) == cols, matrix)):
        return

    x = 0
    y = rows - 1

    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if y == -1:
            y = rows - 1
            x += 1
        matrix[-1].append(matrix[y][x])
        if x == cols - 1 and y >= -1:
            matrix.pop(y)
        y -= 1
