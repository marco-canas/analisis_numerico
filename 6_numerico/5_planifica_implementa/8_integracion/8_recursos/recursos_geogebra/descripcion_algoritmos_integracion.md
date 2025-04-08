### **Algoritmo en GeoGebra para la Regla de Simpson (n=2) en \( f(x) = e^{x^2} \) sobre [0,1]**

Aquí tienes una **secuencia detallada** para implementar paso a paso el método de integración numérica de Simpson en GeoGebra, comparando con el resultado exacto de SciPy (Python):

---

#### **1. Definir la función y dominio**  
- **Entrada en GeoGebra**:  
  ```geogebra
  f(x) = e^(x^2)
  a = 0
  b = 1
  n = 2
  ```

---

#### **2. Crear partición regular (3 puntos)**  
- **Fórmula**: \( h = \frac{b - a}{n} = 0.5 \).  
- **Puntos de la partición**:  
  ```geogebra
  x0 = a
  x1 = a + h
  x2 = b
  ```
  *Resultado*: \( x_0 = 0 \), \( x_1 = 0.5 \), \( x_2 = 1 \).

---

#### **3. Puntos medios y valores de \( f \)**  
- **Puntos medios** (para parábolas):  
  ```geogebra
  m1 = (x0 + x1) / 2
  m2 = (x1 + x2) / 2
  ```
- **Evaluar \( f \) en los puntos clave**:  
  ```geogebra
  f0 = f(x0)
  f1 = f(x1)
  f2 = f(x2)
  fm1 = f(m1)
  fm2 = f(m2)
  ```

---

#### **4. Trazar puntos y parábolas**  
- **Puntos del gráfico**:  
  ```geogebra
  P0 = (x0, f0)
  P1 = (x1, f1)
  P2 = (x2, f2)
  Pm1 = (m1, fm1)
  Pm2 = (m2, fm2)
  ```
- **Parábolas** (usando comandos de ajuste cuadrático):  
  ```geogebra
  Parabola1 = AjustePolinómico({P0, Pm1, P1}, 2)
  Parabola2 = AjustePolinómico({P1, Pm2, P2}, 2)
  ```

---

#### **5. Calcular áreas bajo parábolas (Regla de Simpson)**  
- **Fórmula para $ n=2 $** (1 parábola por subintervalo):  
  $$
  \text{Área} = \frac{h}{3} \left( f(x_0) + 4f(x_1) + f(x_2) \right)
  $$
- **En GeoGebra**:  
  ```geogebra
  h = (b - a) / n
  AreaSimpson = (h / 3) * (f0 + 4 * f1 + f2)
  ```

---

#### **6. Comparar con valor exacto (SciPy-Python)**  
- **Valor "exacto"** (calculado previamente con SciPy):  
  ```python
  from scipy.integrate import quad
  result, _ = quad(lambda x: np.exp(x**2), 0, 1)
  ```
  *Resultado*: $ \approx 1.46265 $.  
- **En GeoGebra**:  
  ```geogebra
  ValorExacto = 1.46265
  Error = abs(ValorExacto - AreaSimpson)
  ```

---

#### **7. Visualización final**  
- **Gráficos**:  
  - Mostrar \( f(x) \) en color rojo.  
  - Parábolas en azul (áreas aproximadas).  
  - Puntos \( P0, P1, P2, Pm1, Pm2 \) resaltados.  
- **Leyenda**:  
  ```geogebra
  Texto("Área Simpson: " + AreaSimpson)
  Texto("Error: " + Error)
  ```

---

### **Resultado Esperado**  
- **Área aproximada (GeoGebra)**: \( \approx 1.47573 \).  
- **Error**: $\approx 0.01308$.  

---

### **Explicación Didáctica**  
- **Para estudiantes**:  
  > *"La regla de Simpson usa parábolas en lugar de rectas (como el trapecio). Con solo 2 intervalos, ¡aproximamos la integral de \( e^{x^2} \) con un error del 0.9%!"*  

- **Extensión**: Modificar \( n \) para ver cómo disminuye el error.  

¿Necesitas el archivo `.ggb` exportado o ajustar algún paso?