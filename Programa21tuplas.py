#TUPLAS
#Son listasinmutables o que no cambia. no se modifica.
#son mas rapidas, menos espacio, formatean, se pueden usar como claves en un diccionario
"""
sintaxis
nombreTupla=(elem1,elem2,elem3...)
la diferencia es que se colocan los (), en vez de los [], pero se manejan igual.

"""

mitupla = ("Juan", 13, 1, 1995)

print(mitupla[1]) #se busca igual que en la lista

#metodo list, se usa para cambiar una tupla en lista

milista=list(mitupla)
print(mitupla)
print(milista)

#metodo tuple, es lo inverso, este convierte una lista en tupla

# para buscar en tupla

print("Juan" in mitupla)

#esto es para que cuente cuantas veces hay un elemento en una tupla
print(mitupla.count(13))
#print(lista.count[13]) no funciona en lista

#metodo len es para ver la longitud de una tupla
print("Longitud tupla: ",len(mitupla)) #funciona igual en lista tupla
print("Longitud Lista: ",len(milista))

#tuplas unituraria
mitupla2=("Jose",) #sino se coloca la coma muestra una longitud diferencte o erronea
print(len(mitupla2),"\n")

"""
#desempaquetado de tupla
con saber la longitud de la tupla, se puede agregar a distintas variables,
y python lo va agregando en el mismo orden.
"""

nombre, dia, mes, agno=mitupla
print(nombre)
print(dia)
print(mes)
print(agno)

#index, saber la posicion de un elemento
print(mitupla.index("Juan"))
