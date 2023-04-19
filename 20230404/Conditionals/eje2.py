enum="""
Hacer un programa para calcular el jornal de operarios. Se ingresan por consola: categoría, horas trabajadas, días trabajados.

- Si son de categoría A, cobran 100 / hora y un fijo de 100 / día (máximo 30 días)
- Si son categoría B, cobran 80 / hora y un fijo de 100 / día (máximo 24 días)
- Si son categoría C, cobran 60 / hora y un fijo de 50 / día (máximo 20 días)
"""
print(enum)

IS_EJECTED = True

COBRAN_CATEGORIA_A = 100
COBRAN_CATEGORIA_B = 80
COBRAN_CATEGORIA_C = 60
ERROR_MESSAGE_MAX_DAY = 'La cantidad de dias supera al maximo permitido para la categoria seleccionada.'
ERROR_MESSAGE_MAX_HOUR = 'La cantidad de horas no alcanza al valor fijo permitido para la categoria seleccionada.'


category = input('Ingrese categoría (A / B / C): ')

try:
      hours = int(input('Ingresar horas: '))
      days = int(input('Ingrese días: '))
except ValueError:
      print("Debes escribir un número.")
      IS_EJECTED = False

valueTotal = 0
valueDynamic = 0
valueFixed = 0

if IS_EJECTED:
      if hours <= 0 or days <= 0:
            print("Debes escribir un número valido de días o de horas.")
            IS_EJECTED = False

      if category == 'A':
            if days > 30:
                  print(ERROR_MESSAGE_MAX_DAY)
                  if hours > 100:
                        print(ERROR_MESSAGE_MAX_HOUR)

      elif category == 'B':
            if days > 24:
                  print(ERROR_MESSAGE_MAX_DAY)
                  if hours > 100:
                        print(ERROR_MESSAGE_MAX_HOUR)
      elif category == 'C':
            if days > 20:
                  print(ERROR_MESSAGE_MAX_DAY)
                  if hours > 50:
                        print(ERROR_MESSAGE_MAX_HOUR)
      else:
            print('Error en la categoria, vuelva a intentarlo!!')

      recibo=f"""
      Ingrese categoría (A / B / C): \t{category}
      Ingrese horas: \t{hours}
      Ingrese días: \t{days}
      Monto fijo: ${valueFixed}
      Monto variable: ${valueDynamic}
      Monto total: \t${valueTotal}
      """