#!/usr/bin/python3

"""
prime game predictor
"""


def isWinner(x, nums):
    """
    Returns the winner of a game over 'x' rounds
    where each round works witht the corresponding
    enter in the array 'nums'
    Args:
            x: int = number of rounds to perform
            nums: list[int] = an array of int. each round works on the int
            for that round
    """
    ben = 0
    maria = 0
    nums = set(nums)
    nums = list(nums)
    if x <= 0:
        return None
    if nums == []:
        return None
    for y in range(x):
        try:
            n = nums[y]
        except IndexError:
            break
        if n == 1:
            ben = ben + 1
            continue
        if n == 0:
            continue
        count = 1  # non-prime count
        for i in [2, n]:
            for j in [i, n]:
                if i * j > n:
                    break
                count = count + 1
        primeNum = n - count
        if primeNum % 2 == 0:
            ben = ben + 1
        else:
            maria = maria + 1
    if ben == maria:
        return None
    elif ben > maria:
        return 'Ben'
    elif ben < maria:
        return 'Maria'
