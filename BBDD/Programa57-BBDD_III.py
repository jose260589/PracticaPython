import sqlite3

miconexion=sqlite3.connect("gestionproductos")

micursor=miconexion.cursor()
#ejemplo cursor para pedir y enviar datos. datos a base de datos.
# con primary key y auto incremento. esto es con la bd de sqlite.

micursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
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

miconexion.commit()

miconexion.close()
