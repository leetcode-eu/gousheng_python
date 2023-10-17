
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(leet_code_input: str, should_print_tree_code_to_console=False):
    """
    Credit to LeetCode user 'bqrkhn' for this function

    Given the typical leet code input string for
    a tree, where the tree is defined level by
    level such that input[i] has nodes defined
    for a level as input[i+1:nodes_in_level],
    this builds that tree!

    Explicitly, it prints out the code for the tree structure if
    should_print_tree_code_to_console=True,
    and returns the root of the constructed tree regardless
    """
    leet_code_input = leet_code_input[1:-1].split(',')
    if len(leet_code_input) == 0:
        return
    nodes = [('root', leet_code_input[0])]
    for index, current_node in enumerate(leet_code_input[1:]):
        if current_node != 'null':
            if index & 1:
                nodes.append((nodes[index // 2][0] + '.right', current_node))
            else:
                nodes.append((nodes[index // 2][0] + '.left', current_node))
    root = TreeNode(int(nodes[0][1]))
    for node in nodes:
        execution_statement: str = node[0] + ' = TreeNode(' + node[1] + ')'
        if should_print_tree_code_to_console:
            print(execution_statement)
        exec(execution_statement)
    return root


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        deque, result  = [root], []

        while deque:
            current_row_value_list = []

            for _ in range(len(deque)):
                node = deque.pop(0)
                current_row_value_list.append(node.val)

                if node.left:
                    deque.append(node.left)

                if node.right:
                    deque.append(node.right)

            result.append(max(current_row_value_list))

        return result


if __name__ == '__main__' :

    root     = build_tree('[1,3,2,5,3,null,9]')
    solution = Solution()
    solution.largestValues(root = root)