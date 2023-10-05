#Importamops el metodos de la libreria cryptography
from cryptography.fernet import Fernet

#Se genera una clave de cifrado
clave = Fernet.generate_key()

#Cremos un objeto Fernet con la clave generada
fernet = Fernet(clave)

#Frase que vamos a cifrar:
texto_original = "Anita lava la tina"

#Codificamos-Ciframos la frase
texto_cifrado = fernet.encrypt(texto_original.encode())

#Decodificamos-Deciframos la frase
texto_decifrado = fernet.decrypt(texto_cifrado).decode()
print("---------------------------------")
print(f"Texto original: {texto_original}")
print("---------------------------------")
print(f"Texto cifrado: {texto_cifrado}")
print("---------------------------------")
print(f"Texto decifrado: {texto_decifrado}")
print("---------------------------------")