edad = int(input('ingrese su edad: '))
mensaje = ''
# ---------------CASO 1------------------------------
# if edad >= 18:
#     mensaje = "Cuenta con la edad necesario para acceder"
#     if edad >= 50:
#         mensaje += '\nCuenta con descuento adicional del 50%'
#     mensaje += '\nVaya a la sala correspondiente'
# else:
#     mensaje = 'No cuenta con la edad suficiente'
# print(mensaje)

# ---------------CASO 2------------------------------
mensaje = 'Cuenta con la edad suficiente \nIngrese a su sala correspondiente' if edad >= 18 else 'no cuenta con la edad suficiente  \nretirese'
print(mensaje)
