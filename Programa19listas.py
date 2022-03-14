"""
primer ejemplo de lista
 Ferrari2014=["Fernando Alonso", "Kimi Raikkonen"]
 print (Ferrari2014)


 Las operaciones más habituales que se realizan en Python son las siguientes:

lista[i]: Devuelve el elemento que está en la posición i de la lista.
lista.pop(i): Devuelve el elemento en la posición i de una lista y luego lo borra.
lista.append(elemento): Añade elemento al final de la lista.
lista.insert(i, elemento): Inserta elemento en la posición i.
lista.extend(lista2): Fusiona lista con lista2.
lista.remove(elemento): Elimina la primera vez que aparece elemento.
Si representamos todo esto en un ejemplo:

Python
>>> # Acceder a un elemento de la lista.
>>> print(Ferrari2014[1])
Kimi Raikkonen

>>> # pop: Extraemos a Kimi (que está en la posición número 1) de la lista. Alonso está en la posición 0.
>>> Ferrari2014.pop(1)
>>> print(Ferrari2014)
['Fernando Alonso']

>>> # append: Añadimos a Kimi al final de la lista
>>> Ferrari2014.append("Kimi Raikkonen")
>>> print (Ferrari2014)
['Fernando Alonso', 'Kimi Raikkonen']

>>> # del:Eliminamos el elemento de la primera posición de la lista (Fernando)
>>> del(Ferrari2014[0])

>>> # insert: Añadimos a Fernando en la primera posición
>>> Ferrari2014.insert(0, "Fernando Alonso")
>>> print (Ferrari2014)
['Fernando Alonso', 'Kimi Raikkonen']

>>> # extend: Juntamos los pilotos del 2013 y los del 2014. Fernando estará repetido.
>>> Ferrari2014.extend(Ferrari2013)
>>> print (Ferrari2014)
['Fernando Alonso', 'Kimi Raikkonen', 'Fernando Alonso', 'Felipe Massa']

>>> #remove: Borramos la primera vez que aparece Fernando Alonso
>>> Ferrari2014.remove("Fernando Alonso")
>>> print (Ferrari2014)
['Kimi Raikkonen', 'Fernando Alonso', 'Felipe Massa']
 
>>> #index: se usa para buscar el indice en una lista
print(Ferrari2014.index("Fernando Alonso"))


"""

milista=["Maria", "Pepe", "Marta", "Antonio"]
print(milista[:])
print(milista[2]) # por indice
print(milista[0:3]) # una porcion de la lista
#agregar un elemento a la lilsta, esta opcion la agrega al final
milista.append("jose")
#agregar un elemento en un sitio exacto de la lista
milista.insert(2,"Maribel")
#Esto es para ver si existe un elemento en mi lista
#si es verdadero imprime true, de lo contrario imprime false
print("Pepe" in milista) """De esta forma se puede buscar elementos en una lista,
si este existe devuelve true o false si no existe.
nota: aunque exista mas de una vez, solo verifica el primer resultado aunque allan mas.

"""
print(milista[:])


