## TP Datos complejos: Listas
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar range. 

def listaDeNumeros():
  lista = list(range(4,101,4))
  # lista = [x % 4 == 0 for x in range(0,101)]
  return lista
# print(listaDeNumeros())

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar 
# el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

def listaElementos():
  favs = ['Gatitos','Chocolate','Dulce de leche','Arcoiris','Kiwis']
  print(favs[-2])
# listaElementos()

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
def listaVacia():
  lista_vacia = []
  lista_vacia.append("Manzana")
  lista_vacia.append("Bananas")
  lista_vacia.append("Ananas")
  return lista_vacia
# print(listaVacia())

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente. Imprimir la lista resultante por pantalla.
# animales = ["perro", "gato", "conejo", "pez"]
def reemplazoLista():
  animales = ["perro","gato","conejo","pez"]
  animales[1]="loro"
  animales[-1]="oso"
  return animales
# print(reemplazoLista())

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
def removeMax():
  numeros = [8,15,3,22,7]
  numeros.remove(max(numeros))
  ## el código anterior remuevo de la lista números el elemento de máximo valor
  # si hacemos print debería retornar todos los valores exepto el 22
  print(numeros)
# removeMax()

##6) Crear una lista con números del 10 al 30 (incluído),
# haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
def range30():
  lista_numeros = list(range(10,31,5))
  return lista_numeros
# print(range30())

#7) Reemplazar los dos valores centrales (índices 1 y 2) 
# de la lista “autos” por dos nuevos valores cualesquiera.
#  autos = ["sedan", "polo", "suran", "gol"]
def reemplazoElementos():
  autos = ["sedan","polo","suran","gol"]
  autos[1]="wolksvagen"
  autos[2]="fiat"
  return autos
# print(reemplazoElementos())

#8) Crear una lista vacía llamada "dobles" y agregar 
# el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.
def dobles():
  dobles = []
  dobles.append([x*2 for x in range (5,16,5)])
  return dobles
# print(dobles())

#9) Dada la lista “compras”, cuyos elementos representan 
# los productos comprados por diferentes clientes:
# #compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
def listaAnidada():
  compras = [["pan","leche"], ["arroz","fideos","salsa"],["agua"]]
  compras[-1].append("jugo")
  compras[1][1] = "tallarines"
  compras[0].remove("pan")
  return compras
print(listaAnidada())

##10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
#  Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
