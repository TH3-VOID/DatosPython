"""
Ejercicio 1: Validador de Edad
Instrucciones:

- Solicita al usuario que ingrese su edad.
- Usa un try-except para asegurar que la entrada sea un número entero.
- Usa una estructura if-else para indicar si la persona es menor o mayor de edad.

"""

while True:
    num = int(input("Ingrese su edad:"))
    try:
        print("Escriba 0 para salir del programa")
        if num == 0:
            print("Ha salido del programa")
            break
        elif num >= 18:
            print("Usted es mayor de edad")
        else:
            print("Usted es menor de edad")
    except ValueError:
        print("Por favor ingrese valores numericos enteros")
