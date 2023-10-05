"""
Anthony Terán Arellano - 3er Semestre
"""

#Proceso de encriptación de clase
Alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
Clave = "!r#$%&()78956[\_,;:~ç@`^›1234?¡°{}´|<>€§…¸.•kdfhuw"

#Funcion para encriptar la contraseña
def proceso_encriptado(Lv_frase):
    Ov_Frase_Encriptada = ""
    for Letra_ABC in Lv_Frase:
        #Se busca si en la clave se encuentra los respectivos caracteres en la variable Alfabeto
        if(Letra_ABC in Alfabeto):
            #Si se encuentra se procede a agarrar su ubicacion
            indice = Alfabeto.index(Letra_ABC)
            #Y remplazar con un valor de la variable Clave de la misma ubicacion
            Letra_Encriptada = Clave[indice]
            Ov_Frase_Encriptada += Letra_Encriptada
        else:
            #Si no se encuentra tal valor en la variable Alfabeto se utiliza la misma
            Ov_Frase_Encriptada += Letra_ABC
    return Ov_Frase_Encriptada

def proceso_dencriptado(Lv_frase):
    Ov_Frase_Desencriptada = ""
    for Letra_Clave in Lv_Frase:
        #Se busca si en la clave se encuentra los respectivos caracteres en la variable Clave
        if(Letra_Clave in Clave):
            #Si se encuentra se procede a agarrar su ubicacion
            indice = Clave.index(Letra_Clave)
            #Y remplazar con un valor de la variable Alfabeto de la misma ubicacion
            Letra_Encriptada = Alfabeto[indice]
            Ov_Frase_Desencriptada += Letra_Encriptada
        else:
            #Si no se encuentra tal valor en la variable Clave se utiliza la misma
            Ov_Frase_Desencriptada += Letra_Clave
    return Ov_Frase_Desencriptada

#2do - Escribir la palabra/clave y encriptala
Lv_Frase = "Anita lava la tina"
Lv_Frase_Encriptada = proceso_encriptado(Lv_Frase)
print('La frase encriptada es: ', Lv_Frase_Encriptada)


#3ro. Desencriptar la palabra/clave
Lv_Frase_Desencriptada = proceso_dencriptado(Lv_Frase_Encriptada)
print('La frase desencriptoda es: ', Lv_Frase_Desencriptada)