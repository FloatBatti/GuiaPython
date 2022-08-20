# Para abrir un archivo y luego cerrarlo automaticamente se usa la sentencia with
# Se declara de la siguiente manera ---> with open("<nombre del archivo>.text", "<modo>") as <variablearchivo>:
# Los modos los mismos que C pero sin binario

arreglo = [1, 2, 3, 4]
nombre = "Agus"

archi = open("Arreglos.bin", "w")

archi.write(arreglo[0])

archi.close()

archi = open("Arreglos.bin", "r")

print(archi.read())

archi.close()

print("------ \n")
