# El factorial de un número n (n!) es el producto de todos los números enteros positivos menores o iguales que n
print('El factorial de un número n (n!) es el producto de todos los números enteros positivos menores o iguales que n')

first = int(input('Ingrese el valor a factorizar (n!): '))

def factorialWithFor(first):
    aux=1 # Iniciamos el contador en uno
    srt_aux = ''
    if(first == 0):
          print(f'el factorial de 0! = {aux}')
    elif (first != 0):
          for i in range(first):
                srt_aux += f'{(first - i)} x '
                aux = aux * (first - i)
    print(f'El factorial de {first}! es: {srt_aux[0:len(srt_aux)-3]} = {aux}')

factorialWithFor(first)

print('--------------------------------<While>-----------------------------------')


def factorialWithWhile(first):
    aux=1 # Iniciamos el contador en uno
    contador = 0 # Iniciamos el contador en cero
    srt_aux = ''
    if(first == 0):
          print(f'el factorial de 0! = {aux}')
    elif (first != 0):
          while contador < first:
            srt_aux += f'{(first - contador)} x '
            aux = aux * (first - contador)
            contador+=1
    print(f'El factorial de {first}! es: {srt_aux[0:len(srt_aux)-3]} = {aux}')


factorialWithWhile(first)