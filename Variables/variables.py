a = 5

#Definiendo una variable con camelCase
nombreCompletoDeTuTioMaster = "Lucas Dalto"

#Definiendo una variable con snake_case
nombre_Completo_de_tu_tio_master = "Lucas Dalto"

#concatenar con +
bienvenida = "Hola " + "Como estas?" 

#concatenar con f-strings
bienvenida = f"Hola {nombre_Completo_de_tu_tio_master} Como estas?"

#Operadores de pertenecia (in / not in)
print("Lucas " in bienvenida) #true
print("Lucas " not in bienvenida) #false

#Variables en una sola linea
x, y, z = 1, 2, 3
#Tambien pueden ser con datos diferentes. examplo:
name,surname, age, height = "Jose", "Inoa", 36, 1.75
print("Hola, me llamo:",name,surname,". Mi edad es:",age, "y mi altura es:",height)