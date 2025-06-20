"""
Ejercicio 1: Lista de tareas
Objetivo: Practicar listas, input, bucles y match/case.
Instrucciones:

Inicializá una lista vacía tareas = [].

- Mostrá un menú que permita:
-- Agregar tarea
-- Mostrar todas las tareas
-- Eliminar una tarea por nombre
-- Salir
"""
import os
import time

tareas = []
while True:
    try:
        os.system("cls")
        print("Seleccione una opcion a realizar: \n"
              "1. Agregar tarea\n"
              "2. Mostrar todas las tareas\n"
              "3. Eliminar una tarea por nombre\n"
              "4. Salir")
        print("--------------------------------------------------")
        tarea = int(input("Ingrese la opcion que desea realizar: "))

        match tarea:
            case 1:
                os.system("cls")
                newTask = str(input("Ingrese la nueva tarea a realizar: "))
                tareas.append(newTask)
                print(f"Tarea {newTask} agregada correctamente.")
                time.sleep(2)
            case 2:
                os.system("cls")
                if tareas:
                    print("Tareas pendientes:")
                    for i, tarea in enumerate(tareas, start=1):
                        print(f"{i}. {tarea}")
                else:
                    print("No hay tareas para mostrar.")
                time.sleep(2)
            case 3:
                os.system("cls")
                if tareas:
                    TaskDelete = str(
                        input("Ingrese el nombre de la tarea a eliminar: "))
                    try:
                        tareas.remove(TaskDelete)
                        print(f"Tarea {TaskDelete} eliminada correctamente.")
                    except Exception as e:
                        print(f"No se pudo eliminar la tarea: {e}")
                else:
                    print("No hay tareas para eliminar.")
                time.sleep(2)
            case 4:
                print("Saliendo del programa...")
                break
    except ValueError:
        print("Ingrese un valor valido")
