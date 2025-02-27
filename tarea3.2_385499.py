# Programa que calcule la transformación de temperaturas de grados centígrados a grados Fahrenheit

while True:
    try:
        # Pedir al usuario que ingrese la temperatura en grados centígrados
        centigrados = float(input("Ingrese la temperatura en grados centígrados: "))
        
        Fahrenheit = (centigrados * 1.8) + 32
        print(f"{centigrados} grados centígrados son {Fahrenheit} grados Fahrenheit")
        
        # Preguntar al usuario si desea salir
        print("Presione S para salir o cualquier otra tecla para continuar")
        if input().lower() == "s":
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Solicitar al usuario un número entero en el intervalo de 1 a 100
while True:
    try:
        cantidad = int(input("Ingrese un número entero del 1 al 100: "))
        if 1 <= cantidad <= 100:
            break
        else:
            print("Por favor, ingrese un número dentro del intervalo de 1 a 100.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Mostrar el listado del número seguido de todos los menores a él, separados de 3 en 3, pero solo positivos
print("Listado de números:")
for i in range(cantidad, 0, -3):
    print(i, end=", " if i > 3 else "\n")

print("gracias por usar este programa")