#parte de asignacion +=
print("asignacion")
mensaje = "Hola"

mensaje +=" "

mensaje +="Jose"
# usando += se puede asignar o unir cadenas de caracteres en una misma variable.

print(mensaje)
print("Concatenacion")
#parte de concatenacion

mensaje ="Hola"

espacio = " "

nombre = "JOSE"

print(mensaje+espacio+nombre)

#buscar con .find
print("Buscar")

mensaje="Hola Jose"

buscar_subcadena=mensaje.find("Jose")

print(buscar_subcadena)

#la exttracion de caracteres se hace con variable [0:5]

print("extraer cadenas de texto")

mensaje="Hola Jose"

extraer_subcadena = mensaje[1:6]

print(extraer_subcadena)


#comparacion ==

print("comparacion")

mensaje_uno="Hola"

mensaje_dos="Hola"

print(mensaje_uno == mensaje_dos)
