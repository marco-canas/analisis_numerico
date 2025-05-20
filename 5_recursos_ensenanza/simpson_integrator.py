import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from scipy.integrate import quad

class SimpsonIntegrator:
    """
    Módulo para integrar funciones usando el método de Simpson con visualización.
    
    Args:
        f (callable): Función a integrar
        a (float): Límite inferior de integración
        b (float): Límite superior de integración
        n (int): Número de subintervalos (debe ser par)
        f_string (str): Representación en LaTeX de la función (opcional)
    """
    
    def __init__(self, f, a, b, n=2, f_string=None):
        self.f = f
        self.a = a
        self.b = b
        self.n = n if n % 2 == 0 else n + 1  # Asegurar que n es par
        self.f_string = f_string or "f(x)"
        self.x_fine = np.linspace(a, b, 1000)
        self.y_fine = f(self.x_fine)
        self.x_coarse = np.linspace(a, b, n + 1)
        self.y_coarse = f(self.x_coarse)
        self.midpoints = np.array([(self.x_coarse[i] + self.x_coarse[i+1])/2 for i in range(n)])
        self.y_midpoints = f(self.midpoints)
        
    def simpson_rule(self, x0, x2):
        """Calcula el área bajo la parábola para un subintervalo [x0, x2]"""
        h = x2 - x0
        x1 = (x0 + x2) / 2
        return (h / 6) * (self.f(x0) + 4 * self.f(x1) + self.f(x2))
    
    def integrate(self):
        """Calcula la integral aproximada usando el método de Simpson compuesto"""
        integral = 0.0
        for i in range(0, self.n, 2):
            integral += self.simpson_rule(self.x_coarse[i], self.x_coarse[i+2])
        return integral
    
    def plot_sequence(self):
        """Genera la secuencia gráfica del método de Simpson"""
        fig, axs = plt.subplots(4, 2, figsize=(15, 20))
        plt.subplots_adjust(hspace=0.4, wspace=0.3)
        
        # Colores para los subintervalos
        colors = plt.cm.tab10(np.linspace(0, 1, self.n//2))
        
        # --- Gráfico 1: Función y dominio ---
        ax = axs[0, 0]
        self._plot_function(ax)
        ax.axvspan(self.a, self.b, color='skyblue', alpha=0.3, label='Dominio $[a, b]$')
        ax.set_title("1. Función y dominio")
        ax.legend()
        
        # --- Gráfico 2: Puntos de partición ---
        ax = axs[0, 1]
        self._plot_function(ax)
        ax.scatter(self.x_coarse, np.zeros_like(self.x_coarse), color='red', label='Puntos de partición')
        for i in range(self.n//2):
            ax.axvspan(self.x_coarse[2*i], self.x_coarse[2*i+2], color=colors[i], alpha=0.2,
                      label=f'Subintervalo {i+1}')
        ax.set_title("2. Puntos de partición")
        ax.legend()
        
        # --- Gráfico 3: Subintervalos con puntos medios ---
        ax = axs[1, 0]
        self._plot_function(ax)
        ax.scatter(self.x_coarse, np.zeros_like(self.x_coarse), color='red', label='Puntos de partición')
        ax.scatter(self.midpoints, np.zeros_like(self.midpoints), color='magenta', label='Puntos medios')
        for i in range(self.n//2):
            ax.axvspan(self.x_coarse[2*i], self.x_coarse[2*i+2], color=colors[i], alpha=0.2)
        ax.set_title("3. Subintervalos con puntos medios")
        ax.legend()
        
        # --- Gráfico 4: Puntos medios en la función ---
        ax = axs[1, 1]
        self._plot_function(ax)
        ax.scatter(self.midpoints, self.y_midpoints, color='magenta', label='Puntos medios')
        ax.scatter(self.x_coarse, self.y_coarse, color='red', label='Puntos de partición')
        for i in range(self.n//2):
            ax.axvspan(self.x_coarse[2*i], self.x_coarse[2*i+2], color=colors[i], alpha=0.2)
        ax.set_title("4. Puntos medios en la función")
        ax.legend()
        
        # --- Gráfico 5: Tres puntos por subintervalo ---
        ax = axs[2, 0]
        self._plot_function(ax)
        for i in range(self.n//2):
            x_trio = np.array([self.x_coarse[2*i], self.midpoints[2*i], self.x_coarse[2*i+2]])
            y_trio = self.f(x_trio)
            ax.scatter(x_trio, y_trio, color=colors[i], s=100, label=f'Subintervalo {i+1}')
        ax.set_title("5. Tres puntos por subintervalo")
        ax.legend()
        
        # --- Gráfico 6: Parábolas ajustadas ---
        ax = axs[2, 1]
        self._plot_function(ax)
        for i in range(self.n//2):
            x_trio = np.array([self.x_coarse[2*i], self.midpoints[2*i], self.x_coarse[2*i+2]])
            y_trio = self.f(x_trio)
            coeffs = np.polyfit(x_trio, y_trio, 2)
            x_parab = np.linspace(self.x_coarse[2*i], self.x_coarse[2*i+2], 100)
            y_parab = np.polyval(coeffs, x_parab)
            ax.plot(x_parab, y_parab, '--', color=colors[i], label=f'Parábola {i+1}')
        ax.set_title("6. Parábolas ajustadas")
        ax.legend()
        
        # --- Gráfico 7: Áreas bajo parábolas ---
        ax = axs[3, 0]
        self._plot_function(ax)
        for i in range(self.n//2):
            x_trio = np.array([self.x_coarse[2*i], self.midpoints[2*i], self.x_coarse[2*i+2]])
            y_trio = self.f(x_trio)
            coeffs = np.polyfit(x_trio, y_trio, 2)
            x_parab = np.linspace(self.x_coarse[2*i], self.x_coarse[2*i+2], 100)
            y_parab = np.polyval(coeffs, x_parab)
            vertices = list(zip(x_parab, y_parab)) + [(self.x_coarse[2*i+2], 0), (self.x_coarse[2*i], 0)]
            ax.add_patch(Polygon(vertices, color=colors[i], alpha=0.3, label=f'Área {i+1}'))
        ax.set_title("7. Áreas bajo parábolas")
        ax.legend()
        
        # --- Gráfico 8: Resultado final ---
        ax = axs[3, 1]
        ax.axis('off')
        approx = self.integrate()
        exact, _ = quad(self.f, self.a, self.b)
        error = abs(approx - exact)
        ax.text(0.5, 0.7, f'Método de Simpson (n={self.n}):', ha='center', va='center', fontsize=12)
        ax.text(0.5, 0.5, f'{approx:.6f}', ha='center', va='center', fontsize=14, weight='bold')
        ax.text(0.5, 0.3, f'Valor exacto: {exact:.6f}', ha='center', va='center', fontsize=12)
        ax.text(0.5, 0.1, f'Error: {error:.2e}', ha='center', va='center', fontsize=12)
        ax.set_title("8. Resultado de la integración")
        
        plt.show()
        return fig, axs
    
    def _plot_function(self, ax):
        """Función auxiliar para trazar la función y el eje x"""
        ax.plot([self.a, self.b], [0, 0], 'k--', label='Eje x')
        ax.plot(self.x_fine, self.y_fine, 'b-', label=f'$f(x) = {self.f_string}$')
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.legend()


# Ejemplo de uso
if __name__ == "__main__":
    # Definir la función y parámetros