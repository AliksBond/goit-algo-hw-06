def dijkstra_manual(graph, start):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph.nodes()):
        current = None
        current_distance = float('inf')

        for node in graph.nodes():
            if node not in visited and distances[node] < current_distance:
                current = node
                current_distance = distances[node]

        if current is None:
            break

        visited.add(current)

        for neighbor in graph[current]:
            weight = graph[current][neighbor]["weight"]
            new_dist = distances[current] + weight
            if new_dist < distances[neighbo]()_

