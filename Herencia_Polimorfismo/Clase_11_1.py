#tipo clase:  se usa en este caso el @classmethod, para que sus valores sean independientes.
class Pastel:
    def __init__(self,ingredientes) -> None:
        self.ingredientes = ingredientes
    
    def __repr__(self) -> str:
        return f'pastel({self.ingredientes !r})'
    
    @classmethod
    def Pastel_Chocolate(cls):#para este tipo de metodo en vez del self, se usa el cls
        return cls(['harina','leche','chocolate'])
    
    @classmethod
    def Pastel_Vainilla(cls):
        return cls(['harina','leche','vainilla'])
    
    
print(Pastel.Pastel_Vainilla())


