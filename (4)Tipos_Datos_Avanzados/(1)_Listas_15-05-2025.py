# ----------------- LISTAS------------------
# ---------------- CREAR -----------------------
# Caracteristicas: Ordenados, Heterogeneos, Mutables, Con repeticion
LISTA = [1, "perro", True, 22, "gato", "dato", 1.22]
# Crea 10 veces el 0 y la A
lista = [0, "A"] * 10
# crear una lista de listas
Superlist = lista + LISTA
lisT = list(range(10))
lisT = list(range(1, 11))  # del 1 al 10
listNum = list(range(1, 11) * 2)


# ---------------- AGREGAR / INSERTAR -----------------------
# Te permite agregar un nuevo dato al final de la lista
LISTA.append(5)
# te permite insertar un dato en el indice asignado
LISTA.insert(1, "posicion 1")
# Asignas los datos de la lista a variables
v1, v2, v3, v4, *todos = listNum
print(v1, v2, v3, v4, *todos)
v1, v2, *todos, v9, v10 = listNum
print(v1, v2, v9, *todos, v10)
usuarios = [["Elmer", 1], ["Diego", 2], ["Juan", 3]]

# ---------------- CONTAR / BUSCAR -----------------------
# Te envia el numero de veces que se ha repetido un elemento
LISTA.count(1)
# Te indica la posicion de la primera aparicion de un elemento
LISTA.index(1)
print("Juan" in usuarios)  # Busca si el elemento se encuentra en la lista
# ---------------- ELIMINAR -----------------------
# Elimina el elemento
LISTA.remove("perro")  # el dato
LISTA.pop()  # el ultimo dato o coloca el indice
del LISTA[1]  # elimina el dato que est en el indice
# LISTA.clear() #limpia toda la lista
print(LISTA)

# ---------------- ITERAR UNA LISTA -----------------------
for numro in lisT:
    print(numro)
for indice, numro in enumerate(lisT):  # te devuelve una tupla con los indices
    print(indice, numro)

# ---------------- ORDENAR / FILTRAR -----------------------
# Ordena la lista
listNum.sort()  # De menor a mayor
listNum.sort(reverse=True)  # De mayor a menor
list2 = sorted(listNum)  # Crea una nueva lista ordenada
# Crea una nueva lista ordenada De mayor a menor
list2 = sorted(listNum, reverse=True)
list2.reverse()  # invierte la cadena
# Traer unicamente el dato con el indice
nombres = [usuario[0] for usuario in usuarios]  # 1
print(nombres)
nombre = list(map(lambda usuario: usuario[0], usuarios))  # hace lo mismo que 1
print(f"he aqui los usuarios: {nombre}")
# filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]  # 2
# hace lo mismo que 2
usuario = list(filter(lambda usuario: usuario[1] > 1, usuarios))
print(usuario)


# ----------------------- FUNCIONES ------------------
len(lista)  # cuenta los elementos dentro de la lista
min(lisT)  # Devuelve el numero mas pequeño (solo funciona con numericos)
max(lisT)  # Devuelve el numero grande (solo funciona con numericos)
sum(lisT)  # suma todos los numeros dentro de tu arreglo (no debe tener str)
numerosNotDuplicado = list(set(listNum))  # Elimina los duplicados de la lista

# ----------------- MATRIZ ------------------
# Caracteristicas: Ordenados, Heterogeneos, Mutables, Con repeticion
MATRIZ = [[1, "perro", True, 1.22], [1, "perro", True, 1.22], [1, "perro", True, 1.22]]

# print(MATRIZ)
