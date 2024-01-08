'''
Intento hacer programa para: dado un numero entrarlo dentro de un intervalo
Caso Don angel
'''
from io import open
archivo = open("lista.txt", 'a')

num = int(input("Entre un numero del 0 al 99: "))
num0=num1=num2=num3=num4=num5=num6=num7=num8=num9=0
if 0<= num <= 9:
    num0 = 0
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    
    print()
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
        
    
elif 10<= num <= 19:
    num0 = num0 + 1
    num1 = 0
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 20<= num <= 29:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = 0
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 30<= num <= 39:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = 0
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 40<= num <= 49:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = 0
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 50<= num <= 59:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = 0
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 60<= num <= 69:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = 0
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 70<= num <= 79:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = 0
    num8 = num8 + 1
    num9 = num9 + 1
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 80<= num <= 89:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = 0
    num9 = num9 + 1
    print()
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
    print()
    
    
elif 90<= num <= 99:
    num0 = num0 + 1
    num1 = num1 + 1
    num2 = num2 + 1
    num3 = num3 + 1
    num4 = num4 + 1
    num5 = num5 + 1
    num6 = num6 + 1
    num7 = num7 + 1
    num8 = num8 + 1
    num9 = 0
    print()
    print()
    
    lista = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
    print(lista)
else:
    print("Entre un numero del 0 al 99")



archivo.write("lista ",lista,num0,num1,num2,num3,num4,num5,num6,num7,num8,num9)

print(lista,num0,num1,num2,num3,num4,num5,num6,num7,num8,num9)
archivo.close()

    
    
    
