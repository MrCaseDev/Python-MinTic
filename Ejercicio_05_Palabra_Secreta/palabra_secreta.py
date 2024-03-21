import random
import os
import sys

print("""JUEGO:AHORCADO (COMPLETA LA PALABRA)
Atención: Tienes un total de 10 vidas. Adelante !!""")

# variables
palabras = ['cyberpunk', 'neurona', 'realidad', 'artificial',
            'simulacion', 'maquina', 'algoritmo', 'matrix', 'rebelion', 'simulacion']
play_game = True
seleccion_random = random.choice(palabras) # Seleccionar aleatoriamente una palabra de la lista
palabra_auxiliar = seleccion_random
tamano_palabra = len(seleccion_random)
numero_vidas = 10
numero_intentos = 0
posicion = 0
var_progreso = ""
winner = False
lista_incorrectas = []
# Presenta espacios de palabra
for i in range(tamano_palabra):
    var_progreso += "_ "        
print("Palabra: "+ var_progreso.strip())

def busca_letra(entrada, palabra):
    #busca la posicion de la letra en la palabra
    return palabra.find(entrada)

def actualiza_progreso(entrada, indice, progreso, flag_actualiza):
    auxiliar = progreso.replace(" ", "")
    auxiliar = auxiliar[:indice] + entrada + auxiliar[indice + 1:]
    tam = len(auxiliar)
    if flag_actualiza and posicion >= 0:
        progreso = " ".join(auxiliar) # Toma lista y la convierte a string con espacios
    return progreso

def actualiza_seleccion(seleccion, indice):
    caracter_borrado = "*" # Caracter para reemplazar la letra ya descubierta
    if posicion >= 0:
        seleccion = seleccion[:indice] + caracter_borrado + seleccion[indice + 1:]
    return seleccion

def validar_entrada(entrada):
    if  len(entrada) == 1 and entrada.isalpha():
        return True
    elif entrada.isdigit():
        return False
    else:
        return False

while numero_intentos < numero_vidas:
    print(" ")
    letra = input('Digita una letra: ')
    if validar_entrada(letra):
        letra = letra.lower()
        os.system('cls')
        posicion = busca_letra(letra, seleccion_random)
        if posicion != -1:
            while posicion != -1:
                posicion = busca_letra(letra, seleccion_random)
                seleccion_random = actualiza_seleccion(seleccion_random, posicion)
                var_progreso = actualiza_progreso(letra, posicion, var_progreso, True)
            if palabra_auxiliar == var_progreso.replace(" ", ""):
                winner = True
                break
            print("Bien, la letra pertenece a la palabra.")
            print("Palabra: " + var_progreso)
        else:
            numero_intentos += 1
            lista_incorrectas.append(letra)
            print(f"Fallaste!, te quedan {numero_vidas - numero_intentos} vidas. Ya has digitado las siguiente letras incorrectas {lista_incorrectas}")
            var_progreso = actualiza_progreso(letra, posicion, var_progreso, False)
            print("Palabra: " + var_progreso)
    else:
        os.system('cls')
        print("Te entrada no es válida. Deber ser una letra")
        print("Palabra: " + var_progreso.strip())
if winner:
    print("Felicitaciones, ganaste !! Descubriste la palabra: " + var_progreso)
else:
    print("AHORCADO!. Tus vidas se han agotado")
