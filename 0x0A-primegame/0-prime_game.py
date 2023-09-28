#!/usr/bin/python3
"""
Prime Number Game
"""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def next_prime(start, numbers):
    for num in range(start + 1, len(numbers)):
        if numbers[num] and is_prime(num):
            return num
    return None


def isWinner(x, nums):
    if x <= 0 or len(nums) != x:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 0:
            # Skip this round if n is not positive
            continue

        numbers = [True] * (n + 1)
        numbers[0] = numbers[1] = False
        turn_maria = True

        while True:
            prime = next_prime(1, numbers)
            if prime is None:
                break

            for multiple in range(prime, len(numbers), prime):
                numbers[multiple] = False

            if turn_maria:
                turn_maria = False
            else:
                turn_maria = True

        if not turn_maria:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Test with provided edge cases
print(isWinner(5, [2, 5, 1, 4, 3]))  # Output: Ben
print(isWinner(-1, [10]))  # Output: None
print(isWinner(0, [0]))  # Output: None
print(isWinner(6, [1, 1, 0, 0, 1, 8]))  # Output: Ben
print(isWinner(10, [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]))  # Output: Maria
print(isWinner(5, [1, 2, 3, 4, 5]))  # Output: Maria
