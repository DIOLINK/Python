# LA FUNCION RECIBE UN NUMERO ENTERO QUE ES EL NÚMEO DE MES
# LA FUNCIÓN DEVUELVE EL NOMBRE DEL MES
def buscar_mes_nombre(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if ((numero_mes >= 1) and (numero_mes <= 12)):
        nombre_mes = meses[numero_mes - 1]
        return nombre_mes
    else:
        print("Número de mes inválido")
        return ""
