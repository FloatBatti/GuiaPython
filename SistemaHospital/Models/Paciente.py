from Persona import Persona
from Turno import Turno

class Paciente(Persona):
    
    def __init__(self, nombre:str, dni:str, telefono:str, mail:str, obraSocial:str):
        
        super().__init__(nombre, dni, telefono, mail)    
        self._obraSocial = obraSocial
        self._listaTurnos = []
        self._listaDoctores = []
        
     
    def agregarTurno(self, nuevoTurno:Turno):
         
         self._listaTurnos.append(nuevoTurno)
         
    def mostrarTurnos (self):
        
        for turno in self._listaTurnos:
            
            print(turno)
        
