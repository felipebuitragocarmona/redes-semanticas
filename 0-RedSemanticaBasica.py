import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()

# Agregar los nodos
G.add_nodes_from(['ave', 'mamifero', 'reptil',
                  'aguila', 'loro', 'pinguino',
                  'perro', 'gato', 'elefante',
                  'cocodrilo', 'tortuga', 'lagarto'])

# Agregar las relaciones
G.add_edges_from([('ave', 'aguila'), ('ave', 'loro'), ('ave', 'pinguino'),
                  ('mamifero', 'perro'), ('mamifero', 'gato'), ('mamifero', 'elefante'),
                  ('reptil', 'cocodrilo'), ('reptil', 'tortuga'), ('reptil', 'lagarto')])

# Dibujar el grafo
nx.draw(G, with_labels=True)
plt.show()

nx.write_gexf(G, 'Redes/animales.gexf')