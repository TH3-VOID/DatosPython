"""
Ejercicio 6: Historial de operaciones
Objetivo: Listas, funciones, try/except.
Instrucciones:
1. Creá una función que sume, reste, multiplique o divida dos números.
2. Guardá cada operación en una lista como string: "5 + 3 = 8".
3. Permití ver el historial completo al usuario.

Tip: try/except ZeroDivisionError, f-strings.
"""

import random as rd
import os as os
import time as t

historial = []


def obtenerID():
    id = int(rd.randint(1, 1000))
    if historial:
        for dato in historial:
            if dato[0] == id:
                obtenerID()
    return id


def insertHistorial(TipoOperacion, operacion, resultado):
    try:
        Tiempo = t.strftime("%Y-%m-%d %H:%M:%S")
        historial.append((obtenerID(), TipoOperacion, operacion, resultado, Tiempo))
        print("Datos insertados correctamente")
    except Exception as e:
        print(
            f"Ha ocurrido un problema de tipo: ({e}) al tratar de insertar la historia"
        )


def operaciones(TipoOperacion, Num1, Num2):

    try:
        match TipoOperacion:
            case 1:
                resultado = Num1 + Num2
                operador = "+"
            case 2:
                resultado = Num1 - Num2
                operador = "-"
            case 4:
                resultado = Num1 * Num2
                operador = "*"
            case 5:
                resultado = Num1 / Num2
                operador = "/"
        oper = f"{Num1} {operador} {Num2}"
        insertHistorial(TipoOperacion, oper, resultado)
        print("Operacion realizada con exito")
    except ZeroDivisionError:
        print("No se ha podido realizar la divicion por cero")
    except Exception as e:
        print(
            f"Ha ocurrido un problema de tipo: ({e}) al tratar de realizar la operacion"
        )


def showHistorial():
    try:
        if historial:
            for i, datos in enumerate(historial, start=1):
                print(
                    f"{i}. ID: {datos[0]}, Tipo de Operacion: {datos[1]}, Operacion: {datos[2]} = {datos[3]}, fecha: {datos[4]}"
                )
        else:
            print("No hay datos en el historial")
    except Exception as e:
        print(
            f"Ha ocurrido un problema de tipo: ({e}) al tratar de mostrar el historial"
        )


def inicio():

    while True:
        try:
            print("\nBienvenido ingrese la acción que desea realizar:")
            print("1. Operación")
            print("2. Ver historial")
            print("3. Salir")
            opcion = int(input("Opción: "))
            print("-------------------------------------------")
            match opcion:
                case 1:
                    os.system("cls")
                    print(
                        "Ingrese la operacion que desea realizar: \n1. Suma. \n2. Resta. \n3. Multiplicacion. \n4. Division"
                    )
                    operacion = int(input())
                    num1 = float(input("Ingrese el primer numero: "))
                    num2 = float(input("Ingrese el segundo numero: "))
                    operaciones(operacion, num1, num2)
                    t.sleep(2)
                case 2:
                    os.system("cls")
                    showHistorial()
                    t.sleep(4)
                case 3:
                    os.system("cls")
                    print("Gracias por usar el programa")
                    break
        except Exception as e:
            print(
                f"Ha ocurrido un problema de tipo: ({e}) al tratar de realizar la operacion"
            )


inicio()
