class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

    def hablar(self):
        print("Este animal emite algun sonido")

# Herencia
class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura = altura_vuelo

    def hablar(self): # Se pueden sobre escribir metodos *(hablar tambien lo tiene la clase padre)
        print("PIO!!")

    def volar(self):
        print(f"El pajaro vuela a {self.altura} de altura")

piolin = Pajaro(15, "Amarillo",100)

piolin.hablar()

piolin.volar()