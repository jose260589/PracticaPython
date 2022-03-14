print("Introduce dos numeros a comparar: \n")

num1 = int(input("Digite primer numero a comparar: "))
num2 = int(input("Digite segundo numero a comparar: "))

print("\n Los numeros a comprar son: ", num1, " y ", num2, "\n")

if num1 == num2:
    print("Es igual...")

if num1 != num2:
    print("Es Diferente...")

if num1 < num2:
    print("Es menor...")

if num1 > num2:
    print("Es mayor...")

if num1 <= num2:
    print("Es Menor o igual...")

if num1 >= num2:
    print("Es Mayor o igual...")

print("\n Fin")
