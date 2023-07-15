
from datetime import datetime
from hashlib import sha256

import getch
import matplotlib.pyplot as plt_admin

import fileCsv
import filePdf
import sistema

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

    while True:
        print(opciones)
        try:
            opcion = int(input("Seleccione una de las opción (1-4): "))
            if ((opcion < 0) or (opcion > 4)):
                print('Este numero de opcion:', opcion, 'no es correcto.')
            else:
                match opcion:
                    case 1: registrar_auto()
                    case 2: cargar_socio()
                    case 3: mostrar_ganancia_admin()
                    case 4: volver_menu_sistem()
        except ValueError:
            print("Debes escribir un numero de opcion valido.")

# VELVE AL MENU ANTERIOR


def volver_menu():
    print("Volviendo al Menu...")
    mostrar_menu()
    exit()

# GENERAR PRIMERO EL GRÁFICO DE TORTAS Y A CONTINUACION
# CREAR EL ARCHIVO PDF
# LA FUNCIÓN RECIBE COMO PARÁMETROS LA LISTA CON LOS NOMBRES DE
# LOS MESES PROCESADOS Y LOS PORCENTAJES CON LAS GANANCIAS DE CADA MES


def generar_grafico(meses, ganancias):

    fig, ax = plt_admin.subplots(
        figsize=(10, 7),  subplot_kw=dict(aspect="equal"))

    wedges, texts, autotexts = ax.pie(
        ganancias, labels=meses, autopct='%1.1f%%', pctdistance=1.2, labeldistance=.6)
    ax.legend(wedges, meses,
              title="Meses",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    plt_admin.setp(autotexts, size=10, weight="bold")
    fecha_hora_actual = datetime.now()
    fecha = fecha_hora_actual.strftime("%Y%m%d")
    hora = fecha_hora_actual.strftime("%H:%M")
    image_path = './images/grafico_torta.png'
    plt_admin.savefig(image_path)
    plt_admin.show()
    pdf_path = './pdf/grafico_torta.pdf'
    pdf = filePdf.PDF()
    pdf.add_page()
    pdf.chapter_title(f'Gráfico ganancias mensual - ADMINITRADOR')
    pdf.chapter_body(image_path)
    pdf.output(pdf_path)

# ABRIR EL ARCHIVO VIAJES.CSV Y PROCESAR EL MISMO
# DEL PROCESAMIENTO, DEBO IR SACANDO LOS NOMBRES DE LOS MESES (USAR FUNCION BUSCAR_MES_NOMBRE())
# PARA ESTO, SE LEE CON UN FOR CADA UNA DE LAS LIENAS DEL ARCHIVO Y CON LA FUNCION SPLIT VOY
# SACANDO LOS DATOS QUE NECESITO
# OBTENER LAS GANANCIAS DE CADA MES Y LUEGO CALCULAR EL PORCENTAJE DE CADA UNO RESPECTO DEL TOTAL.
# GUARDAR LOS DATOS EN LA LISTA PARA LUEGO GENERAR GRÁFICO Y PDF


def mostrar_ganancia_admin():
    GANANCIA_EMPRESA = 0.3
    if (fileCsv.mkdir_dir('.//data/')):
        resouesta = fileCsv.procesar_viajes_csv(
            './/data//viajes.csv', GANANCIA_EMPRESA)
        generar_grafico(resouesta[0], resouesta[1])

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
        if ((patente_formateada[0:3].isalpha() and patente_formateada[4:6].isdigit()) or ((patente_formateada[0:2].isalpha() and patente_formateada[3:4].isdigit()) and patente_formateada[5:6].isalpha())):
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
    while True:
        registro_auto = []
        # VERIFICAR SI SE PRESIONÓ LA TECLA "ESC"
        print("Presione intro para continuar o Esc para guardar los cambios y volver al menu anterior...")
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            if (len(list_registrar_auto) != 0):
                while True:
                    confirm = input(
                        'Desea guardar los datos ingresados [y/n]: ').lower()
                    if (confirm == 'y'):
                        if (fileCsv.mkdir_dir('.//data/')):
                            fileCsv.save_archivo_csv(
                                ".//data//auto.csv", list_registrar_auto)
                    elif (confirm == 'n'):
                        print('No se guardaron los datos.')
                    volver_menu()
            else:
                volver_menu()

        while True:
            patente = input('Ingrese la patente (LLLNNN o LLNNNLL): ')
            if validar_patente(patente) == -1:
                print('Patente invalida.')
            else:
                registro_auto.append(patente)
                break

        while True:
            print('(No se puede incluir modelos de autos menores a 1995)')
            try:
                modelo = int(input('Ingrese el numero de modelo: '))
                if (modelo < 1995):
                    print('Este numero de modelo:', modelo, 'no es correcto.')
                else:
                    registro_auto.append(modelo)
                    if ((modelo > 2004) and (modelo < 2012)):
                        # (B)=GAMA BAJA=(modelo entre 2004 y 2012)
                        registro_auto.append('B')

                        break
                    elif (modelo >= 2012):
                        # (A)=GAMA ALTA=(modelo 2012 o superior hasta el año actual inlcuido)
                        registro_auto.append('A')
                        break
                    else:
                        registro_auto.append('N')
                        break
            except ValueError:
                print("Debes escribir un número para el modelos del auto.")

        while True:
            print(
                'F (FULL): aire acondicionado/calefaccion | C (SEMI-COMPLETO): sin confort habitaculo')
            servicio = input('Ingrese el tipo de servicio: ').upper()
            if ((servicio == 'C') or (servicio == 'F')):
                registro_auto.append(servicio)
                break
            if (servicio != 'C'):
                if (servicio != 'F'):
                    print("Debes escribir un servicio valido para el auto.")

        list_registrar_auto.append(registro_auto)

# SOLICITA LOS DATOS DEL SOCIO, GENERA EL STRING CON FORMATO CSV Y GUARDA EN EL
# ARCHIVO USUARIOS.CSV. GUARDAR LA CLAVE CIFRADA CON LA FUNCIÓN SHA256()


def cargar_socio():
    list_carga_socios = []
    while True:
        format_registro_socio = []
        # VERIFICAR SI SE PRESIONÓ LA TECLA "ESC"
        print("Presione intro para continuar o Esc para guardar los cambios y volver al menu anterior...")
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            if (len(list_carga_socios) != 0):
                while True:
                    confirm = input(
                        'Desea guardar los datos ingresados [y/n]: ').lower()
                    # LA FUNCION RECIBE COMO PARAMETRO EL DATO A GUARDAR EN EL ARCHIVO USUARIOS.CSV
                    if (confirm == 'y'):
                        if (fileCsv.mkdir_dir('.//data/')):
                            fileCsv.save_archivo_csv(
                                ".//data//usuarios.csv", list_carga_socios)
                            volver_menu()
                    elif (confirm == 'n'):
                        print('No se guardaron los datos.')
                    volver_menu()
            else:
                volver_menu()

        print('Datos del nuevo socio conductor:')
        nombre = input('Ingrese el nombre: ').lower()
        apellido = input('Ingrese el apellido: ').lower()
        while True:
            try:
                legajo = int(input('Ingrese el numero de legajo: '))
                break
            except ValueError:
                print("Debes escribir un número para el legajo.")
        email = input('Ingrese el email: ').lower()
        while True:
            patente = input('Ingrese la patente (LLLNNN o LLNNNLL): ')
            if validar_patente(patente) == -1:
                print('Patente invalida.')
            else:
                break
        clave = sha256(
            input('Ingrese la contraseña: ').encode('utf-8')).hexdigest()
        # SE GENERA LA ESTRUCTURA PARA DE CADA ROW DEL CSV
        format_registro_socio.append(email)
        format_registro_socio.append(clave)
        format_registro_socio.append('socio')  # 2
        format_registro_socio.append(nombre)
        format_registro_socio.append(apellido)
        format_registro_socio.append(legajo)  # 5
        format_registro_socio.append(patente)
        # SE APILAN LOS NUEVOS SOCIOS PARA LUEGO SER GRABADOS EN EL ARCHIVO USUARIOS.CSV
        list_carga_socios.append(format_registro_socio)
