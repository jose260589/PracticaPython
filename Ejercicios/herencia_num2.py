"""Realizar un programa que conste de una clase Persona con dos atributos nombre y edad. 
Los atributos se introducirán por teclado y habrá otro método para imprimir los datos.

Declarar una segunda clase llama Empleado que hereda de la clase Persona y agrega el atributo sueldo.
Debe mostrar si tiene que pagar impuestos o no (sueldo superior a 3000).

Crear un objeto de cada clase.

Especificaciones
1.Implementa tu programa en un archivo con el nombre herencia_num2.py.
2.Declarar las clases y sus atributos.
3. debe crear un objeto de cada clase.
4.Imprimir si el empleado debe pagar impuestos o no."""

#se creo dos clases una persona y otrao Empleados
class Persona:
    pass
    def __init__(self,nombre,edad): #se creo el metodo init para la clase persona
        self.nombre = nombre
        self.edad = edad

    def Imprimir(self):#Metodo para returnar nombre y edad de la persona
        return "{} tiene {} años de edad".format(self.nombre,self.edad)

class Empleado(Persona):# se uso Herencia para esta clase, para que erede los atributos y metodos de la clase padre
    def impuesto(self,sueldo):# metodo creado para validar si el sueldo es mayor a 3000 para pagar impuestos
        if (sueldo>=3000):
            print(f"El empleado {self.nombre} debe pagar impuestos")
        else:
            print(f"El empleado {self.nombre} no debe pagar impuestos")
        
#variables
nombres = input("Digite su nombre: ")
edades = int(input("Digite su edad: "))
#Objetos creados. 
persona1 = Persona(nombres,edades)
print(persona1.Imprimir())
#objeto sueldo
sueldo = int(input("Digite su sueldo: "))
empleado1 = Empleado(nombres,edades)
empleado1.impuesto(sueldo)