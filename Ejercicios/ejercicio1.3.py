#Comparar si el ultimo numero de la Variable Num1
#es diferente al ultimo numero de la Variable Num2
#imprir True si son diferentes, False en caso contrario

num1=45
num2=31

ultimo1=num1%10
ultimo2=num2%10
print(ultimo2)
#print(ultimo1,ultimo2) #Por si se necesita validar el resultado de las variables ultimo1 y ultimo2
#use un if porque ya se usarlo, pero se utilizo una condicion sencilla.
if ultimo1 != ultimo2:
    print("True")
else:
    print("False")

#Segunda forma sin if
condicion = ultimo1 != ultimo2
print(condicion)
