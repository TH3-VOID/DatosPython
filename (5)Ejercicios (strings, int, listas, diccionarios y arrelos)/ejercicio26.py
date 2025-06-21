"""
Ejercicio 26: Sumar matrices (listas de listas)
Descripción:
Recibe dos matrices (listas de listas de números del mismo tamaño) y devuelve una matriz suma.

Pistas:
- Usa dos bucles anidados (for).
- Suma elemento a elemento por su posición.
"""

matriz1 = [[2, 5, 4, 6], [4, 7, 2, 6]]
matriz2 = [[9, 34, 77, 21], [12, 10, 3, 22]]
resultadosMatriz = list()

for i, fila in enumerate(matriz1):
    sumas = list()
    for x, dato in enumerate(fila):
        sumas.append((dato + matriz2[i][x]))
    resultadosMatriz.append(sumas)

# otra forma, medio rara pero mas corta
# resultadosMatriz = [
#     [a + b for a, b in zip(fila1, fila2)]
#     for fila1, fila2 in zip(matriz1, matriz2)
# ]


print(resultadosMatriz)
