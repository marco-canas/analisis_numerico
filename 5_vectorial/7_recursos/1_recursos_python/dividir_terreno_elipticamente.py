import numpy as np
from matplotlib.patches import Ellipse

import matplotlib.pyplot as plt

def distribuir_terreno_eliptico(largo, ancho, num_filas, num_columnas):
    """
    Diseña una distribución de terreno sembrado en porciones elípticas para optimizar el área sembrada y el riego.

    Args:
        largo (float): Largo del terreno en metros.
        ancho (float): Ancho del terreno en metros.
        num_filas (int): Número de filas de elipses.
        num_columnas (int): Número de columnas de elipses.

    Returns:
        None: Genera un gráfico con la distribución de las porciones elípticas.
    """
    # Dimensiones de cada elipse
    a = largo / (2 * num_columnas)  # Semieje mayor
    b = ancho / (2 * num_filas)     # Semieje menor

    # Coordenadas del centro de cada elipse
    x_centros = np.linspace(a, largo - a, num_columnas)
    y_centros = np.linspace(b, ancho - b, num_filas)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, largo)
    ax.set_ylim(0, ancho)
    ax.set_aspect('equal')
    ax.set_title('Distribución de Terreno en Porciones Elípticas')
    ax.set_xlabel('Largo del terreno (m)')
    ax.set_ylabel('Ancho del terreno (m)')

    # Dibujar las elipses
    for x in x_centros:
        for y in y_centros:
            elipse = Ellipse((x, y), width=2*a, height=2*b, edgecolor='blue', facecolor='lightblue', alpha=0.5)
            ax.add_patch(elipse)

    plt.grid(True)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Dimensiones típicas del terreno en el Bajo Cauca Antioqueño
    largo_terreno = 100  # metros
    ancho_terreno = 50   # metros
    filas = 4
    columnas = 6

    distribuir_terreno_eliptico(largo_terreno, ancho_terreno, filas, columnas)