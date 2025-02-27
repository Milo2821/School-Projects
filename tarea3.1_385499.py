#Primera parte; el programa que divide

a = int(input("Ingrese el dividendo: "))

b = int(input("Ingrese el divisor: "))

#Revisar si el divisor es cero

if b==0:
    print("No se puede dividir por cero")

    b= int(input("vuelva a ingresar el divisor: "))

    c = a / b

    print("El resultado de la división es: ", c)
else: 
    c = a / b

    print("El resultado de la división es:", c)



#Segunda parte; el programa que compara números

#Pedir al usuario que ingrese dos números

c = float(input("ingrese un numero cualquiera: "))

d = float(input("ingresa otro numero cualquiera:"))

#Comparar los números

if c > d:
    print(f"El número {c} es mayor que el número {d}")
else:
    print(f"El número {c} es menor que el número {d}")

#En caso de que los números sean iguales

if c == d:
    print(f"El número {c} es igual al número {d}")




#Tercera parte; el programa que calcula la diferencia de años

#Pedir al usuario que ingrese una fecha

actual = int(input("Ingrese el año actual: "))

cualquiera = int(input("Ingrese un año cualquiera: "))

#Calcular la diferencia de años

if actual > cualquiera:
    diferencia = actual - cualquiera

    print(f"El año {cualquiera} fue hace {diferencia} años")
else:
    actual < cualquiera
    diferencia = cualquiera - actual

    print(f"El año {cualquiera} será en {diferencia} años")

if actual == cualquiera:

    print(f"son el mismo año")




#Cuarta parte; convertidor de millas a kilometros y viceversa

#Pedir al usuario que ingrese una cantidad de millas

opcion1 = print("para convertir de millas a kilometros, ingrese 1")

opcion2 = print("para convertir de kilometros a millas, ingrese 2")

opcion = int(input("ingrese una opcion para continuar: "))

#seleccionar opcion y dar un resultado en base a la opcion seleccionada

if opcion == 1:

    millas = float(input("ingresa la cantidad de millas: "))

    kilometros = millas * 1.60934

    print(f"{millas} millas son {kilometros} kilometros")

else:
    opcion == 2

    kilometros = float(input("ingresa la cantidad de kilometros: "))

    millas = kilometros / 1.60934
    
    print(f"{kilometros} kilometros son {millas} millas")

