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
Fl_Ruta_File = Path("./archivos/Archivo190523_02.txt")

#Escribir el contenido
Lv_Contenido = ("Esta es mi primera linea de mi primer archivo.\n")
Lv_Contenido += ("Esta es mi segunda linea de mi primer archivo.\n")
Lv_Contenido += ("Esta es mi tercera linea de mi primer archivo.\n")

#Cargar todo en el archivo -->> Transferir informacion al archivo
Fl_Ruta_File.write_text(Lv_Contenido)

print("Su cuarto archivo ha sido creado, Felicidades.")