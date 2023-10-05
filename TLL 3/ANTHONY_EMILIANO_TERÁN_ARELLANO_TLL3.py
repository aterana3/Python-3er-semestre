"""
Anthony Terán Arellano - 3er Semestre
Lv = Variable local Varchar - Caracter
Ln = '' number
Lf = '' float
Ld = '' decimal

Gv = Variable global Varchar - Caracter
Gn = '' number
Gf = '' float
Gd = '' decimal
"""
import math

#Matemáticas
#Presente por pantalla si es o no es número par
Ln_valor = 5
Ln_Result = Ln_valor % 2

if(Ln_Result == 0) :
    print(f"El numero {Ln_valor} es par")
else:
    print(f"El numero {Ln_valor} no es par")

print("------------------------------")
#Recuperar el valor decimal
Ln_valor = 28.123
Ln_Parte_Entera = Ln_valor/ 1
print(Ln_Parte_Entera)

#Recuperamos el valor en una variable integer
Ln_Parte_Entera = int(Ln_valor//1)
print(Ln_Parte_Entera)

#Recuperarmos la parte decimal
Ln_Parte_Decima = round((Ln_valor % 1), 2)
print(Ln_Parte_Decima)

#Truncar
Ln_Parte_Decima = Ln_valor % 1
Ln_Parte_Decima = '%.3f'%(Ln_Parte_Decima)
print(Ln_Parte_Decima)

print("------------------------------")

Ln_valor = 80.1265
print(f"El número es {Ln_valor}")
Ln_Parte_Entera, Ln_Parte_Decima = math.modf(Ln_valor)
print(f"Su parte entera es {Ln_Parte_Entera} y su parte decimal es {Ln_Parte_Decima}")