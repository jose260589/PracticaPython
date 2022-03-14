"""from tkinter import *

raiz=Tk()

raiz.title("Programa de Jose")
raiz.config(bg="white")
raiz.geometry("650x400")
#Frame------------------------

miFrame=Frame(raiz)
miFrame.pack(fill="both", expand="True")
#miFrame.config(bg="gold", width="400",  height="250")
miFrame.config(bg="gold")
"""
#estas opciones modifican la textura y forma del frime, ya sea el mouse.
#miFrame.config(bd=35)

#miFrame.config(relief="sunken")

#miFrame.config(cursor="hand2")
"""
#-------------------------------------------
miLabel=Label(miFrame, text="Mi primer label", pady=5,padx=5)
miLabel.grid(row=0,column=0)
miLabel2=Label(miFrame, text="Mi segundo label", pady=5,padx=5)
miLabel2.grid(row=1,column=0)

CuadroTexto=Entry(miFrame)
CuadroTexto.grid(row=0,column=1, pady=5,padx=5)

CuadroTexto2=Entry(miFrame)
CuadroTexto2.grid(row=1,column=1, pady=5,padx=5)

"""

"""
#Ejemplo desactivar boton
from tkinter import *

fenster = Tk()
fenster.title("Window")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b2["text"] = "enable"
    else:
        b1["state"] = "normal"
        b2["text"] = "disable"

#--Buttons
b1 = Button(fenster, text="Button", height=5, width=7)
b1.grid(row=0, column=0)    

b2 = Button(text="disable", command=switch)
b2.grid(row=0, column=1)

fenster.mainloop()





raiz.mainloop()

"""
