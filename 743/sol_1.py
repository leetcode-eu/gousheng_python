
from typing import List
import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            if u == v:
                return -1
            graph[u].append((v, w))

        if k not in graph:
            return -1

        node_step_dict = {}
        deque = [(0, k)]
        while deque:
            step, node_label = heapq.heappop(deque)
            if node_label in node_step_dict:
                continue

            node_step_dict[node_label] = step

            for target_node, distance in graph[node_label]:
                if target_node not in node_step_dict:
                    heapq.heappush(deque, (step + distance, target_node))

        return max(node_step_dict.values()) if len(node_step_dict) == n else -1