# Informar superficie y perímetro de un rectángulo. Se ingresan las medidas de ambos lados.
print('Informar superficie y perímetro de un rectángulo. Se ingresan las medidas de ambos lados.')

ladoMayor = int(input('Ingresar lado Mayor: '))
ladoMenor = int(input('Ingresar lado Menor: '))

superfice = ladoMayor * ladoMenor
perimetro = ((ladoMenor * 2) + (ladoMayor * 2))

print('Superfice:',superfice)
print('Perimetro:',perimetro)