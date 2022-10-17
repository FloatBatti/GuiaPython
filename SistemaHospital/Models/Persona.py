
from argparse import Namespace


class Persona:
    
    def __init__ (self,nombre, dni, mail, *telefonos):
        
        self._nombre = nombre
        self._dni = dni
        self._telefono = list(telefonos)
        self._mail = mail
        
    def __str__(self):
        
        return f"Nombre: {self._nombre}\nDNI: {self._dni}\nTelefono: {self._telefono}\nMail: {self._mail}"
        
        
