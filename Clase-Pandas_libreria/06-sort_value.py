import pandas as pd

tabla = pd.read_csv(r'C:\Case\Python-MinTic\Archivos_Ejemplo\Titanic.csv', encoding='utf-8')

print("Esta es la tabla:    ")
print(tabla.head(5))
print(tabla.Pclass.sort_values()) 
# Cuenta la frecuencia de los datos en una columna. Devuele una serie con los indices de los datos unicos y su frecuencia.