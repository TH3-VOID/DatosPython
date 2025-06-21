# ----------------------- DICCIONARIOS -------------------
# Caracteristicas: No Ordenados, Heterogeneos, Mutables, Sin Repeticion (tomara el valor de la ultima repeticion)
diccionario = {"v1": 1, "v2": "2", "v3": True, 1: False, (1, 2): "tupla"}
print(diccionario)

# ----------------------- ELIMINAR ------------------
diccionario.pop("v1")  # metodo 1 para eliminar dato
del diccionario["v2"]  # metodo 2 para eliminar dato
# diccionario.clear()  # elimina todos los datos del diccionario
print(diccionario)

# ----------------------- EDITAR / AGREGAR ------------------
# editar un dato o agregar un nuevo dato, depende si ya existe la key o no
diccionario["v1"] = 2
print(diccionario)
# Actualiza el valor de la key, si no existe la crea
diccionario.update({"v2": 5})
print(diccionario)

# ----------------------- ITERAR ------------------
# forma 1: encontrar si existe una key espcifica
if "v1" in diccionario:
    print(diccionario["v1"])
else:
    print("No se ha encontrado dentro")

# forma 2: iterar y imprimir keys y valores
for key, valor in diccionario.items():
    print(key, valor)


usuarios = [
    {"id": 1, "Nombre": "Juan", "edad": 22},
    {"id": 2, "Nombre": "Elmer", "edad": 21},
    {"id": 3, "Nombre": "Diego", "edad": 20},
]
# forma 3: iterar y acceder a un valor especifico
for usuario in usuarios:
    print(usuario["Nombre"])


# ----------------------- FUNCIONES ------------------
# Devuelve una lista con las claves
diccionario.keys()
print(diccionario.keys())
# Devuelve una lista con los valores
diccionario.values()
print(diccionario.values())
# Devulve una lista de duplas con los pares de datos [(key,dato),(key,dato)...]
diccionario.items()
print(diccionario.items())
# Eliminar una clave y su valor
diccionario.pop("v1")
print(diccionario)
# Obtener los datos sin que truene el codigo, ocupamos get y la key, devuelve "None" si es que no encuentra los datos
print(diccionario.get("x"))
# puedes pasar un valor por defecto en caso de que el primero no este
print(diccionario.get("x", "v3"))
# copiar el diccionario
diccionario2 = diccionario.copy()
