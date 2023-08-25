#lista [] de frutas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Jose"
numeros = [2,5,8,10]

#for usando un if continue, para saltar un dato del bucle
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me voy a comer una {fruta}")
    
#for usando un if break, para detener el bucle    
for fruta in frutas:
    if fruta == "manzana":
        break
    print(f"Me voy a comer una {fruta}")
    

#recoger una cadena de texto (es lo mismo que iterar)
for letra in cadena:
    print(letra)
    
#for duplicando numeros   
numeros_duplicados = list() # se crea una lista vacia
for numero in numeros:
    numeros_duplicados.append(numero*2)
    
print(numeros_duplicados)

#lo mismo de arriba en una sola linea de codigo
numeros_duplicados2 = [x*2 for x in numeros]
print(numeros_duplicados2)