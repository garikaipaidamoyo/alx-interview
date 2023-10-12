#!/usr/bin/python3
"""
Module for minimum operations.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters.

    Args:
        n (int): The target number of H charac

    Returns:
        int: The fewest number of operations to reach n H characters.
    """
    if not isinstance(n, int) or n <= 0:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor

        divisor += 1

    return operations


if __name__ == "__main":
    n = 4
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}"
          .format(n, minOperations(n)))
