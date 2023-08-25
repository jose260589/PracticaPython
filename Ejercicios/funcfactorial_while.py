#funcion factorial de un numero, pero esta vez con el bucle while
def factorial(numero):
    x=numero
    contador=numero
    while(contador!=1):
        contador-=1
        x*=contador
    
    return x
num=10
print(f"El factorial de {num} es {factorial(num)}")