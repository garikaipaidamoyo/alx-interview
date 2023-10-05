#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Should print True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Should print True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Should print False
