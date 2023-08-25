#funciones para atributos

class Persona:
    edad = 27
    nombre = 'Jose'
    pais = "Dominican Republic"

doctor = Persona()

print("La Persona es ",doctor.nombre)
print("La Edad es ",getattr(doctor,"edad")) #tener el valor de un atributo de otra forma, es una funcion.

#validar si algo es verdadero o falso
print("El doctor tiene una edad?",hasattr(doctor,"edad")) #en este caso se usa si un atributo existe o no

#una funcion para hacer cambios de datos en los atributos
setattr(doctor,"nombre","Arismendy")
print("La Persona es ",doctor.nombre)

#una funcion para eliminar atributos
delattr(doctor,"pais")