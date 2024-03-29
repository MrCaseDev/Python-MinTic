nombre = ['Ana','Cristian','Antonio', 'Carlos']
edades = [22,23,24,25,20 ]

combinado = list(zip(nombre, edades))

print(combinado)

for name, old in zip(nombre, edades):
    print(f'Nombre: {name} -- Edad {old}')

# Permite agrupar por el contenido de dos o mas iterables teniendo en cuenta el indice o posicion para agruparlos