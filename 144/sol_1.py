from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, res):
            """

            :param node: iterated node
            :param res: list to contain results
            :return:
            """
            if not node:
                return

            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
            return res

        if not root:
            return []
        else:
            dfs(root, [])

        return dfs(root, [])
