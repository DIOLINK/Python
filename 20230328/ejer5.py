# Calcule la superficie y el volúmen de una esfera, ingresando su radio.
print('Calcule la superficie y el volúmen de una esfera, ingresando su radio.')

import math
# Obtener la informacion del radio para ser usada en otra funcion.
# radio = int(input('Ingresar el radio: '))

# Con el radio obtenido de la funcion anterior calculamos el volúmen y la superficie de una esfera.
# volumen = (4/3)*(math.pi * radio**3 )
# superficie = 4*(math.pi * radio**2 )

# Se imprime por terminal el resultado del calculo del volúmen y la superficie de una esfera.
# print('Volumen:', volumen)
# print('Superficie:', superficie )
casa= 'mi casa'

def show_volumen_superficie(value):
  print('Volumen:', value['volumen'])
  print('Superficie:', value['superficie'])

def get_radio():
  radio = float(input('Ingresar el radio: '))
  return radio

def calculo_volumen_superficie(radio):
  volumen = (4/3)*(math.pi * radio**3 )
  superficie = 4*(math.pi * radio**2 )
  # diccionario => {'volumen': volumen, 'superficie': superficie}
  return {'volumen': volumen, 'superficie': superficie}


show_volumen_superficie(calculo_volumen_superficie(get_radio()))

# respuesta1 = get_radio()
# respuesta2 = calculo_volumen_superficie(respuesta1)
# show_volumen_superficie(respuesta2)

