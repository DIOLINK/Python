def contar_caracteres(frase):
    return len(frase)


def contar_digitos(frase):
    contador_digitos = 0

    for digitos in frase:
        if digitos.isdigit():
            contador_digitos += 1
    return contador_digitos


def contar_vocales(frase):
    vocales = "aeiouáéíóú"
    contador_vocales = 0

    for caracter in frase:
        caracter_minuscula = caracter.lower()

        if caracter_minuscula in vocales:
            contador_vocales += 1
    return contador_vocales


def contar_consonantes(frase):
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    contador_consonantes = 0

    for caracter in frase:
        carater_minuscula = caracter.lower()

        if carater_minuscula in consonantes:
            contador_consonantes += 1
    return contador_consonantes


def main():
    frase = input("Ingresa una frase: ")
    print("Longitud de la frase:", contar_caracteres(frase))
    print("Número de dígitos:", contar_digitos(frase))
    print("Número de vocales:", contar_vocales(frase))
    print("Número de consonantes:", contar_consonantes(frase))


if __name__ == "__main__":
    main()
