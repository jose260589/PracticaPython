"""
sintaxis
try:

"""
#ejemplo
def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1, num2):
    try: #este es el uso del try, lo que este dentro del try se ejecuta, si da error pasa a la exception.
        return num1/num2
    except ZeroDivisionError: # el except, captura el error y muestra el mensaje o la instrucion que se le da nueva vez.
        print("No se puede dividir entre 0.")
        return "Operacion Erronea."
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))
        break
    except ValueError:
        print("Los datos introducidos son erroneos Intenta de nuevo.")

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(op1, op2))
elif operacion=="resta":
    print(resta(op1, op2))
elif operacion=="multiplica":
    print(multiplica(op1, op2))
elif operacion=="divide":
    print(divide(op1, op2))
else:
    print("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del Programa")
