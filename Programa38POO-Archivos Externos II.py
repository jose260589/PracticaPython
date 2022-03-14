from io import open

archivo_texto=open("archivo.txt","r+")

#print(archivo_texto.read())

# modificar posicion del cursor, se usa el metodo seek

#archivo_texto.seek(11)#este es donde empienza a para que podamos leer el archivo

#print(archivo_texto.read())#si el numero 11 lo usamos en el read(), este lee hasta esa posicion

"""
se puede usar de dos formas
archivo_texto=open("archivo.txt","r+") # luego validar si se agrega otra letra o no
de esta forma se puede leer y escribir el documento.
"""

lista_texto=archivo_texto.readlines();

lista_texto[1]=" Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()
