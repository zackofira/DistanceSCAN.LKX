import networkx as nx
import matplotlib.pyplot as plt
import random

# Define the cluster results
cluster_result = {
    0: [33],
    1: [32],
    2: [31],
    3: [28, 29],
    4: [4, 6],
    5: [27],
    6: [23],
    7: [22],
    8: [21],
    9: [18],
    10: [26],
    11: [3, 8, 1],
    12: [14, 15],
    13: [36, 35],
    14: [13, 12],
    15: [2]
}

# Jaccard graph edges with weights
edges_with_weights = [
    (0, 1, 0.614286),
    (0, 2, 0.614286),
    (0, 11, 0.4),
    (1, 3, 0.357143),
    (1, 5, 0.614286),
    (1, 7, 0.64),
    (1, 8, 0.614286),
    (1, 11, 0.64),
    (2, 3, 0.357143),
    (2, 5, 0.614286),
    (2, 6, 0.4),
    (2, 9, 0.46),
    (2, 11, 0.64),
    (3, 4, 0.6625),
    (3, 5, 0.4),
    (3, 8, 0.4),
    (3, 9, 0.46),
    (3, 11, 0.64),
    (4, 6, 0.28),
    (4, 9, 0.64),
    (4, 10, 0.325),
    (4, 37, 0.64),
    (5, 8, 0.46),
    (5, 9, 0.55),
    (5, 24, 0.55),
    (6, 9, 0.1),
    (6, 10, 0.55),
    (6, 11, 0.4),
    (8, 9, 0.1),
    (8, 10, 0.55),
    (8, 11, 0.4),
    (9, 11, 0.8),
    (10, 37, 0.1),
    (12, 13, 0.357143),
    (12, 16, 0.55),
    (12, 17, 0.614286),
    (12, 18, 0.485714),
    (12, 19, 0.614286),
    (12, 20, 0.742857),
    (13, 15, 0.25),
    (13, 16, 0.325),
    (13, 17, 0.7),
    (13, 18, 0.742857),
    (14, 15, 0.228571),
    (14, 16, 0.742857),
    (14, 17, 0.4),
    (14, 19, 0.614286),
    (14, 20, 0.742857),
    (14, 40, 0.7),
    (15, 16, 0.46),
    (15, 17, 0.28),
    (15, 18, 0.614286),
    (15, 19, 0.742857),
    (15, 40, 0.64),
    (16, 18, 0.55),
    (17, 19, 0.55),
    (17, 40, 0.1),
    (18, 19, 0.325),
    (18, 20, 0.1),
    (18, 37, 0.55),
    (19, 20, 0.4),
    (19, 31, 0.64),
    (20, 37, 0.1),
    (21, 22, 0.25),
    (21, 23, 0.1),
    (21, 24, 0.46),
    (21, 25, 0.7),
    (21, 37, 0.7),
    (22, 23, 0.28),
    (22, 24, 0.325),
    (22, 25, 0.325),
    (22, 39, 0.55),
    (23, 24, 0.1),
    (23, 25, 0.55),
    (23, 37, 0.55),
    (24, 25, 0.1),
    (25, 39, 0.8),
    (26, 27, 0.1),
    (26, 28, 0.4),
    (26, 29, 0.4),
    (26, 30, 0.7),
    (26, 37, 0.55),
    (26, 38, 0.7),
    (27, 28, 0.1),
    (27, 29, 0.46),
    (27, 30, 0.55),
    (27, 38, 0.55),
    (28, 29, 0.1),
    (28, 30, 0.1),
    (29, 30, 0.1),
    (29, 37, 0.4),
    (31, 32, 0.28),
    (31, 33, 0.46),
    (31, 36, 0.64),
    (32, 33, 0.125),
    (32, 34, 0.1),
    (32, 35, 0.325),
    (32, 36, 0.7),
    (33, 34, 0.2),
    (33, 35, 0.1),
    (33, 36, 0.64),
    (34, 35, 0.35),
    (34, 36, 0.55),
    (35, 36, 0.4),
    (36, 37, 0.35),
    (36, 38, 0.1),
    (37, 38, 0.8),
]

# Create a graph
G = nx.Graph()

# Add nodes based on clusters
for cluster_id, elements in cluster_result.items():
    G.add_nodes_from(elements)

# Add edges with weights
for edge in edges_with_weights:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Assign random colors to each cluster
node_color_map = {}
for cluster_id, elements in cluster_result.items():
    color = [random.random(), random.random(), random.random()]  # RGB colors
    for node in elements:
        node_color_map[node] = color

# Assign a default color to any node not in the cluster results
default_color = [0.5, 0.5, 0.5]  # Grey color for default
for node in G.nodes():
    if node not in node_color_map:
        node_color_map[node] = default_color

# Generate the colors list for the nodes
colors = [node_color_map[node] for node in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # Use spring layout for positioning nodes
plt.figure(figsize=(15, 15))

# Draw nodes with assigned colors
nx.draw_networkx_nodes(G, pos, node_size=500, node_color=colors)

# Draw edges with varying thickness based on weights
edges = G.edges(data=True)
nx.draw_networkx_edges(G, pos, edgelist=edges, width=[d['weight'] * 5 for (u, v, d) in edges], edge_color='gray')

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

plt.title('Cluster Visualization with Jaccard Graph Edges')
plt.show()
