
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return None

        deque = [root]
        num_nodes_in_layer = len(deque)
        value_list = []

        while deque:
            size_of_same_level = len(deque)
            values_of_same_level = []

            while size_of_same_level:
                node = deque.pop(0)
                children = node.children

                values_of_same_level.append(node.val)

                if children is not None:
                    for child in children:
                        deque.append(child)

                size_of_same_level -= 1

            value_list.append(values_of_same_level)

        return value_list