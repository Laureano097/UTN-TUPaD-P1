# Ejercicio 1

# Definición de Variables
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa Principal

imprimir_hola_mundo()

##-----------------------------------------------------------------------------------------------##

# Ejercicio 2

# Definición de Variables
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa Principal

# Pedimos al usuario su nombre
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
# Imprimimos el saludo
print(saludo)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 3

# Definición de Variables
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


# Programa Principal

# Solicitamos al usuario nombre, apellido, edad y residencia.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su ciudad de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 4
from math import pi
# Definición de Variables


def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

# Programa Principal

# Pedimos el radio al usuario y llamamos a las funciones para que se guarde el valor en area y perimetro
print("Calcular el area y perimetro de un circulo")
radio = float(input("\nIngrese el radio: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostramos los resultados con 2 decimales
print(f"\nEl area es {area:.2f} y perimetro es {perimetro:.2f}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 5

# Definición de Variables

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

# Programa Principal

# Pedimos al usuario que ingrese los segundos
print("\nConvertidor de segundos a horas")
segundos = int(input("\nIngrese los segundos: "))

#Llamamos a la funcion para obtener los resultados y los imprimimos por pantalla
horas = segundos_a_horas(segundos)
print(f"El equivalente de {segundos} segundos a horas es: {horas} horas")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 6

# Definición de Variables
def tabla_multiplicar(numero):
    for i in range(1,11):
        tabla = numero * i
        print(f"{numero} x {i} = {tabla}")

# Programa Principal

# Pedimos el número al usuario
print("\nTabla de Multiplicar")
num = int(input("Ingrese un número: "))

# Llamamos a la función para ver los resultados
tabla_multiplicar(num)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 7

# Definición de Variables
# Operaciones basicas y convertimos a tupla
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    tupla = (suma, resta, mult, div)
    return tupla

# Programa Principal

print("Operaciones básicas con dos números ")
# Ingreso de datos por el usuario
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese un segundo número: "))

suma, resta, mult, div = operaciones_basicas(n1,n2)
# Imprimimos los resultados de forma clara
print(f"\nLa suma es: {suma}\nLa resta es: {resta}\nLa multiplicación es: {mult}\nLa división es: {div:.2f}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 8

# Definición de Variables
# Calculo de IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Programa Principal

print("Calcular IMC (Indice de Masa Corporal)")
# Pedimos el peso y la altura al usuario
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
# Calculamos el IMC usando los datos ingresados por el usuario
imc = calcular_imc(peso, altura)
# Imprimimos los resultados por pantalla con dos decimales
print(f"\nSu IMC es de {imc:.2f}")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 9

# Definición de Variables

# Calculo de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (1.8 * celsius) + 32
    return fahrenheit

# Programa Principal

print("Conversor de Celsius a Fahrenheit")
# Pedimos la temperatura en celsius
celsius = float(input("\nIngrese una temperatura en Celsius: "))
# Calculamos la temperatura en Fahrenheit
resultado = celsius_a_fahrenheit(celsius)
# Imprimimos resultados
print(f"\nSu temperatura de {celsius:.2f} º Celsius es {resultado:.2f} º Fahrenheit")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 10

# Definición de Variables

# Función para el calculo del promedio
def calcular_promedio(a, b ,c):
    promedio = (a + b + c) / 3
    return promedio

# Programa Principal

print("Calculadora de Promedios de 3 notas")
# Pedimos al usuario las 3 notas
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

# Llamamos a la función con las tres notas para calcular el promedio
resultado = calcular_promedio(nota1, nota2, nota3)
# Imprimimos por pantalla los resultados
print(f"\nEl promedio de las 3 notas es: {resultado:.2f}")