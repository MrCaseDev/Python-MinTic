"""INTRODUCCION A PYTHON."""
print("**********************************************************")
print("Bienvenida a la calculadora ! ")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, mult, div")
print("***********************************************************")

RESULTADO = ""

while True:
    if not RESULTADO:
        RESULTADO = input("Ingrese un numero: ")
        if RESULTADO.lower() == "salir":
            break
        RESULTADO = int(RESULTADO)
    op = input("Ingrese la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingrese el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        RESULTADO += n2
    elif op.lower() == "resta":
        RESULTADO -= n2
    elif op.lower() == "mult":
        RESULTADO *= n2
    elif op.lower() == "div":
        RESULTADO /= n2
    else:
        print("La operacion no es valida")
    print(f"El resutlado es {RESULTADO}")
    RESULTADO = ""
    print("/***********************************/")
