class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"


class Figura:
    def calcular_perimetro(self):
        pass


class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 4 * self.lado


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Electrico:
    def __init__(self, marca, modelo):
        Vehiculo.__init__(self, marca, modelo)

    def advertencia(self):
        print('Recuerde que el vehiculo se recarga con electricidad.')


class Gasolina(Vehiculo):
    def __init__(self, marca, modelo):
        Vehiculo.__init__(self, marca, modelo)

    def advertencia(self):
        print('Recuerde que el vehiculo se recarga con gasolina.')

class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando la guitarra.")

class Piano(Instrumento):
    def tocar(self):
        print("Tocando el piano.")


class Bebida:
    def __init__(self, nombre, temperatura):
        self.nombre = nombre
        self.temperatura = temperatura

    def servir(self):
        print(f"Sirviendo {self.nombre} a {self.temperatura} grados Celsius.")


class Refresco(Bebida):
    def __init__(self, nombre, temperatura, gasificado):
        super().__init__(nombre, temperatura)
        self.gasificado = gasificado

    def servir(self):
        super().servir()
        if self.gasificado:
            print("¡Fizz!")


class Café(Bebida):
    def __init__(self, nombre, temperatura, intensidad):
        super().__init__(nombre, temperatura)
        self.intensidad = intensidad

    def servir(self):
        super().servir()
        print(f"Intensidad: {self.intensidad}")

def ejercicio_1():
    while True:
        animal = input("¿Deseas adoptar un perro o un gato? ")
        nombre = input("¿Qué nombre le quieres dar al animal? ")

        if animal.lower() == "perro":
            mascota = Perro(nombre)
            print(f"Has adoptado a un perro llamado {nombre}.")
            print(f"{nombre} dice: {mascota.hacer_sonido()}")
            break
        elif animal.lower() == "gato":
            mascota = Gato(nombre)
            print(f"Has adoptado a un gato llamado {nombre}.")
            print(f"{nombre} dice: {mascota.hacer_sonido()}")
            break
        else:
            print("No tenemos ese animal para adoptar. Por favor, escoge otro.")


def ejercicio_2():
    figura = None
    while not figura:
        tipo_figura = input("Ingrese el tipo de figura (Triangulo/Cuadrado): ")
        if tipo_figura == "Triangulo":
            lado1 = float(input("Ingrese el lado 1 del Triangulo: "))
            lado2 = float(input("Ingrese el lado 2 del Triangulo: "))
            lado3 = float(input("Ingrese el lado 3 del Triangulo: "))
            figura = Triangulo(lado1, lado2, lado3)
        elif tipo_figura == "Cuadrado":
            lado = float(input("Ingrese el lado del Cuadrado: "))
            figura = Cuadrado(lado)
        else:
            print("Tipo de figura inválido. Intente nuevamente.")

    perimetro = figura.calcular_perimetro()
    print("El perímetro de la figura es:", perimetro)


def ejercicio_3():
    coche_seleccionado = ""
    coche_gasolina = Gasolina("Toyota", "Corolla")
    coche_electrico = Electrico("Tesla", "Model S")

    opcion_valida = False
    while not opcion_valida:
        opcion = input("¿Qué coche desea comprar? Ingrese '1' para el coche de gasolina o '2' para el coche eléctrico: ")
        if opcion == "1":
            coche_seleccionado = coche_gasolina
            opcion_valida = True
        elif opcion == "2":
            coche_seleccionado = coche_electrico
            opcion_valida = True
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    print(f"Has comprado el coche: {coche_seleccionado.marca} {coche_seleccionado.modelo}")
    coche_seleccionado.advertencia()


def ejercicio_4():
    instrumento_valido = False
    while not instrumento_valido:
        instrumento = input("¿Qué instrumento quieres tocar? ")
        if instrumento == "guitarra":
            guitarra = Guitarra()
            guitarra.tocar()
            instrumento_valido = True
        elif instrumento == "piano":
            piano = Piano()
            piano.tocar()
            instrumento_valido = True
        else:
            print("No tengo ese instrumento, mejor escoge otro.")


def ejercicio_5():
    while True:
        tipo_bebida = input("¿Qué tipo de bebida desea? (cafe/refresco): ")
        tipo_bebida = tipo_bebida.lower()
        if tipo_bebida == "cafe":
            intensidad = input("Ingrese la intensidad del café: ")
            return Café("Café", "caliente", intensidad)
        elif tipo_bebida == "refresco":
            return Refresco("Refresco", "frío", True)
        else:
            print("No disponemos de esa bebida. Por favor, elija entre café o refresco.")


Ln_opcion = -1

La_menu_principal = [
    "1) Adoptar un animal",
    "2) Calcular el perimetro de un Triangulo/Cuadrado",
    "3) Comprar un coche",
    '4) Tocar un instrumento',
    "5) Pedir una bebida"
]


def imprimirMenu(La_lista):
    print("-------------------------------------")
    for n in La_lista:
        print(n)
    print("-------------------------------------")


if __name__ == "__main__":
    imprimirMenu(La_menu_principal)
    while Ln_opcion < 0 or Ln_opcion > 5:
        try:
            Ln_opcion = int(input("Seleccione opción: "))
        except ValueError:
            print("¡Valor no válido! Por favor, seleccione una opción numérica.")
    match Ln_opcion:
        case 0:
            print("Se ha finalizado el ejercicio")
        case 1:
            ejercicio_1()
        case 2:
            ejercicio_2()
        case 3:
            ejercicio_3()
        case 4:
            ejercicio_4()
        case 5:
            ejercicio_5()

