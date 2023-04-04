# Ingresar dias, horas, minutos y segundos mostrar los segundos totales
print('Ingresar dias, horas, minutos y segundos mostrar los segundos totales.')

DAYS_SECONDS = 86400
HOURS_SECONDS = 3600
MINUTES_SECONDS = 60
IS_EJECTED = True

try:
    days = int(input('Ingresar la cantidad de dias: '))
    hours = int(input('Ingresar la cantidad de horas: '))
    minutes = int(input('Ingresar la cantidad de minutos: '))
    seconds = int(input('Ingresar la cantidad de segundos: '))
except ValueError:
    print("Debes escribir un número.")
    IS_EJECTED = False

if IS_EJECTED:
    totalSeconds = (days * DAYS_SECONDS) + (hours * HOURS_SECONDS) + (minutes * MINUTES_SECONDS) + seconds
    print('Total de segundos:',totalSeconds)
