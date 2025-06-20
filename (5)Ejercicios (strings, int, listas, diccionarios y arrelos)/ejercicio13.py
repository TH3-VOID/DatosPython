"""
Ejercicio 3: Filtrar palabras
Objetivo: Listas + strings + funciones.
Instrucciones:

1. Ingresá una frase.
2. Dividila en palabras.
3. Mostrá solo las palabras que:
 - Tienen más de 5 letras
 - Empiezan con vocal
 - Son palíndromos

Tip: staramatswith(), [::-1], función para detectar palíndromos.
"""


def es_palindromo(cadena):
    es_palindromo = []
    for palabra in cadena:
        palabra = palabra.lower()
        if palabra == palabra[::-1]:
            es_palindromo.append(palabra)
    print(f"Palabras palíndromas: {', '.join(es_palindromo)}")


def palabras_con_mas_de_5_letras(cadena):
    palabras_con_mas_de_5_letras = []
    for palabra in cadena:
        if len(palabra) > 5:
            palabras_con_mas_de_5_letras.append(palabra)
    print(
        f"Palabras con más de 5 letras: {', '.join(palabras_con_mas_de_5_letras)}")


def palabras_que_empiezan_con_vocal(cadena):
    palabras_que_empiezan_con_vocal = []
    for palabra in cadena:
        if palabra[0].lower() in 'aeiou':
            palabras_que_empiezan_con_vocal.append(palabra)
    print(
        f"Palabras que empiezan con vocal: {', '.join(palabras_que_empiezan_con_vocal)}")


while True:
    try:
        frase = input("Ingrese una frase (o 'salir' para terminar): ")
        if frase.lower() == 'salir':
            print("Saliendo del programa...")
            break
        palabras = frase.replace(',', '').split()
        es_palindromo(palabras)
        palabras_con_mas_de_5_letras(palabras)
        palabras_que_empiezan_con_vocal(palabras)
        print("Operaciones completadas.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        break
