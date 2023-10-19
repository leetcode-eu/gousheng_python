

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # generate graph from flights
        graph = {}
        for city in range(n):
            if city != dst:  # the terminal node does not have any neighbours
                graph[city] = {}

        for flight in flights:
            depart, terminal, price = flight
            if depart != dst:
                graph[depart][terminal] = price

        # generate costs from flights. cost is the total price paid for src to certain city
        costs = {}
        for city in range(n):
            if city != src:
                if city in graph[src]:
                    costs[city] = graph[src][city]
                else:
                    costs[city] = float("inf")

        # generate parents from flights.
        parents = {}
        for city, price in graph[src].items():
            parents[city] = src

        processed = []

        def find_lowest_cost_node(costs):
            lowest_cost = float("inf")
            lowest_cost_node = None
            for node in costs:
                cost = costs[node]
                if cost < lowest_cost and node not in processed:
                    lowest_cost = cost
                    lowest_cost_node = node

            return lowest_cost_node

        def find_depth(li, n):
            if n == src:
                return

            elif n in parents:
                li.append(n)
                find_depth(li, parents[n])

            return li

        node = find_lowest_cost_node(costs)
        while node:
            if node == dst:
                continue

            cost = costs[node]
            neighbours = graph[node]  # neighbours is a dictionary
            for n in neighbours.keys():
                if n in costs:
                    new_cost_for_neighbour_n = cost + neighbours[n]
                    if costs[n] > new_cost_for_neighbour_n:
                        if len(find_depth([], n)) < k:
                            costs[n] = new_cost_for_neighbour_n
                            parents[n] = node

            processed.append(node)
            node = find_lowest_cost_node(costs)

        if costs[dst] != float("inf"):
            return costs[dst]
        else:
            return int(-1)


if __name__ == '__main__':
    print(find_depth([], n=6))
