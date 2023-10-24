
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1:
            return l2
        if not l2:
            return l1

        dummy_head = previous_node = ListNode(0)
        carry      = 0

        while l1 or l2:

            if l1 is not None:
                a  = l1.val
                l1 = l1.next
            else:
                a = 0

            if l2 is not None:
                b  = l2.val
                l2 = l2.next
            else:
                b = 0

            sum_digit          = (a + b + carry) % 10
            carry              = (a + b + carry) // 10
            current_node       = ListNode(sum_digit)
            previous_node.next = current_node

            previous_node      = current_node

        if carry == 1:
            previous_node.next = ListNode(carry)

        return dummy_head.next