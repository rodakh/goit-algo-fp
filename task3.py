import heapq


def dijkstra(input_graph, start):
    distances = {vertex: float('infinity') for vertex in input_graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for adjacent, weight in input_graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))

    return distances


example_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

initial_vertex = 'A'
calculated_distances = dijkstra(example_graph, initial_vertex)
print(f"Найкоротші відстані від вершини {initial_vertex} до інших вершин:")
for vertex_in_graph, distance in calculated_distances.items():
    print(f"Вершина {vertex_in_graph} має відстань {distance}")
