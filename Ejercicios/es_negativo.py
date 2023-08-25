def es_negativo(numero):
    if numero < 0:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

#print(es_negativo(numero))

if es_negativo(numero):
    print("El numero es negativo.")
else:
    print("El numero no es negativo.")