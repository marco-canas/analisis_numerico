


def trazar_circunferencia_puntos_cardinales(centro, radio): 
    """_summary_

    Args:
        centro (tuple): _description_
        radio (float): _description_
    """
    import matplotlib.pyplot as plt
    import numpy as np

    h,k = 5,7
    r = 7

    theta = np.linspace(0, 2 * np.pi, 100)
    x = h + r * np.cos(theta) # 
    y = k + r * np.sin(theta)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='Circunferencia')
    # Trazado del centro
    plt.scatter(h, k, color='red', label=f'Centro ({h}, {k}) y radio {r}')
    plt.axis('equal')
    plt.legend(loc = 'upper right')
    plt.title(f'Circunferencia $(x - {h})^2 + (y - {k})^2 = ({r})^{2}$')
    plt.grid(alpha = 0.4) 
    # Trazado de los puntos de la circunferencia correspondientes a 
    # los puntos cardinales  
    norte = (h, k+r)
    sur = (h, k-r)
    este = (h+r, k)
    oeste = (h-r, k)
    abscisas_puntos_cardinales, ordenadas_puntos_cardinales = zip(norte, sur, este, oeste)
    plt.scatter(abscisas_puntos_cardinales, ordenadas_puntos_cardinales, color='purple')
    plt.show()

