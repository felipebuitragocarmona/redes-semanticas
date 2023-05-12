import networkx as nx

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

# Calcular los caminos más cortos entre todos los pares de nodos
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

# Imprimir los caminos más cortos para cada par de nodos
for source, paths in shortest_paths.items():
    for target, path in paths.items():
        print(f"Caminos más cortos entre {source} y {target}: {path}")