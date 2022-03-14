from tkinter import *

#funcion
def codigoBoton():
   minombre.set("José")
   #set: agregar informacion a un objeto
   #get: obtener informacion de un objeto

#raiz
raiz=Tk()
raiz.geometry("650x350")

#frame
miframe=Frame(raiz)
miframe.pack(fill="both", expand="True")
"""Con esta forma se puede expandir el frame con la raiz, que el diametro se encargue
la raiz, y se expande en el pack del frame.

"""
#variable de prueba para escribir en cuadro texto
minombre=StringVar()

#label
label=Label(miframe, text="Nombre")
label.grid(row=0, column=0, padx=10, pady=10)

label4=Label(miframe, text="Password:")
label4.grid(row=1, column=0, padx=10, pady=10)

label2=Label(miframe, text="Apellido")
label2.grid(row=2, column=0, padx=10, pady=10)

label3=Label(miframe, text="Direccion")
label3.grid(row=3, column=0, padx=10, pady=10)

label5=Label(miframe, text="Cuadro de texto")
label5.grid(row=4, column=0, padx=10, pady=10)

#cuadrotexto sticky="e"
cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=0, column=1, sticky="w", padx=10, pady=10)

cuadropass=Entry(miframe)
cuadropass.grid(row=1, column=1, sticky="w", padx=10, pady=10)
cuadropass.config(show="*")

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=2, column=1,sticky="w", padx=10, pady=10)

cuadrodireccion=Entry(miframe, width=30)
cuadrodireccion.grid(row=3, column=1, sticky="w", padx=10, pady=10)

# height: solo funciona en text, no en entry
cuadrotexto=Text(miframe, width=25, height=5)
cuadrotexto.grid(row=4, column=1, sticky="w", padx=10, pady=10)

#barra de desplazamiento
scrollvert=Scrollbar(miframe, command=cuadrotexto.yview)
scrollvert.grid(row=4, column=1, sticky="nse")
cuadrotexto.config(yscrollcommand=scrollvert.set)#donde me encuentro
#mejor forma de usar cuadro de texto con barra de
#desplazamiento hasta ahora.

#boton
boton1=Button(miframe, text="Aceptar", width=7, command=codigoBoton)
boton1.grid(row=5, column=1)

raiz.mainloop()
