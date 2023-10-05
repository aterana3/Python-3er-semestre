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
Manejo de las rutas - Funciones
El metodo pathlib de la libreria Path
Pathlib es un módulo incorporado en python a partir de la version 3.4 que
proporcionan una interfaz orientada a objetos para manipular rutas de archivos y
directorios de una manera más intuitiva y portable
"""
from pathlib import Path

#Creamos el archivo junto con la ruta
Fl_Ruta_File = Path("./archivos/Archivo190523_01.txt")

#Obtener la ruta general
Fl_Ruta_General = Fl_Ruta_File.absolute()
print(f"La ruta general del archivo es: {Fl_Ruta_General}")

#Verificar que existe la ruta
Lb_Existe = Fl_Ruta_File.exists()
print(f"¿La ruta existe? {Lb_Existe}")

#Obtener el nombre del archivo
Fl_Nombre_File = Fl_Ruta_File.name
print(f"El nombre del file es: {Fl_Nombre_File}")

#Obtener la ruta Padre/Raiz/Root
Fl_Ruta_Raiz = Fl_Ruta_File.parent
print(f"El nombre del directorio raiz es: {Fl_Ruta_Raiz}")