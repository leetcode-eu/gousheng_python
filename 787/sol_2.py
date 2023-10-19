
from typing import List


def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    dp_map         = [ [float('inf') ] *n for _ in range( k +2)]
    dp_map[0][src] = 0

    for i in range(1, k+ 2):
        for origin, arrival, price in flights:
            if dp_map[i - 1][origin] + price < dp_map[i][arrival]:
                dp_map[i][arrival] = dp_map[i - 1][origin] + price

    chepest_price = min([dp_map[j][dst] for j in range(k + 2)])

    return chepest_price if chepest_price != float('inf') else -1