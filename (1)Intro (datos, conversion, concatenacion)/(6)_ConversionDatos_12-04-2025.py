#podemos encontrar diferentes tipos de datos al momento 
#de lectura al momento de la entrada de datos 
# x = input('Ingrese un dato: ')
# int(): convierte valores a enteros
# str(): convierte valores a Strings
# float(): convierte valores a decimal
# bool(): valores unicamente tomados falsos: ("")(0)(None)

x = int(input('Coloque un numero: '))
s = str(input('Coloque un dato: '))
f = float(input('Coloque un decimal: '))
bol = bool(input('Coloque un dato boolean: '))

Mensaje = f"""
el valor entero es: {x},
el valor String es: {s},
el valor decimal es: {f},
el valor booleano es: {bol}
"""
print(Mensaje)