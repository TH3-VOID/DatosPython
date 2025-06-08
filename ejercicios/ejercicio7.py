"""
🔹 Ejercicio 2: Validador de contraseñas
Objetivo: Practicar if, funciones, y manejo de errores.
Instrucciones:

- Escribí una función validar_contraseña(cadena) que verifique:
- Mínimo 8 caracteres
- Al menos una mayúscula
- Al menos un número
- Al menos un carácter especial (@, #, $, etc.)

Si no cumple, devolvé un mensaje indicando qué falla.
"""


def validar_cotraseña(cadena):
    if len(cadena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not any(char.isupper() for char in cadena):
        return "La contraseña debe contener al menos una letra mayúscula."
    if not any(char.isdigit() for char in cadena):
        return "La contraseña debe contener al menos un número."
    if not any(char in "@#$%&*!" for char in cadena):
        return "La contraseña debe contener al menos un carácter especial (@, #, $, etc.)."

    return "Contraseña válida."


print("Escribre 0 para salir del programa")
while True:
    try:
        cadena = str(input("Ingrese la contraseña a validar: "))
        if cadena == "0":
            print("Ha salido del programa")
            break
        print(validar_cotraseña(cadena))
    except Exception as e:
        print(f"Ingrese un valor válido, tipo de error: {e}")
        continue
