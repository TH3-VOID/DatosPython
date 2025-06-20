"""
Ejercicio 22: Diccionario de calificaciones
Descripción:
Dado un diccionario donde las llaves son nombres de estudiantes y los valores son listas de 
calificaciones (por ejemplo: {"Juan": [8, 9, 10], "Ana": [7, 8, 7]}), imprime el promedio de 
cada estudiante.

Pistas:
- Recorre el diccionario con un for.
- Calcula el promedio usando sum() y len().
- Muestra el resultado: nombre y promedio.
"""
calificaciones = [{"Nombre":"Elmer","Calificaciones":[9,6,7,9,10,8]},
                  {"Nombre":"Diego","Calificaciones":[9,6,7,7,5,8]},
                  {"Nombre":"Juan","Calificaciones":[8,7,7,9,9,4]}]

def CalcularProm(Alumno,iteration) -> None:
    promedio=  sum(Alumno["Calificaciones"])/len(Alumno["Calificaciones"])
    print(f"{i}. Nombre: {Alumno["Nombre"]}, Promedio: {promedio:.2}")

try:
    for i,alumno in enumerate(calificaciones,start=1):
        CalcularProm(Alumno=alumno, iteration= i)
except Exception as e:
    print(f"Ha ocurrido un error del tipo {e}")
