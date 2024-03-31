class Padre:
    def hablar(self):
        print('Hello, friend')

class Madre:
    def reir(self):
        print('ha ha ha ha !!')
    
    def hablar(self):
        print('Hola, que tal')

class Hijo(Padre, Madre):  # Esto es herencia multiple *(los metodos iguales se toman con prioridad segun se llame)
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()