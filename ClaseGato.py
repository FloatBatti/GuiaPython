# Por convencion, en Python las clases comienzan con mayuscula
# Cada clase tiene un diccionario con su atributo (value) y su valor (key)
# Un objeto es una instancia de una clase

# Ejemplo 1

class Gato:
    
    especie = "Mamifero"  # Atributo de clase. Todos los objetos van a tener el atributo mamifero, es inmutable, estatico constante. Ademas no hace falta crear un objeto para acceder a este atributo
    edadMaxima = 20
    

    def __init__(self, nombre, edad, *alimentos):  # Constructor. Self siempre es una referencia al objeto mismo, siendo siempre el el primer parámetro formal. El constructor define la forma en que se crean los objetos 
    
    # El doble guion bajo indica que no es modificable fuera de la clase
    # Si utilizamos un solo guion bajo indicamos que no se tendria que modificar, pero no quita que sea posible
      
        self.__nombre = nombre
        self.__edad = edad
        self.alimentos = list(alimentos)
        self.__numeroPatas = 4
        
    def __str__(self):
        
        return f"Nombre: {self.__nombre} , Edad: {self.__edad} , Alimentos: {self.alimentos}, Patas: {self.__numeroPatas}"


    # Para que funcione primero se pone el property y luedo el setter
        
    @property  # Es solo un decorador que se le asiganan a los Getters. Al poner esto no se necesita poner parentesis en la llamada del metodo
    def edad(self):
        return self.__edad

    @edad.setter  # Es solo un decorador que se le asiganan a los Setters. Al poner esto no se necesita poner parentesis en la llamada del metodo
    
    def edad(self, edad):
        self.__edad = edad
        
    def __cambiarPatas(self, cantPatas):  # Tambien podemos hacer privado los metodos
        self.__numeroPatas = cantPatas

    def __del__(self):  # Metodo que elimina al objeto de la memoria
        print(f"El objeto de nombre {self.__nombre} se elimino de la memoria")
        
    def verEtapaDeVida(self):
        if self.__edad > 1:
            print(f"{self.__nombre} es adulto")
        else:
            print(f"{self.__nombre} es cachorro")

    def esAlimentoFavorito(self, alimento):  #  Ejemplo de documentar una función
        
        """
        La fucion evalua si el alimento recibido como parametro está en la lista del objeto
        
            Parameter:
                        alimento (str) : Alimento a evaluar
                    
            Return:
                        (boolean) : Retorna True si esta o False de lo contrario
                    
        """
        return alimento in self.alimentos


    @staticmethod  # Metodo estatico. Hace que la funcion se relacione con la clase y no con los objetos. No puede acceder a variables de instancia y tampoco tiene relacion con los datos de la clase. Sirve si queremos tener un metodo de clase que no tenga nada que ver con los atributos (de la clase o su instancia)
    def maullar():
        print(f"Este {Gato.especie} hace Miaw")
        
    @classmethod  # Metodo de clase. Puede acceder a metodos o variables de la clase
    def edadCritica(cls, edad):  # En vez de self lleva un argumento que hace referencia a la propia clase, no a la instancia. Se puede acceder a las variables de clase sin tener que utilizar el nombre de la clase
        return (edad > cls.edadMaxima)
        
        

"""
Atributos: especie, nombre, edad, alimentos
Metodos: __init__, verEtapaDeVida, esAlimentoFavorito
"""

Gato.tipo = "Felino"  # Crea una variable de clase al vuelo. No es una practica que se utiliza

print(Gato.tipo)