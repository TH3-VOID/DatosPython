import logging
import os
import traceback


class Logger:
    _logger = None

    @classmethod
    def __get_logger(cls):
        if cls._logger is not None:
            return cls._logger

        try:
            # Corrección 1: Usar la ruta absoluta del directorio actual
            log_dir = os.path.dirname(os.path.abspath(__file__))
            log_file = os.path.join(log_dir, "app.log")

            # Corrección 2: Asegurar que el archivo existe y tiene permisos
            if not os.path.exists(log_file):
                with open(log_file, "w"):
                    os.chmod(log_file, 0o666)  # Permisos de lectura/escritura

            cls._logger = logging.getLogger("AppLogger")
            cls._logger.setLevel(logging.DEBUG)

            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s", "%Y-%m-%d %H:%M:%S"
            )
            file_handler.setFormatter(formatter)

            # Corrección 3: Limpiar handlers existentes antes de agregar
            cls._logger.handlers = []
            cls._logger.addHandler(file_handler)

            return cls._logger

        except Exception as e:
            print(f"🚨 ERROR AL CONFIGURAR LOGGER: {str(e)}")
            print(traceback.format_exc())
            raise

    @classmethod
    def add_to_log(cls, level, message):
        try:
            logger = cls.__get_logger()
            log_levels = {
                "critical": logger.critical,
                "debug": logger.debug,
                "error": logger.error,
                "info": logger.info,
                "warning": logger.warning,
            }
            log_func = log_levels.get(level.lower(), logger.info)
            log_func(message)

            # Corrección 4: Forzar escritura inmediata
            for handler in logger.handlers:
                handler.flush()

        except Exception as e:
            print(f"🚨 FALLO AL ESCRIBIR EN LOG: {str(e)}")
            print(traceback.format_exc())
