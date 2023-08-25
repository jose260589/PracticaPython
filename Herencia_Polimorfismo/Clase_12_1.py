#Ejemplo Polimorfismo

class Auto:
    
    rueda = 4
    
    def desplazamiento(self):
        print(f'El auto se esta desplazando sobre {Auto.rueda} ruedas')
        

class Moto:
    
    rueda = 2
    
    def desplazamiento(self):
        print(f'La Moto se esta desplazando sobre {Moto.rueda} ruedas')
        

automovil = Auto()

automovil.desplazamiento()

Motocicleta = Moto()

Motocicleta.desplazamiento()