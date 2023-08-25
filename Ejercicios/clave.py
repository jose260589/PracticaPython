#Escribir un programa que almacena una contrasena, y que pida al usuario validar si es la misma.
#no diferenciar de mayuscula ni minuscula.
#Variables
contador = 0
clave1= "condicional"

while contador < 3: #ciclo que no pasa de 3
    
    clave2 = input("Digita la Clave: ")  #Entrada de la clave que introduce el usuario
    
    if (clave1.lower()==clave2.lower()): #condiciona de validacion
        print("Clave Confirmada")
        break                           #decidi usar un break para que termine el programa inmediatamente.
                                        #Tambien podia asignarle a la variable contador un valor mayor a 3
    contador+=1  #contador para que se encargue de aumentar el valor y termine el ciclo

print("Programa Terminado")