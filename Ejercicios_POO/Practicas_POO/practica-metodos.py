# Practica metodos 1
class Perro:
    def ladrar(self):
        print('Guau!')
    
labrador = Perro()

labrador.ladrar()

# Practica metodos 2
class Mago:
    def lanzar_hechizo(self):
        print('Abracadabra!')

merlin = Mago()
merlin.lanzar_hechizo()

# practiva metodos 3
class Alarma:
    @classmethod
    def postergar(cls, cantidad_minutos):
        print(f'La alarma ha sido postergada {cantidad_minutos} minutos')

Alarma.postergar(45)