import traceback as tb
from logging_system import Logger as lg


class Libros:
    _libros = []

    def __init__(self) -> None:
        pass

    @classmethod
    def Addlibro(cls, titulo: str, Autor: str, ISB: int) -> bool:
        try:
            cls._libros.append(
                {"titulo": titulo, "autor": Autor, "SBN": ISB, "prestado": False}
            )
            lg.add_to_log("info", "Libro agregado correctamente")
            return True
        except Exception as e:
            print(f"Error del tipo: {e}, al tratar de ingresar la el libro")
            lg.add_to_log("warning", tb.format_exc())
            return False

    @classmethod
    def PresLibro(cls, sbn: int) -> bool:
        existe = False
        if cls._libros:
            for libro in cls._libros:
                if libro["SBN"] == sbn & libro["prestado"] == False:
                    existe = True
                    libro["prestado"] = True
        return existe

    @classmethod
    def devLibro(cls, sbn: int) -> tuple[bool, bool]:
        devuelto = False
        existe = False
        if cls._libros:
            for libro in cls._libros:
                if libro["SBN"] == sbn & libro["prestado"] == True:
                    libro["prestado"] = False
                    devuelto = True
                    existe = True
        return existe, devuelto

    @classmethod
    def get_libros(cls) -> list:
        return cls._libros

    @classmethod
    def encontrarExistencia(cls, sbn: int) -> tuple[bool, bool, bool]:
        try:
            prestado = False
            existe = False
            ejecucionCorrecta = True
            if cls._libros:
                for libro in cls._libros:
                    if libro["SBN"] == sbn:
                        existe = True
                    if libro["prestado"] == True & libro["SBN"] == sbn:
                        prestado = True
            return existe, prestado, ejecucionCorrecta
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
            lg.add_to_log("warning", e)
            lg.add_to_log("warning", tb.format_exc())
            return False, False, False
