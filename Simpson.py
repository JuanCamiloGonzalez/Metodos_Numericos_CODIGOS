import numpy as np
import matplotlib.pyplot as plt

def f(x):
    #Función que se desea integrar
    return np.sqrt(5 + (x ** 3))

def simpson_method(a, b, n):
    # Implementación del método de Simpson
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    integral = h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])
    return integral

def main():
    # Entradas del usuario
    a = float(input("Ingrese el límite inferior de la integral: "))
    b = float(input("Ingrese el límite superior de la integral: "))
    n = int(input("Ingrese el número de subintervalos (debe ser par): "))

    if n % 2 != 0:
        print("El número de subintervalos debe ser par.")
        return

    # Calculo de la integral usando el método de Simpson
    integral = simpson_method(a, b, n)
    print(f"El valor aproximado de la integral es: {integral}")

    # Generacion de la gráfica de la función integrada
    x = np.linspace(a, b, 100)
    y = f(x)
    plt.plot(x, y, 'r', label='f(x) = sqrt(x)')
    plt.fill_between(x, y, where=[(a <= xi <= b) for xi in x], alpha=0.3)
    plt.title('Gráfica de la función y el área bajo la curva')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
