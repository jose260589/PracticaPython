print("Calculadora con una sola variable \n")
print("********************")
print("* Menu de opciones *")
print("********************")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division Entera")
print("6. Exponente")
print("7. Modulo o resto \n")

numero = int(input("Introduce la Opcion deseada: "))

if numero==1:
    print("\n Elegiste Suma. \n")
    numero=int(input("Digite el primer numero: "))
    numero+=int(input("Digite el segundo numero: "))
    print("\n La suma es: ",numero)
elif numero==2:
    print("\n Elegiste Resta.")
    numero=int(input("Digite el primer numero: "))
    numero-=int(input("Digite el segundo numero: "))
    print("\n La Resta es: ",numero)
elif numero==3:
    print("\n Elegiste Multiplicacion.")
    numero=int(input("Digite el primer numero: "))
    numero*=int(input("Digite el segundo numero: "))
    print("\n La Multiplicacion es: ",numero)
elif numero==4:
    print("\n Elegiste Division.")
    numero=float(input("Digite el Dividendo: "))
    numero/=float(input("Digite el Divisor: "))
    print("\n La Division es: ",round(numero,2))
elif numero==5:
    print("\n Elegiste Division Entera.")
    numero=int(input("Digite el Dividendo: "))
    numero//=int(input("Digite el Divisor: "))
    print("\n La Division Entera es: ",numero)
elif numero==6:
    print("\n Elegiste Exponente.")
    numero=int(input("Digite el numero a Elevar: "))
    numero**=int(input("Digite el numero exponente: "))
    print("\n La Exponensacion es: ",numero)
elif numero==7:
    print("\n Elegiste Resto o Modulo.")
    numero=int(input("Digite el Dividendo: "))
    numero%=int(input("Digite el Divisor: "))
    print("\n El modulo o Resto es: ",numero)
else:
    print("\n Opcion desea no existe")

print("\n Fin.")
