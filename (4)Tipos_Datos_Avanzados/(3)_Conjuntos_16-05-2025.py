# ----------------------- CONJUNTOS -------------------
# Caracteristicas: No Ordenados, Heterogeneos, Mutables, Sin Repeticion
conjunto1 = set()  # se inicializa y esta vacio
conjunto1 = set([1, 2, 3, 4, 5, 6, 7, 10, 1.25, "Aguila"])
conjunto2 = set(["Agula", "tortuga", "Coyote", "Perro",
                "Coca", "Pepsi", "Manzada", 2, 1.25])
conjunto3 = {True, False, 1.25, 3.488, 0.999, "Aguila", 2}

# ----------------------- AGREGAR / EDITAR -------------------
# Añadir algun elemento
conjunto2.add(10)
if "tortuga" in conjunto2:
    conjunto2.remove("tortuga")
    conjunto2.add("Tortuga")
print(f"Con el elemento removido y la nueva adicon: {conjunto2}")
# ----------------------- ELIMINAR -------------------
# Eliminar elemento
conjunto1.remove(1)
# Hace lo mismo solo que este si no lo encuentra no marca error
conjunto3.discard(True)
print(f"Despues de eliminar 1 de conjunto 1: {conjunto1}")
print(f"Despues de remover True de conjunto3: {conjunto3}")

# ----------------------- UNION -------------------
# Todos los elementos que aparecen en A o en B (o en ambos).
print("Union: ", conjunto1.union(conjunto2, conjunto3))
print("Union: ", conjunto1.union(conjunto2))
# | es lo mismo que con la funcion "union"
print("Union: ", conjunto2 | conjunto3)

# ----------------------- INTERSECCION -------------------
# Sólo los que están en AB, y los que estan en AC.
print(
    f"Interseccion: {conjunto1.intersection(conjunto2)}")
print(
    f"Interseccion: {conjunto1 & conjunto3}")

# ----------------------- DIFERENCIA -------------------
# Lo que está en conjunto1 pero no en conjunto3.
print(f"Diferencia: {conjunto2.difference(conjunto3)}")
print(f"Diferencia: {conjunto2 - conjunto3}")

# ----------------------- COMPLEMENTO -------------------
# Todo aquello que se encuentra en el universo y no lo tiene conjunto1
universo = {range(1, 11), 1.25, "Aguila"}
complemento = universo-conjunto1

# ----------------------- DIFERENCIA SIMETRICA ------------------
# Los que están en A o en B, pero no en ambos.
print(f"Diferencia simetrica: {conjunto1.symmetric_difference(conjunto2)}")
print(f"Diferencia simetrica: {conjunto2 ^ conjunto3}")

# ----------------------- SUBCONJUNTO ------------------
# ESTA CONTENIDO conjunto1 DENTRO DE conjunto2
print(
    f"esta contenido conjunto 1 dentro de conjunto 2: {conjunto1.issubset(conjunto2)}")

# ----------------------- SUPERCONJUNTO ------------------
# Conjunto1 contie a conjunto2
print(
    f"Conjunto1 contie a conjunto2: {conjunto1.issuperset(conjunto2)}")

# ----------------------- DISJUNTOS ------------------
# NO COMPARTEN NADA
print(
    f"Comparten elementos: {conjunto1.isdisjoint(conjunto2)}")
