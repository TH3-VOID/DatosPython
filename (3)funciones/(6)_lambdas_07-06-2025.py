import random


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


# Ejemplo de uno de lambdas
def CreadorFuncion(n):  # Este te retorna una funcion que multiplica por n
    return lambda a: a * n


duplicador = CreadorFuncion(2)  # obtienes esta funcion: # lambda a: a * 2
triplicador = CreadorFuncion(3)  # obtienes esta funcion: # lambda a: a * 3
# De tal manera que solo falta que le asignes el valor a 'a'
print(duplicador(5))  # 10
print(triplicador(5))  # 15


numeros = [random.randint(1, 100) for _ in range(10)]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Imprime los números pares de la lista
