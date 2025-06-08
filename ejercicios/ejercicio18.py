"""
Ejercicio 8: Eliminar duplicados
Objetivo: Listas, funciones.
Instrucciones:
1. Ingresá una lista con elementos repetidos (pueden ser números o palabras).
2. Mostrá la lista sin duplicados pero manteniendo el orden original.
Tip: set() no mantiene orden, pero hay otros métodos…
"""

import os
import time


def eiliminar_duplicados(lista):
    Elementos_sin_duplicados = []
    for elemento in lista:
        if elemento not in Elementos_sin_duplicados:
            Elementos_sin_duplicados.append(elemento)
    for i, element in enumerate(Elementos_sin_duplicados, start=1):
        print(f"{i}: {element}")


while True:
    try:
        entrada = str(input(
            "Ingrese una cadena de texto o numeros (Cada elemento separado de otro): "))
        lista = entrada.replace(',', "").split()
        accion = int(input("Ingerse la opcion que desea realizar: \n"
                           "1. Eliminar duplicados\n"
                           "2. Salir\n"))
        match accion:
            case 1:
                os.system("cls")
                eiliminar_duplicados(lista)
                time.sleep(3)
                os.system("cls")
            case 2:
                os.system("cls")
                print("Saliendo del programa...")
                break

    except ValueError:
        print("Entrada no valida ingrese un valor correcto")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
