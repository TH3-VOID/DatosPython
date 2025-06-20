"""
Ejercicio 29: Conversión Celsius-Fahrenheit
Descripción:
Crea una función que reciba una lista de temperaturas en Celsius y regrese una nueva 
lista con las temperaturas en Fahrenheit.

Pistas:
- Recuerda la fórmula: F = C * 9/5 + 32.
- Usa una comprensión de listas.
"""
listF = list()
Cels = str(input("Ingrese los grados separados por comas : "))
listCels = list(Cels.strip().replace(","," ").split())
for grado in listCels: 
    faren = (float(grado)*9/5)+32
    listF.append(faren)
print(listF)
