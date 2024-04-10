import pandas as pd

tabla = pd.read_csv(r'C:\Case\Python-MinTic\Archivos_Ejemplo\VentasTotales1.csv',delimiter=';', encoding='latin1', skiprows=5)

print(tabla)

print(tabla.Articulo=='Gorras')

print(tabla[tabla.Articulo == 'Gorras'])
