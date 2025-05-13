#creando una lista con list() "se usa mas para crear listas vacias" o constructor
# para crear lista se puede hacer "Variable = [datos]"
lista = list(["hola","Jose",34,56,23,True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista, este lo agrega al final
lista.append("JAJAJAJA")

#Agregando un elemento a la lista en un indice especifico
lista.insert(2,"Toma mama")

#agregando varios elementos a la lista
lista.extend([False, 2030])

#Eliminando un elemento de la lista(Por su indice)
lista.pop(0)
#lista.pop(-1) de esta forma elimina el ultimo elemento de la lista

#removiendo un elemento de la lista por su valor
lista.remove("Toma mama")
print(lista)

#ordenando la lista de forma ascendente(si usamos el parametro reverse=True lo ordena en reversa )
#lista.sort() #no soporta al mismo tiempo int and str. 
lista2 = [34,56,True,False,65,2030,False]
lista2.sort(reverse=True)


#inviertiendo los elementos de una lista
lista2.reverse()

#Eliminando todos los elementos de una lista
#lista2.clear()

#asi puede funcionar
#print(dir(('dsafsdfasd',5)))

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(56)

print(elemento_encontrado)

#Crear una lista apartir de un rango
r = list(range(0,10))
print(r) 
