from tkinter import *

raiz=Tk()

raiz.title("Ventana de Prueba")#agregar titulo

raiz.resizable(False, False)#mover tamaño de ventana por usuario

raiz.geometry("650x350")#Dar un tamaño a la pantalla.

raiz.iconbitmap("iconos/folder.ico")#agregar un icono o cambiar el por default de la aplicacion

raiz.config(bg="red")#hacer las configuraciones 

raiz.mainloop()#con este se ejecuta toda la venta. hay que colocar las demas opciones
#antes de esta o no saldran en la ventana, esta es la ultima en colocar
