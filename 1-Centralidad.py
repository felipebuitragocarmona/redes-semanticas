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


print("--------  degree_centrality ----------")
# Calcular la centralidad de grado
grado = nx.degree_centrality(G)

# Imprimir la centralidad de grado de cada nodo
for nodo, centralidad in grado.items():
    print(f"{nodo}: {centralidad}")

print("--------- betweenness_centrality  ----------")
# Calcular la centralidad de intermediación
intermediacion = nx.betweenness_centrality(G)
# Imprimir la centralidad de intermediación de cada nodo
for nodo, centralidad in intermediacion.items():
    print(f"{nodo}: {centralidad}")

plt.show()