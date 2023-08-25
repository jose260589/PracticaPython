#estatico: es para que se trabaje de forma interna, sin importar el exterior
import math

class Pastel:
    def __init__(self,ingredientes,tamaño) -> None:
        self.ingredientes = ingredientes
        self.tamaño = tamaño
        
    def __repr__(self) -> str:
        return (f'Pastel({self.ingredientes !r},'f'{self.tamaño})')
    
    def area(self):
        return self.tamaño_area(self.tamaño)
    
    @staticmethod #para usar un metodo estatico
    def tamaño_area(A): #no es necesario usar la opcion self o cls, puede ser alguna variable diferente
        return A ** 2 * math.pi

nuevo_pastel=Pastel(['Harina','leche','azucar','crema','chocolate'],4)

print(nuevo_pastel.ingredientes)
print(nuevo_pastel.tamaño)
print(nuevo_pastel.tamaño_area(12))
