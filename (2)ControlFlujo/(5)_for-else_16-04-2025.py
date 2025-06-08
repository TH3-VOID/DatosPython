i = 0
buscar = 3
# sin else
for numero in range(5):
    i += 1
    print(i)

# con else
for numero in range(5):
    i += 1
    print(i)
    if numero == buscar:
        print(f'Se ha encontrado: {buscar}')
        break
else:
    print('No se ha encontrado el numero buscado')
