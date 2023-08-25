#creando un conjunto con set()
conjunto = set(["dato1","dato2"])

#meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato 3"}

print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1)
#resultado = conjunto2 <= conjunto1
print(f"Es un subconjunto {resultado}")

resultado = conjunto1.issuperset(conjunto2)
print(f"Es un superconjunto {resultado}")


#verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)

