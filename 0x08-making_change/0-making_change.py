#!/usr/bin/python3
"""
Module for making change.
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given total.

    Args:
        coins (List[int]): List of coin values.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total,
             or -1 if it cannot be met.
    """
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1


if __name__ == "__main__":
    # Example usage
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
