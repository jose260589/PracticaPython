class cubo:
    def __init__(self, ancho, altura, profundidad):
        self.base =  ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.base * self.altura * self.profundidad

base = int(input("Proporciona la base: "))
altura = int(input("Proporciona la altura: "))
profundidad = int(input("Proporciona la profundidad: "))

cubo1 = cubo(base, altura, profundidad)

print(f'volumen del cubo: {cubo1.calcular_volumen()}')