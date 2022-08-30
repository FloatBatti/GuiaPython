from copy import deepcopy



""" --- EJEMPLOS DE LISTAS / ARREGLOS --- """

print(" Ejemplo de Listas/Arreglos ".center(50, "-"))

lista = [1, 2, 3, "agus", True, "curso python"]  # la lista puede ser mixta

listaNum: list[int] = [1, 2, 3, 4, 5, 7]  # Lo casteo a entero

print(f"Lista concatenada: {lista + listaNum} ")  # El + concatena (une) las listas en una sola

print(f"Lista original: {listaNum}")

print(f"Lista repetida {listaNum * 3}")  # El * hace que la lista se repita una cantidad determinada de veces. Obtengo una lista de elementos simples

print(f"Lista con elementos complejos repetidos {[listaNum] * 3}")  # Se crea una lista que contiene 3 listas como elementos

print("Lista incializada de 10 elementos: ", 10*[0])  # Crea una lista de n cantidad de elementos cuyos valores son los que se indican entre corchetes 

print(f"Primeros dos numeros: {listaNum[0:2]}")  # Toma los valores del indice 0 al 2. El elemento del ultimo indice no se toma, es decir, el elemento de la posicion 2 no va a ser devuelto

print(f"Ultimo indice de la lista : {listaNum[-1]}")  # Con numeros negativos puedo navegar de forma inversa

listaNum.append(8)  # agrega un elemento al final de la lista

# Inserta un elemento en el indice elegido ---> <lista>.insert(<indice>, <elemento>)
listaNum.insert(5, 6)  # El elemento que estaba en esa posicion se corre un lugar a la derecha

print(f"Lista Modificada: {listaNum}")

listaNum.remove(5)  # Remueve el elemento ingresado como parametro (la primera aparición). Si no está en la lista se genera un error

listaNum.pop()  # Remueve el ultimo elemento de la lista. Si se indica el indice por parametro se borra el elemento en dicho indice

del listaNum[0]  # Se elimina un elemento especificando un indice

print(f"Remuevo el 5: {listaNum}")

print(f"Posición del numero 4: [{listaNum.index(4)}]")  # Busca cual es la posicion del numero 4

print(3 in listaNum)  # Devuelve True si el elemento esta en la lista, de lo contrario False

lista.extend(listaNum)  # Agrega al final de la lista mas de un elemento. El argumento tiene que ser si o si una estructura del mismo tipo

print(f"Lista extendida: {lista}")

print(f"Veces que se repite el 2: {lista.count(2)}")  # Cuenta la cantidad de veces que un elemento se encuentra en una lista

print(f"El ultimo elemento de listaNum: {listaNum.pop(), listaNum}")  # Elimina y devuelve el ultimo elemento de la lista

del listaNum[1]  # Borra el item de la posición indicada

print(f"Borro el 2 : {listaNum}")

listaNum.reverse()  # Reversa el orden actual de la lista

print(f"La lista al revez quedaria: {listaNum}")

listaNum.sort()  # Ordena la lista de forma ascendente

listaNum.sort(reverse=True)  # Ordena la lista de forma descendente

listaNum.clear()  # Borra todos los elementos de la lista, pero esta sigue en la memoria

del listaNum  # Borra la lista de la memoria


""" --- EJEMPLO DE TUPLAS --- """  # Es una lista inmutable, no se puede modificar. La forma de buscar elementos o metodos, como saber el tamaño, es igual que con listas

print(" Ejemplo de Tuplas ".center(50, "-"))

listaInmutable = (10, 20, 30, 40)  

print(f"Largo de una tupla: {len(listaInmutable)}")

listaMutable = list(listaInmutable)  # Convierto la Tupla en una Lista. Sirve si queremos modificarla

listaInmutable = tuple(listaMutable)  # Convierto la Lista en una Tupla


""" --- EJEMPLO DE SET --- """  # No mantiene un orden, no tiene indices y no permite elementos duplicados. Muchos metodos son iguales a las Tuplas y Listas

print(" Ejemplo de Set ".center(50, "-"))

planetas = {'Marte', 'Jupiter', 'Venus'}

print(planetas)  # No va a ser necesariamente el mismo orden

planetas.add('Tierra')  # Agrega un elemento al final del Set
planetas.add('Tierra')  # Aunque agreguemos nuevamente el dato no se va a agregar al Set

print(f"Se agrega Tierra: {planetas}") 


""" Metodo Zip """  # Une dos estructuras que tengan el mismo largo. Devuelve el tipo de estructura que le indiquemos casteandolo. Cada elemento de la estructura van a ser el par de elementos de las otras listas en el orden de sus indices

print(" Ejemplo del metodo Zip ".center(50, "-"))

zip1= [1,2,3]
zip2= [4,5,6]

zip3 = list(zip(zip1,zip2))

print(zip3)

nombres = ["Agustin", "Juan", "Pablo"]
edades = [24, 40, 15]

dicZip = dict(zip(nombres, edades))  # Devuelve un diccionario con su clave valor

print(dicZip)


