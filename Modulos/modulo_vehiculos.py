class Vehiculos():
    def __init__(self, marca, modelo): #constructor __init__(self,etc):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",
              self.frena)
"""
Para heredar solo hay que colocar entre parentesis(), el nombre de la clase que
esta heredando. ejemplo: class Moto(Vehiculos): 
"""
class Moto(Vehiculos): 
    hcaballito=""

    def caballito(self):
        self.hcaballito="Voy haciendo el caballito."
   #De esta forma se sobreescribe el metodo de 
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ",
              self.frena, "\n", self.hcaballito)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La Furgoneta no esta cargada"

class VElectricos():
    def __ini__(self):
        self.autonomia=100

    def CargarEnergia(self):

        self.cargando=True

"""
cuando se pasan mas clases padres, si hay mas elementos que sean iguales llamara
solo al metodo de la clase mas a la izquierda.
"""
