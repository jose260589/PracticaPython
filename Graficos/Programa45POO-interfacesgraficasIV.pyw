from tkinter import *
#raiz
raiz=Tk()
#frame
miframe=Frame(raiz, width=1000, height=600)
miframe.pack()


#cuadrotexto
cuadrotexto=Entry(miframe)
cuadrotexto.grid(row=0, column=1)

cuadrotexto2=Entry(miframe)
cuadrotexto2.grid(row=1, column=1)
cuadrotexto2.config(show="*")

cuadrotexto3=Entry(miframe)
cuadrotexto3.grid(row=2, column=1)

cuadrotexto4=Entry(miframe)
cuadrotexto4.grid(row=3, column=1)

#label
label=Label(miframe,text="Nombre")
label.grid(row=0, column=0)

label4=Label(miframe,text="Password:")
label4.grid(row=1, column=0)



label2=Label(miframe,text="Apellido")
label2.grid(row=2, column=0)

label3=Label(miframe,text="Direccion")
label3.grid(row=3, column=0)

raiz.mainloop()
