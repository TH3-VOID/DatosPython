"""
Crea un programa que pida al usuario que introduzca su nombre y su edad.Imprima un mensaje
dirigido a ellos que les diga el año en que cumplirán 100 años. Nota: para este ejercicio,
se espera que escribas explícitamente el año(y, por lo tanto, que esté desactualizado el año siguiente).
"""

yearActual = 2025

nombre = str(input("Introdusca su Nombre completo: "))
Edad = int(input("Introduzca su edad actual: "))

print(f"{nombre} cumpliras 100 años en el año {(yearActual)+(100-Edad)}")
