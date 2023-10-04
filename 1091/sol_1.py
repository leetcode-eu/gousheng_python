
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def check_cell(new_cell, visited_cells):
            if 0 <= new_cell[0] < num_rows and 0 <= new_cell[1] < num_cols:
                if grid[new_cell[0]][new_cell[1]] == 0 and new_cell not in visited_cells:
                    return True
            return False

        def check_finish(new_cell):
            if new_cell[0] == num_rows - 1 and new_cell[1] == num_cols - 1:
                return True
            return False

        num_rows, num_cols = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        if num_rows == 1 and grid[0][0] == 0:
            return 1

        direction_deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        deque            = [(0, 0)]
        visited_cells    = set()
        num_steps        = 1

        visited_cells.add((0, 0))

        while deque:
            num_cells_with_same_num_step = len(deque)
            for _ in range(num_cells_with_same_num_step):
                cell = deque.pop(0)
                for direction_delta in direction_deltas:
                    new_cell = (cell[0] + direction_delta[0], cell[1] + direction_delta[1])

                    if check_cell(new_cell, visited_cells):
                        if check_finish(new_cell):
                            return num_steps + 1

                        deque.append(new_cell)

            num_steps += 1
        return -1