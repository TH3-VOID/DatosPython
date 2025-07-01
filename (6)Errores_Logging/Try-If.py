"""
El manejo de excepciones en Python permite controlar errores durante la ejecución de un programa.

Tipo de Error	     |      Causa típica
ZeroDivisionError	    División entre cero
ValueError	            Valor inapropiado (ej: int("a"))
TypeError	            Operación con tipo incorrecto
IndexError	            Índice fuera de lista
KeyError	            Clave no existe en diccionario
FileNotFoundError	    Archivo no encontrado
ModuleNotFoundError	    Módulo no instalado
"""

import traceback as tb
from logging_system import Logger as lg

# ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError as zd:
    print("Error: División entre cero no permitida")
    lg.add_to_log("error", f"Intento de división por cero: {tb.format_exc()}")

# ValueError
try:
    numero = int("abc")
except ValueError as ve:
    print("Error: Valor no convertible a entero")

# typeError
try:
    suma = "10" + 5
except TypeError as tp:
    print("Error: Operación entre tipos incompatibles")

# 4. IndexError:
try:
    lista = [1, 2, 3, 4]
    print(lista[8])
except IndexError as fr:
    print("Error: Fuera del rango")

# 5. KeyError
try:
    diccionario = {"Numero": 2, "Nombre": "Elmer"}
    print(diccionario["Edad"])
except KeyError as ex:
    print("Error: Clave no existe en el diccionario")

# 6. FileNotFoundError
try:
    archivo = open("~/home/emptyman/Descargas/datos.docx")
except FileNotFoundError as e:
    print(f"Error: Archivo no encontrado: {e}")

# 7. ModuleNotFoundError
try:
    import moduloEjemplo as me
except ModuleNotFoundError as e:
    print(f"Error: Módulo no instalado o inexistente: {e}")


# Dame ejercicios para prcaticarlo chat (implementa listas o diccionarios o arreglos, para que pueda practicarlos), agrega pistas y elementos que se pueden ocupar pero no des el código completo, ya que yo tengo que hacer los ejercicios para pensar y resolver
