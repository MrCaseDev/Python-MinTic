""" Escribe una funcion que reciba cualquier palabra como parámetro, y que
devuelva todas las letras únicas(sin repetir) pero en orden alfabético. """

def letras_unicas_ordenadas(word):
    word_array = []
    letra = ""
    posicion = 0

    #Genero una lista
    for letra in word:
        word_array.append(letra.upper())

    # Elimina duplicados
    while posicion < len(word_array):
        letra = word_array[posicion]
        i = posicion + 1
        while i < len(word_array):
            if letra == word_array[i]:
                del word_array[i]
            else:
                i += 1
        posicion += 1
    # Ordena alfabéticamente               
    word_array.sort()
    return word_array
print(letras_unicas_ordenadas("Andres"))
    