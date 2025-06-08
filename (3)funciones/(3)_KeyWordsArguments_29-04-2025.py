# De esta manera se ingresan multiples tipos de datos en una sola funcion,
# De igual manera se es posible manipularlos a base de sus nombres de variable
def set_producto(**datos):
    print(datos)
    print(f"Datos obtenidos: {datos["name"]}")


set_producto(id="id", name="Android", desc="Samsung S24")
