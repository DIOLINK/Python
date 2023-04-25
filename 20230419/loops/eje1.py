# Mostrar los números pares entre dos números que ingresan por teclado.
print('Mostrar los números pares entre dos números que ingresan por teclado.')

first = int(input('Ingrese el valor inicial: '))
second= int(input('Ingrese el valor final: '))

def paresWithFor(first, second):
    print(f'Lista de pares entre {first} y {second}')
    for i in range(first,second+1):
        if(i % 2 == 0):
            print(i)

paresWithFor(first, second)

print('-----------------------------------------------------------------------')


def paresWithWhile(first, second):
    print(f'Lista de pares entre {first} y {second}')
    contador = first  # Iniciamos el contador en cero
    while contador <= second:
        if(contador % 2 == 0):
            print(contador)
        contador+=1


paresWithWhile(first, second)