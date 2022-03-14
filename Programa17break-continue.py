"""sentencias 'break' y 'continue'
break= interrumpe un ciclo while o for
continue= hace una pausa y continua
"""

#ejemplo para break

print("while con la sentencia break \n")
contador =0
while contador < 10:
    contador +=1

    if contador == 5:
        break
    print("Valor actual de la variable: ", contador)


#ejemplo para continue
print("while con la sentencia continue \n")
contador =0
while contador < 10:
    contador +=1

    if contador == 5:
        continue
    print("Valor actual de la variable: ", contador)


