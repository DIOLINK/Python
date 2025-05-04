def calcular_promedio_temp_usuario():
    lista_temp_usuario = []
    print("Bienvenido al programa de cálculo de temperatura.")
    START_PROGRAM = True
    while START_PROGRAM:
        temp_usuario = float(
            input('Ingresa la temperatura en °C (o -273 para terminar): '))
        if temp_usuario == -273:
            START_PROGRAM = False
        else:
            lista_temp_usuario.append(temp_usuario)

    if lista_temp_usuario:
        promedio = sum(lista_temp_usuario)
        print(
            f"El promedio de las temperaturas ingresadas es: {promedio:.2f} °C")
    else:
        print("No se ingresaron temperaturas válidas.")


calcular_promedio_temp_usuario()
