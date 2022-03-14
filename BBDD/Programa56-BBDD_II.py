import sqlite3

#conexion a base de datos
miConexion=sqlite3.connect("zoe")

#cursor
miCursor=miConexion.cursor()


#INSERTAR DATOS A TABLA
"""variosproductos=[
    ("Camisa", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")

    ]

miCursor.executemany("insert into PRODUCTOS VALUES(?,?,?)",variosproductos)
"""

#seleccionar datos
miCursor.execute("select * from PRODUCTOS")

variosproductos=miCursor.fetchall()

# ejemplo 1print(variosproductos[0:4])

for producto in variosproductos:
    print("Nombre Producto: ",producto[0], "Seccion: ", producto[2])

miConexion.commit()


#cerrar conexion
miConexion.close()
