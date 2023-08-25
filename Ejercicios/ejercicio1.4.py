#imprimir True si la edad de Axell es par
#y no es mayor a 24
edad=26
condicion1=(edad%2)  ==0 #validar si la edad es par
condicion2=not(edad>24)
resultado=condicion1 and condicion2
print(resultado)

resultado=condicion1 or condicion2
print(type(resultado) )