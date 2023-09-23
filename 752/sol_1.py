
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        start = '0000'
        if start in deadends:
            return -1

        if start in target:
            return 0

        deque = [(start, 0)]
        tried_sets = []

        while deque:
            number, turns = deque.pop(0)
            current_turns = turns + 1
            for i in range(4):
                for change in [-1, 1]:
                    new_digit = (int(number[i]) + change) % 10
                    new_number = number[:i] + str(new_digit) + number[i + 1:]

                    if new_number == target:
                        return current_turns

                    elif new_number not in deadends and new_number not in tried_sets:
                        tried_sets.append(new_number)
                        deque.append((new_number, current_turns))

        return -1