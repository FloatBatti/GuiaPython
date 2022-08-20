class Persona():  
    
    def __init__ (self, nombre, edad):
        
        self._nombre = nombre  # No le pongo doble guion bajo porque si se hereda, el hijo no puede acceder al atributo
        self._edad = edad
        

    
        
    def __str__(self):
        
        return f"Nombre: {self._nombre}, Edad: {self._edad}"
        

       
class Empleado(Persona):
    
    def __init__ (self, nombre, edad, sueldo):
        
        super().__init__(nombre, edad)  # Los atributos heredados se ubican en el super (Constructor del padre)
        self._sueldo = sueldo
    
    def trabajar():
        print("Estoy trabajando")
    
    def __str__(self):  # Sobreescribe la funcion __str__ del padre
        
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Sueldo: {self._sueldo}"
    



