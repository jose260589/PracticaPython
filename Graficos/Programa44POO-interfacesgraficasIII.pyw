#importar libreria
from tkinter import *

#crear la raiz
root=Tk()
#Titulo de ventana
root.title("Ventana de prueba para label")

#variable para el frame
miFrame=Frame(root, width=500, height=400)

#empaquetar el frame
miFrame.pack()
#para expandir el frame junto a la raiz
#miFrame.pack(fill="both", expand="True")

miFrame.config(bg="white")

#miFrame.config(width="650", height="350")

miLabel=Label(miFrame, text="Hola josé")
miLabel.place(x=0, y=0)
"""
tambien se puede empaquetar el label, pero entonces no aparece correctamente y
la ventana no coje el tamaño del frame, sino el tamaño del objeto en si.
"""
miLabel=Label(miFrame, text="Hola Mari")
miLabel.place(x=0, y=30)

miLabel=Label(miFrame, text="Hola ZOE")
miLabel.place(x=0, y=60)

#metodo obligatorio
root.mainloop()
