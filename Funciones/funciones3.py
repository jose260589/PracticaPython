#crear funcion que retorne un valor solicitando dos numeros.
def sumar_dos_numeros(num1, num2):  
    return num1 + num2

my_result = sumar_dos_numeros(5, 10)
print("El resultado de la suma es:", my_result)

#crear funcion que retorne un valor solicitando dos textos.
def concatenar_textos(name, surname):
    print(f"{name} {surname}")


concatenar_textos(name= "Jose", surname= "Perez")

#crear una funcion que imprima un valor con valor por defecto.
def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Ana", "Gomez")
print_name_with_default("Luis", "Martinez", "Lucho")

#crear una funcion que imprima textos ilimitados.
def imprimir_textos_ilimitados(*textos):
    for texto in textos:
        print(texto)

imprimir_textos_ilimitados("Hola", "Mundo", "Esto", "Es", "Una", "Prueba")
imprimir_textos_ilimitados("Solo", "Dos", "Textos")
imprimir_textos_ilimitados("Uno")