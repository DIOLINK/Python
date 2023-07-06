# Roger Coverzola Bogado

texto = """

"""

RECARGO_TARJETA = 0.13
DESCUENTOS_CAMISA = 0.15
ventas_total = 0
ventas_jeans_SKH = 0
ventas_jeans_ZXC = 0
ventas_total_cliente = []
valor_total_descuentos = []

while True:
    print('(ingrese 0 para finalizar el ingreso de datos)')
    nombre_cliente = input("Ingrese el nombre del cliente : ")
    if nombre_cliente == "0":
        break
    
    cantidad_productos = 0
    valor_total = 0
    
    while True:
        prendas = input("Ingrese la prenda: ").lower()
        if prendas == "0":
            break
        if prendas == "jeans":
            tipo_jeans = input("Ingrese el tipo de Jeans SKH o ZXC: ").lower()
            if tipo_jeans == "skh":
                ventas_jeans_SKH += 1
            elif tipo_jeans == "zxc":
                ventas_jeans_ZXC += 1
        try:
            cantidad_prendas= int(input("Ingrese la cantidad de prendas: "))
        except ValueError:
            print("Debes escribir un número.")

        precio_unitario = float(input("Ingrese el precio unitario: "))
    
        forma_pago = input("Ingrese la forma de pago (efectivo, tarjeta, debito): ").lower()

        if forma_pago == "tarjeta":
                dni_cliente= input("Ingreser el DNI sin puntos: ")
                while len(dni_cliente) <= 8 and len(dni_cliente) >= 7:
                  dni_cliente= input("Ingreser el DNI sin puntos: ")
                recargo = valor_total * RECARGO_TARJETA
                valor_total += recargo
                ventas_total_cliente.append(valor_total)
        elif forma_pago == 'efectivo' or forma_pago == 'debito':
            if prendas == "camisa":
                descuento = valor_total * DESCUENTOS_CAMISA
                valor_total_descuentos.append(descuento)
                valor_total -= descuento
                ventas_total_cliente.append(valor_total)
            else:
                valor_total += (cantidad_prendas * precio_unitario)
                ventas_total_cliente.append(valor_total)

    print("Nombre del cliente:", nombre_cliente.upper())
    print("DNI del cliente:", dni_cliente)
    print("Total de la venta:", sum(ventas_total_cliente))
    print("Total de descuento en la venta:", sum(valor_total_descuentos))


print("Promedio de ventas SKH: ", (ventas_jeans_SKH / len(ventas_total_cliente))*100,'%')
print("Promedio de ventas ZXC: ",(ventas_jeans_ZXC / len(ventas_total_cliente))*100,'%' )
