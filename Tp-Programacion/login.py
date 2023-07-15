import csv
from hashlib import sha256


# COMPARA LA LISTA CON LO INGRESADO.
def comparar_lista(lista_fila, _email, _clave):
    is_email = False
    is_passwd = False
    for elemento in lista_fila:
        if elemento == _email:
            is_email=True
        elif is_email and elemento == sha256(_clave.encode('utf-8')).hexdigest():
            is_passwd=is_email
    return (is_email and is_passwd)

# ESTA FUNCION RECIBE COMO PARAMETROS EL ARCHIVO A PROCESAR, EMAIL Y CLAVE A VALIDAR
# CUANDO ENCUENTRA EL USUARIO QUE COINCIDE CON LA CLAVE Y EL EMAIL. ENTONCES DEBE
# GUARDAR EL PERFIL.
# LA FUNCION DEVUELVE EL PERFIL SI LO OBTUVO
def procesar_lineas(arch, _email, _clave):
    try:
        with open(arch, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for lista_fila in lector_csv:
                if comparar_lista(lista_fila,_email, _clave):
                    archivo_csv.close()
                    return lista_fila[2].lower()
        return ''
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception as error_procesar_lineas:
        print("Ocurrió un error al leer el archivo CSV:", str(error_procesar_lineas))


# print(procesar_lineas(".//data//usuarios.csv",'socio1@gmail.com','otraclave1234*'))
# print(procesar_lineas(".//data//usuarios.csv",'admin@hotmail.com','1234*'))
# print(procesar_lineas(".//data//usuarios.csv",'admin@hotmail.com','1234'))

# RECIBE EL EMAIL Y CLAVE DEL USUARIO
# LLAMAR A LA FUNCION PROCESAR_LINEAS()
# DEVOLVER PERFIL
def validar_login(_email, _clave):
    return procesar_lineas(".//data//usuarios.csv",_email, _clave)