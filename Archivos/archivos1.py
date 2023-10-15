#abrir y cerrar archivos
from io import open
archivo_estudiantes = open("estudiantes.txt","r") #asi abrimos un archivo
print(archivo_estudiantes.readable()) #esta funcion es para saber si un archivo es legible o que se pueda leer
print(archivo_estudiantes.read())#con esta se lee el archivo
print(archivo_estudiantes.readline())#lee la primera linea, si se lee dos veces, lee la segunda.
print(archivo_estudiantes.readlines())#esto crea una lista
archivo_estudiantes.close() #Asi cerramos un archivo