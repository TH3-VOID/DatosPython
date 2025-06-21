edad = int(input("Ingrese su edad: "))
mensaje = ""
if 15 <= edad <= 60:
    mensaje = "Puede tener acceso a la piscina"
else:
    mensaje = "No puede acceder por el margen de la edad"
print(mensaje)
