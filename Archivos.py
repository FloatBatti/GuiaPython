# Para abrir un archivo y luego cerrarlo automaticamente se usa la sentencia with
# Se declara de la siguiente manera ---> with open("<nombre del archivo>.text", "<modo>") as <variablearchivo>:
# Los modos los mismos que C pero sin binario

arreglo = [1, 2, 3, 4]
nombre = "Agus"

""" ABRIMOS Y ESCRIBIMOS UN ARCHIVO """

try:
    
    archivo = open("Archivo.txt", "w", encoding="utf8")  # El ultimo parametro hace que se acepten acentos
    archivo.write("Hola, soy un archivo \n")
    archivo.write("Estoy programando en Python")

except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()


""" ABRIMOS Y LEEMOS UN ARCHIVO """

print("Se abre y lee un archivo con .read()".center(50, "-"))

try:
    
    archivo = open("Archivo.txt", "r", encoding="utf8")

    print(archivo.read())  # Se puede poner como parametro la cantidad de caracteres a leer, sino lee todo el texto

except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()
    

print("Se abre y lee archivo con .readline()".center(70, "-"))

try:
    
    archivo = open("Archivo.txt", "r", encoding="utf8")

    print((archivo.readline()))  # Lee una sola linea.

except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()


print("Se abre y lee un archivo con .readlines()".center(70, "-"))

try:
    
    archivo = open("Archivo.txt", "r", encoding="utf8")

    list = archivo.readlines()  # Lee todas las lineas y devuelve una lista con ellas
    
    print(list)
    print(type(list))


except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()

print("Se abre y lee un archivo con .readlines()[<indice>]".center(70, "-"))

try:
    
    archivo = open("Archivo.txt", "r", encoding="utf8")

    list2 = archivo.readlines()[1]  # Lee la linea en la posicion que le indicamos. Tambien lo devulve como lista
    
    print(list2)
    print(type(list))
    

except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()
