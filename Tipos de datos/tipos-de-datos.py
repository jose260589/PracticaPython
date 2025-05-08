"String"
'tus datos son:'

"""
String 
con 
salto de linea dobles
"""

'''
String 
con 
salto de linea simple
'''

4 
4.4

'''
Ejemplos de funciones en String
'''

MyStr = "Hello worldz"
num = 5

#dir muestra los metodos que puedo usar con cada tipo de datos
#print(dir(MyStr))
#print(dir(num))

print(MyStr.upper()) #colocar todo en mayuscula
print(MyStr.lower()) #colocar todo en minuscula
print(MyStr.swapcase()) #si esta mayuscula convierte a minuscula y viceversa.
print(MyStr.capitalize()) #coloca primera letra tipo capital
print(MyStr.replace('Hello', 'bye')) #remplaza una letra o palabra
print(MyStr.count('o')) #cuenta la cantidad de veces que se reviste un string.

print(MyStr.startswith('Hello')) #para saber si un texto empieza por cierta palabra, resultado es True o False
print(MyStr.endswith('work')) #para saber si un texto termina por cierta palabra, resultado es True o False

print(MyStr.split()) #se usa para separar un texto, si se deja en blanco, se separa por un espacio, se puede agregar otro tipo de caracteres.
print(MyStr.split('o'))

print(MyStr.find('o')) #Devuelve la posicion del primer numero encontrado.
print(len(MyStr))
print(MyStr.index('e'))

print(MyStr.isnumeric())
print(MyStr.isalpha())

#Mostrar los valores o caracteres de un string o texto, como si fuera una lista.
print(MyStr[0])
print(MyStr[1])
print(MyStr[2])
print(MyStr[3])
print(MyStr[4])


#Tres formas de mostrar valor de una variable en Python
Name = "Jose"
print("My Name is "+Name)
print(f"My Name is {Name}")
print("My Name is {0}".format(Name))