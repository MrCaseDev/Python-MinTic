import pandas as pd

tabla = pd.read_csv(r'C:\Case\Python-MinTic\Archivos_Ejemplo\VentasTotales1.csv', delimiter=';', encoding='latin1')
# tabla['Nombre']
# tabla['Nombre','Edad']
# tabla.Edad

#type(tabla)

print(tabla.shape)
print(tabla.shape[0])
print(tabla.shape[1])
print(tabla)