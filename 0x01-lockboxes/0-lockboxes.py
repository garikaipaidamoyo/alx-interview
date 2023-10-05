#!/usr/bin/python3
"""
Module: 0-lockboxes
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of boxes, each containing a list of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    opened = [False] * n  # Initialize all boxes as unopened
    opened[0] = True  # The first box is already open
    keys = [0]  # Start with the key to the first box

    for key in keys:
        for box in boxes[key]:
            if 0 <= box < n and not opened[box]:
                opened[box] = True
                keys.append(box)

    return all(opened)  # Check if all boxes are opened
