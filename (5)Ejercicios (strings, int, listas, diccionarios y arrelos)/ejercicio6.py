"""
Objetivo: Practicar strings, bucles y condiciones.
Instrucciones:
- Pedí al usuario una cadena.
- Contá cuántas vocales (a, e, i, o, u) hay.
- Mostrá cuántas veces aparece cada vocal.
"""

cadena = str(input("Ingrese una cadena: ")).lower().replace(" ", "")
print(
    f"a: {cadena.count('a')}, e: {cadena.count('e')}, i: {cadena.count('i')}, o: {cadena.count('o')}, u: {cadena.count('u')}"
)
