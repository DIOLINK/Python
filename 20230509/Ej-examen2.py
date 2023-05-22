texto = """
El vendedor de un local de vestimenta, solicita que le armemos un programa que
permita registrar las ventas:

- Qué tipo de prenda es (jeans, camisa, etc.) 1er letra en mayúscula
- Talle (s, m, l, xl, xxl) en mayúscula
- Precio Unitario (con 2 decimales)

Si el cliente, abona en efectivo o con tarjeta débito se le hace un 17% de
descuento; si abona con tarjeta en 3 cuotas se le recarga un 10%, en 6 cuotas
recarga el 13%

El programa debe permitir ingresar ventas hasta que el usuario ingrese 0.
Mostrar a medida que se van ingresando: los datos de la prenda, precio
unitario, descuento (si aplica), recargo y en cuántas cuotas (si aplica).

Mostrar, al finalizar el programa:
- cantidad total de ventas
- ganancia total
- promedio de ventas en efectivo/débito
- promedio de ventas en crédito
"""

print(texto)

ventas_efectivo_debito = []
ventas_credito = []
cantidad_ventas = 0
ganancia_total = 0

while True:
    tipo_prenda = input("Ingrese el tipo de prenda (jeans, camisa, etc.): ")
    if tipo_prenda == "0":
        break
    
    talle = input("Ingrese el talle (s, m, l, xl, xxl): ").upper()
    precio_unitario = float(input("Ingrese el precio unitario: "))
    
    descuento = 0
    recargo = 0
    cuotas = 1
    
    forma_pago = input("Ingrese la forma de pago (efectivo, debito, credito): ").lower()
    if forma_pago == "efectivo" or forma_pago == "debito":
        descuento = precio_unitario * 0.17
        precio_unitario -= descuento
        ventas_efectivo_debito.append(precio_unitario)
    elif forma_pago == "credito":
        cuotas = int(input("Ingrese la cantidad de cuotas (3, 6): "))
        if cuotas == 3:
            recargo = precio_unitario * 0.10
        elif cuotas == 6:
            recargo = precio_unitario * 0.13
        precio_unitario += recargo
        ventas_credito.append(precio_unitario)
    
    cantidad_ventas += 1
    ganancia_total += precio_unitario
    
    print("Datos de la prenda:", tipo_prenda.capitalize())
    print("Talle:", talle)
    print("Precio unitario:", precio_unitario)
    print("Descuento:", descuento)
    print("Recargo:", recargo)
    print("Cuotas:", cuotas)
    print('----------------------------------------------------')
    
promedio_efectivo_debito = sum(ventas_efectivo_debito) / len(ventas_efectivo_debito) if ventas_efectivo_debito else 0
promedio_credito = sum(ventas_credito) / len(ventas_credito) if ventas_credito else 0

print("Cantidad total de ventas:", cantidad_ventas)
print("Ganancia total:", ganancia_total)
print("Promedio de ventas en efectivo/débito:", promedio_efectivo_debito)
print("Promedio de ventas en crédito:", promedio_credito)
