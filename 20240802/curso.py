# def divisores_comunes(num1, num2):
#     def obtener_divisores(n):
#         divisores = []
#         contador = 1
#         while contador <= n:
#             if n % contador == 0:
#                 divisores.append(contador)
#             contador += 1
#         return divisores

#     divisores_num1 = set(obtener_divisores(num1))
#     divisores_num2 = set(obtener_divisores(num2))

#     comunes = divisores_num1.intersection(divisores_num2)

#     print(" ".join(map(str, sorted(comunes))))


# def cuadrado_hueco(n):
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             print('*' * n)
#         else:
#             print('*' + ' ' * (n - 2) + '*')


# def diagonal_cuadrado(n):
#     for i in range(n):
#         fila = [' ']*n
#         fila[i] = '*'
#         print(''.join(fila))


# def desde_hasta(lista, desde, hasta):
#     for i in range(desde, hasta):
#         if i < len(lista):
#             print(lista[i])

# # Escribe tu código aquí


# def mostrar_dato_e_indice(datos):
#     i = 0
#     while i < len(datos):
#         print(f"El valor en la posición {i} es {datos[i]}")
#         i += 1


# # Fin
# mostrar_dato_e_indice(["Galleta", "Chocolate", "Caramelo"])


# def juntarPalabras(lista):
#     palabras = [str(elemento) for elemento in lista]
#     return ' '.join(palabras)


# def sumar_datos(cadena):
#     lista = cadena.split()
#     suma = 0
#     for elemento in lista:
#         try:
#             suma += float(elemento)
#         except ValueError:
#             continue
#     return suma


# def agregarStock(cantidades, stock_adicional):
#     nuevas_cantidades = [cantidad + stock_adicional for cantidad in cantidades]
#     return nuevas_cantidades


# def capitalizar_nombres(nombres):
#     nombres_capitalizados = [nombre.capitalize() for nombre in nombres]
#     return nombres_capitalizados


# def transformar(nombres):
#     for i in range(len(nombres)):
#         nombre = nombres[i]
#         nombre_transformado = nombre.strip().capitalize() + '.'
#         nombres[i] = nombre_transformado


# nombres = [" ana", "luis ", " jose", "rosa", "julio "]
# transformar(nombres)
# print(nombres)


# tupla = ("Juan", 8, 'Python')  # Modifica esta línea
# (nombre, nota, curso) = tupla

# print(f"{nombre} tiene {nota} en el curso de {curso}.")
# # El resultado debe ser: "Juan tiene 8 en el curso de Python."
# def aumentar_notas(calificaciones):
#     calificaciones_aumentadas = tuple(
#         calificacion + 1 for calificacion in calificaciones)
#     return calificaciones_aumentadas


# def combinar_tuplas(tupla1, tupla2):
#     resultado = tupla1 + tupla2 + tupla2 + tupla1
#     return resultado


# def modificar_calificaciones(calificaciones):
#     lista_calificaciones = list(calificaciones)
#     if lista_calificaciones[0] < 70:
#         lista_calificaciones[0] += 5
#     if lista_calificaciones[-1] < 70:
#         lista_calificaciones[-1] += 5
#     return tuple(lista_calificaciones)

# def actualizar_inventario(inventario, producto, cantidad):
#     if cantidad == 0:
#         inventario.pop(producto, None)
#     else:
#         inventario[producto] = cantidad
#     return inventario


# def calcular_promedio(notas):
#     if not notas:
#         return 0
#     total_notas = sum(notas.values())
#     cantidad_notas = len(notas)
#     return total_notas / cantidad_notas

def cancion_elefantes():
    i = 1
    while i <= 10:
        print(f"{i} Elefante{'s' if i > 1 else ''} se balanceaba{'n' if i > 1 else ''} sobre la tela de una araña,"
              f"como ve{'ían' if i > 1 else 'ía'} que resistía, {'fueron' if i > 1 else 'fue'} a llamar a otro elefante.", end=" ")
        i += 1


cancion_elefantes()
