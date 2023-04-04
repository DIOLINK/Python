# Nuestro vecino, pintor, nos pide ayuda para calcular cuántas latas de pintura tiene que comprar.

print('Nuestro vecino, pintor, nos pide ayuda para calcular cuántas latas de pintura tiene que comprar.')

SUPERFICE_LITRO_PINTURA = 3
LITROS_PINTURA = 20
IS_EJECTED = True

try:
    superfice = int(input('Ingresar los metros cuadrados que desea pintar: '))
except ValueError:
      print("Debes escribir un número.")
      IS_EJECTED = False

if IS_EJECTED:
    cantidad_litros_pintura = superfice / SUPERFICE_LITRO_PINTURA
    cantidad_latas_pintura = cantidad_litros_pintura / LITROS_PINTURA
    print('latas de 20 Litros necesitas:',cantidad_latas_pintura, ' latas')