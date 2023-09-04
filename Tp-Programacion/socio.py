import traceback
from datetime import datetime
from hashlib import sha256

import admin
import fileCsv
import filePdf
import getch
import matplotlib.pyplot as plt
import pwinput
import sistema
from geopy import distance
from geopy.geocoders import Nominatim

titulo = "MENU DEL SOCIO CONDUCTOR"
opcion = 0
opciones = "1. DAR DE ALTA VIAJE\n2. MODIFICAR DATOS PERSONALES\n3. VER GANANCIAS\n4. SALIR"

# LLAMA A LA FUNCION DE MENU PRINCIPAL


def volver_menu_sistem():
    sistema.main()
    exit()

# ESTA FUNCIÓN MUESTRA EL MENÚ AL USUARIO QUE SE LOGEA COMO SOCIO Y LLAMA
# A LA FUNCIÓN QUE CORRESPONDA PARA PROCESAR LA OPCION SELECCIONADA


def mostrar_menu():
    print(" *" * (len(titulo) + 4))
    print(titulo.center(len(titulo)+30))
    print(" *" * (len(titulo) + 4))
    opcion = 0
    while True:
        print(opciones)
        try:
            opcion = int(input("Seleccione una de las opción (1-4): "))
            if ((opcion < 0) or (opcion > 4)):
                print('Este numero de opcion:', opcion, 'no es correcto.')
            else:
                match opcion:
                    case 1: cargar_viaje()
                    case 2: modificar_datos_personales()
                    case 3: consultar_ganancia()
                    case 4: volver_menu_sistem()
        except ValueError:
            print("Debes escribir un numero de opcion valido.")

# VUELVE AL MENU ANTERIOR


def volver_menu():
    print("Volviendo al Menu...")
    mostrar_menu()
    exit()

# MODIFICAR DATOS PERSONALES


def modificar_datos_personales():
    titulo = "MENU DE MODIFICACIONES DE LOS DATOS PERSONALES"
    print(" *" * (len(titulo) + 4))
    print(titulo.center(len(titulo)+50))
    print(" *" * (len(titulo) + 4))
    nuevos_datos_socio = []
    while True:
        # VERIFICAR SI SE PRESIONÓ LA TECLA "ESC"
        print("Presione intro para continuar o Esc para guardar los cambios o volver al menu anterior...")
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            if (len(nuevos_datos_socio) != 0):
                # LA FUNCION RECIBE COMO PARAMETRO EL DATO A GUARDAR EN EL ARCHIVO VIAJES.CSV
                # DATO ES UN STRING CON EL FORMATO CSV
                while True:
                    confirm = input(
                        'Desea guardar los datos ingresados [y/n]: ').lower()
                    if (confirm == 'y'):
                        if (fileCsv.mkdir_dir('.//data/')):
                            fileCsv.modificar_valores_csv(
                                './/data//usuarios.csv', old_email, old_clave, nuevos_datos_socio)
                        volver_menu()
                    elif (confirm == 'n'):
                        print('No se guardaron los datos.')
                        volver_menu()
            else:
                volver_menu()
        old_email = input("Ingresar mail anterior: ").lower()
        nuevo_email = input('Ingrese su nuevo email: ').lower()
        # REMPLAZA LOS LETRAS CON *
        old_clave = pwinput.pwinput(prompt='Ingresar la clave vieja: ')
        nueva_clave = sha256(
            input('Ingrese la nueva contraseña: ').encode('utf-8')).hexdigest()
        nuevo_nombre = input('Ingrese su nombre: ').lower()
        nuevo_apellido = input('Ingrese su apellido: ').lower()
        while True:
            nueva_patente = input('Ingrese la patente (LLLNNN o LLNNNLL): ')
            if admin.validar_patente(nueva_patente) == -1:
                print('Patente invalida.')
            else:
                break
        nuevos_datos_socio.append(nuevo_email)
        nuevos_datos_socio.append(nueva_clave)
        nuevos_datos_socio.append(nuevo_nombre)
        nuevos_datos_socio.append(nuevo_apellido)
        nuevos_datos_socio.append(nueva_patente)

# GENERAR PRIMERO EL GRÁFICO DE LINEAS Y A CONTINUACION
# CREAR EL ARCHIVO PDF
# LA FUNCIÓN RECIBE COMO PARÁMETROS LA LISTA CON LOS NOMBRES DE
# LOS MESES PROCESADOS Y LAS GANANCIAS DE LOS MISMOS


def generar_grafico(meses, ganancias):
    # Create a figure containing a single axes.
    plt.xlabel('MESES')
    plt.ylabel('$ - GANANCIAS MENSUALES')
    plt.plot(meses, ganancias)  # Plot some data on the axes.
    plt.title('Gráfico de ganancias por mes')
    image_path = f'./images/grafico_socios.png'
    if (fileCsv.mkdir_dir('.//images/')):
        plt.savefig(image_path)
    plt.show()
    pdf_path = './pdf/grafico_linel.pdf'
    if (fileCsv.mkdir_dir('.//pdf/')):
        pdf = filePdf.PDF()
        pdf.add_page()
        pdf.chapter_title(f'Ganancias total: ${sum(ganancias)}')
        pdf.chapter_body(image_path)
        pdf.output(pdf_path)
# ABRIR EL ARCHIVO VIAJES.CSV Y PROCESAR EL MISMO
# DEL PROCESAMIENTO, DEBO IR SACANDO LOS NOMBRES DE LOS MESES (USAR FUNCION BUSCAR_MES_NOMBRE())
# PARA ESTO, SE LEE CON UN FOR CADA UNA DE LAS LIENAS DEL ARCHIVO Y CON LA FUNCION SPLIT VOY
# SACANDO LOS DATOS QUE NECESITO
# OBTENER LAS GANANCIAS DE CADA MES. GUARDAR LOS DATOS EN LA LISTA PARA LUEGO GENERAR GRÁFICO Y PDF


def consultar_ganancia():
    # LUEGO DEL PROCESAMIENTO DEL ARCHIVO, LLAMAR A LA FUNCION GENERAR_GRAFICO()
    # PARA CREAR ARCHIVOS PDF E IMAGEN DE GRÁFICO
    GANANCIA_SOCIOS = 0.7
    if (fileCsv.mkdir_dir('.//data/')):
        respuesta = fileCsv.procesar_viajes_csv(
            './/data//viajes.csv', GANANCIA_SOCIOS)
        generar_grafico(respuesta[0], respuesta[1])

# CALCULA COSTO DE LAS DISTANCIAS


def calcular_costo_distancia(distancia_km):
    monto_minimo = 370
    monoto_incremento = 95
    distancia_base_km = 3
    EXEDIDO = 1.5

    if distancia_km <= distancia_base_km:
        costo = monto_minimo
    else:
        distancia_excedida_km = distancia_km - distancia_base_km
        incrementos_adicionales = distancia_excedida_km / EXEDIDO
        costo = monto_minimo + (incrementos_adicionales * monoto_incremento)

    return costo


def cargar_viaje():
    list_viajes = []
    titulo = "CARGA DE VIAJES"
    print(" *" * (len(titulo) + 4))
    print(titulo.center(len(titulo)+20))
    print(" *" * (len(titulo) + 4))
    while True:
        registro_viaje = []
        # VERIFICAR SI SE PRESIONÓ LA TECLA "ESC"
        print("Presione intro para continuar o Esc para guardar los cambios y volver al menu anterior...")
        tecla = getch.getch()
        if tecla.lower() == chr(27):
            if (len(list_viajes) != 0):
                # LA FUNCION RECIBE COMO PARAMETRO EL DATO A GUARDAR EN EL ARCHIVO VIAJES.CSV
                # DATO ES UN STRING CON EL FORMATO CSV
                while True:
                    confirm = input(
                        'Desea guardar los datos ingresados [y/n]: ').lower()
                    if (confirm == 'y'):
                        if (fileCsv.mkdir_dir('.//data/')):
                            fileCsv.save_archivo_csv(
                                ".//data//viajes.csv", list_viajes)
                            volver_menu()
                    elif (confirm == 'n'):
                        print('No se guardaron los datos.')
                        volver_menu()
            else:
                volver_menu()
        # CARGA LA FECHA (AAAA/MM/DD) Y LA HORA (HH:MM) ACTUAL
        fecha_hora_actual = datetime.now()
        fecha = fecha_hora_actual.strftime("%Y-%m-%d")
        registro_viaje.append(fecha)
        # CARGA Y LA HORA (HH:MM) ACTUAL
        hora = fecha_hora_actual.strftime("%H:%M")
        registro_viaje.append(hora)
        # SOLICITAR AL USUARIO LAS DIRECCIONES DE ORIGEN Y DESTINO
        dir_inicio = input('Ingrese direccion inicio: ')
        registro_viaje.append(dir_inicio)
        dir_destino = input('Ingrese direccion destino: ')
        registro_viaje.append(dir_destino)
        print("PROCESANDO...")
        # DEBE ESTAR ESTA LÍNEA PARA
        geolocator = Nominatim(user_agent="http", timeout=10000)
        # LLAMAR A geolocator.geocode(direccion) PARA QUE DEVUELVE LAS COORDENADAS DE LA DIRECCION
        # DE ORIGEN Y TAMBIEN DE DESTINO
        try:
            location_ini = geolocator.geocode(dir_inicio)
            tupla_location_ini = (location_ini.latitude,
                                  location_ini.longitude)
            location_des = geolocator.geocode(dir_destino)
            tupl_location_des = (location_des.latitude, location_des.longitude)
        except Exception:
            print(traceback.format_exc())
        # CALCULAR LA DISTANCIA Y QUE NO TIRE ERRORES
        # LLAMAR A LA FUNCION geodesic DONDE DEBERÁ DEVOLVER LA DISTANCIA ENTRE ORIGEN Y DESTINO EN km
        distancia_recorida = distance.distance(
            tupla_location_ini, tupl_location_des).km
        registro_viaje.append(distancia_recorida)
        print("%.3f" % distancia_recorida, 'Km')
        print("UBICACIÓN RECIBIDA OK")
        registro_viaje.append(calcular_costo_distancia(distancia_recorida))
        # VALIDA LA PATENTE
        while True:
            patente = input('Ingrese la patente (LLLNNN o LLNNNLL): ')
            if admin.validar_patente(patente) == -1:
                print('Patente invalida.')
            else:
                registro_viaje.append(patente)
                break
        list_viajes.append(registro_viaje)
