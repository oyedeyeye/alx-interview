#!/usr/bin/python3
"""
This module contains an algorithm that resolves the
N-Queen puzzle using backtracking
"""

from typing import List


def isSafe(m_queen, nqueen):
    """
    Determines if queens can kill each other

    Args:
        m_queen: array containing the queen's positions
        nqueen: queen number

    Return:
        True: when queens can not kill each other
        False: when queens can kill each other
    """

    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

        return True


def print_result(m_queen, nqueen):
    """
    Prints list with the Queen's positions

    Args:
        m_queen: array containing the queen's positions
        nqueen: queen number
        """

    result = []

    for j in range(nqueen):
        result.append([i, m_queen[i]])

    print(result)


def Queen(m_queen, nqueen):
    """
    Recursive function that executes Backtracking algorithm

    Args:
        m_queen: array containing the queen's positions
        nqueen: queen number
    """
    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] -= 1

    while ((m_queen[nqueen] < len(m_queen) - 1)):
        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen) is True:

            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)


def solvedNQueens(size):
    """
    Invokes the Backtracking Algorithms

    Args:
        size: size of the chess board
    """
    m_queen = [-1 for i in range(size)]
    Queen(m_queen, 0)


# def solvedNQueens(size: int) -> List[List[str]]:
#     col = set()
#     posDiag = set() # (r + c) = constant value
#     negDiag = set() # (r - c) = constant value
#     res = []
#     board = [["."] * size for i in range(size)]

#     def backtrack(r):
#         if r == size:
#             copy = ["".join(row) for row in board]
#             res.append(copy)
#             return

#         for c in range(size):
#             if c in col or (r + c) in posDiag or (r - c) in negDiag:
#                 continue

#             col.add(c)
#             posDiag.add(r + c)
#             negDiag.add(r - c)
#             board[r][c] = "Q"

#             backtrack(r + 1)

#             col.remove(c)
#             posDiag.remove(r + c)
#             negDiag.remove(r - c)
#             board[r][c] = "."

#     backtrack(0)
#     return res


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except TypeError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solvedNQueens(size)
