# def rango_edades():
#     START = True
#     RANGOS = [[], [], [], []]
#     EDAD = 25

#     while START:
#         edad = int(input("Introduce tu edad de 0 a 100 años: "))
#         if edad < 0 or edad >= 101:
#             # Si la edad es menor que 0 o mayor o igual a 101, se termina el bucle
#             START = False
#         else:
#             if edad >= 0 and edad < 26:
#                 # RANG_0_25.append(edad)
#                 RANGOS[0].append(edad)
#             elif edad >= 26 and edad < 51:
#                 # RANG_26_50.append(edad)
#                 RANGOS[1].append(edad)
#             elif edad >= 51 and edad < 76:
#                 # RANG_51_75.append(edad)
#                 RANGOS[2].append(edad)
#             else:
#                 RANGOS[3].append(edad)
#                 # RANG_76_100.append(edad)
#     # Al finalizar el bucle, se imprime el resultado
#     # Si no se han introducido edades válidas, se imprime un mensaje
#     # Si se han introducido edades válidas, se imprimen los rangos
#     # de edades correspondientes
#     if len(RANGOS[0]) == 0 and len(RANGOS[1]) == 0 and len(RANGOS[2]) == 0 and len(RANGOS[3]) == 0:
#         print("No se han introducido edades válidas.")
#     else:
#         print("Rango de edades:")
#         for i in range(len(RANGOS)):
#             print("Rango de ", int(((i*i*i)/6)-(i*i)+(161*i/6)), " a ", (i + 1) * EDAD,
#                   " años: ", RANGOS[i], "Total: ", len(RANGOS[i]))


# rango_edades()


def votos_empre():
    # Definición de variables
    VOTOS = [0, 0, 0, 0, 0, 0]
    TOTAL_EMPLEADOS = 20
    TOTAL_VOTOS = 0
    while TOTAL_EMPLEADOS != TOTAL_VOTOS:
        # Se pide al usuario que introduzca su voto
        print("Menu de votación")
        print("1. Candidato 1")
        print("2. Candidato 2")
        print("3. Candidato 3")
        print("4. Candidato 4")
        print("5. Blanco 5")
        print("6. Nulo 6")
        voto = int(input("Introduce tu voto (1-6): "))
        if voto < 1 or voto > 6:
            # Si el voto no es válido, se termina el bucle
            print("Voto no válido.\n Por favor, introduce un número entre 1 y 6.")
        else:
            # Se incrementa el contador de votos para la opción seleccionada
            VOTOS[voto - 1] += 1
            TOTAL_VOTOS += 1
    # Al finalizar el bucle, se imprime el resultado
    print("Resultados de la votación:")
    for i in range(len(VOTOS)):
        print("Opción ", i + 1, ": ", VOTOS[i], " votos")
        porcentaje = (VOTOS[i] / TOTAL_VOTOS) * 100
        print(f"Opción {i + 1} : {porcentaje} %")


# Se llama a la función
votos_empre()
