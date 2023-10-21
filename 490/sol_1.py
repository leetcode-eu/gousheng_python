
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        num_rows, num_cols = len(maze), len(maze[0])
        directions         = [[-1,0], [1,0], [0,-1], [0,1] ]
        deque              = [start]
        visited            = set()
        visited.add((start[0], start[1]))

        while deque:
            poped_y, poped_x = deque.pop(0)

            if [poped_y, poped_x] == destination:
                return True

            for dy, dx in directions:
                y = poped_y + dy
                x = poped_x + dx

                while 0<= y <= num_rows-1 and 0<= x <= num_cols-1 and maze[y][x] == 0:
                    y += dy
                    x += dx

                y -= dy
                x -= dx

                if (y, x) not in visited:
                    visited.add((y, x))
                    deque.append([y, x])

        return False


if __name__ == "__main__":
    solution = Solution()
    solution.hasPath(maze=[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start=[0,4], destination=[4,4])