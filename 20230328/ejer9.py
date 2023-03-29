# Para calcular la distancia entre dos puntos en la superficie de la tierra hay que considerar que la diferencia entre grados de longitud varía según la latitud; si t1 y g1 son latitud y longitud de un punto y t2 y g2 son latitud y longitud de otro punto la distancia en kilómetros entre ambos puntos estará dada por:

import math

print('Para calcular la distancia entre dos puntos en la superficie de la tierra hay que considerar que la diferencia entre grados de longitud varía según la latitud; si t1 y g1 son latitud y longitud de un punto y t2 y g2 son latitud y longitud de otro punto la distancia en kilómetros entre ambos puntos estará dada por:')

longitud1 = math.radians(int(input('Ingresar longitud 1: ')))
latitud1 = math.radians(int(input('Ingresar latitud 2: ')))
longitud2 = math.radians(int(input('Ingresar longitud 2: ')))
latitud2 = math.radians(int(input('Ingresar latitud 2: ')))

sinLatitud1 = math.sin(latitud1)
sinLatitud2 = math.sin(latitud2)

cosLatitud1 = math.cos(latitud1)
cosLatitud2 = math.cos(latitud2)
cosLongitud12 = math.cos(longitud1 - longitud2)

value= 6371.01 * math.acos((sinLatitud1 * sinLatitud2) +
(cosLatitud1 * cosLatitud2 * cosLongitud12))

print('La distancia entre dos puntos:', value)