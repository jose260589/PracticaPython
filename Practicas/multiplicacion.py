#Programa simple para presentar tabla de multiplicar.
n = int(input("Digite el numero que desea multiplicar: "))

print("--"*10+"\n")
for i in range(1,21):
    print(n," x ",i," = ",(n*i))
print("--"*10+"\n")