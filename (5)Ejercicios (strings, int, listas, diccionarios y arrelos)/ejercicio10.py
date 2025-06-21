""" "
Ejercicio 6: Adivina el número
Objetivo: Bucles, if, funciones, manejo de entrada.
Instrucciones:
- Generá un número aleatorio del 1 al 100.
- Pedí al usuario que lo adivine.
- Si el número es mayor o menor, indicá pistas.
- Terminá cuando adivine.
"""

import random


def adivinar_numero():
    numSecreto = random.randint(1, 100)
    return numSecreto


def jugar():
    numSecreto = adivinar_numero()
    intentos = 0

    while True:
        try:
            numero = int(input("Adivina el número (1-100): "))
            intentos += 1

            if numero < 1 or numero > 100:
                print("El número debe estar entre 1 y 100.")
                continue

            if numero < numSecreto:
                print("El número es mayor.")
            elif numero > numSecreto:
                print("El número es menor.")
            else:
                print(
                    f"¡Felicidades! Adivinaste el número {numSecreto} en {intentos} intentos."
                )
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")


jugar()
