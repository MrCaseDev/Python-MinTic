class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice MUUUUU!!")
    
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice BEEEE !')

vaca1 = Vaca('Patricia')
oveja1 = Oveja('Rebeca')

vaca1.hablar()
oveja1.hablar()

animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()