"""
sintaxis generador.
Def nombergenerador():
    Instruciones

    yiel numeros #Funciona igual que el return, aunque este tmaiben lo puede llevar.
"""
"""
#Ejemplo 1
def funcionpar(limite):
    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)

        num+=1

    return miLista

print(funcionpar(10))
#ejemplo2
def funcionpar2(limite):
    num=1
 

    while num<limite:
        yield  num*2
        num+=1
    



devuelvePares=funcionpar2(10)
#for i in devuelvePares:
#    print(i)
print(next(devuelvePares))
print("Ejemplo")


print(next(devuelvePares))
print("Ejemplo")


print(next(devuelvePares))
print("Ejemplo")

print(next(devuelvePares))
print("Ejemplo")
"""

"""
yield from: es parecido a una matriz
sintaxis
 # el asterico significa que va a recibir muchos elementos y los
    #va a recibir en forma de tupla.
"""
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento: es lo mismo que yield from, esto hara dos 
        yield elemento

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
    
print(next(ciudades_devueltas))

print(next(ciudades_devueltas))
