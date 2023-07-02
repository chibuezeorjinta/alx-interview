#!/usr/bin/python3
"""for the pascals triangle. My attempt will use recursion"""

def pascal_triangle(n) -> list:
    """
    wrapper function to analyse the recussive main function
    Args:
            n (int): number to rows worth of the triangle

    Returns (list):
            Output from createnewlist function
    """
    if n <= 0:
        return []
    pascalsList = [
        [1]
    ]
    count = 1
    return createnewlist(pascalsList, count, n)

def createnewlist(mainList: list, count, n) -> list:
    """
    Recursive function to create and append new rows of the pascals triangle.
            Args:
                    mainlist (list): Full list of lists
                    count (int): counter to keep track of iterations.
                                                Starts from 1
                    n (int): provided target number of rows

            Return (list):
                    A list of lists (mainlist)
    """
    if count == n:
        return mainList
    else:
        lastlist = mainList[-1]
        workingList = [0, 0]
        newList = []

        for item in lastlist:
            workingList.insert(len(workingList) - 1, item)
        for i in range(len(workingList) - 1):
            newList.append(workingList[i] + workingList[i+1])
        mainList.append(newList)
        count += 1
        return createnewlist(mainList, count, n)
