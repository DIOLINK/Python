# Hacer un programa que genere un número de N cifras (se ingresa por teclado) y pregunte al usuario números hasta que lo adivine.
print('Hacer un programa que genere un número de N cifras (se ingresa por teclado) y pregunte al usuario números hasta que lo adivine.')

import random

intentos = 0
ADIVINA = random.randint(0,100000)


while intentos < 3:
    IS_EJECTED=True
    try:
        first = int(input(f'Ingrese un numero de {len(str(ADIVINA))} sifras: '))
    except ValueError:
      print("Debes escribir un número.")
      IS_EJECTED = False
    if len(str(ADIVINA)) != len(str(first)):
        print(f"Debes escribir un número de {len(str(ADIVINA))}.")
        IS_EJECTED = False

    if IS_EJECTED:
        if(first>ADIVINA):
            print('El numero a adivinar es menor.')
        elif (first<ADIVINA):
            print('El numero a adivinar es mayor.')
        elif (first == ADIVINA):
            print('Adivinaste eres el ganador!!!')
        
        intentos+=1
        if intentos == 3:
            print(f'No has podido adivinar T~T el numero era {ADIVINA}')

