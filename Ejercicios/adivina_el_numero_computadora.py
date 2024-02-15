import random


def adivina_el_numero_computadora(x):
    
    print("==========================")
    print(" !Bienvenido(a) al Juego! ")
    print("==========================")
    print(f"Selecciona el numero entre 1 y {x} para que la computadora intente adivinar el numero.")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    
    while (respuesta != "c"):
        #Generar prediccion 
        if limite_inferior < limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion = limite_inferior #tambien podria ser el limite superior.
    
        #Obtener respuesta del usuario
        respuesta = input(f"Mi predicion es {prediccion}. Si es muy alta, ingresa (A). si es muy baja, ingresa (B). si es correcta ingresa (C)").lower()
    
        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    prediccion(f"Siii, La Computadora adivino el numero {x} correctamente.")
    
    #Intervalo inicial: [1,10]
    #prediccion: 6
    #Respuesta: "a"
    #inverlao [1,5]


adivina_el_numero_computadora(25)# el numero ingresado es el tamaño de probabilidades.