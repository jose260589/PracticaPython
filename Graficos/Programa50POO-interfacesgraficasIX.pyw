from tkinter import *

root=Tk()

varOpcion=IntVar()

def imprimir():
    #print(varOpcion.get())
    if varOpcion.get()==1:
        etiqueta.config(text="Elegiste masculino. ")
    else:
        etiqueta.config(text="Elegiste Femenino. ")

Label(root, text="Genero: ").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=lambda:imprimir()).pack()

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=lambda:imprimir()).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
