# De est manera desempacas los datos dentro de cualquier iterable
lista = [1, 2, 3, 4, 5]
print(*lista)
Tupla = (1, "perro", True, 1.22)
print(*Tupla)


# crear nuevas listas con tus iterables
lista2 = [*lista, *Tupla, 1, 2, 3, 4]
print(lista2)


# Manipula diccionarios
usuarios = {"id": 1, "Nombre": "Juan", "edad": 22}

diccionario = {"v1": 1, "v2": "2", "v3": True, 1: False, (1, 2): "tupla"}
diccionary = {**diccionario, **usuarios, "x": 22}
print(diccionary)
