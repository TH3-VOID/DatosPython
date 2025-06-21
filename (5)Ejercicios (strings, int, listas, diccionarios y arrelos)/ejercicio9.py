"""
Ejercicio 4: Conversor de texto
Objetivo: Practicar manipulación de strings.
Instrucciones:

Hacé una función que reciba una cadena y:
-La convierta a mayúsculas
-La invierta (Hola → aloH)
- Reemplace las vocales por *
-Mostrá los tres resultados.
"""


def convertir_texto(cadena):
    mayusculas = cadena.upper()
    invertida = cadena[::-1]
    reemplazada = (
        cadena.replace("a", "*")
        .replace("e", "*")
        .replace("i", "*")
        .replace("o", "*")
        .replace("u", "*")
    )
    return mayusculas, invertida, reemplazada


cadena = str(input("Ingrese una cadena: "))
resultado = convertir_texto(cadena)
print(f"Mayúsculas: {resultado[0]}")
print(f"Invertida: {resultado[1]}")
print(f"Reemplazada: {resultado[2]}")
