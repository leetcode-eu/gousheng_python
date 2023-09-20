
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # DFS solution 

        def dfs(node, res):
            if not node:
                return

            dfs(node.left, res)
            res.append(node.val)
            dfs(node.right, res)
            return res

        if not root:
            return []
        else:
            dfs(root, [])
        
        return dfs(root, [])
