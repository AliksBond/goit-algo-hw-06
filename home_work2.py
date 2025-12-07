from collections import deque
import networkx as nx

G = nx.Graph()

nodes = ["Центр", "Північ", "Південь", "Схід", "Захід", "Промзона"]
G.add_nodes_from(nodes)

edges = [
    ("Центр", "Північ"),
    ("Центр", "Південь"),
    ("Центр", "Схід"),
    ("Центр", "Захід"),
    ("Північ", "Схід"),
    ("Південь", "Захід"),
    ("Схід", "Промзона"),
    ("Захід", "Промзона")
]
G.add_edges_from(edges)

def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path.append(start)
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path.copy(), visited.copy())
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

start = "Північ"
goal = "Промзона"

print("DFS:", dfs_path(G, start, goal))
print("BFS:", bfs_path(G, start, goal))
