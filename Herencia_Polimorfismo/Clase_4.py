class Calculadora:
    def __init__(self,n1,n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2
        
#en este caso se puede enviar los datos por la clase y no por la funcion
operacion = Calculadora(5,10)
print(operacion.suma)