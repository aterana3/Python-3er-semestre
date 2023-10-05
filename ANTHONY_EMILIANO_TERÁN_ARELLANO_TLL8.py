from pathlib import Path

# Contar números impares: Escribe un programa que cuente la cantidad de números impares/pares en una lista dada.
def ejercicio1():
    La_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Ln_contador_par = 0
    Ln_contador_impar = 0
    print("--------------[Ejercicio 1]------------------")
    for Ln_numero in La_lista:
        if (Ln_numero % 2 == 0):
            Ln_contador_par += 1
        else:
            Ln_contador_impar += 1

    print(f"Hay un total de {Ln_contador_par} numeros par")
    print(f"Hay un total de {Ln_contador_impar} numeros impar")
    print("---------------------------------------------")


# Orden inverso: Escribe un programa que tome una lista de números y la imprima en orden inverso.
def ejercicio2():
    La_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("--------------[Ejercicio 2]------------------")
    La_lista.reverse()
    for Ln_numero in La_lista:
        print(Ln_numero)
    print("---------------------------------------------")


# Ordenamiento de una lista: Escribe un programa que ordene una lista de números ingresada por el usuario de forma
# ascendente o descendente.
def ejercicio3():
    Lv_lista = input("Introduzca serie de numeros separada con espacio: ")
    La_lista = Lv_lista.split(" ")
    for Lv_valores in La_lista:
        try:
            Lv_valor = int(Lv_valores)
        except ValueError:
            La_lista.remove(Lv_valores)
    if len(La_lista) >= 1:
        Lv_ordenar = input("Quiere escribir los valores en Ascedente o Descendente (A/D): ")
        Lv_ordenar.lower()
        if (Lv_ordenar == "a"):
            La_lista.reverse()
            print(La_lista)
        else:
            La_lista.sort()
            print(La_lista)
    else:
        print("La lista no tiene valores para ordenar")


# Búsqueda en una lista: Escribe un programa que busque un elemento específico en una lista ingresada por el usuario
# y muestre su posición.
def ejercicio4():
    Lv_lista = input("Introduzca los valores de una lista con espacio: ")
    La_lista = Lv_lista.split(" ")
    if len(La_lista) >= 1:
        Lv_buscar = input("Introduzca el valor a buscar en la lista: ")
        try:
            Ln_index = La_lista.index(Lv_buscar)
            print(f"El elemento {Lv_buscar} se encuentra en la posicion: {Ln_index}")
        except ValueError:
            print("El elemento no ha sido encontrado")
    else:
        print("Tienes una lista vacia")


# Contar palabras en un archivo: Escribe un programa que cuente la cantidad de palabras en un archivo de texto.
def ejercicio5():
    Fl_archivo = Path("archivos/archivo_pruebas_1.txt")
    Ln_contador = 0
    with Fl_archivo.open(mode="r") as archivo:
        for linea in archivo:
            Ln_contador += len(linea.split(" "))
    print(f"El numero total de palabras es {Ln_contador}")


# Contar líneas en un archivo: Escribe un programa que cuente la cantidad de líneas en un archivo de texto.
def ejercicio6():
    Fl_archivo = Path("archivos/archivo_pruebas_1.txt")
    Ln_contador = 0
    with Fl_archivo.open(mode="r") as archivo:
        for linea in archivo:
            Ln_contador += 1
    print(f"El numero total de lineas es {Ln_contador}")


# Contar caracteres en un archivo: Escribe un programa que cuente la cantidad de caracteres en un archivo de texto.
def ejercicio7():
    Fl_archivo = Path("archivos/archivo_pruebas_1.txt")
    Ln_contador = 0
    with Fl_archivo.open(mode="r") as archivo:
        for linea in archivo:
            Ln_contador += len(linea)
    print(f"El numero total de lineas es {Ln_contador}")


# Buscar y reemplazar: Escribe un programa que busque una palabra en un archivo de texto y la reemplace por otra.
def ejercicio8():
    Fl_archivo = Path("archivos/archivo_pruebas_1.txt")
    with Fl_archivo.open(mode="r") as archivo:
        for linea in archivo:
            Lv_buscar = input("Introduzca el valor a buscar en el archivo: ")
            try:
                Ln_index = linea.index(Lv_buscar)
                print(f"El elemento {Lv_buscar} se encuentra en la posicion: {Ln_index}")
            except ValueError:
                print("El elemento no ha sido encontrado")
            break


if __name__ == "__main__":
    ejercicio1()
    ejercicio2()
    ejercicio3()
    ejercicio4()
    ejercicio5()
    ejercicio6()
    ejercicio7()
    ejercicio8()