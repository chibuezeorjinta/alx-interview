#!/usr/bin/python3
""" Module to calculate changeNum. """


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given amount total

    Args:
    	coins: list = Values of your the coins
    	total:int = target amount

    Returns:
    	changeNum: fewest number of coins needed to meet total
    """
    if total < 1:
        return 0

    if (coins is None or len(coins) == 0):
        return -1

    changeNum = 0
    # Sort the coins from largest to smallest
    sortCoins = sorted(coins, reverse=True)
    money_left = total

    for coin in sortCoins:
        while (money_left % coin >= 0 and money_left >= coin):
            changeNum += money_left // coin
            money_left = money_left % coin

    if money_left == 0:
        changeNum = changeNum
    else:
        changeNum = -1

    return changeNum