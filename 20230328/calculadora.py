# Hacer un programa para calcular el jornal de operarios. Se ingresan por
# consola: categoría, horas trabajadas, días trabajados.
# Si son de categoría A, cobran 100 / hora y un fijo de 100 / día(máximo 30 días)
# Si son categoría B, cobran 80 / hora y un fijo de 100 / día(máximo 24 días)
# Si son categoría C, cobran 60 / hora y un fijo de 50 / día(máximo 20 días)
# El monto por día se contabiliza si en promedio se trabajaron al menos 4 hs / día durante el período informado.
# Ejemplos:
# Ingrese categoría(A / B / C): B
# Ingrese horas: 180
# Ingrese días: 30
# Monto fijo: $2400
# Monto variable: $14400
# Monto total: $16800
# ----------------------------------
# Otro ejemplo:
# Ingrese categoría(A / B / C): C
# Ingrese horas: 100
# Ingrese días: 30
# Monto fijo: $0 - trabaja menos de 4hs promedio
# Monto variable: $6000
# Monto total: $6000

calculadora = True
categoria_A = "A"
categoria_B = "B"
categoria_C = "C"
CATEGORIA_A_COBRAN = 100
CATEGORIA_B_COBRAN = 80
CATEGORIA_C_COBRAN = 60
CATEGORIA_A_MAX_DIAS = 30
CATEGORIA_B_MAX_DIAS = 24
CATEGORIA_C_MAX_DIAS = 20
CATEGORIA_A_B_FIJO_HORAS = 100
CATEGORIA_C_FIJO_HORAS = 50


def get_horas_dias():
    MIN_HORAS_DIA = 4
    horas_trabajadas = int(input("Ingrese horas trabajadas: "))
    dias_trabajados = int(input("Ingrese dias trabajados: "))
    minimo_horas_dias = (horas_trabajadas / dias_trabajados) >= MIN_HORAS_DIA
    return {'horas_trabajadas': horas_trabajadas, 'dias_trabajados': dias_trabajados, 'minimo_horas_dias': minimo_horas_dias}


def mostrar_respuesta(categoria, horas_trabajadas, dias_trabajados, mensaje_error):
    respuesta = f'''
        {mensaje_error}
        Ingrese categoría(A / B / C): {categoria}
        Ingrese horas: {horas_trabajadas}
        Ingrese días: {dias_trabajados}
        Monto fijo: $0
        Monto variable: $0
        Monto total: $0
        '''
    print(respuesta)


while calculadora:
    mensaje_error = ''
    print('Para salir colocar S en categoria.')
    categoria = input("Ingrese su categoria ( A | B | C ): ")
    if categoria.upper() == "S":
        print('Chaito...')
        calculadora = False
    else:
        values = get_horas_dias()
        if not values['minimo_horas_dias']:
            mensaje_error = 'trabaja menos de 4hs promedio'
        elif categoria.upper() == "A":
            if values['dias_trabajados'] <= CATEGORIA_A_MAX_DIAS:
                if values['dias_trabajados'] <= CATEGORIA_A_B_FIJO_HORAS:
                    print('Categoria A hacer las cuentitas')
                else:
                    mensaje_error = f'Las horas trabajadas no son los minimos para la Catetegoria: {
                        categoria.upper()}.'
            else:
                mensaje_error = f'Los dias trabajados supera al maximo para la Catetegoria: {
                    categoria.upper()}.'
        elif categoria.upper() == "B":
            if values['dias_trabajados'] <= CATEGORIA_B_MAX_DIAS:
                if values['dias_trabajados'] <= CATEGORIA_A_B_FIJO_HORAS:
                    print('Categoria B hacer las cuentitas')
                else:
                    mensaje_error = f'Las horas trabajadas no son los minimos para la Catetegoria: {
                        categoria.upper()}.'
            else:
                mensaje_error = f'Los dias trabajados supera al maximo para la Catetegoria: {
                    categoria.upper()}.'
        elif categoria.upper() == "C":
            if values['dias_trabajados'] <= CATEGORIA_C_MAX_DIAS:
                if values['dias_trabajados'] <= CATEGORIA_C_FIJO_HORAS:
                    print('Categoria C hacer las cuentitas')
                else:
                    mensaje_error = f'Los dias trabajados supera al maximo para la Catetegoria: {
                        categoria.upper()}.'
            else:
                mensaje_error = f'Los dias trabajados no son los minimos para la Catetegoria: {
                    categoria.upper()}.'
        else:
            mensaje_error = 'Categoria incorrecta.'
        mostrar_respuesta(
            categoria, values['horas_trabajadas'], values['dias_trabajados'], mensaje_error)
