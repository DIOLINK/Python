# Ingresar las ventas de 4 trimestres calcular e informar el total de ventas y el porcentaje que representa.
print('Ingresar las ventas de 4 trimestres calcular e informar el total de ventas y el porcentaje que representa.')
IS_EJECTED = True

try:
      trimestres1 = int(input('Ingresar trimentre 1: '))
      trimestres2 = int(input('Ingresar trimentre 2: '))
      trimestres3 = int(input('Ingresar trimentre 3: '))
      trimestres4 = int(input('Ingresar trimentre 4: '))
except ValueError:
      print("Debes escribir un número.")
      IS_EJECTED = False

if IS_EJECTED:

      totalVentas = trimestres1 + trimestres2 + trimestres3 + trimestres4

      print('Total ventas:',totalVentas)

      print('Trimestres 1 %:',(trimestres1/totalVentas)*100, '%')
      print('Trimestres 2 %:',(trimestres2/totalVentas)*100, '%')
      print('Trimestres 3 %:',(trimestres3/totalVentas)*100, '%')
      print('Trimestres 4 %:',(trimestres4/totalVentas)*100, '%')
      print('Test porcentual: ',
            (trimestres1/totalVentas)*100+
            (trimestres2/totalVentas)*100+
            (trimestres3/totalVentas)*100+
            (trimestres4/totalVentas)*100,'%')

