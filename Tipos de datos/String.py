#for de usar un string con formato

nombre = "Jose"
edad = 34

#forma basica. 
print("Hola Soy " + nombre) #una sola variable

#forma anterior como se daba formato. "%s":String, "%d":Integer, "%f":Float, "%.number of digitsf": Float with fixed decimal places example %.2f 50.00
#usando el % s
print("Hola soy % s"%nombre)
print("Hola soy % s y tengo % s años."%(nombre,edad))#si son mas de una variable hay que usar una tupla

# Strings  and numbers Other examples with %d and %.2f.
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
print(formated_string)

#usando el metodo formart
print("Hola soy {} y tengo {} años.".format(nombre,edad))

#usando el metodo f-strings(es el que suelo usar)
print(f"Hola soy {nombre} y tengo {edad} años.")