# --------------- AND    OR     NOT ------------------------------
# el not lo que puede hacer es darle el valor contrario a una variable al pareceer
gasonila = True
encendido = True
edad = 18
mensaje = ""

if gasonila and (encendido or edad > 17):
    mensaje = "Puedes Avanzar"
else:
    mensaje = "No cuentas con lo requerido"
print(mensaje)
