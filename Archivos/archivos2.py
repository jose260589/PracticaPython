#abrir y cerrar archivos
from io import open
"""
para escribir se usa 'w' si esta en blanco o no crado.
para agregar otros datos al archivo se puede usar 'a'
"""
archivo_estudiantes = open("estudiantes2.txt","a") #asi abrimos un archivo o lo creamos si no existe.
print(archivo_estudiantes.writable()) #es para ver si tiene permiso de escritura. 
#print(archivo_estudiantes.write("Este es un nuevo archivo\nY podemos hacer saltos de linea"))
"""
Tener en cuenta que para agregar mas lineas en un archivos hay que usar lo siguiente.
si no se hace de esta forma, puede reescribir el texto anterior o colocarlo 
en la misma linea cuando se desee colocar en otra linea.    
"""
#print(archivo_estudiantes.write("\nsalto de linea para hacer pruebas."))
print(archivo_estudiantes.write("\nprueba de agregar una 4ta linea."))
archivo_estudiantes.close() #Asi cerramos un archivo