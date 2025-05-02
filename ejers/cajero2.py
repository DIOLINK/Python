
# Denominaciones de billetes
billete_1000 = 1000
billete_500 = 500
billete_200 = 200
billete_100 = 100
billete_50 = 50
billete_20 = 20
billete_10 = 10

# Solicitar al usuario el monto a retirar
monto = int(input("Ingrese el monto a retirar: "))

# Variables para contar los billetes
total_billetes = 0
billetes_1000 = 0
billetes_500 = 0
billetes_200 = 0
billetes_100 = 0
billetes_50 = 0
billetes_20 = 0
billetes_10 = 0

# Calcular billetes de 1000
if monto >= billete_1000:
    billetes_1000 = monto // billete_1000
    monto = monto % billete_1000
    total_billetes += billetes_1000
# Calcular billetes de 500
if monto >= billete_500:
    billetes_500 = monto // billete_500
    monto = monto % billete_500
    total_billetes += billetes_500
# Calcular billetes de 200
if monto >= billete_200:
    billetes_200 = monto // billete_200
    monto = monto % billete_200
    total_billetes += billetes_200
# Calcular billetes de 100
if monto >= billete_100:
    billetes_100 = monto // billete_100
    monto = monto % billete_100
    total_billetes += billetes_100

# Calcular billetes de 50
if monto >= billete_50:
    billetes_50 = monto // billete_50
    monto = monto % billete_50
    total_billetes += billetes_50
# Calcular billetes de 20
if monto >= billete_20:
    billetes_20 = monto // billete_20
    monto = monto % billete_20
    total_billetes += billetes_20
# Calcular billetes de 10
if monto >= billete_10:
    billetes_10 = monto // billete_10
    monto = monto % billete_10
    total_billetes += billetes_10

print(f"Billetes de 1000: {billetes_1000}")
print(f"Billetes de 500: {billetes_500}")
print(f"Billetes de 200: {billetes_200}")
print(f"Billetes de 100: {billetes_100}")
print(f"Billetes de 50: {billetes_50}")
print(f"Billetes de 20: {billetes_20}")
print(f"Billetes de 10: {billetes_10}")
print(f"Total de billetes: {total_billetes}")
