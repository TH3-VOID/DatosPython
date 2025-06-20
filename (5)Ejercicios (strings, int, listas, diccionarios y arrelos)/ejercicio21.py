"""
Ejercicio 21: Filtrar y convertir listas
Descripción:
Tienes una lista de números enteros. Crea una nueva lista con sólo los números pares 
multiplicados por 3.
Pistas:
- Usa una comprensión de listas ([ ]).
- Recuerda el operador % para saber si un número es par.
- Multiplica por 3 sólo los que sean pares.
"""
import random as rd
NumInt=[]
for i in range(101):
    NumInt.append(rd.randint(1,1000))
NewList = [numero for numero in NumInt if numero%2==0 and numero%3==0]
print(NewList)
