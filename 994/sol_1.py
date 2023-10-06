
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        num_rows, num_cols = len(grid), len(grid[0])
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        fresh_set, rotting_deque = set(), list()
        step = 0

        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == 1:
                    fresh_set.add((i, j))
                if grid[i][j] == 2:
                    rotting_deque.append((i, j, step))

        while rotting_deque:
            y, x, step = rotting_deque.pop(0)
            for delta_y, delta_x in directions:
                if 0 <= y + delta_y <= num_rows - 1 and 0 <= x + delta_x <= num_cols - 1 and (
                y + delta_y, x + delta_x) in fresh_set:
                    fresh_set.remove((y + delta_y, x + delta_x))
                    rotting_deque.append((y + delta_y, x + delta_x, step + 1))

        return step if not fresh_set else -1