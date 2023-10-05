class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)


class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def simplificar(self):
        mcd = self.calcular_mcd(self.numerador, self.denominador)
        self.numerador //= mcd
        self.denominador //= mcd

    def calcular_mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a


class CorreoElectronico:
    def __init__(self, remitente, destinatario, asunto, mensaje):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.mensaje = mensaje

    def enviar(self):
        print(f"Enviando correo de {self.remitente} a {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Mensaje: {self.mensaje}")


class RegistroVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def calcular_total_ventas(self):
        total = sum(venta for venta in self.ventas)
        return total


Ln_opcion = -1

La_menu_principal = [
    "1) Calcular el area de un rectangulo",
    "2) Calcular el perimetro de un rectangulo",
    "3) Simplifica una fracción a su forma más reducida",
    '4) "Enviar" un correo electronico',
    "5) Llevar un registro de cuentas"
]

#Calcular el area de un rectangulo
def ejercicio_1():
    while True:
        try:
            Ln_valor1 = float(input("Introduce el longitud: "))
            Ln_valor2 = float(input("Introduce el ancho: "))

            Lc_rectangulo = Rectangulo(Ln_valor1, Ln_valor2)
            print("Área:", Lc_rectangulo.calcular_area())
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos. Intenta nuevamente.")


def ejercicio_2():
    while True:
        try:
            Ln_valor1 = float(input("Introduce el longitud: "))
            Ln_valor2 = float(input("Introduce el ancho: "))

            Lc_rectangulo = Rectangulo(Ln_valor1, Ln_valor2)
            print("Perimetro:", Lc_rectangulo.calcular_perimetro())
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos. Intenta nuevamente.")


def ejercicio_3():
    while True:
        try:
            Ln_valor1 = float(input("Introduce el numerador: "))
            Ln_valor2 = float(input("Introduce el denominador: "))
            fraccion = Fraccion(Ln_valor1, Ln_valor2)
            fraccion.simplificar()
            print(f"{fraccion.numerador}/{fraccion.denominador}")
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos. Intenta nuevamente.")

#"Enviar" un correo electronico - Clase CorreoElectronico
def ejercicio_4():
    Lv_correo1 = input("Introduce el correo del remitente: ")
    Lv_correo2 = input("Introduce el correo del destinatario: ")
    Lv_asunto = input("Introduce el asunto del correo: ")
    Lv_mensaje = input("Introduce el mensaje a enviar: ")
    correo = CorreoElectronico(Lv_correo1, Lv_correo2, Lv_asunto, Lv_mensaje)
    correo.enviar()

#Llevar un registro de cuentas
def ejercicio_5():
    registro = RegistroVentas()
    while True:
        Lv_venta = input("Ingrese el monto de la venta (0 para finalizar): ")
        if Lv_venta == "0":
            break
        try:
            venta = float(Lv_venta)
            registro.agregar_venta(venta)
        except ValueError:
            print("Valor ingresado inválido. Intente nuevamente.")
    total_ventas = registro.calcular_total_ventas()
    print(f"El total de ventas es: {total_ventas}")


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