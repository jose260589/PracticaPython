#Variables
num1=0
num2=0
Resultado=0
opcion=0

#Menu de la calculadora
print("Calculadora Basica.")
print("1.Suma")
print("2.Resta")
print("3.multiplicacion")
print("4.Division")
opcion=int(input("Elija la operacion aritmetica que desea ejecutar. (Solo colocar el numero y dar Enter): "))
#Condicionales para elejir la opcion a realizar
if opcion==1:
    print("Elijio Suma")
    num1=float(input("Digite Primer Numero: "))
    num2=float(input("Digite Segundo Numero: "))
    Resultado=num1+num2
    print("El resultado de la Suma es:",round(Resultado,2)) #se usa la funcion round para limitar cantidad decimales
elif opcion==2:
    print("Elijio Resta")
    num1=float(input("Digite Primer Numero: "))
    num2=float(input("Digite Segundo Numero: "))
    Resultado=num1-num2
    print("El resultado de la Resta es:",round(Resultado,2)) #se usa la funcion round para limitar cantidad decimales
elif opcion==3:
    print("Elijio Multiplicacion")
    num1=float(input("Digite Primer Numero: "))
    num2=float(input("Digite Segundo Numero: "))
    Resultado=num1*num2
    print("El resultado de la Multiplicacion es:",round(Resultado,2)) #se usa la funcion round para limitar cantidad decimales
elif opcion==4:
    print("Elijio Division")
    num1=float(input("Digite Primer Numero: "))
    num2=float(input("Digite Segundo Numero: "))
    Resultado=num1/num2
    print("El resultado de la Division es:",round(Resultado,2)) #se usa la funcion round para limitar cantidad decimales
else:
    print(f"La Opcion #{opcion} No es Valida por el momento")
    #Este es una forma de manejar String con variables.