# Escribir un programa que muestre la suma de los n primeros números enteros entre 1 y n (n lo ingresan por teclado)
print('Escribir un programa que muestre la suma de los n primeros números enteros entre 1 y n (n lo ingresan por teclado)')

n = int(input('Ingresar numero: '))

value = (n * (n + 1))//2

print(f'La suma de los números entre 1 y {n} es',value)