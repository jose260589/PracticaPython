"""
Calcular nota dividida en 3 partes
1. un 30% en 3 talleres.
2. un 30% en dos evaluaciones cortas realizadas
3. un 40% corresponde al proyecto final, que se divide en un 
50% de un trabajo y otro 50% la sustentacion del proyecto
"""

#funciones
def Nota1( n1,n2, n3):
    resultado=(n1+n2+n3)/3
    global notafinal
    notafinal+=resultado*0.30

    #return notafinal

def Nota2(n1,n2):
    resultado=(n1+n2)/2
    global notafinal
    notafinal+=resultado*0.30

    #return notafinal

def Nota3(n1,n2):
    resultado=(n1+n2)/2
    global notafinal
    notafinal+=resultado*0.40

    #return notafinal

#variables
global notafinal
notafinal=0
#parte 1
print("Favor Digitar las 3 notas que corresponden a los Talleres ")
n1=float(input("Nota Primer Taller: ")) 
n2=float(input("Nota Segundo Taller: "))
n3=float(input("Nota Tercer Taller: "))

Nota1( n1,n2, n3)
print(notafinal)

#parte 2
print("Favor Digitar las 2 notas que corresponden a las evaluaciones ")
n1=float(input("Nota Primera : ")) 
n2=float(input("Nota Segunda : "))

Nota2(n1,n2)
print(notafinal)

#parte 3
print("Proyecto Final ")
n1=float(input("Nota Correspondiente al Trabajo : ")) 
n2=float(input("Nota de Sustentacion del proyecto : "))

Nota3(n1,n2)
print(notafinal)