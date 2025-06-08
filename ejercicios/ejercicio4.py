"""
Pida al usuario un número. Dependiendo de si el número es par o impar, 
imprima un mensaje apropiado para el usuario. Pista: ¿cómo reacciona de manera 
diferente un número par / impar cuando se divide por 2?
Extras:
- Si el número es múltiplo de 4, imprima un mensaje diferente.
- Pida al usuario dos números: un número para verificar (llamarlo) y un número para 
    ividir por (). Si se divide uniformemente en , díselo al usuario. De lo contrario, 
    imprima un mensaje apropiado diferente.
"""
print("escriba 0 para salir")
while True:
    numero = int(input("Ëscriba un numero: "))
    if numero == 0:
        print("Usted ha saldo")
        break
    elif numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} no es par")
