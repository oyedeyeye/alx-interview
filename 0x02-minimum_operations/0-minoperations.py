#!/usr/bin/python3
"""
"""


def minOperations(n):
    """Returns an integer
    If n is impossible to achieve, return 0
    """
    ops = 0
    min_ops = 2
    while n > 1:
        while n % min_ops == 0:
            ops += min_ops
            n /= min_ops
        min_ops += 1
    return ops
