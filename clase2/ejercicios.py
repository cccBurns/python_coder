# EJERCICIO 1

lista1 = [1, 2, 3, 4, 'pepe', 'hola']
lista2 = [1, 5, ('mi', 'gato'), 'richard']

lista1.append(456789)
lista1.append("hola mundo")

lista1[6:] = [456789, 'hola mundo']
print(lista1)