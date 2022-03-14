"""
Diccionarios:
sintaxis van dentro de {},
>>> diccionario = {'Piloto 1':'Fernando Alonso', 'Piloto 2':'Kimi Raikkonen', 'Piloto 3':'Felipe Massa'}
>>> print(diccionario)
{'Piloto 1': 'Fernando Alonso', 'Piloto 3': 'Felipe Massa', 'Piloto 2': 'Kimi Raikkonen'}
}

>>> # get(): Devuelve el valor que corresponde con la key introducida.
>>> print(diccionario.get('Piloto 1'))
Fernando Alonso
 
>>> # pop(): Devuelve el valor que corresponde con la key introducida, y
luego borra la key y el valor.
>>> print(diccionario.pop('Piloto 1'))
Fernando Alonso
>>> print(diccionario)
{'Piloto 3': 'Felipe Massa', 'Piloto 2': 'Kimi Raikkonen'}
 
>>> # update(): Actualiza el valor de una determinada key o lo crea si no existe.
>>> diccionario.update({'Piloto 4':'Lewis Hamilton'})
>>> diccionario.update({'Piloto 2':'Sebastian Vettel'})
>>> print(diccionario)
{'Piloto 4': 'Lewis Hamilton', 'Piloto 2': 'Sebastian Vettel', 'Piloto 3': 'Felipe Massa'}
 
>>> # "key" in diccionario: devuelve verdadero (True) o falso (False) si la key existe en el diccionario.
>>> print ("Piloto 1" in diccionario)
True
>>> print ("piloto 1" in diccionario)
False
>>> print ("Sebastian Vettel" in diccionario)
False
 
>>> # "definición" in diccionario.values(): devuelve verdadero (True) o falso (False) si la definición existe en el diccionario.
>>> print ("Sebastian Vettel" in diccionario.values())
True
 
>>> # del diccionario['key']: Elimina el valor (y el key) asociado a la key indicada.
>>> del diccionario['Piloto 2']
>>> print(diccionario)
{'Piloto 4': 'Lewis Hamilton', 'Piloto 3': 'Felipe Massa'}

"""
#ejemplo 1
diccionario = {'Piloto 1':'Fernando Alonso', 'Piloto 2':'Kimi Raikkonen', 'Piloto 3':'Felipe Massa'}
print(diccionario)

#ejemplo 2
midiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid", "Republica Dominicana":"Santo Domingo"}

print(midiccionario["Francia"])

print(midiccionario)
#asiganar un elemento
midiccionario["Italia"]="Lisboa"

print(midiccionario)

#corregir o modificar un valor del dicccionario
midiccionario["Italia"]="Roma"

print(midiccionario)

#Eliminar un diccionario
del midiccionario["Reino Unido"]

print(midiccionario)

#Diccionarios con tuplas claves
print("\n Diccionarios con tuplas")
mitupla = ("España","Francia","Reino Unido","Alemania")
midiccionario2={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Reino Unido",mitupla[3]:"Berlin"}
print(midiccionario2)

#Diccionario almacene una tupla
midiccionario3={23:"Jorda","Nombre":"Michael","Equipo":"Chicago","anillos":(1991,1992,1993,1996,1997,1998)}
print(midiccionario3["anillos"])

#diccionario dentro de otro diccionario
print("\n Diccionario dentro de otro diccionario.")
midiccionario3={23:"Jorda","Nombre":"Michael","Equipo":"Chicago","anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}}
print(midiccionario3["anillos"])
print(midiccionario3.keys()) #imprimir todas las claves
print(midiccionario3.values())# imprimir todas los valores
print(len(midiccionario3))
