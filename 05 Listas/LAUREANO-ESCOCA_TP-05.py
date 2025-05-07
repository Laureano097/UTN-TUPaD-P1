# Ejercicio 1

#Creamos una lista con range 4 para que empiece desde el primer multiplo de 4 y vaya almacenando los siguientes multiplos
lista = list(range(4,100,4))
print(lista)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 2

#Creación de lista de 5 elementos y usamos -2 para imprimir el penúltimo elemento
lista = [2, 3.5, True, "Hola mundo", 9]
print(lista[-2])

##-----------------------------------------------------------------------------------------------##

# Ejercicio 3

#Creamos la lista vacia
lista = []

#Agregamos las palabras con la función append
lista.append("Hola")
lista.append("UTN")
lista.append("Mundo")

#Imprimimos los resultados
print(lista)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 4

#Lista de animales
animales = ["perro", "gato", "conejo", "pez"]

#Cambiamos el segundo elemento por "loro" y el último por "oso"
animales[1] = "loro"
animales[-1] = "oso"

#Imprimimos los resultados
print(animales)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 5

#La función max(numeros) encuentra el valor máximo de la lista, que en este caso es 22, y .remove() elimina ese elemento de la lista. Al final, el programa imprime el resultado con el 22 eliminado

##-----------------------------------------------------------------------------------------------##

# Ejercicio 6

#Lista de 10 a 30 (incluido) que va de 5 en 5
lista = list(range(10, 31, 5))

#Mostramos solo los 2 primeros elementos con lista[0:2]
print(lista[:2])

##-----------------------------------------------------------------------------------------------##

# Ejercicio 7

#Lista autos
autos = ["sedan", "polo", "suran", "gol"]

#Reemplazo de elementos en indice 1 y 2
autos[1] = "UTN"
autos[2] = 10

##-----------------------------------------------------------------------------------------------##

# Ejercicio 8

#Lista dobles vacía
dobles = []

#Agregamos el doble de 5, 10 y 15 con la función .append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

#Mostramos los resultados
print(dobles)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 9

#Lista compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#Se agrega jugo, se reemplaza fideos por tallarines y se elimina pan
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

#Mostramos los resultados
print(compras)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 10

#Lista anidada
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#Mostramos los resultados por pantalla
print(lista_anidada)