#Importamops el metodos de la libreria cryptography
import os

#Definimos la ruta completa de la carpeta a crear en la unidad C
Lf_ruta = "C:/System_VideoClub"

#Usamos la excepción - Intentar crear la carpeta
try:
    os.mkdir(Lf_ruta)
    print("Carpeta creada exitosamente.")
except OSError as error:
    print(f"No se pudo crear la carpeta: {error}")