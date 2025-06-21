# 1. Verifica si has ingresado un numero
# 2. Si no ha ingresado un numero enviarlo a que ingrese el numero
# 3. Si ha ingresado un numero llevalo a el tipo de operacion que quiere hacer.
# 4. el resultado volvera al inicio y sera el primer numero, y te pedira el siguiente tipo de operacion.

n1 = 0
n2 = 0

while True:
    try:
        if n1 != 0:
            TipoOperacion = str(
                input("Coloque el tipo de operacion que desea realizar: ")
            )
            if TipoOperacion == "salir":
                break
        else:
            n1 = int(input("Digite el primer numero: "))
            TipoOperacion = str(
                input("Coloque el tipo de operacion que desea realizar:")
            )
            if TipoOperacion == "salir":
                break
        n2 = int(input("Coloque el segundo numero: "))
        match TipoOperacion:
            case "+":
                n1 += n2
                print(f"Resultado: {n1}")
            case "-":
                n1 -= n2
                print(f"Resultado: {n1}")
            case "*":
                n1 *= n2
                print(f"Resultado: {n1}")
            case "/":
                if n2 != 0:
                    n1 /= n2
                    print(f"Resultado: {n1}")
                else:
                    print("No se puede dividir por cero")
        n1 = n1
        TipoOperacion = ""
    except Exception as e:
        print("Ingrese un valor valido")
