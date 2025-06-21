"""
Ejercicio 3: Menú interactivo con match
Objetivo: Practicar match/case y bucles.
Instrucciones:

Mostrá este menú hasta que el usuario elija salir:
- 1. Saludar
- 2. Mostrar fecha actual
- 3. Salir
Usá match para decidir qué hacer según la opción.
"""

import os
import datetime
import time

while True:
    try:
        os.system("cls")
        print("Menú:\n" "1. Saludar\n" "2. Mostrar fecha actual\n" "3. Salir")
        opcion = int(input("Ingrese la opcion: "))
        match opcion:
            case 1:
                nombre = str(input("Ingrese su nombre: "))
                print(f"Hola {nombre}, ¡bienvenido!")
                time.sleep(2)
            case 2:
                fecha_actual = datetime.datetime.now()
                print(f"Fecha actual: {fecha_actual.strftime('%Y-%m-%d')}")
                time.sleep(2)
            case 3:
                print("Saliendo del programa...")
                break
    except ValueError:
        print("Ingrese un valor válido.")
        time.sleep(5)
