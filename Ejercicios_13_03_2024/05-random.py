from random import *

aleatorio = randint(1, 50)
print(f'Aleatorio entre 1 y 50 - > {aleatorio}')

aleatorio2 = uniform(1,5)
print(f'Aleatorio entre 1 y 5 - > {round(aleatorio2,2)}')

aleatorio3 = random()
print(f'Random entre 0 y 1 -> {round(aleatorio3,3)}')

colores = ['rojo', 'azul', 'rojo' , 'amarillo', 'naranja' , 'morado', 'rosado'  ]
aleatorio4 = choice(colores)
print(f'Color seleccionado -> {aleatorio4}')

numeros = list(range(3,50,2))
print(numeros)
shuffle(numeros)
print(numeros)