"""
Sacar unidad de mil
"""
""" forma 1 con string
def unidad_mil(numero):
    a=len(numero)
    b=numero[a-4]

    return print(b) 

n=input("Digite numero a validar: ")

if(int(n)>999):
    unidad_mil(n)
else:
    print("El numero ",n," es menor de 1000 ")
    """
#-----------------Ejemplo 2-con enteros----------------------

n=int(input("Digite numero a validar: "))

if(n>999):
    unidad=n%10
    decena=(n%100-unidad)//10
    centena=(n%1000-n%100)//100
    unidadmil=(n%10000-n%1000)//1000
    print("Valor de Unidad de Mil: ", unidadmil)
else:
    print("El numero ",n," es menor de 1000 ")
