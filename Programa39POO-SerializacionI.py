"""
serializacion: consiste en guardar en un fichero externo, un dicionario, un objeto
en codigo binario codificado.

se usa esto
pickle:
metodo dump(): Volcado de datos al fichero binario externo
metodo load(): carga de los datos del fichero binario externo.


"""
"""
#crear un fichero binario
import pickle

lista_nombres=["Pedro","Ana","Maria","Isabel","Jose"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close() #cerrar fichero

del (fichero_binario) #este comando lo borra de memoria
"""

#recuperar los datos del pichero binario.
import pickle

fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)
