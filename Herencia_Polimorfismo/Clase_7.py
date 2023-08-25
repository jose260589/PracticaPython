#Modificar un atributo

class Email:
    pass
    def __init__(self):
        self.enviado = False
    
    def enviar_correo(self):
        self.enviado = True
        

mi_correo = Email()

print(mi_correo.enviado) #False version original

mi_correo.enviar_correo()#llamo al segundo metodo para que actualize el dato
print(mi_correo.enviado)#imprimi el valor actualizado
