
import collections
from typing import List


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
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        deque_1 = [(root, None)]

        while deque_1:
            node, parent_node_val = deque_1.pop(0)
            if parent_node_val is not None:  # MUST PAY ATTENTION TO HERE!!!!! CAN NOT BE LIKE "if parent_node_val: ".
                # BECAUSE WHEN parent_node_val=0, THE CONDITION IS EQUIVALENT TO FALSE, HOWEVER, parent_node_val=0 HAS
                # VALUE
                graph[node.val].append(parent_node_val)

            if node.left:
                deque_1.append((node.left, node.val))
                graph[node.val].append(node.left.val)

            if node.right:
                deque_1.append((node.right, node.val))
                graph[node.val].append(node.right.val)

        deque_2 = [target.val]
        visited_node_vals = set()
        visited_node_vals.add(target.val)
        while k:
            length_deque_2 = len(deque_2)

            for _ in range(length_deque_2):
                node_val = deque_2.pop(0)
                visited_node_vals.add(node_val)

                if len(graph[node_val]) != 0:
                    for connected_node_val in graph[node_val]:
                        if connected_node_val not in visited_node_vals:
                            deque_2.append(connected_node_val)

            k -= 1

        return deque_2


if __name__ == '__main__' :
    # build_tree('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    root = build_tree('[0,1,3,null,2]')
    solution = Solution()
    solution.distanceK(root = root, target =TreeNode(val=1), k=2)