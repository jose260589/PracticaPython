#Concatenar cadenas de caracteres.
#Ejemplo de historias locas.
#Aprende a promar con ____________.

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + organizacion) #Forma basica
# print("Aprende a programar con {}".format(organizacion))#Usando format
# print(f"Aprende a programar con {organizacion}")#Usando F-STRING

#Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (Plural): ")

madlib = f"!Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. !Aprender a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)