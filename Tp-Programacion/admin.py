import csv
from hashlib import sha256

import getch
import matplotlib.pyplot as plt
import sistema
from fpdf import FPDF

titulo = "MENU DEL ADMINISTRADOR"
opcion = ""
opciones = "1. CARGAR AUTO\n2. CARGAR SOCIO CONDUCTOR\n3. VER GANANCIAS\n4. SALIR"

# LLAMA A LA FUNCION DE MENU PRINCIPAL
def volver_menu_sistem():
    sistema.main()
    exit()


# ESTA FUNCIÓN MUESTRA EL MENÚ AL USUARIO QUE SE LOGEA COMO ADMIN Y LLAMA
# A LA FUNCIÓN QUE CORRESPONDA PARA PROCESAR LA OPCION SELECCIONADA
def mostrar_menu():
    print(" *" * (len(titulo) + 4))
    print(titulo.center(len(titulo)+30))
    print(" *" * (len(titulo) + 4))

    print(opciones)
    while True:
        try:
            opcion = int(input("Seleccione una de las opción (1-4): "))
            if ((opcion < 0) or (opcion > 4)):
                print('Este numero de opcion:', opcion,'no es correcto.')
            else:
                match opcion:
                    case 1: registrar_auto()
                    case 2: cargar_socio()
                    case 3: mostrar_ganancia()
                    case 4: volver_menu_sistem()
        except ValueError:
                print("Debes escribir un numero de opcion valido.")
                print(opciones)

# LLAMA A LA FUNCION DE MENU
def volver_menu():
    print("Volviendo al Menu...")
    mostrar_menu()
    exit()


# GENERAR PRIMERO EL GRÁFICO DE TORTAS Y A CONTINUACION
# CREAR EL ARCHIVO PDF
# LA FUNCIÓN RECIBE COMO PARÁMETROS LA LISTA CON LOS NOMBRES DE
# LOS MESES PROCESADOS Y LOS PORCENTAJES CON LAS GANANCIAS DE CADA MES
def generar_grafico(meses, ganancias):
    pass


# LA FUNCION RECIBE UN NUMERO ENTERO QUE ES EL NÚMEO DE MES
# LA FUNCIÓN DEVUELVE EL NOMBRE DEL MES
def buscar_mes_nombre(indice):
    pass


# ABRIR EL ARCHIVO VIAJES.CSV Y PROCESAR EL MISMO
# DEL PROCESAMIENTO, DEBO IR SACANDO LOS NOMBRES DE LOS MESES (USAR FUNCION BUSCAR_MES_NOMBRE())
# PARA ESTO, SE LEE CON UN FOR CADA UNA DE LAS LIENAS DEL ARCHIVO Y CON LA FUNCION SPLIT VOY
# SACANDO LOS DATOS QUE NECESITO
# OBTENER LAS GANANCIAS DE CADA MES Y LUEGO CALCULAR EL PORCENTAJE DE CADA UNO RESPECTO DEL TOTAL. 
# GUARDAR LOS DATOS EN LA LISTA PARA LUEGO GENERAR GRÁFICO Y PDF
def mostrar_ganancia():
    print('mostrar ganancia')
    # meses = []
    # ganancias = []

    # generar_grafico(meses, ganancias)


# SI LA PATENTE TRAE UN CARACTER '-' EN EL MEDIO, LO QUITA
# EJEMPLO: EL USUARIO INGRESA KIU-999. LA FUNCION DEVUELVE: KIU999
def formatear_patente(_patente):
    cadena_formateada = _patente.replace("-", "").upper()
    return cadena_formateada

# VALIDAR POR LONGITUD Y TAMBIEN QUE LOS CARACTERES ALFABETICOS Y NUMÉRICOS
# ESTEN EN EL ORDEN CORRECTO. AYUDARSE CON EL OPERADOR SLICING DE STRINGS
# LA FUNCIÓN DEVUELVE LA PATENTE SI ESTA CORRECTA O -1 SI ES INCORRECTA

def validar_patente(_patente):
    if (len(_patente) >= 6):
        patente_formateada = formatear_patente(_patente)
        if((patente_formateada[0:3].isalpha() and patente_formateada[4:6].isdigit()) or ((patente_formateada[0:2].isalpha() and patente_formateada[3:4].isdigit()) and patente_formateada[5:6].isalpha())):
            return 0
    return -1

# VALIDACIONES
# print(validar_patente('234KIU999'))
# print(validar_patente('KIU999asd'))
# print(validar_patente('KI-U-999-WEB'))

# LA FUNCION PIDE LOS DATOS DEL VEHÍCULO AL USUARIO, VALIDA LA PATENTE, VALIDA EL MODELO
# GENERA EL STRING CON EL FORMATO CSV PARA GUARDAR EN EL ARCHIVO AUTOS.CSV
def registrar_auto():
    list_registrar_auto = []

    # (A)=GAMA ALTA=(modelo 2012 o superior hasta el año actual inlcuido) | (B) =GAMA BAJA =(modelo entre 2004 y 2012)

    while True:
        patente=''
        modelo=''
        servicio=''
        categoria=''
        # VERIFICAR SI SE PRESIONÓ LA TECLA "ESC"
        print("Presione cualquier tecla para continuar o Esc para volver al menu anterior...")
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            volver_menu()
        while True:
            patente = input('Ingrese la patente (LLLNNN o LLNNNLL): ')
            if validar_patente(patente) == -1:
                print('Pantente invalida.')
            else:
                break

        while True:
            print('(No se puede incluir modelos de autos menores a 1995)')
            try:
                modelo = int(input('Ingrese el numero de modelo: '))
                if (modelo < 1995):
                    print('Este numero de modelo:', modelo,'no es correcto.')
                else:
                    if((modelo > 2004) and (modelo < 2012)):
                        # (B)=GAMA BAJA=(modelo entre 2004 y 2012)
                        categoria= 'B'
                        break
                    elif(modelo >= 2012):
                        # (A)=GAMA ALTA=(modelo 2012 o superior hasta el año actual inlcuido)
                        categoria= 'A'
                        break
                    else:
                        categoria='N'
                        break
            except ValueError:
                print("Debes escribir un número para el modelos del auto.")
        while True:
            print('F (FULL): aire acondicionado/calefaccion | C (SEMI-COMPLETO): sin confort habitaculo')
            servicio = input('Ingrese el tipo de servicio: ').upper()
            if (servicio != 'C'):
                if(servicio != 'F'):
                    print("Debes escribir un servicio valido para el auto.")
            else:
                break
        
registrar_auto()

# GRABA EN EL ARCHIVO .CSV ASIGNADO EN EL PATH SI NO EXISTE LO CREA
def save_archivo_csv(path):
    try:
        with open(path, "a+") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
        archivo_csv.close()
    except Exception as error:
        print("Ocurrió un error al leer el archivo CSV:", str(error))


# SOLICITA LOS DATOS DEL SOCIO, GENERA EL STRING CON FORMATO CSV Y GUARDA EN EL
# ARCHIVO USUARIOS.CSV. GUARDAR LA CLAVE CIFRADA CON LA FUNCIÓN SHA256()
def cargar_socio():
    print('carga socio')
    pass


