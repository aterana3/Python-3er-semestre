#Ejemplo 1
class Motor:
    def encender(self):
        print('El motor se ha encendido.')

    def apagar(self):
        print("El motor se ha apagado")

class Bocina:
    def hacer_sonido(self):
        print('Beep beep!')

class Luces:
    def encender_luces(self):
        print('Las luces se han encendido.')

class Coche(Motor, Bocina, Luces):
    pass

