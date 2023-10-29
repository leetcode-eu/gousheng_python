
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        directions = [(-2 ,1), (-1 ,2), (1 ,2), (2 ,1), (2 ,-1), (1 ,-2), (-1 ,-2), (-2 ,-1)]
        target     = [x ,y]
        deque      = [(0 ,0)]
        visited    = set()
        visited.add((0 ,0))
        step       = 0

        while deque:

            for _ in range(len(deque)):

                # 1.
                x_val, y_val = deque.pop(0)
                if [x_val, y_val] == target:
                    return step

                # 2.
                for x_dir, y_dir in directions:
                    if (x_val +x_dir, y_val +y_dir) not in visited:
                        deque.append((x_val + x_dir, y_val + y_dir))
                        visited.add((x_val + x_dir, y_val + y_dir))

            # 3.
            step += 1

        return -1