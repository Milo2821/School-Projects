#PROGRAMACION ORIENTADA A OBJETOS   

#class computadora:
   # def especificaciones(self):
    #    print("intel core i7")
     #   print("16gb ram")
    ##    print("1tb ssd")
     #   print("nvidia geforce rtx 3060")

#computadora_de_juan = computadora()
#computadora_de_maria = computadora()

#computadora_de_juan.especificaciones()

class computadora:
    def __init__(self, procesador, ram, almacenamiento, gpu):
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.gpu = gpu
    def especificaciones(self):
        print("Procesador:", self.procesador)
        print("RAM:", self.ram)
        print("Almacenamiento:", self.almacenamiento)
        print("GPU:", self.gpu)
computadora_de_juan = computadora("i7", "64", "1000Gb", "nvidia geforce rtx 3060")

print(computadora_de_juan.procesador)
print(computadora_de_juan.ram)
print(computadora_de_juan.almacenamiento)
print(computadora_de_juan.gpu)