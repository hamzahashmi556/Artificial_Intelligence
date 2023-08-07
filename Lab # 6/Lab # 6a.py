import sys


def nearest_neighbor(graph, start):
    num_cities = len(graph)
    visited = [False] * num_cities
    visited[start] = True
    path = [start]
    total_distance = 0

    current_city = start
    for _ in range(num_cities - 1):
        nearest_city = None
        min_distance = sys.maxsize

        for city in range(num_cities):
            if not visited[city] and graph[current_city][city] < min_distance:
                nearest_city = city
                min_distance = graph[current_city][city]

        path.append(nearest_city)
        visited[nearest_city] = True
        total_distance += min_distance
        current_city = nearest_city

    path.append(start)
    total_distance += graph[current_city][start]

    return path, total_distance

if __name__ == "__main__":
    # Example usage
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    start_city = 0  # Index of the starting city

    path, total_distance = nearest_neighbor(graph, start_city)

    print("Shortest Path:", path)
    print("Total Distance:", total_distance)
