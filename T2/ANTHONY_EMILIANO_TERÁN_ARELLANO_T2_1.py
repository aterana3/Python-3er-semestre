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

Ln_opcion = -1

La_menu_principal = [
    "1) Crear la fichas de domino",
    "2) Saber cuantas palabras hay en una frase",
    "3) Realizar operacion matematica dividir",
    "4) De una serie de numeros saber cuales son pares",
    "5) De una serie de numeros saber cual es el valor maximo"
]


#Crear la fichas de domino - funcion range
def ejercicio_1():
    print("Se mostraran las piezas de domino")
    for i in range(7):
        for j in range(i, 7):
            print(f"[{i}|{j}]")


#Saber cuantas palabras hay en una frase - len
def ejercicio_2():
    Lv_frase = input("Ingresa una frase: ")

    # Dividir la frase en palabras
    Lv_palabras = Lv_frase.split()

    # Obtener la cantidad de palabras
    Ln_cantidad_palabras = len(Lv_palabras)

    # Mostrar el resultado
    print("La frase tiene", Ln_cantidad_palabras, "palabras.")


#Realizar operacion matematica dividir - funcion round
def ejercicio_3():
    while True:
        try:
            Ln_valor1 = float(input("Introduce el numerador: "))
            Ln_valor2 = float(input("Introduce el denominador: "))
            Ln_resultado = Ln_valor1 / Ln_valor2

            Lv_redondear = input("¿Deseas redondear el resultado? (Sí/No): ")
            Lv_redondear = Lv_redondear.lower()

            if Lv_redondear == "Si" or Lv_redondear == "si":
                Ln_resultado_round = round(Ln_resultado)
                print(f"El resultado de la división redondeando es: {Ln_resultado_round}")
            else:
                print(f"El resultado de la división es: {Ln_resultado}")
            break
        except ValueError:
            print("Error: Debes introducir valores numéricos. Intenta nuevamente.")


#De una serie de numeros saber cuales son pares - funcion list
def ejercicio_4():
    Lv_numeros = input("Introduce una serie de números separados por espacios: ")
    Ln_numeros_lista = Lv_numeros.split()
    Ln_numeros = list(map(int, Ln_numeros_lista))

    Ln_numeros_pares = [num for num in Ln_numeros if num % 2 == 0]

    print("Los números pares son:", Ln_numeros_pares)


#De una serie de numeros saber cual es el valor maximo - funcion max
def ejercicio_5():
    Lv_numeros = input("Introduce una serie de números separados por espacios: ")
    Ln_numeros_lista = Lv_numeros.split()
    Ln_numeros = []

    for Lv_num in Ln_numeros_lista:
        try:
            num = int(Lv_num)
            Ln_numeros.append(num)
        except ValueError:
            continue
    if Ln_numeros:
        Ln_maximo = max(Ln_numeros)
        print("El número máximo es:", Ln_maximo)
    else:
        print("No se encontraron números enteros en la lista.")


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