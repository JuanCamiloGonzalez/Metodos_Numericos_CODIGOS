import numpy as np
import matplotlib.pyplot as plt

# Ingreso de datos por consola
n = int(input("Ingrese el número de puntos de datos: "))
print("Ingrese los valores de x:")
x = np.array([float(input()) for _ in range(n)])
print("Ingrese los valores de y:")
y = np.array([float(input()) for _ in range(n)])

# Calculando la pendiente y la ordenada al origen
m = ((n * np.sum(x * y)) - (np.sum(x) * np.sum(y))) / ((n * np.sum(x**2)) - (np.sum(x)**2))
b = (np.sum(y) - m * np.sum(x)) / n

print("Pendiente (m):", m)
print("Ordenada al origen (b):", b)

# Creando la línea de ajuste
x_line = np.linspace(np.min(x), np.max(x), 100)
y_line = m * x_line + b

# Graficando los datos y la línea de ajuste
plt.scatter(x, y, label='Datos')
plt.plot(x_line, y_line, color='red', label='Línea de ajuste')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ajuste lineal de curvas')
plt.legend()
plt.grid(True)
plt.show()
