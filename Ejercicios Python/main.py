"""
1- Crear una clase llamada Persona que tenga los siguientes atributos: nombre, dni y edad.

La clase debe tener los siguientes metodos:

                                    *Constructor __init__ donde los datos puden ser vacios.
                                    *Setters y Getters.
                                    *mostrar(): Muestra los datos de la persona.
                                    *esMayorDeEdad(): Devuelve un booleano indicando si es mayor de edad o no.
                                    
                                                                        
2- Crear una clase llamada Cuenta que tenga los siguientes atributos: titular (de tipo persona), numero de cuenta (tiene que ser un numero random) y cantidad (indica la cantidad de dinero).

La clase debe tener los siguientes metodos:

                                    *Constructor __init__ donde los datos puden ser vacios.
                                    *Setters y Getters. El atributo cantidad solo se modifica extrayendo o ingresando
                                    *mostrar(): Muestra los datos de la cuenta.
                                    *ingresar(cantidad): Se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
                                    *retirar(cantidad): Se retira una cantidad de la cuenta, si la cantidad supera lo que hay, no se permitira.
                                    
                                    
3- Crear una clase llamada Banco que tenga los siguientes atributos: nombre, cuentas(una lista de todas los numeros de cuenta).

La clase debe tener los siguientes metodos:

                                    *Constructor __init__ donde los datos puden ser vacios.
                                    *mostrar(): Muestra todas las cuentas.
                                    *ingresar(cuenta): Se ingresa una cuenta nueva (solo el numero)
                                    *eliminar(cuenta): Se elimina uma cuenta. Písta: hay una funcion que elimina un elemento buscando de un arreglo.                     
"""

from Models.Persona import *

persona = Persona("Agustin", "40884962", 14)

print(persona)
