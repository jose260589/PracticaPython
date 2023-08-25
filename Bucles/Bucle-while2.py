#While

"""x = 0

while x < 10:
    print("El valor de x es:",x)
    x+=1
"""
num = int(input("Escribe un numero positivo: "))

while num < 0:
    print(f"El numero {num} es negativo, prueba de nuevo")
    num = int(input("Escribe un numero positivo."))

print("El numero es: ",num)