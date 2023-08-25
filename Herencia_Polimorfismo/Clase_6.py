#metodo constructor

class Persona:
    pass #se coloca pass porque no tiene atributos, pero no es necesario, solo por precausion
    def __init__(self,nombre,año):
        self.nombre = nombre
        self.año = año
    
    def descripcion(self):
        return "{} tiene {} años".format(self.nombre,self.año)
    
    def comentario(self,frase):
        return "{} dice: {}".format(self.nombre,frase)
    
doctor = Persona("Jose",34)
print(doctor.descripcion())
print(doctor.comentario("Debe seguir aprendiendo, por lo menos un Franmework como Django"))