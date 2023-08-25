cadena1 ="Hola soy Jose "
cadena2 =" Bienvenido maquinola"

#convierte a mayuscula
mayusc =  cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#Primera letra mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena
busqueda_find = cadena1.find("J") #Devuelve -1 si no encuentra nada

#busqueda una cadena en otra cadena, sino hay concidencias devuelve una excepcion
busqueda_index = cadena1.index("a")

#si es numerico, devolvemos true, sino delvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devolvemos true, sino delvemos false
es_alfanumerico = cadena1.isalpha()


# buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")


#cuenta la cantidad de caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.endswith("H")

#Reempleza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("la","lu")

#separar cadenas con la cadena que le pasemos y la convierte en una lista
cadena_separada = cadena1.split(",")

#se usa para eliminar espacio, tanto del principio como del final de una cadena
cadena_no_espacio = cadena1.strip()+cadena2.strip()

print(cadena_no_espacio)
