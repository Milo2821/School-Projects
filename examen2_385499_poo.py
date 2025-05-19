# Superclase Computadora
class Computadora:
    def __init__(self, procesador, ram, ssd, tarjeta_grafica, placa_madre):
        self.procesador = procesador
        self.ram = ram
        self.ssd = ssd
        self.tarjeta_grafica = tarjeta_grafica
        self.placa_madre = placa_madre

    def mostrar_info(self):
        
        #Muestra la información completa de la computadora.
        
        print("Información de la Computadora:")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Memoria SSD: {self.ssd} GB")
        print(f"Tarjeta Gráfica: {self.tarjeta_grafica}")
        print(f"Placa Madre: {self.placa_madre}")

    def actualizar_ram(self, nueva_ram):
        
        #Actualiza la cantidad de memoria RAM.
        
        self.ram = nueva_ram
        print(f"La RAM ha sido actualizada a {self.ram} GB.")

    def actualizar_ssd(self, nuevo_ssd):
        
        #Actualiza la capacidad de la memoria SSD.
        
        self.ssd = nuevo_ssd
        print(f"La memoria SSD ha sido actualizada a {self.ssd} GB.")

    def encender(self):
        
        #Simula el encendido de la computadora.
        
        print("La computadora se está encendiendo...")

# Subclase Laptop
class Laptop(Computadora):
    def __init__(self, procesador, ram, ssd, tarjeta_grafica, placa_madre, bateria):
        super().__init__(procesador, ram, ssd, tarjeta_grafica, placa_madre)
        self.bateria = bateria  # Capacidad de la batería en mAh

    def mostrar_info(self):
        
       #Sobrescribe el método mostrar_info para incluir la batería.
        
        super().mostrar_info()
        print(f"Batería: {self.bateria} mAh")

    def modo_ahorro(self):
        
        #Activa el modo de ahorro de energía.
        
        print("Modo de ahorro de energía activado.")

# Subclase PCGamer
class PCGamer(Computadora):
    def __init__(self, procesador, ram, ssd, tarjeta_grafica, placa_madre, sistema_refrigeracion):
        super().__init__(procesador, ram, ssd, tarjeta_grafica, placa_madre)
        self.sistema_refrigeracion = sistema_refrigeracion  # Tipo de sistema de refrigeración

    def mostrar_info(self):
        
        #Sobrescribe el método mostrar_info para incluir el sistema de refrigeración.
        
        super().mostrar_info()
        print(f"Sistema de Refrigeración: {self.sistema_refrigeracion}")

    def overclock(self):
        
        #Simula el overclocking del procesador.
        
        print("Overclocking del procesador activado.")

# Crear objetos de las clases
if __name__ == "__main__":

    # Objeto de la clase Computadora
    computadora = Computadora("Intel i5", 8, 256, "Integrada", "ASUS Prime")
    computadora.mostrar_info()
    computadora.actualizar_ram(16)

    print("\n")

    # Objeto de la clase Laptop
    laptop = Laptop("Intel i7", 16, 512, "NVIDIA GTX 1650", "MSI Modern", 6000)
    laptop.mostrar_info()
    laptop.modo_ahorro()

    print("\n")

    # Objeto de la clase PCGamer
    pc_gamer = PCGamer("AMD Ryzen 9", 32, 1024, "NVIDIA RTX 3080", "Gigabyte Aorus", "Refrigeración Líquida")
    pc_gamer.mostrar_info()
    pc_gamer.overclock()
    pc_gamer.encender()