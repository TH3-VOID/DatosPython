"""
Ejercicio 5: Analizador de palabras
Objetivo: Listas + manipulación de strings.
Instrucciones:

1. Pedí al usuario una lista de palabras.
2. Mostrá estadísticas:
 - Cuántas tienen más de 7 letras
 - Cuántas terminan en "s"
 - Cuántas tienen números

Tip: isalpha(), isdigit(), endswith().
"""


def tiene_mas_de_7_letras(palabras):
    palabrasMasDe7 = [palabra for palabra in palabras if len(palabra) > 7]
    print(f"La palabras con mas de 7 letras son: {', '.join(palabrasMasDe7)}")


def terminan_en_s(palabras):
    endWithS = [palabra for palabra in palabras if palabra.endswith("s")]
    print(f"Las palabras que terminan en 's' son: {', '.join(endWithS)}")


def contiene_numeros(palabras):
    NumbersInWords = [
        palabra for palabra in palabras if any(char.isdigit() for char in palabra)
    ]
    print(f"Las palabras que contienen números son: {', '.join(NumbersInWords)}")


try:
    cadena = input("Ingrese una lista de palabras separadas por comas: ")
    palabras = cadena.replace(" ", "").split(",")
    print(palabras)
    if palabras:
        tiene_mas_de_7_letras(palabras)
        terminan_en_s(palabras)
        contiene_numeros(palabras)
        print("Operaciones completadas.")
    else:
        print("No se ingresaron palabras válidas.")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
