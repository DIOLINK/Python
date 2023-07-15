import csv
import os

import helpers
import login

# VALIDAR Y CREAR EL DIRECTORIO SI NO EXISTE


def mkdir_dir(_output_dir):
    response = True
    if not os.path.exists(_output_dir):
        try:
            os.makedirs(_output_dir)
            print(f"El directorio '{_output_dir}' ha sido creado.")
        except OSError as error:
            print(f"Error al crear el directorio '{_output_dir}': {error}")
            response = False
    elif not os.path.isdir(_output_dir):
        print(f"'{_output_dir}' no es un directorio válido.")
        response = False
    elif not os.access(_output_dir, os.W_OK):
        print(f"No tienes permisos de escritura en '{_output_dir}'.")
    else:
        print("El directorio es válido y tienes permisos de escritura.")
    return response


# print(mkdir_dir('.//data'))
# GRABA EN EL ARCHIVO .CSV ASIGNADO EN EL PATH SI NO EXISTE LO CREA


def save_archivo_csv(path, _datos):
    try:
        with open(path, "a+", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            for row in _datos:
                escritor_csv.writerow(row)
            archivo_csv.close()
            print("Los datos se guardaron con exito...")
    except Exception as error:
        print("Ocurrió un error al leer el archivo CSV:", str(error))


def modificar_valores_csv(path, _email, _clave, nuevos_datos_socio):
    # CREAR UN ARCHIVO TEMPORAL PARA PODER USARLO DESPUES.
    archivo_csv_temporal = path + '.temp'
    try:
        with open(path, 'r') as archivo_csv, open(archivo_csv_temporal, 'w', newline='') as archivo_temp:
            lector_csv = csv.reader(archivo_csv)
            escritor_csv = csv.writer(archivo_temp)
            for lista_fila in lector_csv:
                if login.comparar_lista(lista_fila, _email, _clave):
                    # EMAIL
                    lista_fila[0] = nuevos_datos_socio[0]
                    # CLAVE
                    lista_fila[1] = nuevos_datos_socio[1]
                    # NOMBRE
                    lista_fila[3] = nuevos_datos_socio[2]
                    # APELLIDO
                    lista_fila[4] = nuevos_datos_socio[3]
                    # PATENTE
                    lista_fila[6] = nuevos_datos_socio[4]
                escritor_csv.writerow(lista_fila)
        # REEMPLAZAR EL ARCHIVO ORIGINAL POR EL ARCHIVO TEMPORAL
        os.replace(archivo_csv_temporal, path)
        print("Valores modificados exitosamente.")
        archivo_csv.close()
        archivo_temp.close()
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception as error_procesar_lineas:
        print("Ocurrió un error al leer el archivo CSV:",
              str(error_procesar_lineas))


def procesar_viajes_csv(path, porcentual_ganacia):
    meses_unicos_set = []
    ganancias_meses = []
    meses = []
    ganancias = []
    try:
        with open(path, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for lista_fila in lector_csv:
                if lista_fila[0].split('-')[1] not in meses_unicos_set:
                    meses_unicos_set.append(lista_fila[0].split('-')[1])
                    meses.append(helpers.buscar_mes_nombre(
                        int(lista_fila[0].split('-')[1])))
                ganancias_meses.append(
                    [lista_fila[0].split('-')[1], lista_fila[5]])
            archivo_csv.close()
        for list_meses_unicos in meses_unicos_set:
            total_mes = 0
            for list_ganancias in ganancias_meses:
                if list_ganancias[0] == list_meses_unicos:
                    total_mes += float(list_ganancias[1]) * porcentual_ganacia
            ganancias.append(round(total_mes, 2))
        return [meses, ganancias]
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception as error_procesar_lineas:
        print("Ocurrió un error al leer el archivo CSV:",
              str(error_procesar_lineas))
