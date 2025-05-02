# CONS = "lord of the rings"


# def acronimo(frase):
#     palabras = frase.split()
#     print(palabras)
#     if not len(palabras) >= 2:
#         print("Error ingrese al menos dos palabras")
#     else:
#         acumulador_de_letras_para_generear_acronimo = ""
#         for palabra in palabras:
#               acumulador_de_letras_para_generear_acronimo =       acumulador_de_letras_para_generear_acronimo + \
#               palabra[0].upper()
#         respuesta = f'Acronimo: {acumulador_de_letras_para_generear_acronimo}'
#         print(respuesta)


# def main():
#     frase = input("Ingresa una frase: ")
#     acronimo(frase)
#     # print(acronimo(CONS))
#     # print(acronimo('gato'))


# if __name__ == "__main__":
#     main()


def acronimo(frase):
    palabras = frase.split()  # Transforma frase en una liksta de palabras
    if not len(palabras) >= 2:
        print("Error ingrese almenos dos palabras")
    else:
        acumuladorletras = ""  # Acumulador de letras
        for palabra in palabras:  # recorrer las palabras
            # tomamos la posicion inicial de la palabra y la hace mayus y me la guarda dentro de acronimo.
            acumuladorletras = acumuladorletras + palabra[0].upper()
        print("Acronimo:", acumuladorletras)


def main():
    frase = input("Ingresa una frase: ")
    acronimo(frase)


if __name__ == "__main__":
    main()
