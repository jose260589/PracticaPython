"""
Herencia
clase 1 (clase padre o super clase)
clase 2 (puede heredar cosas de clase 1)
clase 3 (puede heredar cosas de clase 1 y clase 2)
clase 4 (puede heredar cosas de clase 1 y clase 2)
clase 5 (puede heredar cosas de clase 1 y clase 2)
"""

class Vehiculos():
    def __init__(self,marca,modelo): #(constructor)
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
    pass # se usa para no colocar o constuir algo mas por el momento en esta otra clase


miMoto=Moto("Honda","CBR")
miMoto.estado()
