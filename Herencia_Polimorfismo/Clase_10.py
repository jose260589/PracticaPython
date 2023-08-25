#parte polimorfismo

class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self) -> str:#representacion informal de una cadena o un objeto, se devolvera un string
        return f"Hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años"
    
    def __repr__(self) -> str:#otra forma, pero esta se ejecuta con el codigo, el otro  solo es para ver los datos
        return f"Hola que tal soy {self.nombre} {self.apellido} y tengo {self.edad} años"

nuevo_estudiando = Estudiante("Jose","Inoa",34)

print(f"{nuevo_estudiando}")
#print(f"{nuevo_estudiando !r}") no se entendio, pero con !r se usa el repr