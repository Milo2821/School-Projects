### Clase ejemplo personajes ###

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza

    def atributos(self):
        print(self.__nombre, ": ", sep="")
        print(".__fuerza:", self.__fuerza)
        print(".__inteligencia:", self.__inteligencia)
        print(".__defensa:", self.__defensa)
        print(".__vida:", self.__vida)
        print("")

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "Ha muerto")

    def daño(self, enemigo):
        if self.__fuerza < enemigo.__defensa:
            return 0
        else:
            return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        if enemigo.__vida < 0:
            enemigo.__vida = 0
        print(self.__nombre, "Ha realizado", daño, "puntos de daño a ", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("El enemigo está vivo y tiene ", enemigo.__vida, "de vida")
        else:
            enemigo.__morir()

link = Personaje("Link", 70, 10, 90, 45)
miranjo = Personaje("Miranjo", 88, 90,30 , 80)

link.atributos()
miranjo.atributos()

link.subir_nivel(10, 40, 3)
print(link.esta_vivo())

#link.daño(miranjo)
#print(link.daño(miranjo))

link.atacar(miranjo)
miranjo.atacar(link)

