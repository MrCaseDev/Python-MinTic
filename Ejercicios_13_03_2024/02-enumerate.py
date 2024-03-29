lista = ['a', 'b', 'c', 'd', 'e']

for indice, item in enumerate(lista):
    print(indice,item)

print(list(enumerate(lista))) # crea una tupa con indice y contenido de la lista