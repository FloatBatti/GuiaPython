""" MANEJO DE CONTEXTO WITH"""

print("Se abre y lee archivo utilizando with".center(70, "-"))
from logging import Manager
from traceback import print_tb

from ClaseArchivos import ManejoArvhivos


with open ("Archivo.txt", "r", encoding="utf8") as archivo:  # With abre y cierra de forma automatica el archivo. No hace falta el poner un bloque Try-Catch
    print(archivo.read())
    
#  Esta operacion hace uso de los metodos __enter__ (cuando se abre) y __exit__ (cuando se cierra). Ambos se pueden sobreescribir y personalizar 


""" UTILIZANDO LA CLASE PERSONALIZADA"""

print("Se abre y lee archivo utilizando Context Manager".center(70, "-"))

with ManejoArvhivos("Archivo.txt") as archivo:
    print(archivo.read())