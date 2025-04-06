from statistics import mode, median, mean
import random

# 1) Escribir un programa que solicite la edad del usuario.
# Si el usuario es mayor de 18 años, mostrar en pantalla que diga “Es mayor de edad”.
def esMayor(x: int):
    print("Es mayor") if (x > 18) else print("No es mayor de edad")

edad = int(input("Ingrese su edad: "))
esMayor(edad)

##2) Escribir un programa que solicite su nota al usuario.
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”;
#  en caso contrario deberá mostrar el mensaje “Desaprobado”.
def notaAprobado(x: int) -> str:
    print("Aprobado") if (x >= 6) else print("Desaprobado")

nota = int(input("Su calificación: "))
notaAprobado(nota)


##3) Escribir un programa que permita ingresar solo números pares.
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
def esPar(x: int) -> bool:
        return x % 2 == 0

def evalEsPar():
    numeropar = int(input("Ingresar un número par: "))
    print("Ha ingresado un número par") if (esPar(numeropar)) else print("Por favor ingrese un número par")
evalEsPar()

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes
# categorías pertenece:
# Niño/a: menor de 12 años.
# adolescente: mayor o igual que 12 años y menor que 18 años.
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# Adulto/a: mayor o igual que 30 años.
def edadCategoria():
    edad = int(input("Su edad: "))
    if edad < 12:
        print("Niño/a")
    else:
        if edad < 18:
            print("Adolescente")
        elif edad >= 18 and edad < 30:
            print("Adulto/a joven")
        else:
            print("Adulto/a")

edadCategoria()


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje
# "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string.
def longPassword():
    password = input("Ingrese contraseña: ")
    length = len(password)
    if length >= 8 and length <= 14:
        print("Contraseña correcta!")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

longPassword()


# escribir un programa que tome la lista numeros_aleatorios,
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo,
# negativo o no hay sesgo. Imprimir el resultado por pantalla.
### Definir la lista numeros_aleatorios de la siguiente forma:
# import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: lista con 50 números entre 1 y 100 elegidos de forma aleatoria.
def determinarSesgo():
    randomnumber = [random.randint(0, 100) for i in range(50)]
    mediana = median(randomnumber)
    moda = mode(randomnumber)
    promedio = mean(randomnumber)
    if promedio > mediana > moda:
        print("Sesgo positivo | a la derecha")
    elif promedio < mediana < moda:
        print("Sesgo negativo | a la izquierda")
    else:
        print("No hay sesgo")

determinarSesgo()


## 7) Escribir un programa que solicite una frase o palabra al usuario.
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final
# e imprimir el string resultante por pantalla;
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
def terminaEnVocal():
    frase = input("Su frase: ")
    vocals = "aeiouáéíóú"
    last_char = frase[-1]
    print(frase + "!") if last_char.lower() in vocals else print(frase)

terminaEnVocal()

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.


def formatName():
    nombre = input("Ingrese su nombre: ")
    print("Formato: \n[1]: MAYÚSCULAS\n[2]: minúsculas\n[3]: Capitales")
    opc = int(input("Ingrese una opción para formatear su nombre: "))
    match opc:
        case 1:
            print(nombre.upper())
        case 2:
            print(nombre.lower())
        case 3:
            print(nombre.title())
        case _:
            print(nombre)

formatName()


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto,
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
def magnitudTerremoto():
    magnitud = int(input("Magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud == 3:
        print("Leve (ligeramente perceptible)")
    elif magnitud == 4:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud == 5:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud == 6:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

magnitudTerremoto()
#
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
# qué mes del año es y qué día es. El programa deberá utilizar esa información para
# imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

dia = int(input("Ingrese el día: (dd): "))
mes = input("Ingrese el mes: ").lower()

def estacionDelanio(dia:int, mes:str):

    def input_error():
        return "dato incorrecto"

    hemisferio = input("Hemisferio ('S'|'N'): ").lower()
    # dia = int(input("Ingrese el día: (dd)"))
    # mes = input("Ingrese el mes: ").lower()

    MESES = [
        "diciembre",
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
    ]

    dia_min = dia < 21

    if dia > 31 or dia <= 0 or mes.lower() not in MESES:
        print(input_error())
    else:
        
        def hemisferio_sur(meses):
            match meses:
                case "enero" | "febrero":
                    print("verano")
                case "diciembre":
                    print("primavera") if dia_min else print("verano")
                case "marzo":
                    print("primavera") if dia_min else print("otoño")
                case "abril"|"mayo":
                    print("otoño")
                case "junio":
                    print("otoño") if dia_min else print("invierno")
                case "julio"|"agosto":
                    print("invierno")
                case "septiembre":
                    print("otoño") if dia_min else print("primavera")
                case "octubre"|"noviembre":
                    print("primavera")
                case _:
                    print("bye")

        def hemisferio_norte(meses):
            match meses:
                case "diciembre":
                    print("otoño") if dia_min else print("invierno")  
                case "enero" | "febrero":
                    print("invierno")
                case "marzo":
                    print("primavera") if dia_min else print("invierno")
                case "abril"|"mayo":
                    print("primavera")
                case "junio":
                    print("primavera") if dia_min else print("verano")
                case "julio"|"agosto":
                    print("verano")
                case "septiembre":
                    print("verano") if dia_min else print("otoño")
                case "octubre"|"noviembre":
                    print("otoño")
                case _:
                    print("bye")

        if hemisferio == "s":
            hemisferio_sur(mes)
        else:
            hemisferio_norte(mes)

estacionDelanio(dia,mes)