from Paciente import Paciente
from Persona import Persona


class Doctor(Persona):
    
    def __init__(self,nombre:str, dni:str, telefono:str, mail:str, especializacion:str):
        
        super().__init__(nombre, dni, telefono, mail)
        self._especializacion = especializacion
        self._listaConsultorios = []
        self._listaPacientes = []
        
    def agregarPaciente(self, nuevoPaciente:Paciente):
        
        self._listaPacientes.append(nuevoPaciente)
        


