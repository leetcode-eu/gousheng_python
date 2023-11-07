
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        num_rows, num_cols = len(maze), len(maze[0])
        directions                   = [[-1 ,0], [0 ,-1], [0 ,1], [1 ,0]]
        step_map                     = [[float('inf') for _ in range(num_cols)] for _ in range(num_rows)]
        step_map[start[0]][start[1]] = 0
        queue                        = [start]

        while queue:
            poped_y, poped_x = queue.pop(0)

            for dy, dx in directions:
                y        = poped_y + dy
                x        = poped_x + dx
                distance = 1

                while 0<= y <= num_rows - 1 and 0 <= x <= num_cols - 1 and maze[y][x] == 0:
                    y += dy
                    x += dx
                    distance += 1

                y -= dy
                x -= dx
                distance -= 1

                if step_map[poped_y][poped_x] + distance < step_map[y][x]:
                    step_map[y][x] = step_map[poped_y][poped_x] + distance
                    queue.append([y, x])

        shortest_distance = step_map[destination[0]][destination[1]]

        return shortest_distance if shortest_distance != float('inf') else -1