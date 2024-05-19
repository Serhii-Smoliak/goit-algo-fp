import heapq
import networkx as nx
from tabulate import tabulate

cities = [
    "Kyiv",
    "Paris",
    "Berlin",
    "Rome",
    "Madrid",
    "London",
    "Amsterdam",
    "Prague",
    "Vienna",
]

edges = [
    ("Kyiv", "Prague", 1389),
    ("Kyiv", "Vienna", 1514),
    ("Kyiv", "Berlin", 1292),
    ("Paris", "London", 344),
    ("Paris", "Berlin", 878),
    ("Paris", "Rome", 1423),
    ("Paris", "Madrid", 1054),
    ("Berlin", "Amsterdam", 577),
    ("Berlin", "Prague", 280),
    ("Berlin", "Vienna", 524),
    ("Rome", "Vienna", 766),
    ("Madrid", "Paris", 1054),
    ("London", "Amsterdam", 357),
    ("Amsterdam", "Prague", 708),
    ("Prague", "Vienna", 251),
]

positions = {
    "Kyiv": (18, 7),
    "Berlin": (9, 8.1),
    "Amsterdam": (5, 7.5),
    "London": (1, 8),
    "Paris": (3, 6),
    "Rome": (7.6, 1),
    "Madrid": (0, 0),
    "Prague": (9, 6),
    "Vienna": (10, 4),
}

G = nx.Graph()

for A, B, weight in edges:
    G.add_edge(A, B, weight=weight)


def dijkstra(start):
    distances = {city: float('infinity') for city in cities}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        (current_distance, current_city) = heapq.heappop(priority_queue)

        for neighbor, weight in G[current_city].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    data = []

    for city in cities:
        result = sorted(list(dijkstra(city).items()), key=lambda x: x[1])
        row = [f"{x[0]} ({x[1]})" for x in result]
        row.append(sum(x[1] for x in result))
        data.append(row)

    print(f"Найкоротші шлях: {min(data, key=lambda x: x[-1])[-1]}", end="\n\n")
    print(tabulate(data, headers=cities, tablefmt="pipe"))
