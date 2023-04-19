contador = 0  # Iniciamos el contador en cero
for i in range(10000):
    if ((i % 33 == 0) & (i != 0)):  # Preguntamos si el residuo es 0 (es múltiplo de 33)
        contador += 1  # Si es múltiplo aumentamos el contador en 1
    # Si no es múltiplo no hacemos nada
print(contador)
'''Supuestamente, este ciclo for nos permite saber que existen 304 múltiplos del número 33 en los números del 0 al 10000
(incluido el 10000 mismo).'''  # Pero esto está mal, solo hay 303 múltiplos, no está funcionando el % ?
