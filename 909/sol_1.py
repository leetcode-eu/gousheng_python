
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n       = len(board)
        visited = set()

        def id_to_rc(id_number):
            row_num = n - 1 - (id_number - 1) // n

            if n % 2 == 0:
                if row_num % 2 == 0:
                    col_num = n - 1 - (id_number - 1) % n
                else:
                    col_num = (id_number - 1) % n
            else:
                if row_num % 2 == 0:
                    col_num = (id_number - 1) % n
                else:
                    col_num = n - 1 - (id_number - 1) % n

            return row_num, col_num

        queue = [(1, 0)]
        visited.add(1)
        while queue:
            id_number, step = queue.pop(0)

            if id_number == n * n:
                return step

            for i in range(1, 7):
                new_id_number = id_number + i

                if new_id_number <= n * n and new_id_number not in visited:

                    visited.add(new_id_number)
                    row_num, col_num = id_to_rc(new_id_number)
                    board_value = board[row_num][col_num]

                    if board_value != -1:
                        queue.append((board_value, step + 1))
                    else:
                        queue.append((new_id_number, step + 1))

        return -1


if __name__ == "__main__":

    solution = Solution()
    board    = [[-1, -1, 19, 10, -1],
                [2,  -1, -1,  6, -1],
                [-1, 17, -1, 19, -1],
                [25, -1, 20, -1, -1],
                [-1, -1, -1, -1, 15]]

    print(solution.snakesAndLadders(board=board))
