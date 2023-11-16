"""
Crear un programa que genere un archivo con la tabla de un numero escrito por el usuario. del 1 al 10
el numero puede ser aleatorio.
"""
from io import open

def archivar(numero):
    multiplos = numero
    newarchivo = open(f"tabla-{multiplos}.txt","a")
    print(newarchivo.writable()) #Ver si tengo permiso de escritura
    print(newarchivo.write(f"Tabla del {multiplos}\n"))
    
    for (i) in range(10): 
        print(newarchivo.write(f"{multiplos} x {i+1} = {multiplos*(i+1)}\n"))
    
    newarchivo.close()


multiplicar = int(input("Digita el numero que se va a multiplicar: "))
archivar(multiplicar)