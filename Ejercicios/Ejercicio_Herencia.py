#Herencia ejercicio practico

class Calculadora:
    pass
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
        
    
    def ingresardatos(self):
        self.datos = [int(input("ingresar datos "+str(i+1)+"= ")) for i in range(self.n)]#str(es para convertir a string, igual que el int que convierte a entero)
        return ""
        
class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2) #esta forma es para limitar la cantidad de valores a trabajar.
        
        
    def suma(self):
        a,b, = self.datos #otra forma de trabajar con datos, sin tener que colocarlos entre ()
        s = a +b
        print("el resultado es: ",s)
        return ""
    
    def resta(self):
        a,b, = self.datos #otra forma de trabajar con datos, sin tener que colocarlos entre ()
        r = a - b
        print("el resultado es: ",r)
        return ""
    
    def multiplicacion(self):
        a,b, = self.datos #otra forma de trabajar con datos, sin tener que colocarlos entre ()
        m = a * b
        print("el resultado es: ",m)
        return ""
    
    def division(self):
        a,b, = self.datos #otra forma de trabajar con datos, sin tener que colocarlos entre ()
        d = a / b
        print("el resultado es: ",d)
        return ""


class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
        
    
    def cuadrada(self):
        import math #importa una libreria matematica
        a, = self.datos
        print("el resultado es: ",math.sqrt(a))
        return ""

#calcular = op_basicas()
#print(calcular.ingresardatos())
#print(calcular.suma())

raiz2 = raiz()
print(raiz2.ingresardatos())
print(raiz2.cuadrada())

#print(isinstance(objeto,clase)) #se usa para validar si es verdad que se esta trabajando con una clase X.

#print(issubclass(op_basicas,Calculadora)(# validar si una subclase pertene a una clase padre
