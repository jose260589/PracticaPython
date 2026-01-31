# crear un programa que simule una rocola
# el programa debe permitir al usuario seleccionar canciones de una lista aleatoria.

import random

class Rocola:
    def __init__(self):
        self.canciones = [
            "Canción 1 - Artista A",
            "Canción 2 - Artista B",
            "Canción 3 - Artista C",
            "Canción 4 - Artista D",
            "Canción 5 - Artista E",
            "Canción 6 - Artista F",
            "Canción 7 - Artista G",
            "Canción 8 - Artista H",
            "Canción 9 - Artista I",
            "Canción 10 - Artista J"
        ]
        self.queue = [] # Lista para las canciones seleccionadas, asi no se repiten.

    def play(self,k):
        if len(self.queue) >= k:
            primero = self.queue.pop(0)
            self.canciones.append(primero)
        indiceRandom = random.randint(0, len(self.canciones) - 1)
        canciones = self.canciones.pop(indiceRandom)
        self.queue.append(canciones)
        return canciones
    
    
Rocola = Rocola()

print(Rocola.play(5))       
print(Rocola.play(5))
print(Rocola.play(5))
print(Rocola.play(5))
print(Rocola.play(5))
print(Rocola.play(5))
print(Rocola.play(5))