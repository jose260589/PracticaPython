"""
en la segunda version hay que hacerlo automatica, para prueba del 1 al 12
"""

from io import open

def archivar(numero):
    multiplos = numero
    newarchivo = open(f"tabla del 1 al 12.txt","a") #crear archivo o modificarlo si este ya esta creado
    print(newarchivo.writable()) #Ver si tengo permiso de escritura
    print(newarchivo.write(f"Tabla del {multiplos}\n\n")) #agregar titulo de la tabla 
    
    for (i) in range(10): 
        print(newarchivo.write(f"{multiplos} x {i+1} = {multiplos*(i+1)}\n")) #de esta forma agrego los datos de las tablas usando un for
    
    print(newarchivo.write("\n\n"))
    newarchivo.close()


#llamado de funcion Usando un for desde afuera de la funcion.
for m in range(12):
    archivar(m+1)