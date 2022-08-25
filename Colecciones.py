from copy import deepcopy

"""" --- EJEMPLOS DE STRINGS --- """

nombre = "Agustin"
myStr = "hOlA mI nOmBre Es aGus"

print(" Colecciones en Python ".center(50,'-'))  # Ubica el String en el centro, y a sus lados los 50 caracteres del tipo que indicamos, es decir 25 '-' de cada lado

print(f"Cantidad de caracteres de 'Agustin': {len(nombre)}")  # Cantidad de caracteres del string

print(f"Tercera letra de 'Agustin': {nombre[2]}")  # Indexación

print(f"Letras del medio de 'Agustin': {nombre[1:6]}")  # Se selecciona una parte del string [inicio:fin]. El fin no se incluye

print(f"String 'Agustin' saltando de a 2 caracteres: {nombre[1:6:2]}")  # Se le agrega otro parametro que indica el paso
# Si usamos una posición que no existe en el 'final' no pasa nada
# Si queremos solo poner un tope final ---> [:final]
# Si queremos solo poner un inicio --->[inicio:]
# Si queremos que se tome el string completo ---> [:]

# Lo que va luego de 'variable.' se llama metodo ----> <cadena>.<metodo>(<valores>)

print(myStr.upper())  # Todo en mayuscula
print(myStr.lower())  # Todo en minuscula
print(myStr.capitalize())  # La primer letra en mayuscula
print(myStr.replace("hOlA", "bye"))  # Reemplaza el primero por el segundo
print(nombre.center(30))  # Devuelve una cadena centrada en un campo de tamaño
print(myStr.split())  # Crea una lista cuyos elementos son las palabras que conformaban una oración

# Busca y devuelve la posicion de inicio del elemento buscado. Si no la encuentra devuelve -1
# Se indica ("<parte buscada>, inicio, fin)-. Si no se aclara el inicio o fin se toma el default
print(myStr.find("Es"))

print(myStr.find("Es", 0, 10))  # Aqui no encuentra y devuelve -1

print(myStr.index("mI"))  # Igual que el .find pero no devuleve -1, da error si no lo encuentra

"""Otros Metodos importantes para strings:

isalnum: Devuelve True o False si es una cadena alfanumerica (letras y numeros)
isalpha: Devuelve True o False si es una cadena alfabetica (solo letras)
isdigit: Devuelve True o False si es una cadena numerica (solo numeros)
islower: Devuelve True o False si es una cadena contiene solo minusculas
isupper: Devuelve True o False si es una cadena contiene solo mayusculas

"""

""" --- EJEMPLOS DE LISTAS --- """

lista = [1, 2, 3, "agus", True, "quiero dormir"]  # la lista puede ser mixta

listaNum: list[int] = [1, 2, 3, 4, 5, 7]  # Lo casteo a entero

print(f"Lista concatenada: {lista + listaNum} ")  # El + concatena las litas

print(f"Lista repetida {listaNum * 3}")  # El * hace que la lista se repita una cantidad determinada de veces
print(f"Lista repetida {[listaNum] * 3}")  # Se crea un arreglo de arreglos

print(f"Lista original: {listaNum}")

print(f"Primeros dos numeros: {listaNum[0:2]}")  # Toma los valores del indice 0 al 2

print(f"Ultimo indice de la lista : {listaNum[-1]}")  # Con numeros negativos puedo navegar de forma inversa

listaNum.append(8)  # agrega un elemento al final de la lista

# Inserta un elemento en el indice elegido ---> <lista>.insert(<indice>, <elemento>)
listaNum.insert(5, 6)  # El elemento que estaba en esa posicion se corre un lugar a la derecha

print(f"Lista Modificada: {listaNum}")

listaNum.remove(5)  # Remueve el elemento elegido (la primera aparición). Si no está en la lista se genera un error
listaNum.pop()  # Remueve el ultimo elemento de la lista
del listaNum[0]  # Se elimina un elemento especificando un indice

print(f"Remuevo el 5: {listaNum}")

print(f"Posición del numero 4: [{listaNum.index(4)}]")  # Busca cual es la posicion del numero 4

print(3 in listaNum)  # Devuelve True si el elemento esta en la lista, de lo contrario False

lista.extend(listaNum)  # Agrega al final de la lista mas de un elemento, en este caso una lista, pero puede ser un
# arreglo

print(f"Lista extendida: {lista}")

print(f"Veces que se repite el 2: {lista.count(2)}")  # Cuenta la cantidad de veces que un elemento se encuentra en
# una lista

print(f"El ultimo elemento de listaNum: {listaNum.pop(), listaNum}")  # Elimina y devuelve el ultimo elemento de la
# lista

del listaNum[1]  # Borra el item de la posición indicada

print(f"Borro el 2 : {listaNum}")

listaNum.reverse()  # Reversa el orden actual de la lista

print(f"La lista al revez quedaria: {listaNum}")

listaNum.sort(reverse=True)  # Ordena la lista de forma descendente

listaNum.sort()  # Ordena la lista de forma ascendente

listaNum.clear()  # Borra todos los elementos de la lista

del listaNum  # Borra la lista de la memoria

""" --- EJEMPLO DE TUPLAS --- """  # La forma de buscar elementos o metodos, como saber el tamaño, es igual que con listas

listaInmutable = (10, 20, 30, 40)  # Se le llama TUPLA y es una lista inmutable, no se puede modificar

print(f"Largo de una tupla: {len(listaInmutable)}")

listaMutable = list(listaInmutable)  # Convierto la Tupla en una Lista. Sirve si queremos modificarla

listaInmutable = tuple(listaMutable)  # Convierto la Lista en una Tupla


""" --- EJEMPLO DE SET --- """  # No mantiene un orden, no tiene indices y no permite elementos duplicados. Muchos metodos son iguales a las Tuplas y Listas

planetas = {'Marte', 'Jupiter', 'Venus'}

print(planetas)  # No va a ser necesariamente el mismo orden

planetas.add('Tierra')  # Agrega un elemento al final del Set
planetas.add('Tierra')  # Aunque agreguemos nuevamente el dato no se va a agregar al Set

print(f"Se agrega Tierra: {planetas}") 


""" Metodo Zip """  # Une dos colecciones que tengan el mismo largo. Devuelve el tipo de coleccion que le indiquemos casteandolo. Cada elemento de la coleccion van a ser el par de elementos de las otras listas en el orden de sus indices

zip1= [1,2,3]
zip2= [4,5,6]

zip3 = list(zip(zip1,zip2))

print(zip3)

nombres = ["Agustin", "Juan", "Pablo"]
edades = [24, 40, 15]

dicZip = dict(zip(nombres, edades))  # Devuelve un diccionario con su clave valor

print(dicZip)


""" Metodo Deepcopy"""  # A diferencia de Copy hace un copiado mas profundo. Se utiliza para copiar variables que almacenen estructuras complejas

listaCompuesta = [1,2,3, ["Gato", "Perro"]]

listaCopiada = deepcopy(listaCompuesta)

print(listaCopiada)