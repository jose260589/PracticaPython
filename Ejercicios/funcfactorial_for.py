#crear una funcion que calcule el factorial de un número pasado por parámetros

def factorial(numeros):
    x=1
    i=1
    for i in range(1, numeros+1):  #de esta forma se puede usar para manejar la funciona range a que empieze por 
        x *= i                     #por otro digito.    #class range(digito que inicia, digito final.)
    
    return x
        
x = 10
print(f"El factorial de {x} es: {factorial(x)}")
"""
digito final, se refiere al digito que desea que termine. ya que el valor de inicio siempre sera 1 menos
que el valor final, pero si desea que termine en ese mismo numero debe sumar 1 al valor final.
de lo contrario use la clase normal range(), ya que esta inicia desde el 0 hasta el numero final menos 1

otra forma de usar la clase range()
range(num-1,1,-1)

num-1=numero inicial
1=digito final
-1 o tercer elemento, es el incremento o descremento. en este caso va por menos 1(-1), esta es la forma que se pueda
aumentar por mas de unoe3w
"""

