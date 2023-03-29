# Realizar el procedimiento inverso al 1: Mostrar cuántos días, horas, minutos y segundos representa una cantidad de segundos ingresados por consola.

DAYS_SECONDS = 86400
HOURS_SECONDS =3600
MINUTES_SECONDS =60

totalSeconds = int(input('Ingresar la cantidad en segundos: '))

days = totalSeconds // DAYS_SECONDS
hours = (totalSeconds - (days * DAYS_SECONDS) )// HOURS_SECONDS
minutes = (totalSeconds - (hours * HOURS_SECONDS) - (days * DAYS_SECONDS)) // MINUTES_SECONDS
seconds = (totalSeconds - (minutes * MINUTES_SECONDS) - (hours * HOURS_SECONDS) - (days * DAYS_SECONDS))

print('La cantidad de Dias es:', days,'la cantidad de Horas es:', hours,'la cantidad de Minutos:', minutes,'la cantidad de Segundos:', seconds)