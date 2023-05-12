import networkx as nx
import community
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()

# Agregar los nodos
G.add_nodes_from(['persona', 'artista', 'deportista', 'cientifico', 'politico',
                  'futbol', 'natacion', 'tennis', 'boxeo', 'atletismo',
                  'pintor', 'musico', 'actor', 'escritor', 'diseñador'])

# Agregar las relaciones
G.add_edges_from([('persona', 'artista'), ('persona', 'deportista'), ('persona', 'cientifico'), ('persona', 'politico'),
                  ('deportista', 'futbol'), ('deportista', 'natacion'), ('deportista', 'tennis'), ('deportista', 'boxeo'), ('deportista', 'atletismo'),
                  ('artista', 'pintor'), ('artista', 'musico'), ('artista', 'actor'), ('artista', 'escritor'), ('artista', 'diseñador')])

# Obtener las particiones utilizando el algoritmo de Louvain
particiones = community.best_partition(G)

# Dibujar el grafo con diferentes colores para cada comunidad
pos = nx.spring_layout(G)
colors = [particiones[nodo] for nodo in G.nodes()]
nx.draw(G, pos, node_color=colors, with_labels=True, cmap=plt.cm.tab20)

# Imprimir el número de comunidades y la modularidad del grafo
num_comunidades = max(particiones.values()) + 1
modularidad = community.modularity(particiones, G)
print("El número de comunidades es:", num_comunidades)
print("La modularidad del grafo es:", modularidad)


for nodo, comunidad in particiones.items():
    print(f"{nodo}: {comunidad}")

plt.show()


