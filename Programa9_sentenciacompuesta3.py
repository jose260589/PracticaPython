"""
sintaxis elif
if condicion:
    instrucion
    instrucion
elif condicion:
    instrucion
    instrucion
else: #si lo amerita
    instrucion
"""

print("conversor \n")

print("Menu de opciones: \n")

print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero.\n")

opcion = int(input("¿Cual es la opcion deseada?: "))

if opcion==1:
    print("\n Conversor de numero a palabra \n")
    num = int(input("¿Cual es el numero a convertir?: "))
    if num==1:
        print("Uno.")
    elif num==2:
        print("Dos.")
    elif num==3:
        print("Tres.")
    elif num==4:
        print("Cuatro.")
    elif num==5:
        print("Cinco.")
    else:
        print("Solo se convierte del 1 al 5")
elif opcion==2:
    print("\n Conversor de palabra a numero \n")
    texto = input("¿Cual es la palabra que deseas convertir?: ")
    if texto=="Uno"  or texto=="uno":
        print("1")
    elif texto=="Dos"  or texto=="dos" or texto=="DOS":
        print("2")
    elif texto=="Tres"  or texto=="tres":
        print("3")
    elif texto=="Cuatro"  or texto=="cuatro":
        print("4")
    elif texto=="Cinco"  or texto=="cinco":
        print("5")
    else:
        print("Solo se convierte del Uno al Cinco")
else:
    print("\n Opcion no encontra")

print("\n Fin.")

#ejemplo 2
print ("Verificacion de acceso\n")

edad_usuario = int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
    print("No puedes pasar.")
else:
    print("Puedes Pasar.")
