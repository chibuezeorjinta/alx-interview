#!/usr/bin/python3
"""using a hashmap, travers the list of list"""


def canUnlockAll(boxes):
    """
        with a list, we dynamically append our available keys while
        removing the opened boxes
            Args:
                boxes: list = a list of lists representing the boxes
            Return: boolean = true if all the boxes can be opened, else false
    """

    Box = {}
    indexlist = []
    openboxes = []
    openboxes.append(0)
    for i, j in enumerate(boxes):
        Box[i] = j
        indexlist.append(i)
    indexlist.remove(0)
    for i in openboxes:
        if Box.get(i) is not []:
            for value in Box.get(i):
                if value not in openboxes:
                    openboxes.append(value)
                    indexlist.remove(value)
        else:
            continue
    if len(indexlist) == 0:
        return True
    else:
        return False
