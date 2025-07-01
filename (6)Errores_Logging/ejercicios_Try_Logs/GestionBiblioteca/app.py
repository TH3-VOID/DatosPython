from logging_system import Logger as lg
import os
import time as t
import traceback as tb
from Biblioteca import Biblioteca as bb


def main():
    while True:
        try:
            lg.add_to_log("info", "Se ha iniciado la aplicacion")
            print("----------------------------------------------------")
            print(
                "Biblioteca Antigua\n"
                "1. Agregar libros\n"
                "2. Prestar Libro\n"
                "3. Devolver libro\n"
                "4. Listar libros\n"
                "5. Buscar Existencia\n"
                "5. Salir"
            )
            print("----------------------------------------------------")
            value = int(input("Ingrese la opcion que desea realizar: "))
            match value:
                case 1:
                    os.system("clear")
                    bb.aggLibro()
                    t.sleep(2)
                    os.system("clear")
                case 2:
                    os.system("clear")
                    bb.presLibro()
                    t.sleep(2)
                    os.system("clear")
                case 3:
                    os.system("clear")
                    bb.regLibro()
                    t.sleep(2)
                    os.system("clear")
                case 4:
                    os.system("clear")
                    bb.listLibros()
                    t.sleep(2)
                    os.system("clear")
                case 5:
                    os.system("clear")
                    bb.SearchBook
                    t.sleep(2)
                    os.system("clear")
                case 6:
                    os.system("clear")
                    print("Programa terminado, saliendo...")
                    t.sleep(2)
                    break
        except ValueError as e:
            print(f"Por favor ingrese un valor valido")
            lg.add_to_log("warning", e)
            lg.add_to_log("warning", tb.format_exc())
            return 0
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            lg.add_to_log("warning", e)
            lg.add_to_log("warning", tb.format_exc())


main()
