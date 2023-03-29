# Calcule la superficie y el volúmen de una esfera, ingresando su radio.
print('Calcule la superficie y el volúmen de una esfera, ingresando su radio.')

import math

radio = int(input('Ingresar el radio: '))

volumen = (4/3)*(math.pi * radio**3 )
superficie = 4*(math.pi * radio**2 )

print('Volumen:', volumen)
print('Superficie:', superficie )
