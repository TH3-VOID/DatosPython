"""
Ejercicio 27: Ordenar un diccionario por valores
Descripción:
Tienes un diccionario con nombres de personas y su edad. Ordena e imprime las personas de mayor
a menor edad.

Pistas:
- Usa la función sorted() con el parámetro key.
- Recuerda que items() te da pares (clave, valor).
"""

diccionary = [
    {"Nombre": "Juan", "Edad": 22},
    {"Nombre": "Elmer", "Edad": 33},
    {"Nombre": "Antonela", "Edad": 22},
    {"Nombre": "Carmela", "Edad": 25},
]
# Ordenar la lista de diccionarios por la clave "Edad" de mayor a menor
newdic = sorted(diccionary, key=lambda x: x["Edad"], reverse=True)

# Imprimir los resultados
for persona in newdic:
    print(f"{persona['Nombre']}: {persona['Edad']}")
