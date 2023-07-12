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
    if n <= 1:
        return 0
    if n is None:
        return 0
    for _ in range(n):
        if (n % len(string_val)) == 0:
            paste_len = len(string_val)
            string_val += ('H' * paste_len)
            count += 2
            if len(string_val) == n:
                return count
        else:
            string_val += ('H' * paste_len)
            count += 1
            if len(string_val) == n:
                return count
    return n


if __name__ == "__main__":
    minOperations()
