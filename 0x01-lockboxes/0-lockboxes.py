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

    allKeys = {0}
    allKeys.update(boxes[0])
    openboxes = [] + boxes[0]

    for key in openboxes:
        if key < len(boxes) and key >= 0:
            allKeys.update(boxes[key])
        new_keys = allKeys - set(openboxes)
        openboxes += new_keys

    useful_keys = [k for k in allKeys if k < len(boxes)]
    if len(useful_keys) == len(boxes):
        return True
    return False