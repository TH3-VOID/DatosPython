"""
Tomemos una lista, digamos por ejemplo esta:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y escribir un programa que imprima todos los elementos de la lista que sean menores que 5.

Extras:
1. En lugar de imprimir los elementos uno por uno, haga una nueva lista que tenga
todos los elementos menos de 5 de esta lista e imprima esta nueva lista.
2. Escribe esto en una línea de Python.
3. Pida al usuario un número y devuelva una lista que contenga solo elementos de la lista original que sean más pequeños que el número proporcionado por el usuario.a
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# def FiltroList(lista, filtro):
#     newlist = []
#     for dato in lista:
#         if dato < filtro:
#             newlist.append(dato)
#     return newlist
print("Escriba 0 para salir")
while True:
    try:
        num = int(input("Escriba un numero: "))
        if num == 0:
            break
        print([dato for dato in a if dato < num])
    except ValueError:
        print("No es un numero intente de nuevo")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
print("Usted ha salido")
