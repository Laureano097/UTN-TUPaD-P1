# Ejercicio 1

#Pedimos la edad al usuario
edad = int(input("Ingrese su edad: "))

#Nos aseguramos que tenga 18 o más años para imprimir el mensaje de "Es mayor de edad"
if edad >= 18:
    print("Es mayor de edad")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 2

#Pedimos una nota al usuario
nota = int(input("Ingrese su nota: "))

#estructura condicional para verificar si está aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 3

#Pedimos al usuario que ingrese un número par
num = int(input("Ingrese un número par: "))

#Estructura condicional para verificar si el número ingresado es par o impar
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 4

#Ingreso de edad por el usuario
edad = int(input("Ingrese su edad: "))

#estructura condicional para determinar niño, adolescente, adulto joven o adulto
if edad < 12:
    print("Es niño/a")
elif edad >= 12 and edad < 18:
    print("Es adolescente")
elif edad >= 18 and edad < 30:
    print("Es aldulto/a joven")
elif edad >= 30:
    print("Es adulto/a")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 5

#Pedimos el ingreso de la contraseña
contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

#Verificamos que la contraseña ingresada este entre los 8 y 14 caracteres
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Has ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 6

#Importamos las funciones random y mode, median y mean de statistics para el ejercicio
import random
from statistics import mode, median, mean

#generamos la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#asignamos los resultados a las variables para poder compararlas en el proximo paso
valorMode = mode(numeros_aleatorios)
valorMedian = median(numeros_aleatorios)
valorMean = mean(numeros_aleatorios)

#Estructura secuncial para verificar si hay sesgo positivo, negativo, no hay sesgo
if valorMean == valorMedian == valorMode:
    print("No hay sesgo")
elif valorMean > valorMedian > valorMode:
    print("Hay sesgo positivo")
elif valorMean < valorMedian < valorMode:
    print("Hay sesgo negativo")
else: #else agregado para el caso en el que no haya un sesgo definido
    print("No hay sesgo definido (distribución irregular)")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 7
#Pedimos al usuario el ingreso de una frase o palabra y lo almacenamos en frase_lower en minusculas
#Para poder determinar mejor si termina en vocal o no

frase = input("Ingrese una frase o palabra: ")
frase_lower = frase.lower()

#Nos aseguramos de que tambien acepten las palabras que terminen en vocal con tilde
if frase_lower.endswith(('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú')):
    print(f"{frase}!")
else:
    print(frase)

##-----------------------------------------------------------------------------------------------##

# Ejercicio 8

#Ingreso de datos por el usuario
name = input("Ingrese su nombre: ")

#mostramos el menú
print("1. Nombre en mayúsculas.")
print("2. Nombre en minúsculas.")
print("3. Nombre con la primera letra en mayúscula.")
print("----------------------------------------------")

#ingreso de datos para la opción deseada.
option = input("Ingrese el número de la opción deseada: ")

#Estructuara condicional para convertir la opción deseada y mostrar los resultados.
if option == "1":
    print(f"{name.upper()}")
elif option == "2":
    print(f"{name.lower()}")
elif option == "3":
    print(f"{name.title()}")
else:
    print("Opción no válida. Por favor ingrese 1, 2 o 3.")

##-----------------------------------------------------------------------------------------------##

# Ejercicio 9

#Uso de función try-except para evitar el crasheo al ingresar valores incorrectos
try:
    magnitud = float(input("Ingrese la magnitud de un terremoto, segun la escala de Richter: "))
#Estructura condicional para determinar la clasificación de los terremotos
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy fuerte (puede causar daños significativos)")
    elif magnitud >= 7:
        print("Extremo (puede causar graves daños a gran escala)")

except ValueError:
    print("Ingrese una magnitud de escala Richter") 

##-----------------------------------------------------------------------------------------------##

# Ejercicio 10

# Menu para seleccionar hemisferio
print("------- Menú Principal -------")
print("1. Hemisferio norte")
print("2. Hemisferio sur")

#Ingreso de datos del usuario
hemisferio = int(input("Ingrese el hemisferio en el que se encuentra: "))
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

#condicionales para determinar la estación en el hemisferio norte
if hemisferio == 1: #Hemisferio norte
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en Invierno.")
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Primavera.")
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en Verano.")
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        print("Se encuentra en Otoño")
    else:
        print("Fecha no válida.")

#condicionales para determinar la estación en el hemisferio sur
if hemisferio == 2: #Hemisferio sur
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en Verano.")
    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en Otoño.")
    elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en Invierno.")
    elif (mes == 9 and dia >= 21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        print("Se encuentra en Primavera")
    else:
        print("Fecha no válida.")
else:#Mensaje de error si el usuario ingresa otro número que no sea 1 o 2 para norte o sur
    print("Hemisferio no válido, Ingrese 1 (Norte) o 2 (Sur)")