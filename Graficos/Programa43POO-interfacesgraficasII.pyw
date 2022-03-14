#importar libreria
from tkinter import *

#crear la raiz
raiz=Tk()
#Titulo de ventana
raiz.title("Ventana de prueba")

#Metodo para impedir que la pantalla se pueda redimensionar
#resizable(ancho, alto) 0,0 ó True 1 o False 0

#raiz.resizable(0,0) # con 0,0, se queda se un tamaño pequeño, o True o False


#cambiar tamaño de la ventana por defecto
raiz.geometry("650x350")

#color background
raiz.config(bg="red")

#variable para el frame
miFrame=Frame()

#empaquetar el frame
miFrame.pack()
#para expandir el frame junto a la raiz
#miFrame.pack(fill="both", expand="True")

miFrame.config(bg="yellow")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

miFrame.config(cursor="hand2")


#metodo obligatorio
raiz.mainloop()
