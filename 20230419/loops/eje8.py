# Hacer un programa que multiplique p x q mediante sumas sucesivas. (p y q se ingresan por consola)

print('Hacer un programa que multiplique p x q mediante sumas sucesivas. (p y q se ingresan por consola)')

IS_EJECTED=True
try:
    p = int(input('Ingrese P: '))
    q = int(input('Ingrese Q: '))
except ValueError:
        print("Debes escribir un número.")
        IS_EJECTED = False

if IS_EJECTED:
      acum = 0
      isNegative = False
      if (q<0):
          isNegative = not isNegative
          q*=-1
      if (p<0):
          isNegative = not isNegative
          p*=-1
      for i in range(q):
          acum+=p

      if isNegative:
          print(f'p x q => {p} x -{q} = -{acum}')
      else:
          print(f'p x q => {p} x {q} = {acum}')