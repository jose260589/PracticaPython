""" 
Imprimir dos numeros en una misma linea, y hacer calculos matematicos basicos.
split()= es un metodo o funcion de tipo string 'str', en la cual puede dividir sus datos segun su espacio
"""

numero1, numero2 = input("Digite dos numeros:").split()

suma = int(numero1) + int(numero2)
resta = int(numero1) - int(numero2)
multi = int(numero1) * int(numero2)
div = int(numero1) / int(numero2)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multi}")
print(f"Division: {div}")
