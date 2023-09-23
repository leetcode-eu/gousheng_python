
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # No node
        if not head:
            return None
        # Single node
        if not head.next:
            return TreeNode(head.val)

        def find_middle(head_of_current_linked_list):
            prev_slow = slow = fast = head_of_current_linked_list
            while fast and fast.next:
                prev_slow = slow
                slow      = slow.next
                fast      = fast.next.next

            return prev_slow, slow

        prev_middle, middle = find_middle(head)
        prev_middle.next    = None

        tree_node       = TreeNode(middle.val)
        tree_node.left  = self.sortedListToBST(head)
        tree_node.right = self.sortedListToBST(middle.next)

        return tree_node