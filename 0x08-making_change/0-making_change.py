#!/usr/bin/python3
"""
makeChange(coins, total): determine the fewest number of coins
    needed to meet a given amount total
"""


import sys


def makeChange(coins, total):
    """ Return: fewest number of coins needed to meet total """
    if total == 0:
        return 0

    length = len(coins)

    # initialize the result to max value the variable can hold
    result = sys.maxsize

    for i in range(0, length):
        if (coins[i] <= total):
            sub_result = makeChange(coins, total - coins[i])
            if (sub_result != sys.maxsize and sub_result + 1 < result):
                result = sub_result + 1

    return result
