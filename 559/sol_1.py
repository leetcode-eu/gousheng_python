
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        max_depth = 0
        deque = [root]
        next_layer_num_children = 1

        while deque:
            num_children = next_layer_num_children
            next_layer_num_children = 0

            for _ in range(num_children):
                node = deque.pop(0)
                children = node.children

                if children is not None:
                    next_layer_num_children += len(children)
                    for child in children:
                        deque.append(child)

            max_depth += 1

        return max_depth