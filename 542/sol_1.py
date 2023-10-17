
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions         = [(-1 ,0), (0 ,-1), (1 ,0), (0 ,1)]
        deque              = []
        visited_set        = set()  # prevent the infinite loop from happening due to the existence of circle
        # in the graph
        num_rows, num_cols = len(mat), len(mat[0])
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf')
                else:
                    deque.append((i, j))

        while deque:
            y, x = deque.pop(0)
            visited_set.add((y ,x))

            for dir_y, dir_x in directions:
                new_y, new_x = y+ dir_y, x + dir_x

                if 0 <= new_y <= num_rows - 1 and 0 <= new_x <= num_cols - 1:

                    if (new_y, new_x) not in visited_set:
                        deque.append((new_y, new_x))

                    if mat[y][x] + 1 < mat[new_y][new_x]:
                        mat[new_y][new_x] = mat[y][x] + 1

        return mat