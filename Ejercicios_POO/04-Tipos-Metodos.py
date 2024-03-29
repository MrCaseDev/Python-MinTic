class Pajaro:
    alas = True
    def __init__(self, color , especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'el pájaro ha volado {metros} metros')
        self.piar()
        
    def pintar_negro(self): # metodos de instancia
        self.color = 'negro'
        print(f'Ahora el pájaro es de color {self.color}')

    @classmethod  # metodo de clase
    def poner_huevos(cls, cantidad):
        print(f'el pájaro puso {cantidad} huevos')

    @staticmethod # metodo estatico
    def mirar():
        print('El pajaro está observando')

piolin = Pajaro('amarillo','periquillo')
piolin.pintar_negro()

piolin.alas = False

############# Como usar el metodo de clase
Pajaro.poner_huevos(3)

Pajaro.mirar()

