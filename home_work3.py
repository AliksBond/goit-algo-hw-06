import networkx as nx

G = nx.Graph()

G.add_weighted_edges_from([
    ("Центр", "Північ", 4),
    ("Центр", "Південь", 6),
    ("Центр", "Схід", 3),
    ("Центр", "Захід", 5),
    ("Північ", "Схід", 2),
    ("Південь", "Захід", 2),
    ("Схід", "Промзона", 7),
    ("Захід", "Промзона", 3)
])

paths = dict(nx.all_pairs_dijkstra_path(G))
lengths = dict(nx.all_pairs_dijkstra_path_length(G))

for start in paths:
    print("Від:", start)
    for end in paths[start]:
        print("До:", end, "Шлях:", paths[start][end], "Довжина:", lengths[start][end])
    print()
