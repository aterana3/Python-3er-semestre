"""
Anthony Terán Arellano - 3er Semestre
Lv = Variable local Varchar - Caracter
Ln = '' number
Lf = '' float
Ld = '' decimal
Fl = '' archivo

Gv = Variable global Varchar - Caracter
Gn = '' number
Gf = '' float
Gd = '' decimal
"""
#Escribir un archivo desde 0 en memoria
import io

#Crear un objeto archivo en memoria
Fl_Stream = io.StringIO()

#Cargar la informacion en memoria
#\n - Salto de linea
Fl_Stream.write("Esta es mi primera linea de mi primer archivo.\n")
Fl_Stream.write("Esta es mi segunda linea de mi primer archivo.\n")
Fl_Stream.write("Esta es mi tercera linea de mi primer archivo.\n")

#Recuperamos la informacion de memoria para pasarlo a fisico
Lv_Informacion = Fl_Stream.getvalue()

#Transferir la informacion a un archivo fisico
with open("Archivo170523_03.txt", "w") as archivo_disco:
    archivo_disco.write(Lv_Informacion)

#No se debe de cerrar si se usa el metodo with
print("Su tercer archivo ha sido creado felicidades.")
