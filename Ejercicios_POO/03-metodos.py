class Pajaro:
    alas = True
    def __init__(self, color , especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'el pájaro ha volado {metros} metros')

piolin = Pajaro('amarillo', 'periquillo')

piolin.volar(50)
piolin.piar()