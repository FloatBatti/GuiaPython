from DAO.Connection import *

connection = Connection()


resultSet = connection.ExecuteOneQuery("select * from empleados where id_empleado = 1")

print(resultSet)

connection.Close()



    
    
#resultSet = connection.ExecuteNoQuery("""insert into empleados(nombre_empleado,dni, telefono, cbu, id_cargo, id_local)
                                      
                                      #values('Francisco', '12345678','2236064852', '0003666454', 1, 1)""")


