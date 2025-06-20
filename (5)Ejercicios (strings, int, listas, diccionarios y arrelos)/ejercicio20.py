"""
Ejercicio 20: Contador de palabras únicas
Descripción:
Dado un texto (string), obtén todas las palabras únicas, ignora mayúsculas/minúsculas 
y muestra cuántas veces aparece cada palabra.
Pistas:

- Puedes usar .lower() para normalizar.
    el valor la cantidad de veces que aparece.
- Puedes recorrer con un for la lista de palabras.
"""
import os
diccionario = list()
def palabras(): 
    cadenaPalapbras = str(input("Ingrese una cadena de palabras: "))
    palabras = list(
        cadenaPalapbras.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
        .lower().replace(",","").replace(":","").replace("(","").replace(")","").replace(".","").split())
    
    os.system("clear")

    for palabra in palabras:
        encontrada = False
        for item in diccionario:
            if item["Palabra"] == palabra:
                item["Num"] +=1
                encontrada = True
                break
        if not encontrada:
            diccionario.append({"Palabra": palabra, "Num": 1})

    for i,datos in enumerate(diccionario,start=1):
        print(f"{datos["Palabra"]}:{datos["Num"]}")

palabras()