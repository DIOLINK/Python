# Hacer un programa que permita mostrar un ticket de devolución de envases para un supermercado.

print('Hacer un programa que permita mostrar un ticket de devolución de envases para un supermercado.')

PRICE_PER_BOTTLE_GLASS = 1.50
PRICE_PER_BOTTLE_PLASTIC = 2.00


bottleGlasses = int(input('Ingresar la cantidad de envases vidrio: '))
bottlePlastic = int(input('Ingresar la cantidad de envases plastico: '))

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