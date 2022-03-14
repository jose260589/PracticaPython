import sqlite3

#conexion a base de datos
miConexion=sqlite3.connect("zoe")

#cursor
miCursor=miConexion.cursor()

#Se usa para crear una tabla si ya esta creada se comenta o borra para que no se ejecute mas de una vez
#miCursor.execute("create table PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#INSERTAR DATOS A TABLA
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

miConexion.commit()


#cerrar conexion
miConexion.close()
