import pandas as pd

tabla = pd.read_csv(r'C:\Case\Python-MinTic\Archivos_Ejemplo\VentasTotales1.csv', delimiter=';', encoding='latin1', skiprows=5)

print(tabla.index[2])

print(tabla.set_index('Vendedor'), inplace=True)

print(tabla.reset_index(inplace=True))