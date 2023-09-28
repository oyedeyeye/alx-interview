#!/usr/bin/python3
"""
Prime Number Game
"""


def check_prime_number(n):
    """ check if n is a prime number """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True


def next_prime_number(start, numbers):
    """checks next primes in the list"""
    for num in range(start + 1, len(numbers)):
        if numbers[num] and check_prime_number(num):
            return num
    return None


def isWinner(x, nums):
    """
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        numbers = [True] * (n + 1)
        numbers[0] = numbers[1] = False
        turn_maria = True

        while True:
            prime = next_prime_number(1, numbers)
            if prime is None:
                break

            for multiple in range(prime, len(numbers), prime):
                numbers[multiple] = False

            if turn_maria:
                maria_wins += 1
            else:
                ben_wins += 1

            turn_maria = not turn_maria

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
