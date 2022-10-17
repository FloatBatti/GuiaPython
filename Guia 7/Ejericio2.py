import random

class Numeros:
    
    def __init__(self) -> None:
        
        self._listaNumeros = []
        self.guardarNumerosRandom()
        
    
    def __str__ (self):
        return f"{self._listaNumeros}"
    
    
    def candidato (self):
        
        numeroCandidato = int(input("Ingrese un numero para saber las veces que se repite: "))
        
        veces = self._listaNumeros.count(numeroCandidato)
        
        print(f"La cantidad de veces que se repite el numero {numeroCandidato} es {veces}")
        
        
    def guardarNumerosRandom(self):
        
        cant = int(input("Ingrese la cantidad de numeros a ingresar: "))
        
        min = int(input("Ingrese el valor minimo: "))
        
        max = int(input("Ingrese el valor maximo: "))
        
        for num in range(cant):
            
            numero = random.randint(min,max)
            
            self._listaNumeros.append(numero)
    
    

numeros = Numeros()

print(numeros)

numeros.candidato()
