#Sentencias condicionales.
# if condicion
#        se hace de esta forma, con espacio y todas las demsa son iguales
#        sentencia 2, y asi sucecibamente, cuando no pertenezca a la misma condicion
#se quita los espacios.

"""
jo=4

if jo==5:
    print("es correcto ")
    print("segunda condicion ")
print("condicion fuera")
"""
#ejeomplo 1
"""print("Sistema para calcular el promedio de un alumno.")

nombre= input("Para comenzar, ¿Cual es tu nombre?: ")

mat = int(input(nombre + " ¿Cual es tu calificacion en matematicas?: "))
qui = int(input(nombre + " ¿Cual es tu calificacion en Quimica?: "))
bio = int(input(nombre + " ¿Cual es tu calificacion en Biologia?: "))

promedio = (mat+qui+bio) / 3
# La palabra reservada round, se usa para limitar la cantidad de decimales
if promedio >= 6:
    print("Felicidades " + nombre + ' "Aprobaste" con un promedio de: ', promedio)
    print("Felicidades " + nombre + ' "Aprobaste" con un promedio de: ', round(proedio,2))
else:
    print("Lo sentimos " + nombre + ' has " reprobado" con un promedio de: ', promedio)
    print("Lo sentimos " + nombre + ' has " reprobado" con un promedio de: ', round(promedio,2))

print("fin.")
"""

#ejemplo 2
"""print("Programa de evaluacion de notas de alumnos \n")
# def con esto se crea una funcion
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"

    return valoracion

nota_alumno =int(input("Digite nota del alumno: "))
print(evaluacion(nota_alumno))
"""
#ejemplo 3
print ("Verificacion de acceso\n")

edad_usuario = int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
    print("No puedes pasar.")
else:
    print("Puedes Pasar.")
