#Polimorfismo por funcion

class Tomate:
    def tipo(self):
        print('Vegetal')
    def color(self):
        print('Rojo')

class Manzana:
    def tipo(self):
        print('Fruta')
    def color(self):
        print('Verde')

def mercado(objeto):
    objeto.tipo()
    objeto.color()
    
nuevo_tomate = Tomate()
print("Tomate")#opcional
mercado(nuevo_tomate)

print("Manzana")#opcional
nueva_manzana = Manzana()
mercado(nueva_manzana)