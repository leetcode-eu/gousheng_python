
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        stack = [root]
        res   = []

        while stack:
            node = stack.pop()

            if isinstance(node, TreeNode):
                stack.append(node.val)

                if node.right is not None:
                    stack.append(node.right)

                if node.left is not None:
                    stack.append(node.left)
            else:
                val = node
                res.append(val)

        return res