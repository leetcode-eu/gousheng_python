
from typing import Optional, List


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Another idea is to apply DFS for nodes of p tree and q tree SIMULTANEOUSLY
        # Previously, we perform DFS only on one tree's node, however, now we perform DFS
        # on p tree and q tree simultaneously to continuously check the equality of their nodes

        # reaching bottom Nones
        if p==None and q==None:
            return True

        # only one of them is None
        elif p==None or q==None:
            return False

        # both of them have values but different
        elif p.val != q.val:
            return False

        # p.val = q.val
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
