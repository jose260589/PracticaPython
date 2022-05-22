from io import open

#Abrir y cerrar archivo Texto.txt
#archivo_texto=open("Texto.txt","r", encoding="utf-8")
archivo_texto=open("Texto.txt","r")
texto=archivo_texto.read()
archivo_texto.close()

#Abrir, colocar en una variable y cerrar archivo indice
archivo_indice=open("indices.txt","r")

#longitud archivo indice
indice=archivo_indice.seek(len(archivo_indice.read())) 
archivo_indice.seek(0)
valores_indice=archivo_indice.read()

archivo_indice.close

#variables
contador1=0
contador2=0
a=""
lista_indice=[]
texto2=""

for contador1 in valores_indice:
    if contador1!=",":
        a+=contador1
    else:
        lista_indice.append(int(a))
        a=""        

if a!="":
    lista_indice.append(int(a))

#while del nuevo texto
while (contador2<len(lista_indice)):
    a=lista_indice[contador2]
    texto2+=texto[a:a+1]
    contador2+=1

print(texto2) #Print Para ver el nuevo mensaje.

#Abrir y cerrar archivo Texto2.txt para almacenar el nuevo mensaje.
archivo_texto=open("Texto2.txt","w")

archivo_texto.write(texto2)

archivo_texto.close()
