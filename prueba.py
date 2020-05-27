"""
lista= [[1,2,3],[4,5,6],[7,8,9]]

lista2 = []
lista2.append([])
lista2.append([])
lista2.append([])

contador = 0
for x in lista:
    lista2[0].append(x[0])
    lista2[1].append(x[0]*x[0])
    contador = contador + 1

lista2.append([])
lista2.append([])
lista2[0].append(100)
lista2[1].append(200)

print(lista2)
"""
def validar(mensaje, )