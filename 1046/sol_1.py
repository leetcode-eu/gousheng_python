
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()

            if x != y:
                stones.append(y -x)

            stones.sort()

        return stones[0] if len(stones) == 1 else 0