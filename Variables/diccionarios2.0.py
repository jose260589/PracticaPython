#creando diccionarios{} con dict() con esta funcion se pueden crear diccionarios vacios

diccionario = dict(nombre="Jose", apellido="Inoa")

#las listas [] no pueden ser claves, pero si las tuplas ()
diccionario = {("jose","inoa"):"loco loco"}
#diccionario = {[]"jose","inoa"]:"loco loco"} #da error por ser una lista

#creando diccionario con fromkeys() de esta forma el dato sale a none
diccionario = dict.fromkeys(["nombre","apellido","Subcriptores"])
#creando diccionario con fromkeys() de esta forma el dato sale "vacio" o el valor que se ponga despues de los []
diccionario = dict.fromkeys(["nombre","apellido","Subcriptores"],"Vacio")

print(diccionario)