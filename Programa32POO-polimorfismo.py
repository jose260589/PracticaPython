class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


"""
#esta es la forma de hacer sin polimorfismo
miVehiculo=Moto()

miVehiculo.desplazamiento()

miVehiculo2=Coche()

miVehiculo2.desplazamiento()

miVehiculo3=Camion()

miVehiculo3.desplazamiento()

"""

#metodo para usar polimorfismo
def desplazamiento(vehiculo):
    vehiculo.desplazamiento()

#se llama la instancia de manera normal
mivehiculo=Moto()

#lo que cambia es aqui, en vez de usar la instancia mi vehiculo, se llama al metodo
# desplazamiento y como self se pone la instancia.

desplazamiento(mivehiculo)
