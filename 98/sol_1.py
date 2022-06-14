# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        def InOrder(root, res):
            
            if not root:
                return
            
            InOrder(root.left, res)
            res.append(root.val)
            InOrder(root.right, res)
            
            return res
        
        inorder_values = []
        InOrder(root, inorder_values)
        
        for i in range(len(inorder_values)-1):
            if inorder_values[i] >= inorder_values[i+1]:
                return False
        
        return True
