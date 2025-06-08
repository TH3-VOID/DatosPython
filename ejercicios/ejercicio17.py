import os as os
import time as t
import random as rd
import string  # Necesario para generar letras aleatorias

palabras = []
palabrasUser = []

# Generar 5 palabras aleatorias
for i in range(5):  # Cambié a range(5) porque range(1,6) hace 5 iteraciones pero empieza en 1
    longitud = rd.randint(5, 10)
    palabra = ''.join(rd.choices(string.ascii_lowercase, k=longitud))
    print(palabra)
    t.sleep(3)
    os.system("cls")
    palabras.append(palabra)

# Pedir al usuario que ingrese las palabras
for i in range(len(palabras)):  # Mejor usar el largo real de la lista
    # Agregué lower() y strip()
    entrada = input(f"Palabra {i+1}: ").lower().strip()
    palabrasUser.append(entrada)

# Verificar respuestas
for n in range(len(palabras)):
    if palabras[n] == palabrasUser[n]:
        print(f"Palabra {n+1}: Correcto (era '{palabras[n]}')")
    else:
        print(
            f"Palabra {n+1}: Incorrecto (era '{palabras[n]}', dijiste '{palabrasUser[n]}')")
