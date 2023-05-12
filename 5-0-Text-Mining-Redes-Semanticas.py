import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string

import numpy as np
import networkx as nx


# Cargar el archivo
with open('Textos/cambioClimatico.txt', 'r',encoding="utf-8") as f:
    texto = f.read()

# Convertir a minúsculas
texto = texto.lower()

# Eliminar signos de puntuación y números
texto = texto.translate(str.maketrans('', '', string.punctuation))
texto = texto.translate(str.maketrans('', '', string.digits))

# Eliminar palabras de parada
stop_words = set(stopwords.words('spanish'))
tokens = nltk.word_tokenize(texto)
palabras_sin_stop_words = [p for p in tokens if not p in stop_words]

# Realizar stemming
stemmer = nltk.stem.SnowballStemmer('spanish')
palabras_stemmed = [stemmer.stem(p) for p in palabras_sin_stop_words]

# Unir las palabras en un solo texto
texto_procesado = ' '.join(palabras_stemmed)

print(texto_procesado)

palabras = texto_procesado.lower().split()


# Construcción de la matriz de co-ocurrencia
vocabulario = sorted(set(palabras))
N = len(vocabulario)
co_ocurrencias = np.zeros((N, N))
ventana =4
for i, palabra_i in enumerate(vocabulario):
    for j, palabra_j in enumerate(vocabulario):
        if i != j:
            for k in range(len(palabras) - ventana + 1):
                if palabras[k] == palabra_i and palabras[k + ventana - 1] == palabra_j:
                    co_ocurrencias[i, j] += 1

# Creación de la red semántica
G = nx.Graph()
for i, palabra in enumerate(vocabulario):
    # Se agregan los nodos
    G.add_node(palabra)

    # Se agregan las aristas
    for j in range(i + 1, N):
        if co_ocurrencias[i, j] > 0:
            G.add_edge(vocabulario[i], vocabulario[j], weight=co_ocurrencias[i, j])

# Visualización de la red semántica en Gephi
nx.write_gexf(G, "Redes/red_semantica_cambio_climatico_coocurrencia_ventana_4.gexf")