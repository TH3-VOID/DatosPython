"""
Ejercicio 4: Mini base de datos de usuarios
Objetivo: Listas de diccionarios, if, match, funciones.
Instrucciones:

1. Cada usuario debe ser un diccionario con nombre, edad, email.
2. Almacenalos en una lista.
3. Permití:
 - Agregar un nuevo usuario
 - Buscar por nombre
 - Mostrar todos
 - Eliminar por nombre

Tip: list comprehension, next() con default.
"""
import os as os
import time as t
usuarios = []


def AddUser(nombre, edad, email):  # Agrega un nuevo usuario a la lista de usuarios
    usuarios.append({"nombre": nombre, "edad": edad, "email": email})
    print(f"Se ha agregado correctamente el usuari: {nombre}")


def searchUser(name):  # Busca un usuario por nombre y devuelve el primer encontrado o None si no existe
    return next((user for user in usuarios if user["nombre"].lower() == name.lower()), None)


def showUsers():
    if usuarios:
        for i, user in enumerate(usuarios, start=1):  # Muestra todos los usuarios
            print(
                f"{i}. Nombre: {user["nombre"]}, edad: {user["edad"]}, email: {user["email"]}")
    else:
        print("No hay usuarios registrados.")


def deleteUser(name):  # Elimina un usuario por nombre
    user = searchUser(name)
    if user != None:
        usuarios.remove(user)
        print(f"Usuario {name} eliminado exitosamente.")
    else:
        print(f"No se encontró el usuario {name} para eliminar.")


while True:
    try:
        os.system("cls")
        print("Seleccione una opción: \n"
              "1.Agregar \n"
              "2.Buscar \n"
              "3.Mostrar \n"
              "4.Eliminar \n"
              "5.Salir")
        print("--------------------------------------------------")
        opcion = int(input("Ingrese la opcion que desea realizar: "))
        match opcion:
            case 1:
                os.system("cls")
                nombre = input("Ingrese el nombre del usuario:")
                edad = int(input("Ingrese la edad del usuario: "))
                email = input("Ingrese el email del usuario: ")
                AddUser(nombre, edad, email)
                t.sleep(2)
            case 2:
                os.system("cls")
                nombre = input("ingrese el nombre del usuario a buscar: ")
                user = searchUser(nombre)
                if user != None:
                    print(
                        f"Nombre: {user["nombre"]}, edad: {user["edad"]}, email: {user["email"]}")
                    t.sleep(2)
                else:
                    print(f"No se encontró el usuario con nombre: {nombre}.")
                    t.sleep(2)
            case 3:
                os.system("cls")
                showUsers()
                t.sleep(2)
            case 4:
                os.system("cls")
                nombre = input("Ingrese el nombre del usuario a eliminar: ")
                deleteUser(nombre)
                t.sleep(2)
            case 5:
                print("Saliendo del programa...")
                break
    except ValueError:
        print("Por favor, ingrese un valor válido.")
        t.sleep(2)
    except Exception as e:
        os.system("cls")
        print(f"Ha ocurrido un error: {e}")
        break
