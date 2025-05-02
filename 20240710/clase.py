# '''
# patente = "GGH789"

# p1 = patente[0:3]
# print(p1)

# if p1.isalpha():
#     print("Letras OK")


# p2 = patente[3:6]

# if p2.isdigit():
#     print("digit ok")

# print(frase.count(" "))

# cont = frase.count(" ")
# print(cont)
# '''


# '''
# patente = input("ingreselapatente: ")

# if len(patente) == 6:
#     p1 = patente[0:3]
#     p2 = patente[3:6]
#     if p1.isalpha() and p2.isdigit():
#         print("1")
#     else:
#         print("-1")

# elif len(patente) == 9:
#     p1 = patente[0:2]
#     p2 = patente[3:6]
#     p3 = patente[7:9]
#     if p1.isalpha() and p3.isalpha() and p2.isdigit():
#         print("2")
#     else:
#         print("-1")

# else: #len(patente) != 6 and len(patente) != 9:
#     print("-1")
# '''

# frase = input("ingrese una frase: ")

# cont = frase.count(" ")
# num = cont+1

# print(f"la cantidad de palabras es {num}")

# #ejer 1
# def contador_palabras(frase):
#     palabras = frase.split()
#     return len(palabras)


# def main():
#     frase = input("Ingresa una frase: ")
#     print('La cantidad de palabras es:',
#           contador_palabras(frase), 'Miu')


# if __name__ == "__main__":
#     main()

def verificadorPatentes(patente):
    if len(patente) == 6:
        if patente[0:3].isalpha() and patente[3:6].isdigit():
            return "1"
    elif len(patente) == 7:
        if patente[0:2].isalpha() and patente[2:5].isdigit() and patente[5:7].isalpha():
            return "2"
    return "-1"  # Error


def main():

    patente = input("Ingresar patente o ingresa X para terminar: ")
    print(verificadorPatentes(patente))


if __name__ == "__main__":
    main()
