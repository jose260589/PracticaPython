"""
Las funciones no son como en llava que se puede usar el mismo nombre, con diferentes parametros.
no recuerdo bien pero creo que se llama polimorfismo.
"""
#def saludar():
 #   print("Hola, como estas")
    
def saludar(name, saludo="Hola"):
    mensaje = f"{saludo} {name}, como estas?"
    print(mensaje)
    
saludar("Jose")