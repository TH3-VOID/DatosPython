"""
Ejercicio 24: Eliminar duplicados y ordenar
Descripción:
Recibe una lista de números con duplicados. Devuelve una nueva lista sin duplicados 
y ordenada de menor a mayor.

Pistas:
- Usa un set para quitar duplicados.
- Convierte de nuevo a lista y usa .sort() o sorted().
"""
import random as rd
numeros = [rd.randint(1,10) for _ in range(20)]
print(numeros)
numeros =list(set(numeros))
numeros.sort()
print(numeros)
