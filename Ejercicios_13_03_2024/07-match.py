# serie = "N-02"

# match serie:
#     case "N-01":
#         print('Samsung')
#     case "N-02":
#          print('Nokia')
#     case "N-03":
#         print('Motorola')
#     case _:
#         print("No existe producto")

pelicula = {
    'titulo':'matrix',
    'ficha_tecnica':{
        'protagonista':'Kenau Reeves',
        'director':'Lana'
    }
}

cliente = {
    'nombre':'Luis',
    'ocupacion':'Docente',
    'edad':45
}

elemento = [cliente,pelicula,'libro']

for e in elemento:
    match e:
        case {'nombre':nombre,
            'edad':edad,
            'ocupacion':ocupacion}:
            print('Es un cliente')
            print(nombre,edad, ocupacion)
        case {'titulo':titulo,
            'ficha_tecnica':{
                'protagonista':protagonista,
                'director':director}}:
            print("Es una pelicula")
            print(titulo, director, protagonista)
        case _:
            print('No pertenece al elemento')