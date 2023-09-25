# -*- coding: utf-8 -*-
"""DistanciaCoseno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_T4HXrIkTKDG3gerAO5ykIjruIQ7SmrT
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

# Cargar el conjunto de datos
data = pd.read_csv('/content/drive/MyDrive/movie-DB-2000s.csv', encoding='latin-1')

# Preprocesar los datos
data.fillna('', inplace=True)

# Combinar las características
data['Contenido'] = data['Title'] + ' ' + data['Genres'] + ' ' + data['Actor1'] + ' ' + data['Actor2'] + ' ' + data['Actor3'] +  ' ' + data['Director']

# Definir la cadena de entrada
input_string = 'show me all the drama movies'

# Función para calcular la distancia del coseno entre dos vectores
def cosine_distance(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    if magnitude1 == 0 or magnitude2 == 0:
        return None  # Evitar división por cero

    return 1 - (dot_product / (magnitude1 * magnitude2))

# Tokenización de palabras para la cadena de entrada y el contenido
input_tokens = set(input_string.split())
data_tokens = [set(content.split()) for content in data['Contenido']]

# Crear un conjunto de todas las palabras clave en el conjunto de datos
all_tokens = set()
for content_tokens in data_tokens:
    all_tokens.update(content_tokens)
all_tokens.update(input_tokens)

# Calcular distancias del coseno para todas las películas en el conjunto
cosine_distances = []

for content_tokens in data_tokens:
    # Crear vectores binarios para la cadena de entrada y el contenido
    input_vector = np.array([1 if token in input_tokens else 0 for token in all_tokens])
    content_vector = np.array([1 if token in content_tokens else 0 for token in all_tokens])

    # Calcular la distancia del coseno
    cosine_distance_value = cosine_distance(input_vector, content_vector)
    cosine_distances.append(cosine_distance_value)

# Agregar distancias al DataFrame de datos
data['cosine_distance'] = cosine_distances

# Ordenar por las distancias del coseno más pequeñas y obtener las 5 mejores recomendaciones
top_rec = data.sort_values(by=['cosine_distance']).head(5)

top_rec[['Title', 'Genres', 'Director', 'Actor1', 'Actor2', 'Actor3', 'cosine_distance']]