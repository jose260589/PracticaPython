"""edad=107
#concatenacion de condiciones
if 0<edad<100 : #esta es una forma de ahorrar codigo, seria lo mismo que:
#if 0<edad and edad<100:                #if 0<edad and edad<100:
    print("edad Correcta")
else:
    print("Edad Incorrecta")
"""
"""
# esta es una variante de usar el switch case, con un diccionario
def calculo(op,a,b):
	return{
		'sum': lambda: a +b,
		'rest': lambda: a-b,
		'mult': lambda: a*b,
		'div': lambda: a/b
		}.get(op, lambda: None)()

print(calculo('sum',3,4))

"""
"""
# otra variante de switch case con if concatenados
salario_presidente =int(input("Introduce salario presidente: "))
print("Salario Presidente: " + str(salario_presidente))

salario_director =int(input("Introduce salario director: "))
print("Salario Director: " + str(salario_director))

salario_jefe_area =int(input("Introduce salario jefe area: "))
print("Salario Jefe Area: " + str(salario_jefe_area))

salario_administrativo =int(input("Introduce salario administrativo: "))
print("Salario Administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("\n Todo funciona correctamente.")
else:
    print("\n Algo falla en esta empresa")

"""

"""
#Operadores and, or
print("Programa de becas del colegio.\n ")

dist=int(input("Introduce distancia de la escuela en KM. "))
num_herm=int(input("Introduce el no. de hermanos en el cole "))
salfam=int(input("Introduce Salario Familiar Anual. "))

if dist>40 and num_herm>2 or salfam <=20000:
    print("Hay que darle Becas.")
else:
    print("No es necesaria la beca.")
"""

#operador in

print("Asignaturas optativas")
print("Informatica Grafica - pruebas de sofware - usabilidad y accesibilidad")
asignatura=input("Escribe la asignatura Escogida: ")
asignatura= asignatura.lower()
print(asignatura)

if asignatura in ("informatica grafica", "pruebas de sofware", "usabilidad y accesibilidad"):
    print("Asignatura elegida: "+asignatura)
else:
    print("asignatura no existe.")
#lower(): Funcion para colocar los string en minusculas
#upper(): Funcion para colocar los string en mayusculas
