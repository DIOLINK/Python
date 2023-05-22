# Dados como datos 10 números enteros (se ingresan por teclado), obtener la suma de los números impares y el promedio de los números pares.

print('Dados como datos 10 números enteros (se ingresan por teclado), obtener la suma de los números impares y el promedio de los números pares.')

IS_EJECTED=True

contador = 0
contador_pares=0
suma_impares=0
suma_pares=0

while contador < 10:
      try:
        value = int(input('Ingrese un numero: '))
      except ValueError:
        print("Debes escribir un número.")
        IS_EJECTED = False
      if IS_EJECTED:

          if(value % 2 == 0):
              contador_pares+=1
              suma_pares+=value
          else:
              suma_impares+=value
      contador+=1

print(f'La suma de los números impares es: {suma_impares} y el promedio de los números pares es: {suma_pares / contador_pares}')