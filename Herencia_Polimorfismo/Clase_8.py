#Herencia

class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def descripcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre,self.tipo)

class Pikachu(Pokemon):#para que herede, la clase hijp se agrega () y dentro de este se coloco el nombre de la clase padre
    def ataque(self,tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)

class Charmander(Pokemon):#para que herede, la clase hijp se agrega () y dentro de este se coloco el nombre de la clase padre
    def ataque(self,tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre,tipoataque)


nuevo_pokemon = Pikachu("zoe","electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("attack trueno"))