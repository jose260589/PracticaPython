"""
#usando def se crean funciones, se crean con parametros o sin estos.
def saludar():
    print("Hola Jose, Mi maestro, como va todo?")    
    

#asi se ejecuta o llama una funcion
saludar()
"""

#crear una funciona con parametros
def saludar(nombre, sexo):
    sexo = sexo.lower() #nombre este en minuscula.
    
    if sexo == "mujer":
        abjetivo = "reina"
    elif sexo == "hombre":
        abjetivo = "titan"
    else:
        abjetivo = "amor"
    
    print(f"Hola {nombre}, mi {abjetivo}, como va todo?")
    
    
saludar("Jose","hombre")

#quede en la parte que menciona la contraseña