#!/usr/bin/python3
"""
Prime Number Game
"""


def check_prime_number(n):
    """ check if n is a prime number """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
        return True


def add_prime_number(n, primes):
    """Adds primes to list"""
    last_prime_number = primes[-1]
    if n > last_prime_number:
        for i in range(last_prime_number + 1, n + 1):
            if check_prime_number(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_prime_number(max(nums), primes)

    for round in range(x):
        _sum = sum((i != 0 and i <= nums[round])
                   for i in primes[:nums[round] + 1])
        if (_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
