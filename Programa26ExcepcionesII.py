"""
#ejemplo 1
def evaluaEdad(edad):
    
    if edad<0:
        raise TypeError("No se permiten edades negativas. ")
    
    if edad<20:
        return "eres muy joven "
    elif edad<40:
        return "Eres Joven "
    elif edad<65:
        return "Eres Maduro "
    elif edad<100:
        return "Cuidate... "

print(evaluaEdad(-15))
"""

#ejemplo2
import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError ("El numero no puede ser negativo ")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un numero: "))
try:
    print("\n La Raiz Cuadrada de ",op1," es ",calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print("ErrorDeNumeroNegativo")

print("Programa Terminado. ")
