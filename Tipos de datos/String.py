#for de usar un string con formato

nombre = "Jose"
edad = 34

#forma basica. 
print("Hola Soy " + nombre) #una sola variable

#usando el % s
print("Hola soy % s"%nombre)
print("Hola soy % s y tengo % s años."%(nombre,edad))#si son mas de una variable hay que usar una tupla

#usando el metodo formart
print("Hola soy {} y tengo {} años.".format(nombre,edad))

#usando el metodo f-strings(es el que suelo usar)
print(f"Hola soy {nombre} y tengo {edad} años.")