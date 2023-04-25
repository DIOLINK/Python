# Imprimir la tabla de multiplicar de un número entero K (que se ingresa por teclado), entre 1 y 10.
print('Imprimir la tabla de multiplicar de un número entero K (que se ingresa por teclado), entre 1 y 10.')

first = int(input('Ingrese el valor de la tabla: '))
LENGTH = 10

def tablaWithFor(first):
    print(f'La Tabla de {first} es :')
    for i in range(LENGTH+1):
            print(i,'x',first,'=',i * first)

tablaWithFor(first)

print('-----------------------------------------------------------------------')


def tablaWithWhile(first):
    print(f'La Tabla de {first} es :')
    contador = 0  # Iniciamos el contador en cero
    while contador <= LENGTH:
            print(contador,'x',first,'=',contador * first)
            contador+=1


tablaWithWhile(first)