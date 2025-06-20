"""
Ejercicio 28: Buscador en listas de diccionarios
Descripción:
Dada una lista de diccionarios de empleados (con claves: "nombre", "puesto", "sueldo"), 
pide al usuario un puesto y muestra todos los empleados con ese puesto.

Pistas:
- Usa un bucle para recorrer la lista.
- Verifica si el valor de la clave "puesto" coincide con lo que pide el usuario.


"""

empleados = [
    {"nombre": "Ana López", "puesto": "Analista", "sueldo": 15000},
    {"nombre": "Juan Pérez", "puesto": "Desarrollador", "sueldo": 20000},
    {"nombre": "Carla Ramírez", "puesto": "Desarrollador", "sueldo": 21000},
    {"nombre": "Luis Gómez", "puesto": "Soporte", "sueldo": 13000},
    {"nombre": "Sofía Ruiz", "puesto": "Analista", "sueldo": 15500},
    {"nombre": "Mario Mendoza", "puesto": "Gerente", "sueldo": 30000},
    {"nombre": "Paola Méndez", "puesto": "Soporte", "sueldo": 13500},
    {"nombre": "Roberto Campos", "puesto": "Desarrollador", "sueldo": 22000},
    {"nombre": "Gloria Vela", "puesto": "Analista", "sueldo": 16000}
]

puesto_buscar = str(input("Ingrese el puesto que desea buscar: "))
empleados_encontrados = [empleado for empleado in empleados 
                         if empleado["puesto"].lower() == puesto_buscar.strip().lower() ]
if empleados_encontrados:
    print(f"Empleados con el puesto de {puesto_buscar}: ")
    for empleado in empleados_encontrados:
        print(f"Nombre: {empleado["nombre"]}, sueldo: {empleado["sueldo"]}")
