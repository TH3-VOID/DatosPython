""""
Ejercicio 2: Promedio de calificaciones
Objetivo: Listas, funciones, try/except.
Instrucciones:

1. Pedí al usuario que ingrese varias calificaciones separadas por comas.
2. Convertí esa entrada en una lista de números.
3. Calculá:
- Promedio
- Calificación máxima
- Calificación mínima

4. Mostrá los resultados con una función.

Tip: split(','), float(), sum(), len(), max(), min().
"""

while True:
    try:
        entrada = str(
            input("Ingrese las calificacionesc separadas por comas: "))
        if entrada.lower() == 'salir':
            print("Saliendo del programa...")
            break
        Calificaciones = [float(cal)
                          for cal in entrada.split(',') if float(cal) > 0 and float(cal) <= 10]
        if Calificaciones:
            Promedio = sum(Calificaciones)/len(Calificaciones)
            maximo = max(Calificaciones)
            minimo = min(Calificaciones)
            print(
                f"Promedio: {Promedio:.2f} \n Calificación máxima: {maximo} \n Calificación mínima: {minimo}")
    except ValueError:
        print("Por favor, ingrese calificaciones válidas separadas por comas.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
