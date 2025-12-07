import networkx as nx
import matplotlib.pyplot as plt

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

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

for node, degree in G.degree():
    print(node, degree)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=12)
plt.show()
