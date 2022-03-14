import sqlite3

miconexion=sqlite3.connect("gestionproductos")

micursor=miconexion.cursor()
#ejemplo cursor para pedir y enviar datos. datos a base de datos.
# con primary key y auto incremento. esto es con la bd de sqlite.
#UNIQUE: significa unico, que no se puede repetir
"""
#insectar 
micursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
    ''')


productos=[
    ("pelota",20,"jugueteria"),
    ("pantalon",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarròn",45,"ceramica")

    ]

micursor.executemany("insert into PRODUCTOS values (NULL,?,?,?)",productos)
"""
"""
#leer
micursor.execute("select * from PRODUCTOS where seccion='confeccion'")

#asignar datos del cursor a una variable
productos=micursor.fetchall()
"""
"""
#update
micursor.execute("update PRODUCTOS set precio=35 where nombre_articulo='pelota'")
"""
"""
#delete
micursor.execute("delete from PRODUCTOS where id=3")
"""
miconexion.commit()

miconexion.close()
