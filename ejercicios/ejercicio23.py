"""
Ejercicio 23: Conversión de listas a diccionario
Descripción:
Tienes dos listas: una con nombres y otra con teléfonos. Junta ambas en un solo diccionario 
donde el nombre sea la clave y el teléfono el valor.

Pistas:
- Usa la función zip() para unir ambas listas.
- Crea el diccionario usando dict().
"""

Telefono = [1212121212,6666666666,9898989898,9393939393,3232323232]
Nombres = ["Elmer","Diego", "Yuresmy", "Alex", "Leonardo"]
dic = dict()
for i, nombre in enumerate(Nombres, start=0):
    dic.update({nombre:Telefono[i]})
print(dic)