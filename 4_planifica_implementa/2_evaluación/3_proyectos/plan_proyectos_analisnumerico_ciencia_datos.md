# Prompt  

Dame un diseño de proyecto de aplicación del método numérico de Newton - Raphson a la ciencia de datos, específicamente de aplicación al Deep Learning o redes Neuronales aplicadas a las ciencias agrarias o a las ciencias económicas. Este proyecto es para asignar a equipos de dos estudiantes de la Licenciatura en Matemáticas de la Universidad de Antioquia y es para que ellos presenten esta aplicación de los métodos numéricos a través de cuadernos Jupyter editados en Visual Studio Code (VS Code). Pero agregale al diseño de este proyecto, la abligación de que los estudiantes presenten este proyecto al profesor Marco Julio Cañas en el espacio de asesoría, antes de grabar el video de exposición o sistentación de este proyecto en un video de 15 a 20 minutos.   


Perfecto, Marco Julio 🙌. Te propongo un **diseño de proyecto académico** claro, aplicable y bien estructurado, que cumple con tu enfoque de aprendizaje invertido, problematizador y con integración de métodos numéricos, ciencia de datos y Deep Learning en ciencias agrarias o económicas. Aquí lo tienes:

---

# **Diseño de Proyecto Académico**

## Aplicación del Método de Newton–Raphson en Ciencia de Datos con Deep Learning

**Licenciatura en Matemáticas — Universidad de Antioquia (Campus Caucasia)**

---

### **1. Título del proyecto**

*Aplicación del Método Numérico de Newton–Raphson a la Optimización de Modelos de Deep Learning en Ciencias Agrarias o Económicas.*

---

### **2. Contexto**

El método de Newton–Raphson es una técnica numérica clásica utilizada para resolver ecuaciones no lineales, pero también constituye la base de algunos algoritmos modernos de optimización, como la actualización de parámetros en redes neuronales.
En las ciencias agrarias y económicas, el Deep Learning se aplica a problemas como:

* Predicción de cosechas a partir de datos meteorológicos.
* Clasificación de suelos mediante imágenes satelitales.
* Predicción de precios de productos agrícolas.
* Modelado del consumo de bienes y servicios en economías locales.

Este proyecto busca integrar el **método de Newton–Raphson** como estrategia de optimización aplicada al **entrenamiento de redes neuronales** en un contexto real de las ciencias agrarias o económicas.

---

### **3. Objetivos**

#### Objetivo general

Aplicar el método de Newton–Raphson a la optimización de modelos de Deep Learning en problemas de ciencia de datos vinculados a las ciencias agrarias o económicas, usando cuadernos Jupyter en VS Code.

#### Objetivos específicos

1. Implementar el método de Newton–Raphson en Python para resolver un problema de optimización en el entrenamiento de redes neuronales.
2. Explicar cómo este método se relaciona con algoritmos modernos de optimización (ej. Gradiente Descendente y variantes como Adam).
3. Diseñar un caso práctico en ciencias agrarias o económicas que use datos reales o simulados.
4. Documentar todo el proceso en un cuaderno Jupyter con explicaciones matemáticas, código Python y visualizaciones.
5. Presentar los avances en sesión de asesoría con el profesor Marco Julio Cañas **antes de grabar el video final**.
6. Grabar y entregar un video de **15–20 minutos** exponiendo el proyecto.

---

### **4. Metodología del proyecto**

1. **Formación de equipos**: grupos de **2 estudiantes**.
2. **Selección del caso de aplicación**:

   * Ciencias agrarias: predicción de rendimiento de arroz, café, plátano o maíz.
   * Ciencias económicas: proyección de precios o demanda de productos en mercados locales.
3. **Etapas del trabajo**:

   * **Fase 1 (Investigación):** revisión teórica del método Newton–Raphson y su conexión con la optimización en redes neuronales.
   * **Fase 2 (Implementación):** programación del método Newton–Raphson en Python y adaptación a un problema de entrenamiento de red neuronal simple (ej. perceptrón multicapa).
   * **Fase 3 (Aplicación):** correr el modelo con datos (reales o simulados) en un cuaderno Jupyter.
   * **Fase 4 (Asesoría obligatoria):** presentación preliminar al profesor Marco Julio Cañas para recibir retroalimentación antes de la grabación.
   * **Fase 5 (Producto final):** grabación de un video de **15 a 20 minutos** explicando la fundamentación matemática, la implementación en Python y la aplicación práctica.

---

### **5. Entregables**

1. **Cuaderno Jupyter** en VS Code con:

   * Introducción teórica.
   * Desarrollo matemático del método.
   * Implementación en Python.
   * Caso aplicado (agrario o económico).
   * Resultados y conclusiones.
2. **Asesoría obligatoria con el profesor** antes de la grabación.
3. **Video de 15–20 minutos** (subido a YouTube en lista de reproducción definida por el profesor).

---

### **6. Criterios de evaluación**

* **Claridad matemática** (20%): explicación del método Newton–Raphson y su relación con la optimización.
* **Implementación en Python** (20%): código funcional, bien comentado y ejecutado en cuaderno Jupyter.
* **Aplicación práctica** (20%): pertinencia y justificación del caso elegido en ciencias agrarias o económicas.
* **Presentación académica** (20%): calidad del video y claridad en la exposición.
* **Cumplimiento de la asesoría previa** (20%): retroalimentación recibida aplicada al proyecto.

---

### **7. Recursos sugeridos**

* Lenguaje: **Python**.
* Librerías: `numpy`, `matplotlib`, `scikit-learn`, `torch` o `tensorflow`.
* Editor: **Visual Studio Code** con extensión Jupyter.
* Fuentes de datos:

  * IDEAM (clima en Colombia).
  * FAO (estadísticas agrícolas).
  * DANE (estadísticas económicas).
  * Datos simulados si no hay acceso a datasets reales.

---

¿Quieres que te prepare también un **ejemplo inicial de código en Jupyter Notebook** (un prototipo) donde se muestre cómo implementar Newton–Raphson para optimizar una función de pérdida en una red neuronal simple, para que los estudiantes lo usen como punto de partida?

Perfecto 🙌. Te armo un **prototipo de cuaderno Jupyter** en Python donde los estudiantes puedan ver cómo se aplica el **método de Newton–Raphson** en un problema sencillo de optimización vinculado al entrenamiento de una red neuronal muy básica.

La idea es que vean:

1. La implementación del método Newton–Raphson.
2. Cómo se aplica para encontrar mínimos de una función de pérdida (ejemplo: función cuadrática).
3. Cómo se conecta esto con la optimización en redes neuronales (entrenamiento de un perceptrón simple).

Aquí tienes el prototipo:

---

```python
# ==========================================
# Proyecto: Método de Newton-Raphson aplicado a Deep Learning
# Prototipo de implementación en Jupyter Notebook
# ==========================================

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Implementación genérica de Newton-Raphson
# -----------------------------
def newton_raphson(f, f_prime, f_double_prime, x0, tol=1e-6, max_iter=50):
    """
    Método de Newton-Raphson para encontrar raíces o puntos críticos.

    Parámetros:
    f  : función objetivo
    f_prime : primera derivada
    f_double_prime : segunda derivada
    x0 : valor inicial
    tol : tolerancia
    max_iter : número máximo de iteraciones
    """
    x = x0
    history = [x0]
    
    for i in range(max_iter):
        fx = f_prime(x)
        dfx = f_double_prime(x)
        
        if abs(dfx) < 1e-8:  # evitar divisiones por cero
            print("Derivada segunda demasiado pequeña, detener iteración.")
            break
        
        x_new = x - fx / dfx
        history.append(x_new)
        
        if abs(x_new - x) < tol:
            break
        x = x_new
    
    return x, history

# -----------------------------
# 2. Ejemplo sencillo: minimizar una función cuadrática
# -----------------------------
# f(x) = (x-3)^2 + 2
f = lambda x: (x-3)**2 + 2
f_prime = lambda x: 2*(x-3)
f_double_prime = lambda x: 2

x0 = 0.0
optimo, hist = newton_raphson(f, f_prime, f_double_prime, x0)

print("Mínimo encontrado en x =", optimo)
print("Valor mínimo f(x) =", f(optimo))

# Graficar la función y el proceso iterativo
x_vals = np.linspace(-1, 6, 200)
y_vals = f(x_vals)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label="f(x)")
plt.scatter(hist, [f(x) for x in hist], color="red", zorder=5, label="Iteraciones NR")
plt.title("Newton-Raphson aplicado a una función cuadrática")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# -----------------------------
# 3. Aplicación básica en un perceptrón simple
# -----------------------------
# Queremos minimizar la función de pérdida MSE para un perceptrón con un solo peso
X = np.array([1, 2, 3, 4], dtype=float)  # entradas
y = np.array([2, 4, 6, 8], dtype=float)  # salidas (y = 2x idealmente)

# Función de pérdida: MSE en términos del peso w
def loss(w):
    y_pred = w * X
    return np.mean((y - y_pred)**2)

# Primera derivada (gradiente respecto a w)
def loss_prime(w):
    y_pred = w * X
    return -2 * np.mean(X * (y - y_pred))

# Segunda derivada (Hessiano respecto a w)
def loss_double_prime(w):
    return 2 * np.mean(X**2)

# Aplicar Newton-Raphson al problema de entrenamiento
w0 = 0.5
w_opt, w_hist = newton_raphson(loss, loss_prime, loss_double_prime, w0)

print("\nPeso óptimo encontrado:", w_opt)
print("Error cuadrático medio con w*:", loss(w_opt))

# Graficar convergencia de la pérdida
w_vals = np.linspace(0, 3, 200)
loss_vals = [loss(w) for w in w_vals]

plt.figure(figsize=(8,5))
plt.plot(w_vals, loss_vals, label="Función de pérdida (MSE)")
plt.scatter(w_hist, [loss(w) for w in w_hist], color="red", label="Iteraciones NR")
plt.title("Optimización del peso de un perceptrón simple con Newton-Raphson")
plt.xlabel("Peso w")
plt.ylabel("MSE")
plt.legend()
plt.grid()
plt.show()
```

---

### 🔑 Explicación del prototipo

1. **Parte 1:** Se implementa Newton–Raphson de forma genérica.
2. **Parte 2:** Se aplica a una función cuadrática para ilustrar la convergencia al mínimo.
3. **Parte 3:** Se conecta con Deep Learning entrenando un **perceptrón simple con un solo peso**, usando Newton–Raphson para minimizar el **MSE**.

👉 Esto les muestra a los estudiantes cómo el **Newton–Raphson es un precursor de los métodos modernos de optimización** que usan las redes neuronales (ej. gradiente descendente, Adam).

---

¿Quieres que te prepare este prototipo también en formato de **plantilla didáctica con celdas de texto y código Markdown**, listo para que tus estudiantes lo usen directamente en un cuaderno Jupyter?
