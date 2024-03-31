# Practica herencia 1
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

alumno1= Alumno('Cristian',23)

print('Alumno: ' + alumno1.nombre)

#Practica herencia 2
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas):
        super().__init__(edad, nombre, cantidad_patas)

# practica herencia 3
class Vehiculo:
    def acelerar(self):
        print('acelerandoo>>>>>>')

    def frenar(self):
        print('frenando<<<<<<<<<')

class Automovil(Vehiculo):
    pass

carro = Automovil()

carro.acelerar()
carro.frenar()