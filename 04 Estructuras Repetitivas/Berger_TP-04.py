import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
def enterosHasta(n):
    for i in range(n + 1):
        print(i)
enterosHasta(100)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad
# de dígitos que contiene.
def cuantosDigitos():
    n = int(input("Ingrese un número: "))
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    print(count)
cuantosDigitos()


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
def sumaRango():
    acc = 0
    print("Ingrese dos números a continuación: ")
    x = int(input("x = "))
    y = int(input("y = "))
    for i in range(x, y + 1):
        acc += i
    print(f"La suma del rango entre {x} e {y} es = {acc}")
sumaRango()


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume ensecuencia.
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
def sumaRangoInt():
    acc = 0
    print("Ingrese un número a continuación: ")
    n = 1
    while n != 0:
        try:
            n = int(input())
        except ValueError:
            print("El dato debe ser numérico")
            continue
        acc += n
    print(f"La suma del rango entre es = {acc}")
sumaRangoInt()

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
def adivinaRandom():
    random = random.randint(0,9)
    count = 0
    n = int(input("Ingrese un número entre 0 y 9: "))
    while n != random:
        count += 1
        n = int(input("ingrese  un nro entre 0 y 9: "))
    print(f"Número: {random} | intentos: {count}")
adivinaRandom()


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
def numerosDecr():
    for i in range(100,-1,-2):
        print(i)
numerosDecr()

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero = int(input("Ingrese un nro para el límite del rango: "))
def sumaRangoIndef(n):
    acc = 0;
    for i in range(0,n):
        acc += i
    return acc
print(sumaRangoIndef(numero))

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor,
# pero debe estar preparado para procesar 100 números con un solo cambio).
def cuantosEnteros(lim):
    cont_pares = 0
    cont_impares = 0
    cont_negativos = 0
    cont_positivos = 0
    print("Ingrese un número para clasificar.\nPara parar presione [0]")

    while lim > 0:
        n = int(input("Ingrese un número entero: "))
        if n % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1
        if n > 0:
            cont_positivos += 1
        else:
            cont_negativos += 1
        lim -= 1
        
    print("Positivos: ",cont_positivos)
    print("Negativos: ",cont_negativos)
    print("Pares: ",cont_pares)
    print("Impares: ",cont_impares)
cuantosEnteros(100) # cambiar parámetro

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
def calcularMedia(n):
    i = n
    acc = 0
    while i != 0:
        val =  float(input("Ingrese un número: "))
        acc += val
        i -= 1
    prom=acc/n
    print(f"Total = {acc}\tCantidad de valores = {n}")
    print(f"Promedio es = {prom}")

calcularMedia(100) #cambiar el parámetro

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def digitosInversos():
    num = int(input("Ingrese un número: "))
    aux = num
    final = ""
    while aux > 0:
        resto = aux % 10
        final += str(resto)
        aux = aux // 10
        # num = num // 10
    print(f"{num} al inverso es: {int(final)}")

digitosInversos()