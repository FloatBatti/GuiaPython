# Para abrir un archivo y luego cerrarlo automaticamente se usa la sentencia with
# Se declara de la siguiente manera ---> with open("<nombre del archivo>.text", "<modo>") as <variablearchivo>:
# Los modos los mismos que C pero sin binario

arreglo = [1, 2, 3, 4]
nombre = "Agus"

try:
    
    archivo = open("Archivo.txt", "w", encoding="utf8")  # El ultimo parametro hace que se acepten acentos
    archivo.write("Hola, soy un archivo")

except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()


try:
    
    archivo = open("Archivo.txt", "r")

    print(archivo.read())

except Exception as e:
    
    print(e)
    
finally:
    
    archivo.close()

print("------ \n")
