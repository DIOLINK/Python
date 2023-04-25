# Un corredor de seguros necesita cobrar a su lista de clientes morosos. Nos pide que calculemos el valor de la deuda, ingresando el total anual de la póliza y los meses adeudados.

print('Un corredor de seguros necesita cobrar a su lista de clientes morosos. Nos pide que calculemos el valor de la deuda, ingresando el total anual de la póliza y los meses adeudados.')
AÑO_MESES = 12
IS_EJECTED=True
IS_EXIT = True
while IS_EJECTED:
    
    try:
        poliza = int(input('Ingrese el total anual de la póliza: '))
        if(poliza == 0):
              print("<--- Fin --->")
              IS_EXIT = False
              IS_EJECTED = False
    except ValueError:
        print("Debes escribir un número.")
        IS_EJECTED = False
        
    if IS_EJECTED:
        try:
            deuda_meses = int(input('Ingrese el total anual de los meses adeudados: '))
        except ValueError:
            print("Debes escribir un número.")
        response = f"""
              póliza anual: \t{poliza}
              meses adeudados: \t{deuda_meses}
              debe: \t\t{(poliza / AÑO_MESES) * deuda_meses}
              """
        print(response)