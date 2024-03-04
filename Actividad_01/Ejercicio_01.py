""" Ejercico 01:
Crea una funcion llamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 numeros es un valor entre 10 y 15, va a devolver el número de valor intermedio. """

def devolver_distintos(n1, n2, n3):
    numero_return = 0
    numeros = [n1, n2, n3]
    numeros.sort(reverse=True)
    suma_numeros = n1 + n2 + n3
    
    if suma_numeros  > 15 :
        numero_return = numeros[0] # numero mayor
    elif suma_numeros < 10 :
        numero_return = numeros[2] # numero menor
    else: 
        numero_return = numeros[1] # numero intermedio
    return numero_return

print(devolver_distintos(5,4,3))