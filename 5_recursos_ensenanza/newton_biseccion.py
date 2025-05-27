"""
Módulo NewtonBiseccion - Implementación de métodos numéricos para encontrar raíces

Contiene:
- Clase NewtonBiseccion: Implementa los métodos de Newton-Raphson y Bisección para encontrar raíces de funciones,
  con visualización gráfica y comparación de métodos.

Autor: [Tu nombre]
Fecha: [Fecha]
Versión: 1.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import approx_fprime

class NewtonBiseccion:
    """
    Clase que implementa los métodos numéricos de Newton-Raphson y Bisección para encontrar raíces de funciones.
    
    Atributos:
        f (function): Función a analizar
        
    Métodos:
        graficar_funcion: Muestra un gráfico de la función en un intervalo
        newton: Aplica el método de Newton-Raphson
        biseccion: Aplica el método de Bisección
        comparar: Compara ambos métodos en una tabla
    """
    
    def __init__(self, func=None):
        """
        Inicializa la clase con la función a analizar.
        
        Args:
            func (function, optional): Función a analizar. Si es None, usa una función por defecto.
        """
        # Función por defecto si el usuario no proporciona una
        if func is None:
            self.f = lambda x: x**3 + 5 * 10**(-5)*x**2 - 10**-14
        else:
            self.f = func

    def graficar_funcion(self, a=0, b=3, puntos=400):
        """
        Grafica la función en el intervalo [a, b].
        
        Args:
            a (float): Límite inferior del intervalo
            b (float): Límite superior del intervalo
            puntos (int): Número de puntos para la gráfica
        """
        x = np.linspace(a, b, puntos)
        y = self.f(x)
        
        plt.figure(figsize=(8,5))
        plt.plot(x, y, label='f(x)')
        plt.axhline(0, color='red', linestyle='--')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico de la función')
        plt.legend()
        plt.grid(True)
        plt.show()

    def newton(self, x0=1.5, tol=1e-6, max_iter=20, dx=1e-6):
        """
        Método de Newton-Raphson para encontrar raíces.
        
        Args:
            x0 (float): Valor inicial
            tol (float): Tolerancia para la convergencia
            max_iter (int): Número máximo de iteraciones
            dx (float): Delta para cálculo numérico de derivada
            
        Returns:
            DataFrame: Tabla con resultados de cada iteración
        """
        datos = []
        x = np.atleast_1d(x0).astype(float)  # Convertir a array 1D
        
        for i in range(max_iter):
            f_val = self.f(x[0])  # Extraer el valor escalar
            df_val = approx_fprime(x, lambda x_vec: self.f(x_vec[0]), dx)
            
            if df_val[0] == 0:
                break
                
            x_new = x - f_val / df_val
            
            datos.append({
                'Iteración': i+1,
                'x': x[0],
                'f(x)': f_val,
                "f'(x)": df_val[0],
                'Error': abs(x_new[0] - x[0])
            })
            
            if abs(x_new[0] - x[0]) < tol:
                break
                
            x = x_new
            
        return pd.DataFrame(datos)

    def biseccion(self, a=0, b=3, tol=1e-6, max_iter=50):
        """
        Método de Bisección para encontrar raíces.
        
        Args:
            a (float): Extremo izquierdo del intervalo inicial
            b (float): Extremo derecho del intervalo inicial
            tol (float): Tolerancia para la convergencia
            max_iter (int): Número máximo de iteraciones
            
        Returns:
            DataFrame: Tabla con resultados de cada iteración
            
        Raises:
            ValueError: Si no hay cambio de signo en el intervalo [a,b]
        """
        datos = []
        fa = self.f(a)
        fb = self.f(b)
        
        if fa * fb > 0:
            raise ValueError("La función no cambia de signo en el intervalo dado.")
            
        for i in range(max_iter):
            c = (a + b) / 2
            fc = self.f(c)
            
            datos.append({
                'Iteración': i+1,
                'a': a,
                'b': b,
                'c': c,
                'f(c)': fc,
                'Error': abs(b - a)/2
            })
            
            if abs(fc) < tol or abs(b - a)/2 < tol:
                break
                
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
                
        return pd.DataFrame(datos)

    def comparar(self, x0=1.5, a=0, b=3, tol=1e-6, max_iter=20):
        """
        Compara los métodos de Newton y Bisección.
        
        Args:
            x0 (float): Valor inicial para Newton
            a (float): Extremo izquierdo para Bisección
            b (float): Extremo derecho para Bisección
            tol (float): Tolerancia para ambos métodos
            max_iter (int): Número máximo de iteraciones
            
        Returns:
            DataFrame: Tabla comparativa de ambos métodos
        """
        df_newton = self.newton(x0, tol, max_iter)
        df_biseccion = self.biseccion(a, b, tol, max_iter)
        
        # Igualar número de filas para comparación
        max_len = max(len(df_newton), len(df_biseccion))
        df_newton = df_newton.reindex(range(max_len)).reset_index(drop=True)
        df_biseccion = df_biseccion.reindex(range(max_len)).reset_index(drop=True)
        
        df_comp = pd.concat([
            df_newton.add_prefix('Newton_'),
            df_biseccion.add_prefix('Biseccion_')
        ], axis=1)
        
        return df_comp


# Ejemplo de uso (se puede descomentar para pruebas)
if __name__ == "__main__":
    # Crear instancia con función por defecto
    ejemplo = NewtonBiseccion()
    
    # Mostrar gráfico
    ejemplo.graficar_funcion()
    
    # Aplicar métodos
    print("\nResultados método de Newton:")
    print(ejemplo.newton(x0=1.0))
    
    print("\nResultados método de Bisección:")
    print(ejemplo.biseccion())
    
    print("\nComparación de métodos:")
    print(ejemplo.comparar())