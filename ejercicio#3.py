num1 =  int(input("Digita primer numero: "))
num2 =  int(input("Digita segundo numero: "))
num3 =  int(input("Digita tercer numero: "))

if num1 > num2 and num1 > num3:
    print("\n El numero ",num1, " es el mayor")
elif num2 > num1 and num2 > num3:
    print("\n El numero ",num2, " es el mayor")
elif num3 > num1 and num3 > num2:
     print("\n El numero ",num3, " es el mayor")
else:
    print("\n Todos los numeros son iguales")

print("\n Fin.")
