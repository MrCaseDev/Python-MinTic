contador = 0
contador_L1 = 0
contador_L2 = 0
contador_L3 = 0

cTexto = input("Ingresa un texto (párrafo, frase, poema, etc.) => ")
cLetras = input("Ahora, ingresa tres (3) letras que tú quieras. Importante, separa las letras por un guión (-) => ")

cTexto.lower()
cLetras.lower()

aLetras = cLetras.split("-")
aTexto = list(cTexto)

for i in range(len(aLetras)):
    # Recorro cada una de las letras a buscar
    for n in range(len(aTexto)):
        # comparo y cuento las apariciones
        if aLetras[i] == aTexto[n]:
            contador += 1
    
    if aLetras[i] == aLetras[0]:
        contador_L1 = contador
    elif aLetras[i] == aLetras[1]:
        contador_L2 = contador
    elif aLetras[i] == aLetras[2]:
        contador_L3 = contador

    contador = 0

print(f"La letra '{aLetras[0]}' aparece {contador_L1} veces en el texto, la letra '{aLetras[1]}' aparece {contador_L2} y la letra '{aLetras[2]}' aparece {contador_L3} veces.")