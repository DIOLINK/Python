# Hacer un programa que permita mostrar un ticket de devolución de envases para un supermercado.

print('Hacer un programa que permita mostrar un ticket de devolución de envases para un supermercado.')

PRICE_PER_BOTTLE_GLASS = 1.50
PRICE_PER_BOTTLE_PLASTIC = 2.00

IS_EJECTED = True

try:
    bottleGlasses = int(input('Ingresar la cantidad de envases vidrio: '))
    bottlePlastic = int(input('Ingresar la cantidad de envases plastico: '))
except ValueError:
    print("Debes escribir un número.")
    IS_EJECTED = False

if IS_EJECTED:
    countedBottles = bottlePlastic + bottleGlasses
    totalValuedBottleGlasses = bottleGlasses * PRICE_PER_BOTTLE_GLASS
    totalValuedBottlePlastic = bottlePlastic * PRICE_PER_BOTTLE_PLASTIC

    totalValue = totalValuedBottleGlasses + totalValuedBottlePlastic

    ticket = f"""
    Ingrese botellas:
    vidrio: \t{bottleGlasses}
    plástico: \t{bottlePlastic}
    Devolución de botellas
    ========================
    plástico {bottlePlastic} \t{totalValuedBottlePlastic}
    vidrio {bottleGlasses} \t{totalValuedBottleGlasses}
    ------------------------
    total {countedBottles} \t{totalValue}
    """

    print(ticket)