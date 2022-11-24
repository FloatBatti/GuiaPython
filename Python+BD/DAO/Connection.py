from shutil import ExecError
import mysql.connector


class Connection:

    def __init__(self):
        
        try:
            self.mydb = mysql.connector.connect(
                
                host="localhost",
                user="root",
                password="",
                database="frutas_magicas"
            )
            
        except Exception as ex:
            
            print("Error en base de datos")
            
    
    def ExecuteOneQuery(self, query):
        
        cursor = self.mydb.cursor()
        cursor.execute(query)
        
        return cursor.fetchone()   
    
    
    def Execute(self, query):
        
        cursor = self.mydb.cursor()
        cursor.execute(query)
        
        return cursor.fetchall()
    
    
    def ExecuteNoQuery(self, query):
        
        cursor = self.mydb.cursor()
        cursor.execute(query)
        
        self.mydb.commit()
        
    def Close(self):
        
        self.mydb.close()
        
        

