from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width="500", height="400")
miFrame.pack()

#para colocar imagenes.
"""
miImagen=PhotoImage(file="direccion imagen")
Label(miFrame, image=miImagen).place(x=100,y=200)
"""

miLabel=Label(miFrame, text="Hola Mundo")
#miLabel.pack()#en paquetado, pero esto se puede cambiar.
miLabel.place(x=100,y=200)# otra forma de mover o cambiar el tamaño cuando esta equivocado.

raiz.mainloop()