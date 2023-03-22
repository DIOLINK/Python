# Ingresar dias, horas, minutos y segundos mostrar los segundos totales

DAYS_SECONDS = 86400
HOURS_SECONDS =3600
MINUTES_SECONDS =60

days = int(input('Ingresar la cantidad de dias: '))
hours = int(input('Ingresar la cantidad de horas: '))
minutes = int(input('Ingresar la cantidad de minutos: '))
seconds = int(input('Ingresar la cantidad de segundos: '))

totalSeconds = (days * DAYS_SECONDS) + (hours * HOURS_SECONDS) + (minutes * MINUTES_SECONDS) + seconds

print('Total de segundos:',totalSeconds)
