import pandas as pd

tabla = pd.read_csv(r'C:\Case\Python-MinTic\Archivos_Ejemplo\VentasTotales1.csv', delimiter=';', encoding='latin1')

print(tabla.head(4))