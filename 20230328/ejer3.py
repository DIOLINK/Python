# Informar superficie y perímetro de un rectángulo. Se ingresan las medidas de ambos lados.
print('Informar superficie y perímetro de un rectángulo. Se ingresan las medidas de ambos lados.')

ladoMayor = float(input('Ingresar lado Mayor: '))
ladoMenor = float(input('Ingresar lado Menor: '))

superfice = ladoMayor * ladoMenor
perimetro = ((ladoMenor * 2) + (ladoMayor * 2))

print('Superfice:', superfice)
print('Perimetro:', perimetro)
