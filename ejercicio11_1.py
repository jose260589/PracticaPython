def DevuelveMax(num1,num2):
    
    if num1>num2:
        resultado=num1
    else:
        resultado=num2

    return resultado

print("Verificar cual numero es mayor\n")

numero1=int(input("Digite primer numero: "))

numero2=int(input("Digite segundo numero: "))


print(DevuelveMax(numero1,numero2))
