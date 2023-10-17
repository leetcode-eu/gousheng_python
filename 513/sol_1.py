
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        deque = [root]
        while deque:
            next_level_nodes = []
            for node in deque:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            if len(next_level_nodes) != 0:
                deque = next_level_nodes
            else:
                return deque[0].val