# Convertir una distancia en Km a metros, pulgadas, yardas y millas.
print('Convertir una distancia en Km a metros, pulgadas, yardas y millas.')

KM_YARDAS = 1093.31
KM_MILLAS = 0.621371
KM_PULGADAS = 39370.1
KM_METROS = 1000

kilometros = int(input('Ingresar la cantidad en kilometros: '))

yardas = kilometros * KM_YARDAS
millas = kilometros * KM_MILLAS
pulgadas = kilometros * KM_PULGADAS
metros = kilometros * KM_METROS

print(kilometros,'Representa en Yardas:',yardas)
print(kilometros,'Representa en Millas:',millas)
print(kilometros,'Representa en Pulgadas:',pulgadas)
print(kilometros,'Representa en Metros:',metros)