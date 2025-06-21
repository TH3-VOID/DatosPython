saludo = "Hola a todos"


def saludo1():
    saludo = "Hola Elmer"
    print(saludo)


def saludo2():
    saludo = "Hola Diego"
    print(saludo)


def saludo3():
    global saludo
    print(saludo)  # sde esta manera se imprime la variable global


print(saludo)
saludo1()
saludo2()
saludo3()
