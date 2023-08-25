#Hacer una funcion que nos genere un numero aleatorio entre dos parametros pasados.
import random


def Numeroaleatorio(numero1,numero2):
    mayor=0
    menor=0
    #aleatorio=0
    if numero1 < numero2:
        mayor=numero2
        menor=numero1
    elif numero2 < numero1:
        mayor=numero1
        menor=numero2
    else:
        print("Error ambos numeros son iguales")
        #break
    
    aleatorio=random.randint(menor,mayor)
        
    return aleatorio
    
    
primer=100
segundo=100

print(Numeroaleatorio(primer,segundo))