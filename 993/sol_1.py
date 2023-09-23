
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        deque = [(root, 0)]
        records = {}

        while deque:
            parrent_node, prev_depth = deque.pop(0)
            current_depth = prev_depth + 1

            if parrent_node.left:
                deque.append((parrent_node.left, current_depth))
                records[parrent_node.left.val] = (parrent_node, current_depth)

            if parrent_node.right:
                deque.append((parrent_node.right, current_depth))
                records[parrent_node.right.val] = (parrent_node, current_depth)

        if x not in records or y not in records:
            return False

        x_parrent_node, x_depth = records[x]
        y_parrent_node, y_depth = records[y]

        return x_parrent_node is not y_parrent_node and x_depth == y_depth