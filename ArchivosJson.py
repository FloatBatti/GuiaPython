import json #Los Json guardan diccionarios, por ende los objetos tienen que ser transformados en estos

from SistemaHospital.Models.Persona import Persona

fileName= "Data/Personas.json"
data=[]

"""
with open (fileName, "r", encoding="utf8") as archivo:
            
    contenido = archivo.read()
    jsonContent = json.loads(contenido)
    
    print(jsonContent[0])
    
    persona= Persona(
        
        jsonContent[0]["_nombre"],
        jsonContent[0]["_dni"],
        jsonContent[0]["_telefono"],
        jsonContent[0]["_mail"]
        
        )
    
    print(type(jsonContent))
    
    print(persona)
"""

with open (fileName, "r", encoding="utf8") as archivo:  # Lo abro en modo lectura
    
    try:
        data = json.load(archivo) #Mejor opcion para manipular. Devuelvo todo el json como una lista
        
    except:
        print("Archivo vacio")
        data=[]
    
    
with open (fileName, "w", encoding="utf8") as archivo:  # Lo abro en modo escritura
    
    persona = Persona("Cosme Fulanito", "12345678", "mailfake@gmail.com", "2237654321", "11578497", "261587954")
    
    objectDict = persona.__dict__  # Le doy formato de diccionario al objeto
    
    data.append(objectDict)  # Agrego el objeto a la lista
    
    json.dump(data, archivo, indent= 4, separators=(", ", " : "))  # Cargo la lista nueva al Json, es decir, actualice mi archivo


