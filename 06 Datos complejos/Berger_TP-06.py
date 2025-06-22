
#1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: Naranja = 1200, Manzana = 1500
def agregarAlDic(d,k,v):
    d[k] = v

precios_frutas = {
    "Banana":1200,
    "Ananá":2500,
    "Melón":3000,
    "Uva":1450
}
agregarAlDic(precios_frutas,"Naranja",1200)
agregarAlDic(precios_frutas,"Manzana",1500)

print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas: Banana = 1330,Manzana = 1700
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700

print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios.
lista_frutas = [key for key in precios_frutas.keys()]
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

# agenda_test = {
#     "angie":3735789012,
#     "papi":3735446243,
#     "lucho":3621436712,
#     "fer":113456234
# }
agenda = {}
def checkearnombre(d,nombre="Anon"):
    return nombre in d

def pedir_datos(stop):
    i = 0
    while i < stop:
        nombre = input("Nombre del contacto")
        while checkearnombre(agenda,nombre):
            print("Ese nombre ya existe")
            nombre = input("Nombre del contacto")
        num = int(input("Numero: "))
        agenda[nombre] = num
        i += 1
    print(agenda)

def buscar_agenda(nombre):
    nombre = nombre.lower()
    if nombre not in agenda:
        print("No encontrado")
 
    for key,value in agenda.items():
        if nombre in key:
            print(f"{nombre}: Nro: {value}")

def pedir_nombre():
    x = input("Buscar: ")
    return x

# pedir_datos(3)
# nombre = pedir_nombre()
# buscar_agenda(nombre)

#5) Solicita al usuario una frase e imprime: Las palabras únicas (usando un set). 
#  Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresar una frase: ")
frase_copy = [x.strip(".") for x in frase.split(" ")]

palabras_repetidas = {}
leng = len(frase_copy)
count = 0
for i in range(leng):
    palabra = frase_copy[i]
    if frase_copy.count(palabra) > 1:
        count = frase_copy.count(palabra)
        palabras_repetidas[palabra] = count
 
frase_set = set(frase_copy)
# print(f"Frase original: {frase}")
# print(f"Palabras que se repiten: {palabras_repetidas}")
# print(f"Sin repetidas: {frase_set}")

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

def ingresar_nombres():
    alumnos = []
    print("Ingresar un alumno, presione [X] para terminar.")
    n = input("Ingersar un nombre: ")
    while True:
        dic = {}
        if n.lower() == "x":
            break
     
        dic["nombre"] = n
        notas = []
        for i in range(1,4):
            nota = int(input(f"Ingresar nota {i}:"))
            notas.append(nota)
             
        dic["notas"] = tuple(notas)
        alumnos.append(dic)
        n = input("Ingersar un nombre: ")
    return alumnos

def calcular_promedio():
    x = ingresar_nombres()
    for item in x:
        notas = item["notas"]
        promedio = round(sum(notas) / len(notas), 2)
        item["promedio"] = promedio 
    return x

# print(calcular_promedio())

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
def sets_de_aprobados():
    parcial_1 = {1, 2, 3, 4, 5,12,15}
    parcial_2 = {4, 5, 6, 7, 8,12,21}

    aprueban_ambos = parcial_1.intersection(parcial_2)
    print(f"Aprobados en ambos parciales: {aprueban_ambos}")

    aprobados_uno = parcial_1.symmetric_difference(parcial_2)
    print(f"Aprobados solo en uno de los parciales: {aprobados_uno}")

    total_aprobados = parcial_1.union(parcial_2)
    print(f"Total de aprobados al menos un parcial: {total_aprobados}")

# sets_de_aprobados()
#Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

inventario = {
    "manzanas": 50,
    "peras": 30,
    "naranjas": 20
}
def consultar_stock():
    consult_stock = input("Ingrese el nombre del producto para consultar su stock: ").lower()
    for key, value in inventario.items():
        if key == consult_stock:
            print(f"El stock de {key} es: {value}")
            break
        else:
            print(f"No hay stock de {consult_stock}")
            agregar = input("¿Desea agregar un nuevo producto? (si/no): ").lower()
            if agregar == "si":
                agregar_producto()
            break

def agregar_producto():
    nuevo = input("Ingrese el nombre del nuevo producto: ").lower()
    if nuevo in inventario:
        unidades = int(input(f"¿Cuántas unidades desea agregar al stock de {nuevo}? "))
        inventario[nuevo] += unidades
        print(f"Nuevo stock de {nuevo}: {inventario[nuevo]}")
    else:
        unidades = int(input(f"{nuevo} no existe. ¿Cuántas unidades desea agregar? "))
        inventario[nuevo] = unidades
        print(f"{nuevo} agregado con un stock de {unidades} unidades.")

consultar_stock()

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos
# ej:  agenda = { 
#   ("lunes","10:00") : "reunion",
#   ("martes","15:00"):"clase de inglés"
#} Permití consultar qué actividad hay en cierto día y hora

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.