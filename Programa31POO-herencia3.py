class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("Nombre: ",self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, Lugar_residencia):
        #De esta forma se busca el init de la clase que se hereda
        super().__init__(nombre_empleado, edad_empleado, Lugar_residencia)

        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()

        print(" Salario: ", self.salario, " Antiguedad: ", self.antiguedad)


#objetos
Antonio=Persona("Antonio", 55, "España")

#Antonio.descripcion()
#---------------------------
#Objetos
Manuel=Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()
"""
isinstance: se para ver si una instancia persona o hereda de una clase.
solo devuelve true, no el nombre de la clase.
"""
print(isinstance(Manuel, Persona))
print(isinstance(Manuel, Empleado))

print(isinstance(Antonio, Persona))
print(isinstance(Antonio, Empleado))
