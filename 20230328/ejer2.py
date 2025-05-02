# Realizar el procedimiento inverso al 1: Mostrar cuántos días, horas, minutos y segundos representa una cantidad de segundos ingresados por consola.

# variables estaticas | constantes
DAYS_SECONDS = 86400  # 1 DIA => 24 HORA => 1440 MINUTOS => 86400 SEGUNDOS 
HOURS_SECONDS = 3600  # 1 HORA => 60 MINUTOS => 3600 SEGUNDOS
MINUTES_SECONDS = 60  # 1 MINUTO => 60 SEGUNDOS

print('EJ: 3 días, 10 horas, 20 minutos, 7 segundos son 296407 segundos')
totalSeconds = int(input('Ingresar la cantidad en segundos: '))

days = totalSeconds // DAYS_SECONDS
hours = (totalSeconds - (days * DAYS_SECONDS)) // HOURS_SECONDS
minutes = (totalSeconds - (hours * HOURS_SECONDS) - (days * DAYS_SECONDS)) // MINUTES_SECONDS
seconds = (totalSeconds - (minutes * MINUTES_SECONDS) - (hours * HOURS_SECONDS) - (days * DAYS_SECONDS))

print('La cantidad de Dias es:', days, 'la cantidad de Horas es:', hours,
      'la cantidad de Minutos:', minutes, 'la cantidad de Segundos:', seconds)
