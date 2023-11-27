import nltk
import networkx as nx
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

# Texto de ejemplo
texto = "dignid human fundament convivent pacif just virtud dignid human tod person derech vid libert dignid human principi gui luch derech human"

# Tokenización
tokens = word_tokenize(texto)

# Creación de bigramas
bigramas = list(ngrams(tokens, 2))

# Conteo de frecuencia de los bigramas
frecuencias = Counter(bigramas)

# Creación del grafo
grafo = nx.Graph()

# Agregar nodos y arcos al grafo
for bigrama, frecuencia in frecuencias.items():
    palabra1, palabra2 = bigrama
    grafo.add_edge(palabra1, palabra2, weight=frecuencia)

nx.write_gexf(grafo, "Redes/derechos_humanos_bigramas.gexf")