#!/usr/bin/python3
"""Get minimum operations with copy all and paste only"""


def minOperations(n: int = None) -> int:
    """
    Takes in an int, to return the minimum operations
    of copy all and paste to get to the target int
    when target is a prime, it returns n.
    if the current length of the string is a multiple
    of the target, do copy all and paste.
    else only paste.
    Args:
        n: int = target value to find minimum operations.
    Return: int = count of minimum operations.
    """
    string_val: str = 'H'
    count: int = 0
    paste_len: int = 0

    if n is None or n <= 1:
        return 0

    while len(string_val) < n:
        if n % len(string_val) == 0:
            paste_len = len(string_val)
            count += 2
        else:
            count += 1
        string_val += ('H' * paste_len)

    return count if len(string_val) == n else n
