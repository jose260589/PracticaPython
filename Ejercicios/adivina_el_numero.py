import random


def adivina_el_numero(x):
    
    print("==========================")
    print(" !Bienvenido(a) al Juego! ")
    print("==========================")
    print("Tu meta es adivinar el numero generado por la Computadora")
    
    numero_aleatorio = random.randint(1,x) # Nmero aleatorio entre 1 y x inclusive.
    
    prediccion = 0
    
    while (numero_aleatorio != prediccion):
        #El usuario agrega un numero.
        prediccion = int(input(f"Digita un numero entre 1 y {x}: "))
        
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este Numero es muy Pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este Numero es muy Grande.")
    
    print(f"Felicidades, Adivinaste el numero {x} Correctamente.")


adivina_el_numero(25)# el numero ingresado es el tamaño de probabilidades.