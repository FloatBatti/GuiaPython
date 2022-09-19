class Alumno:
   
    def __init__(self):
       
        self.nombre = input("Ingrese su Nombre: ")
        self.apellido = input("Ingrese su Apellido: ")
        self.notas = []
       
        cant = int(input("Ingrese cantidad de notas a subir: "))
       
        for nota in range(1,cant+1):
           
            self.notas.append(float(input(f"Ingrese la nota numero {nota}: ")))
           
     
    def __str__(self):
           
            return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Notas: {self.notas}"
       
 
alumno1 = Alumno()

