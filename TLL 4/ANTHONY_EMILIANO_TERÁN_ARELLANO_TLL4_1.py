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
#Crear un archivo en TXT
#W - write(Sobreescribe el archivo/remplaza el archivo)
#R - read(Leer el archivo)
#A = Añadir informacion al archivo
#Si no existen parametros, la configuracion por defecto sera Read

Fl_Archivo = open("Archivo170523_01.txt", "w")

#Escribir linea del archivo
#\n - Salto de linea
Fl_Archivo.write("Esta es mi primera linea de mi primer archivo.\n")
Fl_Archivo.write("Esta es mi segunda linea de mi primer archivo.\n")
Fl_Archivo.write("Esta es mi tercera linea de mi primer archivo.\n")

#Cierre
Fl_Archivo.close()

print("Su primer archivo ha sido creado felicidades.")

#Crear un archivo -->> consume memoria
#No cierra -->> Procesos huerfanos, procesos separados
#No cierra -->> No se puede continuar