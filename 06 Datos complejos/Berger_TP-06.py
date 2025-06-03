
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

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

#5) Solicita al usuario una frase e imprime: Las palabras únicas (usando un set). 
#  Un diccionario con la cantidad de veces que aparece cada palabra.


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).