class Alumno:
    
    def __init__(self):
        
        self._nombre = input("Ingrese nombre: ")
        self._apellido = input("Ingrese apellido: ")
        self._notas = []
        self.subirNotas()
        
        
        
    def subirNotas(self):
        
        op = 1
        indice = 1
        
        while(op == 1):
            
            nota = (float(input(f"Ingrese la nota numero {indice}. ")))
            
            if (nota >= 0 and nota <= 10):
                
                 self._notas.append(nota)
                 indice += 1
                 
            else:
                
                print("La nota esta fuera de rango")
                 
        
            op = int(input("Presione 0 para salir o 1 para seguir: "))
                 
            
            
alum = Alumno()      
            
    