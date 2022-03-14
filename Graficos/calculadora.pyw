"""
idea calculadora
que cada vez que se le de a un signo de matematica
este guarde la suma en una variable global, y sume y muestre
que signo se esta usando con concatenacion, y que si se usa
el signo de igual muestre ese resultado, tambien, si se cambia
de signo este lo cambie sin problemas.

"""

from tkinter import *

raiz=Tk()
raiz.title("Calculadora")
raiz.resizable(0,0)
#raiz.geometry()

miframe=Frame(raiz)
miframe.pack()

#Funciones
def numeroPulsado(num):
    #global resultado

    
    #pregunto y desabilito el punto
    if num==".":
        BotonComa["state"] = "disabled"
        #print("Datos: ",numeroPantalla)
        numeroPantalla.set(numeroPantalla.get()+num)
    else:
       numeroPantalla.set(numeroPantalla.get()+num)

def operaciones(operacion,num):
    operador=operacion
    global resultado
    numeroPantalla.set("")

    if (operacion=="suma"):
        print("suma "+num)
        resultado+=int(num)
        
    elif(operacion=="resta"):
        print("resta "+num)
        resultado-=int(num)
        
    elif(operacion=="multiplica"):
        print("multiplica "+num)
        resultado*=int(num)
        
    elif(operacion=="divide"):
        print("dividir "+num)
        resultado/=int(num)
        

    #numeroPantalla.set(resultado)
    
"""
def suma(num):
    global operacion
    global resultado

    resultado+=int(num)
    operacion="suma"

    numeroPantalla.set(resultado)
"""
def el_resultado():
    global resultado
    numeroPantalla.set(resultado)
    
        
#Variables
numeroPantalla=StringVar()
numeroPantalla.set("0")
operacion=""
resultado=0
#numero=IntVar()
#numero2=DoubleVar()
#bal=BooleanVar()

print( numeroPantalla)

#pantalla
pantalla=Entry(miframe, textvariable=numeroPantalla )
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
#columnspan: es para combinar columnas y filas
pantalla.config(bg="black" , fg="#03f943", justify="right")

#Botones primera fila
Boton7=Button(miframe, text="7", justify="center", width=3, command=lambda: numeroPulsado("7"))
Boton7.grid(row=2, column=1)

Boton8=Button(miframe, text="8", justify="center", width=3, command=lambda: numeroPulsado("8"))
Boton8.grid(row=2, column=2)

Boton9=Button(miframe, text="9", justify="center", width=3, command=lambda: numeroPulsado("9"))
Boton9.grid(row=2, column=3)

BotonDividir=Button(miframe, text="/", justify="center", width=3, command=lambda:operaciones("divide",numeroPantalla.get()) )
BotonDividir.grid(row=2, column=4)

#Botones Segunda Fila
Boton4=Button(miframe, text="4", justify="center", width=3, command=lambda: numeroPulsado("4"))
Boton4.grid(row=3, column=1)

Boton5=Button(miframe, text="5", justify="center", width=3, command=lambda: numeroPulsado("5"))
Boton5.grid(row=3, column=2)

Boton6=Button(miframe, text="6", justify="center", width=3, command=lambda: numeroPulsado("6"))
Boton6.grid(row=3, column=3)

BotonMultiplicar=Button(miframe, text="X", justify="center", width=3, command=lambda:operaciones("multiplica",numeroPantalla.get()))
BotonMultiplicar.grid(row=3, column=4)

#Botones tercera Fila
Boton1=Button(miframe, text="1", justify="center", width=3, command=lambda: numeroPulsado("1"))
Boton1.grid(row=4, column=1)

Boton2=Button(miframe, text="2", justify="center", width=3, command=lambda: numeroPulsado("2"))
Boton2.grid(row=4, column=2)

Boton3=Button(miframe, text="3", justify="center", width=3, command=lambda: numeroPulsado("3"))
Boton3.grid(row=4, column=3)

BotonRestar=Button(miframe, text="-", justify="center", width=3, command=lambda:operaciones("resta",numeroPantalla.get()))
BotonRestar.grid(row=4, column=4)

#Botones cuarta Fila
Boton0=Button(miframe, text="0", justify="center", width=3, command=lambda: numeroPulsado("0"))
Boton0.grid(row=5, column=1)

BotonComa=Button(miframe, text=".", justify="center", width=3, command=lambda: numeroPulsado("."))
BotonComa.grid(row=5, column=2)

BotonIgual=Button(miframe, text="=", justify="center", width=3, command=lambda:el_resultado())
BotonIgual.grid(row=5, column=3)

BotonSumar=Button(miframe, text="+", justify="center", width=3, command=lambda:operaciones("suma",numeroPantalla.get()))
BotonSumar.grid(row=5, column=4)

raiz.mainloop()
