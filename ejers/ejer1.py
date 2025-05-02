hola1 = 0
valor_true = "  x  "
valor_false = "  -  "
respuestas = []
heder = f"""
    numero\t par \tinpar\tmulti_3\tprimo
    """
while hola1 < 2:
    numero = int(input("ingrese numeros en la tabla: "))
    numero_par = valor_false
    numero_multi_3 = valor_false
    numero_inpar = valor_false
    numero_primo = valor_false

    if numero % 2 == 0:
        numero_par = valor_true
    else:
        numero_inpar = valor_true
        if numero % 3 == 0:
            numero_multi_3 = valor_true
        if numero == 1:
            numero_primo = valor_true
        elif numero < 1:
            numero_primo = valor_false
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    numero_primo = valor_false
            numero_primo = valor_true

    respuesta = f"""
  \t{numero}\t{numero_par}\t{numero_inpar}\t{numero_multi_3}\t{numero_primo}
  """
    respuestas.append(respuesta)
    hola1 += 1

print(heder)
for respuesta in respuestas:
    print(respuesta)
