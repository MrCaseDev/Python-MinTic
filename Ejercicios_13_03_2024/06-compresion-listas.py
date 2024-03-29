palabra = 'python'

# lista = []

# for letra in palabra:
#     lista.append(letra)

# print(lista)

lista = [letra for letra in palabra]
print(lista)

lista2 = [n for n in range(0,23,2)]
print(lista2)

lista3 = [n for n in range(0,100,5) if n*2 > 50]
print(lista3)