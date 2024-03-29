#Herencia en POO
class Animal:
    def __init__(self, edad, color):
        self.color = color
        self.edad = edad
    
    def nacer(self):
        print('El animal ha nacido')

class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color) # super indica que los parametros del constructor se heredan de la clase padra
        self.altura_vuelo = altura_vuelo

piolin = Pajaro(12,'amarillo', 100)
piolin.nacer()

print(Pajaro.__bases__) # como saber si la clase hereda de otra clase
print(f'altura de vuelo de piolin es {piolin.altura_vuelo} metros')

