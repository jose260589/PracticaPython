#Programa para recibir un bono de empleado.
def recibir_bono(salario):
    if salario >= 50000:
        return True
    else:
        return False


salario= float(input("Ingrese el salario del empleado: "))

# Llamada a la función
resultado = recibir_bono(salario)
print("El empleado recibe bono:", resultado)