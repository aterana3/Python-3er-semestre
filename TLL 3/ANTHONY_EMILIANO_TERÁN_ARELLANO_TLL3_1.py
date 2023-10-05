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
#Matemáticas
#Presente por pantalla si es o no es número par
Ln_valor = 3
Ln_Result = Ln_valor % 2

if(Ln_Result == 0) :
    print(f"El numero {Ln_valor} es par")
else:
    print(f"El numero {Ln_valor} no es par")

if(Ln_valor > 0):
    print(f"El numero {Ln_valor} es positivo")
else:
    print(f"El numero {Ln_valor} es negativo")

print("------------------------------")
#Indique si el valor PAR Positivo o Par negativo
Ln_valor = 5
Ln_Result = Ln_valor % 2
if(Ln_Result == 0) :
    if (Ln_valor > 0):
        print(f"El numero {Ln_valor} es positivo par")
    else:
        print(f"El numero {Ln_valor} es negativo par")
else:
    if (Ln_valor > 0):
        print(f"El numero {Ln_valor} es negativo impar")
    else:
        print(f"El numero {Ln_valor} es positivo impar")

print("------------------------------")