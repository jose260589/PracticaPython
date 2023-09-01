#Polimorfisco con metodos.

class Colombia:
    def capital(self):
        print("Bogota")
    def idioma(self):
        print("Español")

class Francia:
    def capital(self):
        print("Paris")
    def idioma(self):
        print("Frances")
        
colombiano = Colombia()
frances = Francia()
#es bueno en este caso usar un for
for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()