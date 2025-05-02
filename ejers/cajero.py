# (5 4 0 0)monto_b
process = True

B1000 = 1000
B500 = 500
B200 = 200


b_1000 = 0
b_500 = 0
b_200 = 0
b_100 = 0

axu = 0
clientes_dia = 1
while clientes_dia < 3:
    monto_b = int(input("Ingrese el monto a extraer: "))
    axu = monto_b
    while axu >= B1000:
        axu -= B1000
        b_1000 += 1

    while axu >= B500:
        axu -= B500
        b_500 += 1

    while axu >= B200:
        axu -= B200
        b_200 += 1

    print(b_1000, 'Billetes de ', B1000, b_1000*B1000)
    print(b_500, 'Billetes de ', B500, b_500*B500)
    print(b_200, 'Billetes de ', B200, b_200*B200)

    print(b_1000+b_500+b_200, 'Total de Billetes')
    clientes_dia += 1

print('Total de Clientes', clientes_dia-1,
      b_1000 / (clientes_dia-1), 'Promedio', b_1000)
