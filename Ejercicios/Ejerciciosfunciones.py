#El archivo Ejerciciosfunciones1.py va con el ejemplo para llamar las funciones desde otro archivo

def holamundo():
    print("Hola Mundo")

def sumar(a,b):
    resultado = a+b
    print(f"la suma de {a} + {b} es {resultado}")

def paroimpar(numero):
    if((numero%2)==0):
        resultado="Es par"
    else:
        resultado="Es impar"
        
    print(f"El numero {numero} es {resultado}")

"""
holamundo()
sumar(5,10)
paroimpar(8)
"""