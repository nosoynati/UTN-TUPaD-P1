from math import trunc, pi

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
n = input("Nombre: ")
saludar_usuario(n)

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
pregunta_datos()

# 4. Crear dos funciones: 
# calcular_area_circulo(radio) que reciba el radiocomo parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambasfunciones
def calcular_area_circulo(radio:float):
    return round(pi * pow(radio,2),2)

def calcular_perimetro_circulo(radio:float):
    return round((2 * pi * radio),2)

def preguntar_radio():
    radio = float(input("Radio: "))
    print(f"Perímetro: {calcular_perimetro_circulo(radio)}")
    print(f"Area: {calcular_area_circulo(radio)}")
# print(f"area: {calcular_area(5):.2f}")
preguntar_radio()


#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro
# y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado 
def segundos_a_horas(segundos:int):
    hours = trunc(segundos / pow(60,2))
    # mins = trunc((hours / 60) * 100)
    print(f"{hours}H")

def convertir_segs():
    segs = int(input("Convertir segundos: "))
    return segundos_a_horas(segs)
convertir_segs()

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero = 1):
    for i in range(1,11):
        print(f"{numero} * {i} = {numero * i}")
def pedirNumero():
    a = int(input("Generar table del: "))
    return tabla_multiplicar(a)
pedirNumero()

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos
def suma(a,b):
    return a + b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    while b == 0:
        b = int(input("Error. Ingrese un numero distinto de 0: "))
    return a/b

def resta(a,b):
    return a - b

def solicitarNumeros():
    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))
    return (a,b)

def operaciones_basicas(a=1,b=1):
    return (suma(a,b),resta(a,b),multiplicacion(a,b),division(a,b))

a, b = solicitarNumeros()
suma, resta, mult, div = operaciones_basicas(a,b)
print(f"suma: {suma}, resta: {resta}, multiplicación: {mult}, división: {div}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos. Mostrar el resultado con dos decimales. 

def calcular_peso(peso:float,altura:float):
    imc = peso / pow(altura,2)
    return round(imc,2)

def calcular_imc():
    peso = int(input("Peso (Kg): "))
    altura = float(input("Altura (M): "))
    imc = calcular_peso(peso, altura)
    print(f"IMC: {imc}")
calcular_imc()

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado
def celcius_a_fahrenheit(celcius:float):
    return (celcius * 1.8) + 32

def convertir_grados():
    grados = float(input("Grados (°C): "))
    far = celcius_a_fahrenheit(grados)
    print(f"{grados}°C -> {far}°F")
convertir_grados()

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado
def calcular_promedio(a:float,b:float,c:float):
    sum = 0
    for x in [a,b,c]: sum += x
    return round((sum / 3),2)

def promedios():
    a = float(input("Nota 1: "))
    b = float(input("Nota 2: "))
    c = float(input("Nota 3: "))
    print(f"Promedio: {calcular_promedio(a,b,c)}")
promedios()









    
