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

#Caracteres
print("--------------------Cadena de caracteres--------------------")
#Frase original
Lv_Frase = "Anita lava la tina"
#Longitud de la frase
print(f"Cantidad de caracteres en la frase {len(Lv_Frase)}")

print(" ")

print("--------------------Frase modificada--------------------")
Lv_Frase = "Anita" + "'-'" + "lava" + "'-'" + "la" + "'-'" + "tina"
print(f"Cadena de caracteres modificada manual mente (quemada):", Lv_Frase)

print(" ")

print("--------------------Frase mayuscula o minuscula--------------------")
Lv_Frase = "Anita"
print(Lv_Frase.upper())
print(Lv_Frase.lower())

print(" ")

print("--------------------Frase presentada varias veces--------------------")
#Presentar espacios despues de una frase/palabra
Lv_Frase = "Anita"
print("Opcion 1.-", Lv_Frase * 3)

Lv_Frase = "Anita "
print("Opcion 2.-", Lv_Frase * 3)

Lv_Frase = "Anita"
Lv_Frase = Lv_Frase + " "
print("Opcion 3.-", Lv_Frase * 3)

Lv_Frase = "Anita"
print("Opcion 4.-", (Lv_Frase + ' ') * 3)

Lv_Frase += " "
print("Opcion 5.-", Lv_Frase * 3)

print(" ")

print("--------------------Encontrar una subcadena--------------------")
Lv_Frase = "Anita lava la tina"
#Encontrar la ubicacion de la cadena
Ln_Frase_Encontrar = Lv_Frase.find("tina")
if(Ln_Frase_Encontrar != -1) :
    print(f"La frase se encuentra en la posicion {Ln_Frase_Encontrar}")
else:
    print(f"No se encuentra")

print(" ")

#Cambiar de mayuscula a minuscula y viceversa
print("--------------------Volver a mayuscula--------------------")
Lv_Frase = "Anita lava la tina"
Lv_Frase_May = Lv_Frase.upper()
Lv_Frase_Min = Lv_Frase.lower()

print(Lv_Frase)
print(Lv_Frase_May)
print(Lv_Frase_Min)

Lv_Frase = Lv_Frase_May.capitalize()
print(Lv_Frase)

print(" ")

print("--------------------Remplazar un caracter por otro--------------------")

Lv_Frase = "Anita lava la tina"
Lv_Frase_Update = Lv_Frase.replace("tina", "#")
print("--remplazar manualmente--")
print(Lv_Frase_Update)
print(" ")

Lv_Frase_2 = "Nosotros"

Lv_Frase_Update = Lv_Frase.replace("Anita", Lv_Frase_2)
print("--remplazar variable--")
print(Lv_Frase_Update)
print(" ")

Lv_Frase_2 = ""

Lv_Frase_Update = Lv_Frase.replace("lava", Lv_Frase_2)
print("--uso remplazar para eliminar--")
print(Lv_Frase_Update)

print(" ")

print("--------------------Salto de linea--------------------")
Lv_Frase = "Anita\nlava\nla\ntina"
print(Lv_Frase)

print(" ")

print("--------------------Posiciones--------------------")
Lv_Frase = "Anita lava la tina"
Lv_Frase_2 = Lv_Frase[6:10]
print(Lv_Frase_2)

Lv_Frase_2 = Lv_Frase[14:18]
print(Lv_Frase_2)
Lv_Frase = "Hola mundo"

print("\n Frase de abajo a arriba")
print(Lv_Frase[0])
print(Lv_Frase[1])
print(Lv_Frase[2])
print(Lv_Frase[3])
print(Lv_Frase[4])
print(Lv_Frase[5])
print(Lv_Frase[6])
print(Lv_Frase[7])
print(Lv_Frase[8])
print(Lv_Frase[9])

print("\n Frase de arriba a abajo\n")
print(Lv_Frase[-1])
print(Lv_Frase[-2])
print(Lv_Frase[-3])
print(Lv_Frase[-4])
print(Lv_Frase[-5])
print(Lv_Frase[-6])
print(Lv_Frase[-7])
print(Lv_Frase[-8])
print(Lv_Frase[-9])
print(Lv_Frase[-10])

print("--------------------Recuperar patrones en una cadena--------------------")

print(Lv_Frase[1:9:2])

print(Lv_Frase[1:8:4])
print(Lv_Frase[1:9:3])