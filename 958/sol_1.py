
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        deque = [(root, 1)]
        values = []
        while deque:
            node, position_number = deque.pop(0)
            values.append(position_number)
            if node.left:
                deque.append((node.left, position_number * 2))
            if node.right:
                deque.append((node.right, position_number * 2 + 1))

        return len(values) == values[-1]