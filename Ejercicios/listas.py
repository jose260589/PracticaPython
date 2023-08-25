#crear un listado con 5 palabras ingresadas por el usuario
#imprimir las lista por pantalla y preguntar al usuario si desea  insertar o eliminar algun elemento de la lista
#si eligio insertar pedir el elemento a añadir
#si eligio eliminar pedir el elemento a eliminar
#si eligio nada, devolver un mensaje de despedida

#variables
contador = 0
opcion = 0
palabras = [] #lista vacia

while contador < 5: #con este while se agregan las primeras 5 palabras de la lista
    palabra=input(f"Digite palabra #{contador+1}: ")
    palabras.append(palabra)
    
    contador+=1

#While que maneja el menu de opciones para el usuario de agregar o eliminar palabras de la lista
while opcion!=3:
    #Zona de imprimir lista y menu de opciones para el usuario
    print("\n")
    print(palabras)
    print("\n")
    print("Elija Opcion a ejecutar.")
    print("Opcion 1:Insertar un elemento Nuevo a la lista.")
    print("Opcion 2.Eliminar un elemento de la lista")
    print("Opcion 3.Salir")
    print("\n")
    
    opcion = int(input("Digite Opcion a realizar: "))#Entrada por teclado de opcion a elegir
    #Condicionales segun la opcion del usuario
    if opcion==1:
        palabra=input("Digite palabra nueva a insertar: ")
        palabras.append(palabra)
    elif opcion==2:
        palabra=input("Digite palabra a eliminar: ")
        palabras.remove(palabra)
    elif opcion==3:
        print("\n")
        print("Muchas Gracias por Participar")

    if(opcion != 1 and opcion != 2 and opcion != 3):#condicional if para validar si el usuario elige una opcion que no existe en el menu
        print(f"Opcion #{opcion} no Existe, Intente otra vez")