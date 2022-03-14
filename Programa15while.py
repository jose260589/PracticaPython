"""
while condicion:
    instruccion
    instruccion
    instruccion
    Contador de ser necesario
"""
#Ejemplo 1
"""x=1
while x<3:
    print(x)
    x+=1
print("Fin.")
"""

#ejemplo2
"""x=1
while x<=1000:
    print(x,"Jose")
    x+=1
print("Fin.")"""

#ejemplo 3
"""edad= int(input("Introduce tu edad por favor: "))

while edad<0: # tambien puede hacer esto. edad<0 or edad>100 
    print(" Has introducido una edad negativa. Vuelve a intentarlo.")
    edad= int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar")
print("Edad del aspirante " + str(edad))
"""

#ejemplo 4
import math # para usar una clase hay que importarla igual que java

print("Programa de calculo de raiz cuadrada.")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo.")

    if intentos==2:
        print("Has consumido todos tus intentos, El programa ha finalizado.")
        break;

    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos+=1

if intentos<2:
    solucion= math.sqrt(numero)
    print("La raiz cuadrada de ",numero," es ",solucion)
