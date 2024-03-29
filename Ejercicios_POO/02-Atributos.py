class Pajaro:
    alas = True
    def __init__(self, color , especie):
        self.color = color
        self.especie = especie

tucan = Pajaro('negro','piciformes')

print(tucan.color)
print(tucan.alas)
print(Pajaro.alas)

# Practicas Clases 1
class Personaje:
    pass

harry_potter  = Personaje()

# Practicas Clases 2

class Dinosaurio:
    pass

velocitaptor = Dinosaurio()
tiranosaurio = Dinosaurio()
branquiosaurio = Dinosaurio()


# Practicas Clases 3
class PlatafromaStreaming:
    pass

netflix = PlatafromaStreaming()
hbo_max  =  PlatafromaStreaming()
amazon_prime_video = PlatafromaStreaming()

# Practicas atributos 1
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
    
casa_blanca = Casa('blanco', 4)

# Practicas atributos 2
class Cubo:
    carass = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')

# Practicas atributos 3
class Personaje2:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


