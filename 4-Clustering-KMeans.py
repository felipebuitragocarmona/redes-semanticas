import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create the graph
G = nx.Graph()

# Add the nodes
G.add_nodes_from(['ave', 'mamifero', 'reptil',
                  'aguila', 'loro', 'pinguino',
                  'perro', 'gato', 'elefante',
                  'cocodrilo', 'tortuga', 'lagarto'])

# Add the edges
G.add_edges_from([('ave', 'aguila'), ('ave', 'loro'), ('ave', 'pinguino'),
                  ('mamifero', 'perro'), ('mamifero', 'gato'), ('mamifero', 'elefante'),
                  ('reptil', 'cocodrilo'), ('reptil', 'tortuga'), ('reptil', 'lagarto')])

# Convert the graph to a NumPy array
A = nx.to_numpy_array(G)
print(A)


# Apply KMeans clustering
kmeans = KMeans(n_clusters=3).fit(A)

# Print the cluster labels for each node
for i, label in enumerate(kmeans.labels_):
    print(f"Node {list(G.nodes())[i]}: Cluster {label}")

# Define the colors for each cluster
color_map = {0: 'red', 1: 'blue', 2: 'green'}

# Create a list of colors for each node based on its cluster label
node_colors = [color_map[label] for label in kmeans.labels_]

# Draw the graph with the colors for each node
nx.draw(G, with_labels=True, node_color=node_colors)
plt.show()

