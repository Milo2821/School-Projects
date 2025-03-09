# Solicitar al usuario la cantidad de números a ingresar

n = int(input("Ingrese la cantidad de números a evaluar: "))

# Inicializar una lista para almacenar los números

lista = []

# Ingresar cada número

for i in range(n):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

# Inicializar variables para la suma de negativos y el producto de positivos

suma_negativos = 0
producto_positivos = 1

# Evaluar cada número en la lista

for i in lista:
    if i < 0:
        suma_negativos += i
    elif i > 0:
        producto_positivos *= i

# Mostrar los resultados en pantalla

print(f"La suma de los números negativos es: {suma_negativos}")

print(f"El producto de los números positivos es: {producto_positivos}")