import math

PI_CONS = math.pi  # En python no existen las constantes. Por convencion se pone la variable en mayuscula y las palabras divididas por un '_'. Las constantes se declaran en un modulo distinto
pi = round(PI_CONS, 4)  # Lo redondeo a 4 decimales
print(pi)

# La funcion input siempre devuelve una cadena de caracteres, por eso se castea

name = input("Ingrese nombre: ")  # Se pide ingresar un nombre

edad = int(input("Ingrese edad: "))  # Se pide ingresar una edad y se castea para que tome un int y no un string

temp = int(input("Temperatura: "))

nombre = "Gonzalo"

# Se pone la f antes de las comilla para meter variables dentro de la oración con {}
print(f"Soy {name} y tengo {edad}")

print(type(name))  # Muestra el tipo de dato

print(name + " y " + nombre)  # Se puede concatenar cadenas de caracteres con +

# Es importante buscar la parte entera para los algoritmos de búsqueda binaria
print(20 / 3)  # El resultado es un flotante
print(20 // 3)  # Muestra la parte entera del resultado, devuelve un int
print(20.5 / 3.2)
print(20.5 // 3.2)
print(5 ** 3)  # significa potencia, sería 5 al cubo

# El if se declara de la siguiente manera. Se puede no usar {}, por ejemplo en el else

if temp < 25:
    print("Hace frio")
else:
    print("Hace calor")
