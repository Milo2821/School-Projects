#Victor Emilio Ramos Gonzalez, Matricula 385499
# Función para calcular el determinante de una matriz 2x2
def determinante_2x2(matriz):

    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        return "Error: La matriz debe ser de tamaño 2x2."
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

# Función para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):

    pi = 3.1416
    return pi * (radio ** 2) * altura

# Función para calcular la derivada numérica de una función f(x)
def derivada_numerica(f, x, h=0.0001):

    return (f(x + h) - f(x)) / h

# Ejemplos de uso
if __name__ == "__main__":

    # Ejemplo 1: Determinante de una matriz 2x2
    matriz = [[4, 2], [3, 1]]
    print("Determinante de la matriz 2x2:", determinante_2x2(matriz))

    # Ejemplo 2: Volumen de un cilindro
    radio = 3
    altura = 5
    print("Volumen del cilindro:", volumen_cilindro(radio, altura))

    # Ejemplo 3: Derivada numérica de una función
    # Definir una función f(x)
    def f(x):
        return x ** 2 + 3 * x + 2

    x = 2  # Punto en el que se evalúa la derivada
    print("Derivada numérica de f(x) en x =", x, "=", derivada_numerica(f, x))