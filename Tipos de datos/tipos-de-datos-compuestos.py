"""
son datos compuestos por varios datos de distintos tipos
"""
#lista
lista = ["Jose Inoa", "Soy Arismendy",True,1.85]
print(lista[1])

lista[1] = "Soy Jose" #agregar o modificar datos en lista
print(lista[1])
#tuplas
tuplas = ("Jose Inoa", "Soy Arismendy",True,1.85)
print(tuplas[1]) #cuando se quiere modificar una tupla esto no se permite

#tuplas[1] = "Soy Jose" #agregar o modificar datos en tuplas. no se puede modificar

# creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Jose Inoa", "Soy Arismendy",True,1.85}

#creando diccionario(dict)
diccionario = {
    'nombre' : "Jose Inoa",
    'canal' : "Soy Arismendy",
    'estado_emocional' : True,
    'altura' : 1.84
    
}


print(diccionario['nombre'])