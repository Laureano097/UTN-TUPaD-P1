# Ejercicio 1

# Imprimir por pantalla Hola Mundo!
print("Hola Mundo!")

#-----------------------------------------------------------------------------------#
# Ejercicio 2

# Programa para solicitar nombre y dar saludo como respuesta
nombre = input("Hola, ¿como se llama ? ")
# Impresion de saludo
print(f"Hola {nombre}!")

#-----------------------------------------------------------------------------------#
# Ejercicio 3

# Presentacion de usuario

# Se ingresan los datos del usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ubicacion = input("ingrese su lugar de residencia: ")

# Se imprimen todos los datos almacenados
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ubicacion}.")

#-----------------------------------------------------------------------------------#
# Ejercicio 4

# # Programa para calcular área y perímetro de un circulo.

radio = int(input("Escriba el radio de un círculo: "))

# Calculo de área y perímetro
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio

# Muestra de resultados por print
print(f"El área es {area:.2f} y el perímetro es {perimetro:.2f}.")

#-----------------------------------------------------------------------------------#
# Ejercicio 5

# Programa para mostrar segundos equivalente a horas.
segundos = int(input("Ingrese un número entero de segundos: "))

# Calculo para pasar segundos a horas
horas = segundos / 3600

# MOstramos el resultado y lo formateamos para que muestre 2 decimales.
print(f"El equivalente a horas de los segundos ingresados es: {horas:.2f} horas.")

#-----------------------------------------------------------------------------------#
# Ejercicio 6

# Programa para calcular la tabla de un número ingresado

numero = int(input("Ingrese un número: "))

print(f"{numero} * 1 =", numero * 1)
print(f"{numero} * 2 =", numero * 2)
print(f"{numero} * 3 =", numero * 3)
print(f"{numero} * 4 =", numero * 4)
print(f"{numero} * 5 =", numero * 5)
print(f"{numero} * 6 =", numero * 6)
print(f"{numero} * 7 =", numero * 7)
print(f"{numero} * 8 =", numero * 8)
print(f"{numero} * 9 =", numero * 9)
print(f"{numero} * 10 =", numero * 10)

#-----------------------------------------------------------------------------------#
# Ejercicio 7

# Calculos entre dos números enteros distintos de 0

# Ingreso de los dos números
n1 = float(input("Ingrese un número entero: "))
n2 = float(input("Ingrese otro número entero: "))

if n1 == 0 or n2 == 0:
    print("Uno o más números ingresados es 0")
else:
#Muestra de resultados de operacioens aritméticas
    print("Suma: ", n1 + n2)
    print("División: ", n1 / n2)
    print("Multiplicación: ", n1 * n2)
    print("Resta: ", n1 - n2)


#-----------------------------------------------------------------------------------#
# Ejercicio  8

# Programa para calcular el IMC

# Solicitamos peso y altura
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

# Calculo de IMC
imc = peso / (altura ** 2)

# Se muestra el IMC con 2 decimales
print(f"Su IMC es de: {imc:.2f}.")

#-----------------------------------------------------------------------------------#
# Ejercicio 9 

# # Conversión temperatura en celsius a fahrenheit

# Ingreso de temperatura en celsius
celsius = float(input("Ingrese una temperatura en celsius: "))

# Calculo para transformar a fahrenheit
fahren = celsius * 1.8 + 32

# Mostrando la equivalencia por pantalla.
print(f"La temperatura ingresada de {celsius:.2f}º celsius es de {fahren:.2f}º fahrenheit")

#-----------------------------------------------------------------------------------#
# Ejercicio 10

# Calculo de promedio de 3 números

# Ingreso de los 3 números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

# Calculo del promedio de 3 números
promedio = (n1 + n2 + n3) / 3

# Resultado por pantalla
print(f"El promedio es de: {promedio:.2f}")