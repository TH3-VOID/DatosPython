val1 = int(input("Ingresa numero 1: "))
val2 = int(input("Ingresa numero 2: "))
suma =val1+val2
res =val1-val2
mult =val1*val2
div =val1/val2

mensaje = f"""
Suma: {suma}
Resta: {res}
Multiplicacion: {mult}  
División: {div}
"""
print(mensaje)