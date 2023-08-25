#herencia multiple

class Telefono:
    def __init__(self):
        pass
    
    def llamar(self):
        print("Llamando...")
    
    def ocupado(self):
        print("Ocupado...")

class Camara:
    def __init__(self):
        pass
    
    def fotografia(self):
        print("Tomando fotos...")
        
class Reproduccion:
    def __init__(self):
        pass
    
    def reproduccionmusica(self):
        print("Reproduciendo musica...")
    
    def reproduccionvideo(self):
        print("Reproduciendo video...")
        
class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):#se usa para destruir una clase. o ahorrar memoria.
        print("Telefono apagado...")
        


movil = Smartphone()
print(movil.llamar())

#print(dir(movil))
#dir: se usa para ver que metodos o caracteristicas puedo usar con ese objeto. se usa para muchas otras funciones.