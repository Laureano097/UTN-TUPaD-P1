# Ejercicio 1

#Uso de ciclo for para que vaya desde 0 hasta 100 incluido
for count in range(0,101):
    print(count) #Imprimimos los números linea x linea

##-----------------------------------------------------------------------------------------------##

# Ejercicio 2
#Pedimos los datos al usuario
num = int(input("Ingrese un número entero: "))
#Estructura condicional y repetitiva para obtener la cantindad de digitos
if num == 0:
    cant_dig = 1
else:
    dig = abs(num)
    cant_dig = 0
    while dig > 0:
        dig = dig // 10
        cant_dig += 1
#Imprimimos por pantalla los resultados
print(f"La cantidad de dígitos que tiene su número es: {cant_dig}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 3
#Ingreso de los 2 números
n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
#Inicializamos suma en 0
suma = 0
#Si n1 es menor a n2 se suma normal
if n1 < n2:   
    for count in range(n1+1, n2):
        suma += count
else: #Si n2 es mayor a n1 invertimos y hacemos con paso -1
    for count in range(n1-1, n2, -1):
        suma += count
#Imprimimos por pantalla los resultados
print(f"La suma entre los números comprendidos es: {suma}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 4

#Inicializamos suma en 0
suma = 0
#Ingreso del primer número puede ser 0 y no corta el programa
num = int(input("Ingrese números enteros (0 para salir del programa): "))
#Uso de estrucutra repetitiva while para el ingreso de números y condición 0 para cortar
while True:
    suma += num
    num = int(input("Ingrese números enteros (0 para salir del programa): "))
    if num == 0:
        break
#Imprimimos resultados por pantalla
print(f"\nLa suma de los números ingresados es {suma}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 5

#Importamos la libreria random para poder usar la función random.radiant()
import random
#win_num genera un número aleatorio entre 0 y 9 incluidos
win_num = random.randint(0,9)
intentos = 0 #Inicializamos intentos en 0
num = None #Inicializamos num en None para que no haya errores si el número random es 0

#Mensaje de bienvenida al juego
print("Adivina el número secreto entre 0 y 9 (incluidos)")

#Bucle while con funcion try y except valueError para aseguranos que solo se ingresen números
#Y no crashee el programa
while num != win_num:
    try:
        num = int(input("Tu intento: "))
        intentos += 1
        if num < 0 or num > 9:
            print("Debe ser entre 0 y 9 (incluidos)")
            continue
        
        if num == win_num:
            print(f"Felicitaciones lo lograste con: {intentos} intentos")
    except ValueError:
        print("Por favor ingresa un número válido")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 6

#Ciclo for para imprimir en orden decreciente solo los pares entre 0 y 100
for count in range(98,0, -2):
    print(count)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 7

#Mensaje de bienvenida
print("Calcular la suma de todos los números entre 0 y x número")

#Inicializamos suma en 0
#Pedinos un número al usuario
suma = 0
num = int(input("Ingrese un número entero positivo: "))

if num <= 0: #Error al ingresar un número negativo o 0
    print("Error: Ingrese un número entero positivo mayor que 0.")
else:    
    for count in range(0, num):
        suma += count #Almacenamos los números en suma y los sumamos
    #Mostramos por pantalla el resultado
    print(f"\nLa suma de todos los números comprendidos entre 0 y {num} es: {suma}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 8

#Inicializamos variables
par = 0
impar = 0
negativo = 0
positivo = 0

#Estructura repetitiva y condicional para el ingreso de los 100 números
for count in range(1,101):
    num = int(input("Ingrese 100 números enteros: "))
    if num % 2 == 0:
        par += 1   
    else:
        impar += 1
    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1

#Imprimimos el resultado por pantalla
print(f"\nResultado: {par} pares, {impar} impares, {positivo}, positivos y {negativo} negativos")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 9

print("Calcular la media de 100 números")
#Importamos solo mean de statistics
from statistics import mean

#Armamos la lista y la dejamos vacia
numeros = []

#Bucle for que aceptar números float y función .append() para guardar los datos en la lista numeros
for count in range(100):
    num = float(input("Ingrese 100 números: "))
    numeros.append(num)

#Calculo de la media
promedio = mean(numeros)

#Imprimimos por pantalla los resultados
print(f"\nLa media de los 100 números ingresados es: {promedio}.")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 10

num = int(input("Ingrese un número: "))

lastDig = 0 # Almacenará el último dígito en cada iteración
num_inv = 0 # Se construye el número invertido

# Contemplamos el caso en el que el número es negativo
negativo = False
if num < 0:
    negativo = True
    num = abs(num)

while num > 0:
    lastDig = num % 10 # Paso 1: Obtener el último dígito
    num_inv = num_inv * 10 + lastDig # Paso 2: Construir el número invertido
    num = num // 10 # Paso 3: Eliminar el último dígito del original

# Le agregamos el signo si es negativo
if negativo:
    num_inv = -num_inv
print(num_inv) # Imprimimos por pantalla el resultado