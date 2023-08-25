diccionario = {
    "nombre" : 'Jose',
    "apellido" : 'Inoa',
    "sueldo" : 1000000
}
"""
keys() -> devuelve las claves (tambien nos sirve para iterar)
values() -> devuelve los datos del diccionario sin las claves
get() -> devuelve el valor de una clave
clear() -> elimina todos los elementos
pop() -> elimina un elemento
items() -> para iterar el dict
"""
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get()
claves = diccionario.get("sueldo")

print(claves)
#eliminando todo del diccionario
#diccionario.clear

#eliminando un elemento del diccionario
diccionario.pop("sueldo")

print(diccionario)

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
