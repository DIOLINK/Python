cliente_siclo = True
nombre_cliente_mayor_gasto = ""
importe_cliente_mayor_gasto = 0
iva = 21
while cliente_siclo:
    producto_cliente = True
    print("Hola Cliente!!!, para salir del programa es con el 0.")
    nombre_cliente = input("Ingresa tu nombre: ")
    if nombre_cliente == "0":
        cliente_siclo = False
        producto_cliente = False
        print("Gracias vuelva pronto.")
        print('Cliente que más gasto: ', nombre_cliente_mayor_gasto)
        print('Cliente Total sin iva: ', importe_cliente_mayor_gasto)
    else:
        total_productos = 0
        importe_total = 0
        while producto_cliente:
            if (importe_total > importe_cliente_mayor_gasto):
                nombre_cliente_mayor_gasto = nombre_cliente
                importe_cliente_mayor_gasto = importe_total
            print("Bienvenido ", nombre_cliente,
                  "!!!, para volver atras es con una n como nombre.")
            nombre_producto = input("Ingresa nombre del producto: ")
            if nombre_producto.lower() == "n":
                producto_cliente = False
                print("Volviendo al ingreso de Clientes!!")
            else:
                importe_producto = int(
                    input("Ingresa el importe del producto: "))
                if (importe_producto >= 0):
                    total_productos += 1
                    importe_total += importe_producto
                else:
                    print(importe_producto,
                          ": Es un importe incorrecto.")

        print("Total Productos: ", total_productos)
        print("Total Importe sin iva: ", importe_total)
        print("Total Importe con iva", iva, ": ",
              importe_total+((importe_total*iva)/100))
