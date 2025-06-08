animal = ' tejOn MielEro '
print(animal.upper()) # convierte todas en mayusculas
print(animal.lower()) # convierte todo en minusculas
print(animal.capitalize()) # convierte todo en texto normal, T no paso a mayuscula debido a que hay un espacio en [0] 
print(animal.title()) # Convierte cada primer caracter a una mayuscula
print(animal.strip()) #quita espacios a la izquierda y a la derecha
print(animal.rstrip()) #quita espacios a la derecha
print(animal.lstrip()) #quita espacios a la izquierda 
print(animal.strip().capitalize())
#como se ve donde se ocupa el strip y el capitalize juntos se puede observar que de esa manera se puede concatenar
#cada metodo con otro de esa manera formulando y limpiando el texto ya existente.
print(animal.find("e")) # este lo que hace es una busqueda si encuetra manda en que posicion esta, sino -1
print(animal.replace("tjOn","Tejon")) # este tiene o puede cambiar el string "campo antiguo","campo nuevo", si no encuentra no hace algo

# ESTOS SON UNO DE LOS MAS OCUPADOS
print("tej" in animal)# te dice si ha encontrado por medio de booleans
print("a" not in animal)# te dice si no ha entrado por medio de  booleans


