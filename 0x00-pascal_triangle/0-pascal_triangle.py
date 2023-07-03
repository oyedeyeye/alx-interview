#!/usr/bin/python3
"""
function that returns list of lists of integers representing
Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    computes list representing the pascal triangle
    """
    if n <= 0:
        return []
    resArr = [[1]]

    for i in range(n - 1):
        temp = [0] + resArr[-1] + [0]
        row = []

        for j in range(len(resArr[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        resArr.append(row)
    return resArr
