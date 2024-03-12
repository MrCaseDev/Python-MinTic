print("***Programa: Calcula comisiones ****")
cNombre =input("Cuales tu nombre? => ")
nTotal_Ventas = float(input("Cual es el total de tus ventas al mes? => "))

nComision = round(nTotal_Ventas*13/100,2)

print(f"{cNombre} :Tu comisión mensual es de -> {nComision} pesos")