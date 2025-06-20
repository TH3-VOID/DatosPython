"""
Ejercicio 25: Inventario simple
Descripción:
Crea un sistema simple de inventario usando un diccionario, donde la clave es el nombre 
del producto y el valor la cantidad en existencia.

El programa debe:
1. Permitir agregar productos y cantidades.
2. Permitir actualizar la cantidad de un producto.
3. Mostrar el inventario al final.

Pistas:
- Usa un bucle para pedir datos.
- Puedes usar input() para interactuar.
- Las claves serán los productos, los valores las cantidades.
"""
import os
import time as t

inventario = []

def menu() -> int:
    print("_______________________________________________________________")
    print("Bienvenido Usuario. \nPor favor digite la acción que desea realizar:")
    print("1. Agregar producto\n"
          "2. Actualizar cantidad de producto\n"
          "3. Mostrar inventario\n"
          "4. Eliminar producto\n"
          "5. Salir")
    print("_______________________________________________________________")
    return int(input("Ingrese la opción que desea realizar: "))

def agregar_producto() -> None:
    existe = False
    print("_______________________________________________________________")
    nombre = input("Ingrese el producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    clave = (nombre.strip()
                  .lower()
                  .replace("á","a")
                  .replace("é","e")
                  .replace("í","i")
                  .replace("ó","o")
                  .replace("ú","u"))
    if inventario:
        for _, item in enumerate(inventario, start=1):
            if item["Producto"] == clave:
                existe = True
                actualizar_producto(valor=cantidad, nombre=clave)
        if not existe:
            nuevo_id = len(inventario) + 1
            inventario.append({
                "id": nuevo_id,
                "Producto": clave,
                "Cantidad": cantidad
            })
            print(f"Producto \"{clave}\" agregado correctamente")
    else:
        inventario.append({
            "id": 1,
            "Producto": clave,
            "Cantidad": cantidad
        })
        print(f"Producto \"{clave}\" agregado correctamente")
    print("_______________________________________________________________")

def actualizar_producto(valor: int, nombre: str = "") -> None:
    if valor != 0:
        resp = input("¿Desea actualizar este producto? S/N: ")
        if resp and resp[0].lower() == "s":
            for item in inventario:
                if item["Producto"] == nombre:
                    item["Cantidad"] += valor
                    print("Cantidad actualizada correctamente")
        else:
            print("Ingresando nuevo producto")
            agregar_producto()
    else:
        print("_______________________________________________________________")
        id_buscar = int(input("Ingrese el ID del producto: "))
        extra = int(input("Ingrese la cantidad que desea agregar: "))
        encontrado = False
        for item in inventario:
            if item["id"] == id_buscar:
                item["Cantidad"] += extra
                print(f"Producto {item['Producto']} actualizado correctamente.")
                encontrado = True
        if not encontrado:
            print("No se ha encontrado el producto a actualizar")
        print("_______________________________________________________________")

def mostrar_inventario() -> None:
    print("___________________________PRODUCTOS___________________________")
    if inventario:
        for item in inventario:
            print(f"{item['id']}. Producto: {item['Producto']}, Cantidad: {item['Cantidad']}")
    else:
        print("No hay productos en stock")
    print("_______________________________________________________________")

def eliminar_producto() -> None:
    print("_______________________________________________________________")
    id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    encontrado = False
    for idx, item in enumerate(inventario):
        if item["id"] == id_eliminar:
            inventario.pop(idx)
            print(f"Producto {item['Producto']} eliminado correctamente.")
            encontrado = True
        elif item["id"] > id_eliminar:
            item["id"] -= 1
    if not encontrado:
        print(f"El producto con ID {id_eliminar} no existe")
    print("_______________________________________________________________")

while True:
    try:
        opcion = menu()
        if opcion == 5:
            os.system("clear")
            print("Saliendo del programa...")
            t.sleep(2)
            os.system("clear")
            break
        match opcion:
            case 1:
                os.system("clear")
                agregar_producto()
                t.sleep(2)
                os.system("clear")
            case 2:
                os.system("clear")
                actualizar_producto(valor=0)
                t.sleep(2)
                os.system("clear")
            case 3:
                os.system("clear")
                mostrar_inventario()
                t.sleep(2)
                os.system("clear")
            case 4:
                os.system("clear")
                eliminar_producto()
                t.sleep(2)
                os.system("clear")
    except ValueError:
        print("Por favor, ingrese un valor válido.")
        t.sleep(2)
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
        t.sleep(2)
