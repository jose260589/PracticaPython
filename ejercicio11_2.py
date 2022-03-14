"""Crea un programa que pida por teclado “Nombre”,
“Dirección” y “Tfno”. Esos tres datos deberán ser
almacenados en una lista y mostrar en consola el mensaje:
    “Los datos personales son: nombre apellido teléfono”
    (Se mostrarán los datos introducidos por teclado).
"""
nombre=input("Digite nombre: ")
direccion=input("Digite direccion: ")
telefono=input("Digite telefono: ")

milista=[nombre, direccion, telefono]

print("Los datos personales son: "+str(milista[:]))
