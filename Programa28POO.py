"""
hacer clase
sintaxis
class nombre_clase():
    instruciones
    funciones
    metodos
"""
class Coche():
    
#constructor: es lo que le da un estado inicial a un objeto.
    """
sintaxis constructor
def __init__(self):
    self.propiedad
    self.propiedad

encencapsulacion sintaxis
se colococa dos  guiones bajos _
self.__ruedas=4 # de esta forma no podra ser modificado el valor de la variable.
"""
    def __init__(self): #
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 # colocando dos _, se encapsula una variable, y esta no podra ser
        #modificada desde fuera de la clase.
        self.__enmarcha=False
#los dos def son metodos, son parecidos a las funciones, pero usan el self
#self hace referencia al objeto o referencia, ejemplo, un text
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo==True): #if(self.__enmarcha and chequeo), tambien se puede poner de esta forma, lo que significa que pregunta que sean True, sin necesidad de agregar la linea entera.
            return "El choche esta en marcha."
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. no podemos arrancar"
        else:
            return "El coche esta detenido."

    def estado(self):
        print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
   #para encapsular un metodo se se coloca dos guiones bajos__
    def __chequeo_interno(self):
        print("Realizando Cheque Interno.")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerrada"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

#de esta forma se instancia una clase, a diferencia de java no se usa new
miCoche=Coche()

print(miCoche.arrancar(True)) #llama al metodo arrancar

miCoche.estado() #llama al metodo estado.

print("\n Segundo objeto--------------------\n")

miCoche2=Coche()

print(miCoche2.arrancar(False)) #llama al metodo arrancar
miCoche2.estado() #llama al metodo estado.


#constructor: es lo que le da un estado inicial a un objeto.
