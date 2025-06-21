import random as rd
import os
import time as t


def obtenerPalabraSecreta() -> str:
    palabras = ["palabra", "python", "programacion", "ejercicio", "desafio", "codigo"]
    return rd.choice(palabras).upper()


def mostrarProgreso(palabra: str, letrasAdivinadas: list) -> str:
    progreso = ""
    for letra in palabra:
        if letra in letrasAdivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()


def juegoAhorcado() -> None:
    palabraSecreta = obtenerPalabraSecreta()
    letrasAdivinadas = []
    intentos = len(palabraSecreta)
    juegoTerminado = False

    print("¡Bienvenido al juego de adivinar la palabra secreta!")

    while not juegoTerminado:

        print(f"Tienes {intentos} intentos para adivinar la palabra secreta.")
        print("Palabra:", mostrarProgreso(palabraSecreta, letrasAdivinadas))
        letra = str(input("Ingresa una letra: ").upper())
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
        elif letra in letrasAdivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
        else:
            letrasAdivinadas.append(letra)
            if intentos > 0:
                if letra in palabraSecreta:
                    print("¡Bien hecho! La letra está en la palabra.")
                else:
                    intentos -= 1
                    print("Lo siento, esa letra no está en la palabra.")
            else:
                print("Lo siento, has perdido. La palabra era:", palabraSecreta)
                juegoTerminado = True
        if "_" not in mostrarProgreso(palabraSecreta, letrasAdivinadas):
            juegoTerminado = True
            print("Felicidades has concluido el juego la palabra era:", palabraSecreta)
        t.sleep(2)
        os.system("cls")


juegoAhorcado()
