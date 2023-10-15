#abrir y cerrar archivos
from io import open
archivo_estudiantes = open("estudiantes2.txt","w") #asi abrimos un archivo o lo creamos si no existe.
print(archivo_estudiantes.writable()) #es para ver si tiene permiso de escritura. 
print(archivo_estudiantes.write("Este es un nuevo archivo\nY podemos hacer saltos de linea"))
"""
Tener en cuenta que para agregar mas lineas en un archivos hay que usar lo siguiente.
    
"""
archivo_estudiantes.close() #Asi cerramos un archivo