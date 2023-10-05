#Anthony Terán Arellano - 3er Semestre
#Lv = Variable local Varchar - Caracter
#Ln = "" number
#Lf = "" float
#Ld = "" decimal

#Gv = Variable global Varchar - Caracter
#Gn = "" number
#Gf = "" float
#Gd = "" decimal

import math

#Cadenas
Lv_Cadena1 = "Hola mundo"
Lv_Cadena2 = 'Hola mundo'
Lv_Cadena3 = 'Según lo que dijo la compañera: "Yo no fui"'
Lv_Cadena4 = "El valor del iva es '0.12'"

print(Lv_Cadena1)
print(Lv_Cadena2)
print(Lv_Cadena3)
print(Lv_Cadena4)

#Valores numericos

Ln_Valor1 = 2
Ln_Valor2 = 2

print("Suma")
Ln_Result = Ln_Valor1 + Ln_Valor2
print(Ln_Result)

print("Resta")
Ln_Result = Ln_Valor1 - Ln_Valor2
print(Ln_Result)

print("Multiplicacion")
Ln_Result = Ln_Valor1 * Ln_Valor2
print(Ln_Result)


print("Division")
Ln_Result = Ln_Valor1 / Ln_Valor2
print(Ln_Result)

print("Potencia")
Ln_Result = Ln_Valor1 ** Ln_Valor2
print(Ln_Result)

print("Seno")
Lf_Radianes = (Ln_Valor1 * math.pi) / 180
Ln_Result = math.sin(Lf_Radianes)
print(Ln_Result)

print("Coseno")
Lf_Radianes = (Ln_Valor1 * math.pi) / 180
Ln_Result = math.cos(Lf_Radianes)
print(Ln_Result)

#Asignacion
Lv_variables = 2.3
print(type(Lv_variables))

#Caracteres
Lv_Frase = "Anita lava la tina"
print(f"Cantidad de caracteres en la frase {Lv_Frase}: {len(Lv_Frase)}")