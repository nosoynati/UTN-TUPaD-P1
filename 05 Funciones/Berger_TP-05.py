from math import ceil, floor, pi
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
# n = input("Nombre: ")
# saludar_usuario(n)

#Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedirlos datos al usuario.
def informacion_personal(nombre=None, apellido=None, edad=0, residencia = "Argentina"):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

def pregunta_datos():
    nom = input("Nombre: ")
    last = input("Apellido: ")
    edad = int(input("Edad: "))
    place = input("Residencia: ")
    return informacion_personal(nom,last,edad,place)
# pregunta_datos()

# 4. Crear dos funciones: 
# calcular_area_circulo(radio) que reciba el radiocomo parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambasfunciones
def calcular_area_circulo(radio,):
    return round(pi * pow(radio,2),2)

def calcular_perimetro_circulo(radio):
    return round((2 * pi * radio),2)

def preguntar_radio():
    radio = float(input("Radio: "))
    print(f"Perímetro: {calcular_perimetro_circulo(radio)}")
    print(f"Area: {calcular_area_circulo(radio)}")
# print(f"area: {calcular_area(5):.2f}")
# preguntar_radio()


#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado 
def segundos_a_horas(segundos):
    return None

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    return None

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos
def operaciones_basicas(a,b):
    return None

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos. Mostrar el resultado con dos decimales. 
def calcular_peso(peso,altura):
    return None

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado
def celcius_a_fahrenheit(celcius):
    return None

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado
def calcular_promedio(a,b,c):
    return None