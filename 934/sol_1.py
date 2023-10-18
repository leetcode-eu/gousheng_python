
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        deque = []
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        num_rows, num_cols = len(grid), len(grid[0])
        visited_set = set()

        def find_first_island():
            for i in range(num_rows):
                for j in range(num_cols):
                    if grid[i][j] == 1:
                        return dfs(i, j)

        def dfs(i, j):
            if (i, j) not in visited_set:
                deque.append((i, j))
                visited_set.add((i, j))

                for dir_y, dir_x in directions:
                    if 0 <= dir_y + i <= num_rows - 1 and 0 <= dir_x + j <= num_cols - 1 and grid[dir_y + i][dir_x + j] == 1:
                        dfs(i + dir_y, j + dir_x)

        find_first_island()

        k = 0
        while deque:
            for _ in range(len(deque)):
                y, x = deque.pop(0)
                visited_set.add((y, x))

                for dir_y, dir_x in directions:
                    if 0 <= dir_y + y <= num_rows - 1 and 0 <= dir_x + x <= num_cols - 1:
                        if grid[dir_y + y][dir_x + x] == 1 and (dir_y + y, dir_x + x) not in visited_set:
                            return k
                        elif grid[dir_y + y][dir_x + x] == 0 and (dir_y + y, dir_x + x) not in visited_set:
                            deque.append((dir_y + y, dir_x + x))

            k += 1

        return -1


if __name__ == '__main__' :
    solution = Solution()
    solution.shortestBridge([[0, 1],[1, 0]])