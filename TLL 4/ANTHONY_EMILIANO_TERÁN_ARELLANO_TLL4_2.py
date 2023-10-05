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
#as - parametro para añadir un alias
with open("Archivo170523_02.txt", "w") as File02:
    File02.write("Esta es mi primera linea de mi primer archivo.\n")
    File02.write("Esta es mi segunda linea de mi primer archivo.\n")
    File02.write("Esta es mi tercera linea de mi primer archivo.\n")

#No se debe de cerrar si se usa el metodo with
print("Su segundo archivo ha sido creado felicidades.")
