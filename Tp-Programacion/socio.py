from datetime import datetime


from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import matplotlib.pyplot as plt
from fpdf import FPDF



titulo = "MENU DEL SOCIO CONDUCTOR"
opcion = ""
opciones = "1. DAR DE ALTA VIAJE\n2. MODIFICAR DATOS PERSONALES\n3. VER GANANCIAS\n4. SALIR"


# LA FUNCION RECIBE UN NUMERO ENTERO QUE ES EL NÚMEO DE MES
# LA FUNCIÓN DEVUELVE EL NOMBRE DEL MES
def buscar_mes_nombre(indice):
    pass
    
    

# GENERAR PRIMERO EL GRÁFICO DE LINEAS Y A CONTINUACION
# CREAR EL ARCHIVO PDF
# LA FUNCIÓN RECIBE COMO PARÁMETROS LA LISTA CON LOS NOMBRES DE
# LOS MESES PROCESADOS Y LAS GANANCIAS DE LOS MISMOS
def generar_grafico(meses, ganancias):
    pass
 


# ABRIR EL ARCHIVO VIAJES.CSV Y PROCESAR EL MISMO
# DEL PROCESAMIENTO, DEBO IR SACANDO LOS NOMBRES DE LOS MESES (USAR FUNCION BUSCAR_MES_NOMBRE())
# PARA ESTO, SE LEE CON UN FOR CADA UNA DE LAS LIENAS DEL ARCHIVO Y CON LA FUNCION SPLIT VOY
# SACANDO LOS DATOS QUE NECESITO
# OBTENER LAS GANANCIAS DE CADA MES. GUARDAR LOS DATOS EN LA LISTA PARA LUEGO GENERAR GRÁFICO Y PDF
def consultar_ganancia():

    meses = []
    ganancias = []

    # LUEGO DEL PROCESAMIENTO DEL ARCHIVO, LLAMAR A LA FUNCION GENERAR_GRAFICO()
    # PARA CREAR ARCHIVOS PDF E IMAGEN DE GRÁFICO
    
    generar_grafico(meses, ganancias)
    



# LA FUNCION RECIBE COMO PARAMETRO EL DATO A GUARDAR EN EL ARCHIVO VIAJES.CSV
# DATO ES UN STRING CON EL FORMATO CSV
def registrar_viaje(dato):
    pass

def cargar_viaje():
    print("Datos del viaje: ")
    # SOLICITAR AL USUARIO LAS DIRECCIONES DE ORIGEN Y DESTINO 
  

    print("PROCESANDO...")

    geolocator = Nominatim(user_agent="http", timeout=10000) # DEBE ESTAR ESTAR LÍNEA PARA
    # CALCULAR LA DISTANCIA Y QUE NO TIRE ERRORES

    # LLAMAR A geolocator.geocode(direccion) PARA QUE DEVUELVE LAS COORDENADAS DE LA DIRECCION
    # DE ORIGEN Y TAMBIEN DE DESTINO
    print("UBICACIÓN RECIBIDA OK")
    
    # LLAMAR A LA FUNCION geodesic DONDE DEBERÁ DEVOLVER LA DISTANCIA ENTRE ORIGEN Y DESTINO EN km

    # CALCULAR EL PRECIO
    precio = 0
   
    # TOMAR LA FECHA ACTUAL CON  datetime.now().strftime()

    # FORMAR EL STRING PARA GUARDAR EN ARCHIVO VIAJES.CSV CON EL FORMATO SOLICITADO

    # LLAMAR A LA FUNCIÓN registrar_viaje()



# ESTA FUNCIÓN MUESTRA EL MENÚ AL USUARIO QUE SE LOGEA COMO SOCIO Y LLAMA
# A LA FUNCIÓN QUE CORRESPONDA PARA PROCESAR LA OPCION SELECCIONADA
def mostrar_menu():
    print(" *" * (len(titulo) + 4))
    print(titulo.center(len(titulo)+30))
    print(" *" * (len(titulo) + 4))

    print(opciones)
    opcion = input("Seleccionar una opción:")

    while opcion != "4":
        pass




