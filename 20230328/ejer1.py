# Ingresar dias, horas, minutos y segundos mostrar los segundos totales
# EJ: 3 días, 10 horas, 20 minutos, 7 segundos son 296407 segundos

# (days * DAYS_SECONDS) = SEGUNDOS | days = (SEGUNDOS // DAYS_SECONDS) =>
# ((days * DAYS_SECONDS) // DAYS_SECONDS) = days * (DAYS_SECONDS // DAYS_SECONDS) = days * 1 = days

# Funcion sin Parametros
def cambiar_dias_horas_minutos_segundos_a_segundos():
    # variables estaticas | constantes
    DAYS_SECONDS = 86400  # 1 DIA => 24 HORA => 1440 MINUTOS => 86400 SEGUNDOS
    HOURS_SECONDS = 3600  # 1 HORA => 60 MINUTOS => 3600 SEGUNDOS
    MINUTES_SECONDS = 60  # 1 MINUTO => 60 SEGUNDOS

    print('Ejer1')

    days = int(input('Ingresar la cantidad de dias: '))
    hours = int(input('Ingresar la cantidad de horas: '))
    minutes = int(input('Ingresar la cantidad de minutos: '))
    seconds = int(input('Ingresar la cantidad de segundos: '))

    totalSeconds = (days * DAYS_SECONDS) + (hours * HOURS_SECONDS) + \
        (minutes * MINUTES_SECONDS) + seconds

    print('Total de segundos:', totalSeconds)
    print(f'{days} días, {hours} horas, {minutes} minutos, {
          seconds} segundos son {totalSeconds} segundos')


# cambiar_dias_horas_minutos_segundos_a_segundos()

# Función sin parametros
def get_params():
    days = int(input('Ingresar la cantidad de dias: '))
    hours = int(input('Ingresar la cantidad de horas: '))
    minutes = int(input('Ingresar la cantidad de minutos: '))
    seconds = int(input('Ingresar la cantidad de segundos: '))

    # retorno un diccionarios con los valores de {days,hours,minutes,seconds}
    # diccionario es un objeto tipo diccionario el cual esta conformado por una {[Key:string]: value}
    # return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}
    # return (days,  hours,  minutes,  seconds) => Tupla=(days, hours, minutes, seconds) => Tupla[0]=days
    return (days,  hours,  minutes,  seconds)

# Función con parametros
def cambiar_dias_horas_minutos_segundos_a_segundos(param):
    # variables estaticas | constantes
    DAYS_SECONDS = 86400  # 1 DIA => 24 HORA => 1440 MINUTOS => 86400 SEGUNDOS
    HOURS_SECONDS = 3600  # 1 HORA => 60 MINUTOS => 3600 SEGUNDOS
    MINUTES_SECONDS = 60  # 1 MINUTO => 60 SEGUNDOS

    print('Ejer1')

    totalSeconds = (param[0] * DAYS_SECONDS) + (param[1] * HOURS_SECONDS) + \
        (param[2] * MINUTES_SECONDS) + param[3]

    print('Total de segundos:', totalSeconds)
    print(f'{param[0]} días, {param[1]} horas, {param[2]} minutos, {param[3]} segundos son {totalSeconds} segundos')


# params = get_params()
# cambiar_dias_horas_minutos_segundos_a_segundos(params['days'], params['hours'], params['minutes'], params['seconds'])

cambiar_dias_horas_minutos_segundos_a_segundos(get_params())
