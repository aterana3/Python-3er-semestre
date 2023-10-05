from pathlib import Path

Fl_Ruta_File = Path("C:/aterana3/RegActivFijo.txt")
Fl_File_Sec = Path("C:/aterana3/ControlSecuencia.txt")


ActivoFijosRegistro = {
    "CodActivoFijo": "",
    "CodBarra": "",
    "CodQr": "",
    "CodRfId": "",
    "CodEAN13": "",
    "CodEAN128": "",
    "Descripcion": "",
    "UbicaEmp": "",
    "UbicaArea": "",
    "UbicaDpto": ""
}


def inicializarArchivos():
    try:
        Fl_Ruta_Parent = Fl_Ruta_File.parent
        Lb_Existe_Ruta = Fl_Ruta_Parent.exists()
        if not Lb_Existe_Ruta:
            Fl_Ruta_Parent.mkdir()
            print(f"Se ha creado la carpeta del sistema {Fl_Ruta_Parent}")
            with open(Fl_Ruta_File, "w") as archivo:
                archivo.write("")
    except IOError:
        print("Contacte a la area de sistema +592 22222222")


def getSec(Iv_Control):
    Ln_valor = 0
    with open(Fl_File_Sec, "r") as archivoSecuencia:
        for linea in archivoSecuencia:
            Control, Secuencia = linea.strip().split(":")
            if Control == Iv_Control:
                Ln_valor = int(Secuencia) + 1
    return Ln_valor


def UpdateSec(Iv_Control, Iv_secuencia):
    OV_Mensaje = "No"
    LineaUpdate = ""
    with open(Fl_File_Sec, "r") as archivoSecuencia:
        for linea in archivoSecuencia:
            Control, Secuencia = linea.strip().split(":")
            if Control == Iv_Control:
                Secuencia = Iv_secuencia
            LineaUpdate += f"{Control}:{Secuencia}\n"
    with open(Fl_File_Sec, "w") as archivoSecuencia:
        archivoSecuencia.write(LineaUpdate)
        OV_Mensaje = "Si"
    return OV_Mensaje


inicializarArchivos()

for clave, valor in ActivoFijosRegistro.items():
    valor = input("{}: ".format(clave))
    ActivoFijosRegistro[clave] = valor

while True:
    Lv_guardar = input("¿Desea guardar los datos del registro? (S/N) ").upper()
    if Lv_guardar == "S":
        Ln_secuencia = getSec("ActFijReg")

        Linea = f"Activo{Ln_secuencia}="
        for clave, valor in ActivoFijosRegistro.items():
            Linea += f"{clave}: {valor},"
        Linea = Linea.rstrip() + "\n"

        with open(Fl_Ruta_File, "a") as archivo:
            archivo.write(Linea)

        UpdateSec("ActFijReg", Ln_secuencia)
        print("Se ha guardado correctamente el registro")
        break
    elif Lv_guardar == "N":
        print("Ha decido no guardar los datos \nFinalizando proceso..")
        break
    else:
        print("Seleccione una opcion correcta!")