#!/usr/bin/python3
"""
makeChange(coins, total): determine the fewest number of coins
    needed to meet a given amount total
    achieving 0(n) through Bottom-Up approach
"""


def makeChange(coins, total):
    """ Return: fewest number of coins needed to meet total """
    if total <= 0:
        return 0

    temp = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total % coin <= total:
            temp += total // coin
            total = total % coin

    return temp if total == 0 else -1
