# Diccionario de datos del usuario
import json
# Importar las librerias/Bibliotecas
from pathlib import Path

Fl_Ruta_Sec = Path("C:/GestorContactos/cache.txt")
Fl_Ruta_File = Path("C:/GestorContactos/contactos.json")

# Estructura de diccionario
Dcc_ContactSystem = {
    "Nombre": "",
    "Telefono": "",
    "Correo": "",
}

Dcc_Contactos = {}


# 1.- Crear los archivos
def inicializarArchivos():
    if not Fl_Ruta_File.parent.exists():
        Fl_Ruta_File.parent.mkdir()
        print("Se creó la carpeta", Fl_Ruta_File.parent)

    if not Fl_Ruta_File.exists():
        with open(Fl_Ruta_File, 'w') as archivoContacto:
            archivoContacto.write("{}")
            print("Se creó el archivo para los contactos", Fl_Ruta_File)
    if not Fl_Ruta_Sec.exists():
        with open(Fl_Ruta_Sec, 'w') as archivoCache:
             archivoCache.write("Contactos:0")
        print("Se creó el archivo para el cache", Fl_Ruta_Sec)


# 2.- Leer la informacion del archivo
def recuperarRegistro():
    Dcc_Contactos_Read = {}
    with Fl_Ruta_File.open(mode="r") as archivo:
        # Crear el diccionario con el contenido del json
        Dcc_Contactos_Read = json.load(archivo)
    return Dcc_Contactos_Read


# *************************************************

# Obtener secuencia
def Prc_ContrSecuencia(Iv_Registro):
    On_Secuencia = 0
    # Accedemos al file txt y recuperamos el registro
    with Fl_Ruta_Sec.open(mode="r") as archivoSecuencia:
        for registro in archivoSecuencia:
            # Control = valor a recuperar
            # Secuencia = La secuencia/cantidad de registros
            Control, Secuencia = registro.strip().split(":")
            if Control == Iv_Registro:
                On_Secuencia = int(Secuencia) + 1
                break
    return On_Secuencia


# Actualizar secuencia
def Prc_UpdateSecuencia(Iv_Registro, In_Secuencia):
    Ov_Mensaje = ""
    # Accedemos al file de secuencia en forma de lectura
    with Fl_Ruta_Sec.open(mode="r") as archivoSecuencia:
        for registro in archivoSecuencia:
            # Control = valor a recuperar
            # Secuencia = La secuencia/cantidad de registros
            Control, Secuencia = registro.strip().split(":")
            if Control == Iv_Registro:
                Secuencia = In_Secuencia
            Linea = Control + ":" + str(Secuencia) + "\n"
    # Accedemos al archivo en forma de escritura y agregamos el nuevo valor
    with Fl_Ruta_Sec.open(mode="w") as archivoSecuencia:
        archivoSecuencia.write(Linea)
        Ov_Mensaje = "SI"
    return Ov_Mensaje


# Guardar registro
def guardarRegistro():
    # Guardar la informacion de los contactos en el json
    with Fl_Ruta_File.open(mode="w") as archivo:
        json.dump(Dcc_Contactos, archivo)


# Mostrar una lista de los contactos en el sistema
def listaContacto():
    print("Lista de contacto: ")
    #Mostrar los contactos
    for Contactos, valores in Dcc_Contactos.items():
        print(f"id:{Contactos} - {valores['Nombre']}")


# Mostrar los datos de un contacto
def MostrarDatosContacto():
    print("Que contacto desea saber sus datos: ")
    # Se muestra una lista de los contactos
    for Contactos, valores in Dcc_Contactos.items():
        print(f"id:{Contactos} - {valores['Nombre']}")
    while True:
        try:
            # Solicitar id de usuario a mostrar datos
            Op_contacto = int(input("Introduce el id de contacto a mostrar: "))
            for Contactos, valores in Dcc_Contactos.items():
                # Validar que exista el contacto
                if int(Contactos) == Op_contacto:
                    # Mostrar datos del contacto
                    for clave, valor in valores.items():
                        print(f"{clave}: {valor}")
                    break
                else:
                    print("Ese contacto no existe!")
                    print("Terminando proceso...")
                    break
            break
        except ValueError:
            print("Opción no valida.")


# Añadir un nuevo contacto
def añadirContacto():
    # Solicitar datos para añadir al registro
    print("Ingrese los datos del nuevo contacto: ")
    for clave in Dcc_ContactSystem:
        valor = input("{}: ".format(clave))
        Dcc_ContactSystem[clave] = valor
    while True:
        # Preguntar si se desea guardar
        Lv_Guardar = str(input("Desea guardar los datos del contacto (S/N): ")).upper()
        # Si es "S" se procede a guardar los datos
        if Lv_Guardar == "S":
            print("Procesando...")
            # Obtener la cantidad de contactos registrados
            Ln_secuencia = Prc_ContrSecuencia("Contactos")
            # Guardar los datos en el diccionario
            Dcc_Contactos[str(Ln_secuencia)] = Dcc_ContactSystem
            # Actualizar el registro
            Prc_UpdateSecuencia("Contactos", Ln_secuencia)
            guardarRegistro()
            print("Contacto guardado")
            break
        elif Lv_Guardar == "N":
            # Cancelamos el proceso de crear un nuevo usuario
            print("Proceso cancelado.")
            interfaz()
            break
        else:
            print("Opción no valida.")


def actualizarContacto():
    print("Que contacto desea actualizar: ")
    # Se muestra una lista de los contactos
    for Contactos, valores in Dcc_Contactos.items():
        print(f"id:{Contactos} - {valores['Nombre']}")
    while True:
        try:
            # Solicitar id de usuario a actualizar
            Op_contacto = int(input("Introduce el id de contacto a actualizar: "))
            for Contactos, valores in Dcc_Contactos.items():
                # Validar que exista ese contacto
                if int(Contactos) == Op_contacto:
                    # Preguntar nuevamente los datos del Contacto
                    for clave in Dcc_ContactSystem:
                        valor = input("{}: ".format(clave))
                        # Establecer los nuevos valores a la clave
                        Dcc_ContactSystem[clave] = valor
                        Dcc_Contactos[Contactos] = Dcc_ContactSystem
                        # Actualizar el registro
                        guardarRegistro()
                    print("Contacto actualizado!")
                    break
                else:
                    print("Ese contacto no existe!")
                    print("Terminando proceso...")
                    break
            break
        except ValueError:
            print("Opción no valida.")


def eliminarContacto():
    print("Que contacto desea eliminar: ")
    # Se muestra una lista de los contactos
    for Contactos, valores in Dcc_Contactos.items():
        print(f"id:{Contactos} - {valores['Nombre']}")
    while True:
        Op_eliminar = False
        try:
            # Solicitar id de usuario a eliminar
            Op_contacto = int(input("Introduce el id de contacto a eliminar: "))
            for Contactos, valores in Dcc_Contactos.items():
                # Si el contacto existe Op_eliminar pasara a un valor True, caso contrario False
                if int(Contactos) == Op_contacto:
                    Op_eliminar = True
                    break
            # Validar Op_eliminar
            if Op_eliminar:
                # Borrar contacto del registro y actualizar el registro
                Dcc_Contactos.pop(str(Op_contacto))
                guardarRegistro()
                print("Contacto eliminado!")
            else:
                # No existe contacto finalizar el proceso
                print("Ese contacto no existe!")
                print("Terminando proceso...")
            break
        except ValueError:
            print("Opción no valida.")


def interfaz():
    print("Seleccione que desea hacer:")
    print("1.- Lista de contacto")
    print("2.- Mostrar datos de contacto")
    print("3.- Añadir contacto")
    print("4.- Actualizar contacto")
    print("5.- Eliminar contacto")
    print("6.- Salir")
    while True:
        try:
            Ln_opcion = int(input("Introduzca opcion: "))
            if Ln_opcion == 1:
                listaContacto()
                break
            elif Ln_opcion == 2:
                MostrarDatosContacto()
                break
            elif Ln_opcion == 3:
                añadirContacto()
                break
            elif Ln_opcion == 4:
                actualizarContacto()
                break
            elif Ln_opcion == 5:
                eliminarContacto()
                break
            elif Ln_opcion == 6:
                print("Programa finalizado.")
                break
        except ValueError:
            print("Ha introducido una opcion invalida")


if __name__ == "__main__":
    # Se crean las carpetas y archivos de sistema, en caso de que exista se omite este proceso
    inicializarArchivos()
    # Se recupera la lista de registro de contactos para evitar hacer varias consultas
    Dcc_Contactos = recuperarRegistro()
    # Se carga la "interfaz" del usuario
    interfaz()
