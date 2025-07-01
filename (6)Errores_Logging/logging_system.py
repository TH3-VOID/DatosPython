"""
Logger Avanzado para Aplicaciones Python
----------------------------------------
Este módulo proporciona un sistema de registro (logging) robusto y fácil de usar.
Registra eventos de la aplicación en un archivo con formato claro, manejando errores
y creando automáticamente la estructura de directorios necesaria.

Características principales:
1. Singleton pattern: Una sola instancia de logger en toda la aplicación
2. Auto-creación de directorios de logs
3. Formato de tiempo y mensaje estandarizado
4. Manejo seguro de errores en el propio logger
5. Soporte para múltiples niveles de registro (debug, info, warning, error, critical)

Uso básico:
Logger.add_to_log("info", "Mensaje informativo")
Logger.add_to_log("error", "Algo salió mal")

Autor: Elmer Tolentino Cabrera
Versión: 1.0
"""

# Importación de herramientas necesarias
# -------------------------------------
import logging  # Módulo principal para el sistema de registro
import os  # Para trabajar con carpetas y rutas de archivos
import traceback  # Para obtener detalles técnicos cuando hay errores


class Logger:
    """
    La fábrica de diarios digitales
    -------------------------------
    Esta clase gestiona todo el sistema de registro usando el patrón Singleton
    (solo existe un diario principal aunque lo intentes crear múltiples veces)
    """

    # Variable de clase para almacenar la única instancia del diario
    # Inicialmente vacía (None) porque aún no se ha creado
    _logger = None

    @classmethod
    def __get_logger(cls):
        """
        Constructor interno del diario (Método privado)
        -----------------------------------------------
        Responsabilidades:
        1. Verificar si el diario ya existe
        2. Si no existe, crear toda la infraestructura:
           - Carpeta de logs
           - Archivo de registro principal
           - Formato de las entradas
        3. Devolver el diario listo para usar
        """

        # PASO 1: Verificar si ya tenemos un diario creado
        # -----------------------------------------------
        if cls._logger is not None:
            # Si ya existe, lo devolvemos inmediatamente
            return cls._logger

        # PASO 2: Configurar rutas y directorios
        # --------------------------------------
        # Ruta de la carpeta donde guardaremos los archivos de registro
        log_dir = "(6)Errores_Logging/logs"  # Directorio principal

        # Combinar carpeta y nombre de archivo (compatible con Windows/Mac/Linux)
        log_file = os.path.join(log_dir, "app.log")

        # Asegurar que la carpeta exista - CRÍTICO PARA EVITAR ERRORES
        # Si la carpeta no existe, la crea automáticamente
        # exist_ok=True significa: "No muestres error si ya existe"
        os.makedirs(log_dir, exist_ok=True)

        # PASO 3: Crear el diario (logger) principal
        # ------------------------------------------
        # Obtener o crear un diario con nombre identificador "AppLogger"
        cls._logger = logging.getLogger("AppLogger")

        # Configurar el nivel de captura MÍNIMO (DEBUG = captura todo)
        # Niveles: DEBUG < INFO < WARNING < ERROR < CRITICAL
        cls._logger.setLevel(logging.DEBUG)

        # PASO 4: Crear el "escritor" para archivos
        # -----------------------------------------
        # FileHandler es el empleado que escribe en el archivo físico
        file_handler = logging.FileHandler(log_file, encoding="utf-8")

        # Nivel para este escritor (DEBUG = escribe todos los mensajes)
        file_handler.setLevel(logging.DEBUG)

        # PASO 5: Diseñar el formato de las entradas
        # ------------------------------------------
        # Creamos una plantilla para cada entrada del diario:
        # - %(asctime)s: Fecha y hora
        # - %(levelname)s: Nivel del mensaje (INFO, ERROR, etc.)
        # - %(message)s: El mensaje en sí
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",  # Estructura
            "%Y-%m-%d %H:%M:%S",  # Formato de fecha: Año-Mes-Día Hora:Minuto:Segundo
        )

        # Asignar esta plantilla al escritor de archivos
        file_handler.setFormatter(formatter)

        # PASO 6: Conectar el escritor al diario
        # --------------------------------------
        # Verificar si el diario ya tiene escritores asignados
        if not cls._logger.hasHandlers():
            # Si no tiene, agregamos nuestro escritor de archivos
            cls._logger.addHandler(file_handler)

        # Devolver el diario completamente configurado
        return cls._logger

    @classmethod
    def add_to_log(cls, level, message):
        """
        Añadir una entrada al diario (Método público)
        --------------------------------------------
        Parámetros:
        level (str): Tipo de entrada ('debug', 'info', 'warning', 'error', 'critical')
        message (str): Texto descriptivo del evento

        Este método es a prueba de errores: si falla el registro,
        mostrará información en la consola sin detener la aplicación.
        """
        try:
            # OBTENER EL DIARIO
            # -----------------
            # Llama al constructor interno (lo crea si es la primera vez)
            logger = cls.__get_logger()

            # DICCIONARIO DE NIVELES - TRADUCTOR DE IMPORTANCIA
            # ------------------------------------------------
            # Relaciona palabras clave con funciones específicas:
            log_levels = {
                "critical": logger.critical,  # Eventos catastróficos
                "debug": logger.debug,  # Detalles técnicos
                "error": logger.error,  # Errores recuperables
                "info": logger.info,  # Información normal
                "warning": logger.warning,  # Advertencias
            }

            # SELECCIONAR LA FUNCIÓN CORRECTA
            # -------------------------------
            # Convertir el nivel a minúsculas para ser flexible (acepta "ERROR", "error", etc.)
            # Si no reconoce el nivel, usa "info" por defecto
            log_function = log_levels.get(level.lower(), logger.info)

            # ESCRIBIR LA ENTRADA EN EL DIARIO
            # -------------------------------
            # Ejecuta la función seleccionada con el mensaje
            log_function(message)

        except Exception as e:
            # MANEJO DE EMERGENCIAS - SI EL REGISTRO FALLA
            # -------------------------------------------
            # Esto captura cualquier error en el propio sistema de registro

            # 1. Mostrar mensaje de error claro en consola
            print(f"🚨 FALLO EN EL SISTEMA DE REGISTRO: {str(e)}")

            # 2. Imprimir informe técnico para diagnóstico
            print(traceback.format_exc())
