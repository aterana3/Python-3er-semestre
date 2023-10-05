"""
Anthony Terán Arellano - 3er Semestre
Lv = Variable local Varchar - Caracter
Ln = '' number
Lf = '' float
Ld = '' decimal
La = '' array
Lb = '' boolean

Gv = Variable global Varchar - Caracter
Gn = '' number
Gf = '' float
Gd = '' decimal
Ga = '' array
Gb = '' boolean
"""

Ln_opcion = 0

La_menu_principal = [
    "1) Comprobar si un numero es positivo o negativo",
    "2) Comprobar si un numero es par o impar",
    "3) Comprobar si un numero es multiplo de 3",
    "4) Comprobar que una palabra es palíndromo",
    "5) Calcular el descuento en una tienda según el monto de compra"
]

def imprimirMenu(La_lista):
    print("-------------------------------------")
    for n in La_lista:
        print(n)
    print("-------------------------------------")


#Comprobar si un numero es positivo o negativo
def ejercicio_1():
    Lb_resultado = False
    while not Lb_resultado:
        try:
            Ln_valor = int(input("Ingrese un numero: "))
            if Ln_valor > 0:
                print(f"El numero {Ln_valor} es positivo")
            elif Ln_valor < 0:
                print("El número es negativo.")
            else:
                print("El número es cero.")
            Lb_resultado = True
        except ValueError:
            print("¡Valor no válido! Por favor, ingrese valor numérico.")


#Comprobar si un numero es par i impar
def ejercicio_2():
    Lb_resultado = False
    while not Lb_resultado:
        try:
            Ln_valor = int(input("Ingrese un numero: "))
            if Ln_valor % 2 == 0:
                print(f"El numero {Ln_valor} es par")
            else:
                print(f"El numero {Ln_valor} es impar")
            Lb_resultado = True
        except ValueError:
            print("¡Valor no válido! Por favor, ingrese valor numérico.")


#Comprobar si un numero es multiplo de 3
def ejercicio_3():
    Lb_resultado = False
    while not Lb_resultado:
        try:
            Ln_valor = int(input("Ingrese un numero: "))
            if Ln_valor % 3 == 0:
                print(f"El numero {Ln_valor} es múltiplo de 3.")
            else:
                print(f"El numero {Ln_valor} es no múltiplo de 3.")
            Lb_resultado = True
        except ValueError:
            print("¡Valor no válido! Por favor, ingrese valor numérico.")


#Verificar si una palabra es un palíndromo
def ejercicio_4():
    Lv_palabra = input("Ingrese una palabra: ")
    Lv_palabra = Lv_palabra.replace(" ", "").lower()
    if Lv_palabra == Lv_palabra[::-1]:
        print("La palabra es un palíndromo.")
    else:
        print("La palabra no es un palíndromo.")


#Calcular el descuento en una tienda según el monto de compra 10% de descuento se obtendra
def ejercicio_5():
    print("Si el monto es mayor a 100 se dara un descuento de 10%")
    Lb_resultado = False
    while not Lb_resultado:
        try:
            Ln_valor = float(input("Ingrese el monto de compra: "))
            if Ln_valor >= 100:
                Lf_descuento = 0.1 * Ln_valor
                Lf_monto_total = Ln_valor - Lf_descuento
                print(f"Se aplica un descuento de ${Lf_descuento:.2f}.")
                print(f"El monto total a pagar es: ${Lf_monto_total:.2f}.")
            else:
                print("No aplica descuento.")
                print(f"El monto total a pagar es: ${Ln_valor:.2f}.")
            Lb_resultado = True
        except ValueError:
            print("¡Valor no válido! Por favor, ingrese valor numérico.")


if __name__ == "__main__":
    imprimirMenu(La_menu_principal)
    while True:
        try:
            Ln_opcion = int(input("Seleccione opción: "))
            if Ln_opcion < 0 or Ln_opcion > 5:
                print("¡Opción inválida! La opción debe ser menor o igual a 4.")
            else:
                break
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