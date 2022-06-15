"""Este programa simula un listado de un profesor y necesita saber cuantas veces
los estudiantes participan un sus diferentes cursos
"""
# variables
lista1 =[]
lista2 =[]
cantestudiantes=0
estudiante=""

cantestudiantes=int(input("Digite cuantos estudiantes tiene el Profesor Santiago ")) 
#llenado de listas
for a in range(cantestudiantes):
    estudiante=input("Digite el Estudiando #"+str(a+1)+" ")
    lista1.append(estudiante)
    if estudiante in lista2:
        continue
    else:
        lista2.append(estudiante)
        
lista2.sort() #ordenar lista
#print(lista1)
#print(lista2)

for b in range(len(lista2)):
    cont=lista1.count(lista2[b])
    print(lista2[b],cont)