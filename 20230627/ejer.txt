def verificadorPatentes(patente):
    if len(patente) == 6:
        if patente[0:3].isalpha() and patente[3:6].isdigit():
            return "1"
    elif len(patente) == 9:
        if patente[0:2].isalpha() and patente[3:6].isdigit() and patente[7:10].isalpha():
            return "2"
    return "-1"  # Error


def vtv():
    listaPatentes = []
    isRun = True
    while isRun:
        if len(listaPatentes) > 0:
            print(listaPatentes)
        patente = input("Ingresar patente o ingresa X para terminar: ")
        if patente.lower() == "x":
            isRun = False
        elif verificadorPatentes(patente) != "-1":
            listaPatentes.append(patente)
        else:
            print('Error en la patente ingresada', patente)


vtv()

# print(verificadorPatente('123qwe') != "-1") # False
# print(verificadorPatente('qw%%%123qw') != "-1") # False

# print(verificadorPatente('123qwe'))  # -1
# print(verificadorPatente('qwe123'))  # 1
# print(verificadorPatente('qw-123-qw'))  # 2
# print(verificadorPatente('qw%%%123qw'))  # -1
