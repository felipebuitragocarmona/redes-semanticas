import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import string

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