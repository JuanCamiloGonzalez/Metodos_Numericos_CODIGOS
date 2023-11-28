#def funcion(x):
    # Define aquí la función que deseas resolver
    # Ejemplo: return x**2 - 4

def metodo_biseccion(a, b, tol):
    if funcion(a) * funcion(b) >= 0:
        print("La función no cumple con el criterio de bisección.")
        return None

    iteraciones = 0
    while abs(b - a) > tol:
        c = (a + b) / 2
        if funcion(c) == 0:
            break
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c
        iteraciones += 1

    resultado = (a + b) / 2


# Solicitar la función al usuario
funcion_str = input("Ingresa la función a resolver (en términos de x): ")
funcion = lambda x: eval(funcion_str)

# Solicitar los límites del intervalo
a = float(input("Ingresa el límite inferior del intervalo: "))
b = float(input("Ingresa el límite superior del intervalo: "))

# Solicitar la tolerancia
tolerancia = float(input("Ingresa la tolerancia deseada: "))

# Ejecutar el método de bisección
metodo_biseccion(a, b, tolerancia)
print(f"La raíz aproximada es: {resultado}")
print(f"Se realizaron {iteraciones} iteraciones.")
