# Hacer programas que generen las siguientes figuras, con la cantidad de niveles ingresados desde teclado
print('Hacer programas que generen las siguientes figuras, con la cantidad de niveles ingresados desde teclado')

IS_EJECTED=True
FIJO = 10
GLIFO = '*'


try:
    first = int(input('Ingrese el numero de piso maximo 10: '))
    if(first > 10):
      print("El maximo es 10.")
      IS_EJECTED = False
    elif(first <= 0):
      print("El minimo es 1.")
      IS_EJECTED = False
except ValueError:
    print("Debes escribir un número.")
    IS_EJECTED = False

second = input('Tenes opciones de diseños a,b,c,d,e,f:').lower()


if IS_EJECTED:
   
    print(f'Altura ingresada es: {first}')
    rango = first + 1
    match second:
        case "a":
            print("Opcion de diseños a:")
            for i in range(first):
                print(GLIFO * FIJO)

        case "b":
            print("Opcion de diseños b:")
            for i in range(first):
                print(GLIFO * (i + 1))

        case "c":
            print("Opcion de diseños c:")
            for i in range(first):
                print((GLIFO * (i + 1)).rjust(first,' '))

        case "d":
            print("Opcion de diseños d:")
            for i in range(first):
                print((GLIFO * (i + 1)).rjust(first,' ') + GLIFO * i)

        case "e":
            print("Opcion de diseños e:")
            LEVEL=''
            for i in range(first,-1,-1):
                if( i == 0):
                    LEVEL +="""
                    -------------------
                    |       PB        |
                    -------------------
                    """
                else:
                    LEVEL +=f"""
                    -------------------
                    |     nivel {i}     |
                    -------------------
                    """
            print(LEVEL)

        case "f":
            print("Opcion de diseños f:")
            GLIFO='_'
            SPACES=' '
            for i in range(first):
                
                LEFT = f" /{GLIFO * i}{GLIFO * i}\ "
                print((first - i),SPACES * (first - i) + LEFT)
        case _:
            print("Opcion de diseños invalido.")
