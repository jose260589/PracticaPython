"""
Sintaxis
class nombre_clase():
    instruciones
    instruciones
"""
"""
#ejemplo1
class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
#los dos def son metodos, son parecidos a las funciones, pero usan el self
#self hace referencia al objeto o referencia, ejemplo, un text
    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "El choche esta en marcha."
        else:
            return "El coche esta detenido."

#de esta forma se instancia una clase, a diferencia de java no se usa new
miCoche=Coche()

print(miCoche.largoChasis)
print("El coche tiene ",miCoche.ruedas," ruedas.")

miCoche.arrancar() #llama al metodo arrancar

print(miCoche.estado()) #llama al metodo estado.

print("\n Segundo objeto--------------------\n")

miCoche2=Coche()

print("Tamaño del Chasis ",miCoche2.largoChasis)
print("El coche tiene ",miCoche2.ruedas," ruedas.")

print(miCoche2.estado()) #llama al metodo estado.
"""

#ejemplo2
class Coche():
    
#constructor: es lo que le da un estado inicial a un objeto.
    """
sintaxis constructor
def __init__(self):
    self.propiedad
    self.propiedad

encapsulacion sintaxis
se colococa dos  guiones bajos _
self.__ruedas=4 # de esta forma no podra ser modificado el valor de la variable.
"""
    def __init__(self): #
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4 # colocando dos _, se encapsula una variable, y esta no podra ser
        #modificada desde fuera de la clase.
        self.enmarcha=False
#los dos def son metodos, son parecidos a las funciones, pero usan el self
#self hace referencia al objeto o referencia, ejemplo, un text
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El choche esta en marcha."
        else:
            return "El coche esta detenido."

    def estado(self):
        print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ", self.largoChasis)
        

#de esta forma se instancia una clase, a diferencia de java no se usa new
miCoche=Coche()

print(miCoche.arrancar(True)) #llama al metodo arrancar

miCoche.estado() #llama al metodo estado.

print("\n Segundo objeto--------------------\n")

miCoche2=Coche()
miCoche2.ruedas=2 #como la variable ruedas esta encapsulada no cambia su valor

print(miCoche2.arrancar(False)) #llama al metodo arrancar
miCoche2.estado() #llama al metodo estado.


#constructor: es lo que le da un estado inicial a un objeto.
