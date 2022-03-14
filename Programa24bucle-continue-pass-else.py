#ejemplo con for
#continue: deja una instrucion sin ejecutar, suele pasar en los bucles
#pass: no ejecuta algo, se usa mucho en funciones
#else en blucle, se usa parecido a las condicionales.

#ejemplo continue
for letra in "Python":
    if letra=="h":
        continue #buela una ejecucion
        #break  #Interrumpe el ciclo

    print("Viendo la letra: "+letra)


#ejemplo pass
"""while True:
    pass

class Miclase:
    pass

def MiFuncion():
    pass
    """

email=input("Introduce tu email, por favor: ")

for i in email:

    if i=="@":
        arroba=true

        break;

else:
    arroba=False
