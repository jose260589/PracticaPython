"""
interfaces graficas
librerias
Tkinter - es la libreria por defecto, pero hay otras, es un puente para la
libreria TCL/TK
WxPython
PyQT
PyGTK

Estructura de ventana con Tkinter
Raix(tk) dentro de esta se usa un frame
frame dentro de este se usa los widgets
widgets(botones, menus,cuadro de texto, etc)

para hacer que los archivos se ejecuten sin la ventana de python, solo hay que
cambiar la extension .py por .pyw. w=sistema operativo.
"""
#importar libreria
from tkinter import *

#crear la raiz
raiz=Tk()
#Titulo de ventana
raiz.title("Ventana de prueba")

#este metodo es para impedir que las ventanas se puedan agrandar o que tengas
#un tamaño en especifico
#resizable(ancho, alto)
raiz.resizable(0,0) # con 0,0, se queda se un tamaño pequeño, o True o False

#Agregar un icono 
#raiz.iconbitmap("Ruta")
#nota: debe ser la imagen tipo .ico

#cambiar tamaño de la ventana por defecto
raiz.geometry("650x350")

#color background
raiz.config(bg="red")

#metodo para ejecutar, el mainloop: es como un evento
#este metodo debe estar en ultimo lugar, porque debe
#estar a la escucha y se puede ejecutar
raiz.mainloop()
