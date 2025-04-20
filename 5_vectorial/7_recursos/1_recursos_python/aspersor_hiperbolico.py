import numpy as np

import plotly.graph_objects as go

def diseno_aspersores_hiperbolico(a, b, rango_x=(-30, 30), puntos=100):
    """
    Diseña un sistema de aspersores con patrón hiperbólico para riego.

    Parámetros:
    - a (int): Semieje mayor de la hipérbola (distancia entre los focos/2).
    - b (int): Semieje menor de la hipérbola (radio efectivo de riego).
    - rango_x (tuple): Rango de valores para el eje x.
    - puntos (int): Número de puntos para graficar la hipérbola.

    Retorna:
    - fig (plotly.graph_objects.Figure): Gráfico interactivo del diseño.
    """
    x = np.linspace(rango_x[0], rango_x[1], puntos)
    y = b * np.sqrt((x**2 / a**2) - 1)
    
    # Crear figura interactiva
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Hipérbola Superior'))
    fig.add_trace(go.Scatter(x=x, y=-y, mode='lines', name='Hipérbola Inferior'))
    fig.add_trace(go.Scatter(x=[-a, a], y=[0, 0], mode='markers', name='Aspersores'))
    
    fig.update_layout(
        title='Diseño de Sistema de Riego Hiperbólico',
        xaxis_title='Distancia (m)',
        yaxis_title='Cobertura (m)',
        showlegend=True
    )
    
    return fig

# Ejemplo de uso
if __name__ == "__main__":
    a = 15  # Semieje mayor
    b = 10  # Semieje menor
    figura = diseno_aspersores_hiperbolico(a, b)
    figura.show()