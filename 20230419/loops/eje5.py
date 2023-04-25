# Hacer una función que reciba como parámetros N1 y N2 y devuelva cuántos múltiplos de N1 hay que sean menores que N2. Ej.: ulMenores(2, 15) -> 6 (4, 6, 8, 10, 12, 14). Hacerlo con for y con while ¿Cuál es la ventaja de cada una?
print('Hacer una función que reciba como parámetros N1 y N2 y devuelva cuántos múltiplos de N1 hay que sean menores que N2. Ej.: ulMenores(2, 15) -> 6 (4, 6, 8, 10, 12, 14). Hacerlo con for y con while ¿Cuál es la ventaja de cada una?')
n1 = int(input('ingrese N1: '))
n2 = int(input('ingrese N2: '))


def mulMenoresFor(n1, n2):
    sumaMultiplos = '('
    contador = 0  # Iniciamos el contador en cero
    for i in range(n2):
        if (i % n1) == 0:  # Preguntamos si el residuo es 0 (es múltiplo de n1)
            sumaMultiplos += f'{i}, '
            contador += 1  # Si es múltiplo aumentamos el contador en 1, si no es múltiplo no hacemos nada
    print('Con un For =>\t ', 'Hay ', contador,
          'múltiplos de', n1, '->', sumaMultiplos[0: len(sumaMultiplos) - 2], ')')


mulMenoresFor(n1, n2)
print('-----------------------------------------------------------------------')


def mulMenoresWhile(n1, n2):
    sumaMultiplos = '('
    contador = 0  # Iniciamos el contador en cero
    contadorMultiplos = 0  # Iniciamos el contador en cero
    while contador < n2:
        if (contador % n1) == 0:  # Preguntamos si el residuo es 0 (es múltiplo de n1)
            sumaMultiplos += f'{contador}, '
            contadorMultiplos += 1
        contador += 1  # Si es múltiplo aumentamos el contador en 1, si no es múltiplo no hacemos nada
    print('Con un While =>\t ', 'Hay ', contadorMultiplos,
          'múltiplos de', n1, '->', sumaMultiplos[0: len(sumaMultiplos) - 2], ')')


mulMenoresWhile(n1, n2)
