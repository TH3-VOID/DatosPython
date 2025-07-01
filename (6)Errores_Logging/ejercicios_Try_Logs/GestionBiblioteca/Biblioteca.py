from logging_system import Logger as lg
from Libros import Libros as l
import traceback as tb


class Biblioteca:
    _respuesta = None

    def __init__(self) -> None:
        pass

    @classmethod
    def aggLibro(cls) -> None:
        try:
            Titulo = str(input("Ingrese el titulo del libro: "))
            Autor = str(input("Ingrese el Nombre del Arutor: "))
            SBN = int(input("Ingrese el SBN: "))

            cls._respuesta = l.Addlibro(Titulo, Autor.strip().lower(), SBN)
            if cls._respuesta == True:
                print(f'Libro "{Titulo}" agregado correctamente')
                cls._respuesta = False
            else:
                print("No pudo agregarse correctamente el libro")
        except ValueError as ex:
            lg.add_to_log("warning", f"Ingrese un itpo de dato valido: {ex}")
            print(f"Tipo de dato no valido")
        except Exception as e:
            lg.add_to_log("warning", f"Error: {e}")
            lg.add_to_log("warning", tb.format_exc())

    @classmethod
    def presLibro(cls):
        try:
            SBN = int(input("Ingrese el SBN: "))
            prestado: bool = l.PresLibro(SBN)
            if prestado == True:
                print("Libro Prestado exitosamente")
            else:
                print("No se han encontrado existencias del libro")
        except ValueError as ex:
            lg.add_to_log("warning", f"Ingrese un itpo de dato valido: {ex}")
            print(f"Tipo de dato no valido")
        except Exception as e:
            lg.add_to_log("warning", f"Error: {e}")
            lg.add_to_log("warning", tb.format_exc())
        cls._respuesta = None

    @classmethod
    def regLibro(cls):
        try:
            SBN = int(input("Ingrese el SBN: "))
            devuelto: tuple = l.devLibro(SBN)
            if devuelto[0] == True & devuelto[1] == True:
                print("Libro devuelto exitosamente")
            else:
                print("No se han encontrado existencias del libro")
        except ValueError as ex:
            lg.add_to_log("warning", f"Ingrese un itpo de dato valido: {ex}")
            print(f"Tipo de dato no valido")
        except Exception as e:
            lg.add_to_log("warning", f"Error: {e}")
            lg.add_to_log("warning", tb.format_exc())
        cls._respuesta = None

    @classmethod
    def listLibros(cls):
        libros = l.get_libros()
        if libros:
            for i, libro in enumerate(libros, start=1):
                print(
                    f"{i}. Titulo: {libro["titulo"]}, Autor: {libro["autor"]}, SBN: {libro["SBN"]}"
                )
        else:
            print("Por el momento no tenemos existencias")

    @classmethod
    def SearchBook(cls):
        try:
            SBN = int(input("Ingrese el SBN: "))
            existencia: tuple = l.encontrarExistencia(SBN)
            if existencia[2] == True:
                if existencia[1] == True & existencia[2] == True:
                    estado = "Prestado" if existencia[1] == True else "En Stock"
                    print(f"Libro encontrado, Estado: {estado}")
                else:
                    print("Sin copias del libro")
            else:
                print("Error al procesar la peticion")
        except ValueError as ex:
            lg.add_to_log("warning", f"Ingrese un itpo de dato valido: {ex}")
            print(f"Tipo de dato no valido")
        except Exception as e:
            lg.add_to_log("warning", f"Error: {e}")
            lg.add_to_log("warning", tb.format_exc())
