
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, res):
            if node.left is not None:
                dfs(node.left, res)

            if node.right is not None:
                dfs(node.right, res)

            res.append(node.val)

            return res

        if not root:
            return []
        else:
            return dfs(root, [])