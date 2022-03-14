"""
Archivos Externos
es para la persistencia de datos

Hay dos tipos.
Manejo de archivos externor
Base de Datos.

Tiene 4 Faces.
creacion
apertura
manipulacion
cierre
------------------------------------------------------
para abrirlo
open()
example:
variable=indicacion
archivo_texto=open()

dentro de open() pide 2 argumentos.
1. nombre del archivo que vamos a abrir
2. El modo que se va a abrir
distintos modos(
r:lectura: solo para leer
w:escritura: para agregar datos si esta vacio
a:append: agregar datos si este ya tenia datos
)
example:
archivo_texto=open("archivo.txt","w")
agregar datos
variable del archivo.metodo(Variable de cadena a agregar)
example
cerrarlo(para que se graben los datos hay que cerrarlo)
nombre
"""

from io import open
"""
#leer o crear el archivo sino existe, en este caso es crear o escribir
archivo_texto=open("archivo.txt","w")

#ejemplo 1
frase="Estupendo dia para estudiar python \n el miercoles"
#escribir texto
archivo_texto.write(frase)
#cerrar archivo para que se guarden los datos.
archivo_texto.close()
"""
"""
#Ejemplo2 leer
#leer o crear el archivo sino existe, en este caso es leer
archivo_texto=open("archivo.txt","r")
#almacena en la variable texto todo los datos de del archivo que esta leyendo
texto=archivo_texto.read()
#cerrar archivo
archivo_texto.close()
#imprimir datos de la variable texto
print(texto)
"""

"""
#ejemplo3
#leer o crear el archivo sino existe, en este caso es leer
archivo_texto=open("archivo.txt","r")
#almacena en la variable texto todo los datos de del archivo que esta leyendo
texto=archivo_texto.readlines() #con este metodo readline, lee los datos inea a linea
#cerrar archivo
archivo_texto.close()
#imprimir datos de la variable texto
print(texto[1])
"""

#ejemplo3
#agrega datos al archivo sin borrar lo anterior gardado.
archivo_texto=open("archivo.txt","a")
#almacena en la variable texto todo los datos de del archivo que esta leyendo
texto=archivo_texto.write("\n siempre es una buena ocasion para  estudiar python") #escribir en el archivo
#cerrar archivo
archivo_texto.close()

