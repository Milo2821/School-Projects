# cantidad de números a ingresar

n = int(input("Ingrese la cantidad de números a evaluar: "))

# Inicializar una lista para almacenar los números

lista = []

# Ingresar cada número

for i in range(n):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

# Evaluar cada número en la lista para determinar si es primo

for i in lista:
    if i < 2:
        print(f"El número {i} no es primo.")
    else:
        es_primo = True
        j = 2
        while j <= int(i ** 0.5):
            if i % j == 0:
                es_primo = False
            j += 1
        if es_primo:
            print(f"El número {i} es primo.")
        else:
            print(f"El número {i} no es primo.")