"""
Anthony Terán Arellano - 3er Semestre
Lv = Variable local Varchar - Caracter
Ln = '' number
Lf = '' float
Ld = '' decimal
Lb = '' boolean
Fl = '' archivo

Gv = Variable global Varchar - Caracter
Gn = '' number
Gf = '' float
Gd = '' decimal
Gb = '' boolean
Fg = '' archivo
"""

"""
Manejo de las rutas
El metodo pathlib de la libreria Path
Pathlib es un módulo incorporado en python a partir de la version 3.4 que
proporcionan una interfaz orientada a objetos para manipular rutas de archivos y
directorios de una manera más intuitiva y portable
"""
from pathlib import Path

#Crear el archivo junto con la ruta
Fl_Ruta_File = Path("./archivos/Archivo190523_04.txt")

#Combinar funciones y procesos

#1.- Preguntar si existe la ruta
Lb_Existe_Raiz = Fl_Ruta_File.parent.exists()
if Lb_Existe_Raiz:
    Lb_Existe_Archivo = Fl_Ruta_File.exists()
    if Lb_Existe_Archivo:
        # Si existe el archivo lo abro y leo
        with Fl_Ruta_File.open(mode="r") as archivo:
            for linea in archivo:
                print(linea)
    else:
        #Si no existe el archivo se crea el archivo
        with Fl_Ruta_File.open(mode="w") as archivo:
            archivo.write("Esta es mi primera linea de mi primer archivo.\n")
            archivo.write("Esta es mi segunda linea de mi primer archivo.\n")
            archivo.write("Esta es mi tercera linea de mi primer archivo.\n")
            print("El archivo ha sido creado con exito.")
else:
    #Si no existe la ruta se manda un mensaje codigo de error.
    print("Codigo 035 - La ruta especificada no existe, contacte a la area de sistemas.")