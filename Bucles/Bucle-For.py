"""
for in: ejemplo : for variable temporal in variableinicial:
"""

animales = ["perro","gato","loro","cocodrilo"]
numeros = [52,16,14,72]
"""
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')
    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
"""    
#iterar dos listas al mismo tiempo(deben tener mismo tamaño de elementos)
"""
for (animal,numero) in zip(animales,numeros):
    print(f"Recorriendo lista 1: {animal}")
    print(f"Recorriendo lista 2: {numero}")
"""
"""
#for con rango: el primer rango es el inicio y el segundo es donde termina -1, si solo pongo un solo
#numero el rango empieza en 0 hasta el numero que coloco -1 for num in range(10)
for num in range(5,10):
    print(num)

#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    
#forma optima de recorrer una lista
for num in enumerate(numeros): #te esta forma se crea una tupla ()
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    #print(num)
"""

"""
#Desafio
for i,num in enumerate(numeros):
    print(f"valor I: {i},valor num: {num} valor ")
"""
"""
#for usando else, se usa para que se ejecute un comando despues de terminar el bucle, este siempre se ejecutara sin importar 
#lo que se alla ejecutado en el bucle for
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
"""

diccionario = {
    "nombre" : "Jose",
    "apellido" : "Inoa",
    "sueldo" : 50000
}

#for para iterar diccionarios (Normal) solo obtener las claves o keys
for key in diccionario.items():
    print(key)
    
#for para iterar diccionarios (Correcta) para obtner las claves y los valores  n
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la key del diccionario es: {key} y el valor es: {value}")
