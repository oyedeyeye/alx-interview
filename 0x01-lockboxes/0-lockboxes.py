#!/usr/bin/python3
"""canUnlockAll(boxes): method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened
        Args:
            boxes (list): a list of lists
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        boxIdx = locked_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[boxIdx])
            unlocked_boxes.add(boxIdx)
    return n == len(unlocked_boxes)
