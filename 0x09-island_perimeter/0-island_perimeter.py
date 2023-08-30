#!/usr/bin/python3
"""
function def island_perimeter(grid): that returns the perimeter of the island
described in grid:
    grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to the
    water surrounding the island).
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if grid is None or len(grid) is None or len(grid[0]) is None:
        return

    result = 0
    for r in range(1, len(grid)):
        for c in range(1, len(grid[r])):
            if grid[r][c] == 1:
                result += 4

                if grid[r][c - 1] == 1:
                    result -= 2

                if grid[r - 1][c] == 1:
                    result -= 2

    return result
