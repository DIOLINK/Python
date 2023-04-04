# Indique si un número ingresado por consola es par o impar y si es divisible o no por 3

IS_EJECTED = True
EVEN_ODD = 'es par pero no es multiplo de 3.'

try:
    value = int(input('Ingresar un número: '))
except ValueError:
    print("Debes escribir un número.")
    IS_EJECTED = False

if IS_EJECTED:
    if value % 2 != 0:
        EVEN_ODD = 'es impar y es multiplo de 3.'

print("El número",value, EVEN_ODD)