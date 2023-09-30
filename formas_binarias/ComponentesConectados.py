import numpy as np
import cv2

# Función para encontrar el representante (padre) de un conjunto
def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, parents[x])
    return parents[x]

# Función para unir dos conjuntos
def union(parents, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)
    if root_x != root_y:
        parents[root_x] = root_y

def CCL(binary_image):
    # Obtener dimensiones de la imagen
    height, width = binary_image.shape

    # Inicializar una matriz para el etiquetado de componentes conectados
    labels = np.zeros((height, width), dtype=int)

    # Inicializar un conjunto de padres para el etiquetado
    parents = list(range(height * width))  # Suponemos un máximo de height * width componentes

    # Etiquetar componentes conectados
    current_label = 1

    for y in range(height):
        for x in range(width):
            if binary_image[y, x] == 255:
                neighbors = []
                if y > 0 and binary_image[y - 1, x] == 255:
                    neighbors.append(labels[y - 1, x])
                if x > 0 and binary_image[y, x - 1] == 255:
                    neighbors.append(labels[y, x - 1])

                if not neighbors:
                    labels[y, x] = current_label
                    current_label += 1
                else:
                    min_neighbor = min(neighbors)
                    labels[y, x] = min_neighbor
                    for neighbor in neighbors:
                        if neighbor != min_neighbor:
                            union(parents, min_neighbor, neighbor)

    # Recorrer la matriz de etiquetas para actualizar los componentes conectados
    for y in range(height):
        for x in range(width):
            if binary_image[y, x] == 255:
                labels[y, x] = find(parents, labels[y, x])

    # Crear un mapeo de colores para los componentes
    color_map = {}
    colored_image = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            if binary_image[y, x] == 255:
                label = labels[y, x]
                if label not in color_map:
                    color_map[label] = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
                colored_image[y, x] = color_map[label]
    
    return colored_image
        
