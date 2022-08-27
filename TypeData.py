import math
from copy import copy, deepcopy

PI_CONS = math.pi  # En python no existen las constantes. Por convencion se pone la variable en mayuscula y las palabras divididas por un '_'. Las constantes se declaran en un modulo distinto
pi = round(PI_CONS, 4)  # Lo redondeo a 4 decimales
print(pi)

vacio = None # Indica que la variable no guarda ningun valor

# La funcion input siempre devuelve una cadena de caracteres, por eso se castea

name = input("Ingrese nombre: ")  # Se pide ingresar un nombre

edad = int(input("Ingrese edad: "))  # Se pide ingresar una edad y se castea para que tome un int y no un string

temp = int(input("Temperatura: "))

# Es importante buscar la parte entera para los algoritmos de búsqueda binaria
print(20 / 3)  # El resultado es un flotante
print(20 // 3)  # Muestra la parte entera del resultado, devuelve un int
print(20.5 / 3.2)
print(20.5 // 3.2)
print(5 ** 3)  # significa potencia, sería 5 al cubo




"""" --- STRINGS --- """

# Los Strings son Inmutables, es decir, cuando devolvemos un String formateado por un método, la variable que lo almacena, apunta a otra direccion de memoria. No se cambia el String original, sino que se crea uno nuevo

print(" Metodos y caracteristicas de los Strings ".center(50,'-'))  # Ubica el String en el centro, y a sus lados los caracteres que indicamos. El String indicado tambien se cuenta dentro de cuenta de los 50 caracteres

nombre = "Agustin"
myStr = "hOlA mI nOmBre Es aGus"
stripp = "       Soy un Texto #&$ "

# Se pone la f antes de las comilla para meter variables dentro de la oración con {}
print(f"Soy {name} y tengo {edad}")

print(type(name))  # Muestra el tipo de dato

print(name + " y " + nombre)  # Se puede concatenar cadenas de caracteres con +

print(nombre.center(30))  # Devuelve una cadena centrada en un campo de tamaño

print(" Strings en Python ".center(50,'-'))  # Ubica el String en el centro, y a sus lados los caracteres del tipo que indicamos. El String indicado tambien se cuenta dentro de los 50

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

if temp < 25:
    print("Hace frio")
else:
    print("Hace calor")
    
""" AYUDA EN PYHTON """

help(math)  # Nos devuelve informacion de clases y metodos. Con la tecla Enter se puede ver mas informacion
