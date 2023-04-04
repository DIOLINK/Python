# Hacer un programa que pregunte un número de cuatro cifras y muestre la suma de sus dígitos.

print('Hacer un programa que pregunte un número de cuatro cifras y muestre la suma de sus dígitos.')

value = input('Ingresar un número de cuatro cifras: ')

if len(value) == 4:
    sum = int(value[0]) + int(value[1]) + int(value[2]) + int(value[3])

    print(f"La suma de los dígitos de {value} es: {sum}")
elif len(value) != 4:
    print('El numero ingresado no es un número de cuatro cifras. ej: 1368')
